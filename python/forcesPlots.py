# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
from msk_modelling_python.src.bops import *
import msk_modelling_python.src.bops as bp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

dir_name = "/Users/marcelhacker/Documents/opensim-deadlift-techniques"  # your dircetory


################################ CLASSES ###########################################
class athlete:
    def __init__(self, name, mass, model, technique):
        # informations
        self.name = name  # "athlete_x", used for reading files
        self.mass = mass  # "57"
        self.model = model  # "athlete_x_scaled"
        self.technique = technique  # "sumo" or "conventional", preffered deadlift


################################ CREATING ATHLETES ###########################################
athletes = []  # appending instances to athletes list
athletes.append(
    athlete(
        "athlete_0_increased_force_3",
        "57",
        "athlete_0_scaled_increased_force_3",
        "conventional",
    ),
)
athletes.append(
    athlete(
        "athlete_1",
        "87",
        "athlete_1_scaled",
        "sumo",
    ),
)


def get_paths_athlete(athlete, model_name=None):
    # todos include moment arm paths in the emptybar trails, not only in the weighted trails
    # todos recheck moment arms paths, and add moment arms to conv
    if model_name == None:
        print("No model name given, get_paths_athlete")
        return None
    else:
        print("\n model name:", model_name)
        print("\n athlete name:", athlete.name)

        data = {}
        # set athletes model and static trail
        data["osim"] = dir_name + "/" + athlete.name + "/" + model_name + ".osim"
        data["static_c3d"] = dir_name + "/" + athlete.name + "/static.c3d"
        data["static_trc"] = dir_name + "/" + athlete.name + "/static.trc"

        # sumo, emptybar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, emptybar trails
            trail_prefix = "sumo_emptybar_"  # folder prefix
            data["ik_sumo_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_sumo_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_sumo_emptybar_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["id_sumo_emptybar_path_" + str(i)])
            # print("\n", data["id_sumo_emptybar_path_" + str(i)])
            # print("\n", data["muscle_forces_sumo_emptybar_path_" + str(i)])

        # sumo, fullbar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, fullbar trails
            trail_prefix = "sumo_dl_"  # folder prefix
            data["ik_sumo_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_sumo_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
            data["moment_arms_hip_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_hip_flexion_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_l.sto
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_hip_flexion_l.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_knee_angle_r.sto
            data["moment_arms_knee_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_knee_angle_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_knee_angle_l.sto
            data["moment_arms_knee_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_knee_angle_l.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_ankle_angle_r.sto
            data["moment_arms_ankle_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_ankle_angle_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_ankle_angle_l.sto
            data["moment_arms_ankle_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_ankle_angle_l.sto"
            )
            data["muscle_forces_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["id_sumo_path_" + str(i)])
            # print("\n", data["id_sumo_path_" + str(i)])
            # print("\n", data["muscle_forces_sumo_path_" + str(i)])

        # conv, emptybar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, emptybar trails
            trail_prefix = "conv_emptybar_"  # folder prefix
            data["ik_conv_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_conv_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_conv_emptybar_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["ik_conv_emptybar_path_" + str(i)])
            # print("\n", data["id_conv_emptybar_path_" + str(i)])
            # print("\n", data["muscle_forces_conv_emptybar_path_" + str(i)])

        # conv, fullbar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, fullbar trails
            trail_prefix = "conv_dl_"  # folder prefix
            data["ik_conv_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_conv_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["ik_conv_path_" + str(i)])
            # print("\n", data["id_conv_path_" + str(i)])
            # print("\n", data["muscle_forces_conv_path_" + str(i)])

        return data


def time_normalise_df(df, fs=""):

    if not type(df) == pd.core.frame.DataFrame:
        raise Exception("Input must be a pandas DataFrame")

    if not fs:
        try:
            fs = 1 / (df["time"][1] - df["time"][0])
        except KeyError as e:
            raise Exception('Input DataFrame must contain a column named "time"')

    normalised_df = pd.DataFrame(columns=df.columns)

    for column in df.columns:
        normalised_df[column] = np.zeros(101)

        currentData = df[column]
        currentData = currentData[~np.isnan(currentData)]

        timeTrial = np.arange(0, len(currentData) / fs, 1 / fs)
        Tnorm = np.arange(0, timeTrial[-1], timeTrial[-1] / 101)
        if len(Tnorm) == 102:
            Tnorm = Tnorm[:-1]
        normalised_df[column] = np.interp(Tnorm, timeTrial, currentData)

    return normalised_df


def mean_trail_values(
    data_1_time_normalised,
    data_2_time_normalised,
    data_3_time_normalised=None,
):
    """
    calculate the mean value of the given trails
    Input:
    Data Frame of the trail files, columns have to identical!

    Output:
    New data frame with the mean of values
    """
    data = pd.DataFrame()  # make a copy of delivered dataFrame

    for column in data_1_time_normalised.columns:
        if data_3_time_normalised == None:
            print("2 data trails given")
            data[column] = (
                data_1_time_normalised[column] + data_2_time_normalised[column]
            ) / 2
        else:
            print("3 data trails given")
            data[column] = (
                data_1_time_normalised[column]
                + data_2_time_normalised[column]
                + data_3_time_normalised[column]
            ) / 3
    return data


def sum_muscle_forces(muscleForces, muscle_group="Hamstrings", limbs="rl"):  #
    """sum_muscle_forces
    sum of intrested muscle forces

    Input:
    muscleForces must be time normalised to 101 values, data frame
    muscle_group = String e.g. "Hamstrings", "Quadriceps"
    limbs = "rl"  # rl for right and left, "r" or "l"
    Output:
    Array with the sum of the hole muscle forces
    """
    muscles_of_interest = []

    if limbs == "r" or limbs == "l":
        print("limb configuration not programmed, in sum_muscle_forces")

    if muscle_group == "Hamstrings" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "semimem_r",
            "semiten_r",
            "bflh_l",
            "bfsh_l",
            "semimem_l",
            "semiten_l",
        ]
    if muscle_group == "Hamstrings lateral" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "bflh_l",
            "bfsh_l",
        ]
    if muscle_group == "Hamstrings medial" and limbs == "rl":
        muscles_of_interest = [
            "semimem_r",
            "semiten_r",
            "semimem_l",
            "semiten_l",
        ]

    if muscle_group == "Hip flexors" and limbs == "rl":  # rec fem added
        muscles_of_interest = [
            "recfem_r",
            "recfem_l",
            "iliacus_r",
            "iliacus_l",
            "psoas_r",
            "psoas_l",
            "tfl_r",
            "tfl_l",
        ]
    if muscle_group == "Vasti" and limbs == "rl":
        muscles_of_interest = [
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]

    if muscle_group == "Quadriceps" and limbs == "rl":
        muscles_of_interest = [
            "recfem_r",
            "recfem_l",
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]
    if muscle_group == "Gluteus maximus" and limbs == "rl":
        muscles_of_interest = [
            "glmax1_r",
            "glmax2_r",
            "glmax3_r",
            "glmax1_l",
            "glmax2_l",
            "glmax3_l",
        ]
    if muscle_group == "Gluteus medius" and limbs == "rl":
        muscles_of_interest = [
            "glmed1_r",
            "glmed2_r",
            "glmed3_r",
            "glmed1_l",
            "glmed2_l",
            "glmed3_l",
        ]
    if muscle_group == "Gluteus minimus" and limbs == "rl":
        muscles_of_interest = [
            "glmin1_r",
            "glmin2_r",
            "glmin3_r",
            "glmin1_l",
            "glmin2_l",
            "glmin3_l",
        ]
    if muscle_group == "Triceps surae" and limbs == "rl":
        muscles_of_interest = [
            "gaslat_r",
            "gasmed_r",
            "soleus_r",
            "gaslat_l",
            "gasmed_l",
            "soleus_l",
        ]
    if muscle_group == "Adductors" and limbs == "rl":
        muscles_of_interest = [
            "addbrev_r",
            "addlong_r",
            "addmagDist_r",
            "addmagIsch_r",
            "addmagMid_r",
            "addmagProx_r",
            "addbrev_l",
            "addlong_l",
            "addmagDist_l",
            "addmagIsch_l",
            "addmagMid_l",
            "addmagProx_l",
        ]

    if muscle_group == "All" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "semimem_r",
            "semiten_r",
            "bflh_l",
            "bfsh_l",
            "semimem_l",
            "semiten_l",
            "recfem_r",
            "recfem_l",
            "iliacus_r",
            "iliacus_l",
            "psoas_r",
            "psoas_l",
            "tfl_r",
            "tfl_l",
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
            "glmax1_r",
            "glmax2_r",
            "glmax3_r",
            "glmax1_l",
            "glmax2_l",
            "glmax3_l",
            "glmed1_r",
            "glmed2_r",
            "glmed3_r",
            "glmed1_l",
            "glmed2_l",
            "glmed3_l",
            "glmin1_r",
            "glmin2_r",
            "glmin3_r",
            "glmin1_l",
            "glmin2_l",
            "glmin3_l",
            "gaslat_r",
            "gasmed_r",
            "soleus_r",
            "gaslat_l",
            "gasmed_l",
            "soleus_l",
            "addbrev_r",
            "addlong_r",
            "addmagDist_r",
            "addmagIsch_r",
            "addmagMid_r",
            "addmagProx_r",
            "addbrev_l",
            "addlong_l",
            "addmagDist_l",
            "addmagIsch_l",
            "addmagMid_l",
            "addmagProx_l",
        ]
    if muscles_of_interest == []:
        print("no muscle sum choosen, in sum_muscle_forces")

    sum_forces = [0] * 101  # defined arry length

    for i in range(len(muscles_of_interest)):
        index = 0
        for value in muscleForces[muscles_of_interest[i]]:
            sum_forces[index] = sum_forces[index] + value
            index += 1
    return sum_forces


def plot_data(
    axs,
    data_1,
    label_data_1,
    color_data_1,
    data_2,
    label_data_2,
    color_data_2,
    legend,
    y_label,
    x_label,
):
    plt.sca(axs)
    plt.plot(
        data_1,
        label=label_data_1,
        color=color_data_1,
    )
    plt.plot(
        data_2,
        label=label_data_2,
        color=color_data_2,
    )
    if legend:
        plt.legend()
    plt.ylabel(y_label)
    plt.xlabel(x_label)


if __name__ == "__main__":

    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_forces_plot = False
    run_emptybar_comparison = False
    run_muscle_force_sum_plot = False
    run_total_force_comparison = False
    run_trail_comparison = True

    file_paths = get_paths_athlete(athletes[0], athletes[0].model)
    ##################################################################################################
    # IK sumo
    ik_sumo_emptybar_0 = pd.read_csv(
        file_paths["ik_sumo_emptybar_path_0"],
        sep="\t",
        skiprows=10,
    )
    ik_sumo_emptybar_1 = None
    ik_sumo_emptybar_2 = None
    ik_sumo_emptybar_3 = None
    ik_sumo_0 = None
    ik_sumo_1 = pd.read_csv(file_paths["ik_sumo_path_1"], sep="\t", skiprows=10)
    ik_sumo_2 = None
    ik_sumo_3 = None
    # IK conv
    ik_conv_emptybar_0 = None
    ik_conv_emptybar_1 = None
    ik_conv_emptybar_2 = None
    ik_conv_emptybar_3 = None
    ik_conv_0 = None
    ik_conv_1 = pd.read_csv(file_paths["ik_conv_path_1"], sep="\t", skiprows=10)
    ik_conv_2 = pd.read_csv(file_paths["ik_conv_path_2"], sep="\t", skiprows=10)
    ik_conv_3 = None
    # ID sumo
    id_sumo_1 = pd.read_csv(file_paths["id_sumo_path_1"], sep="\t", skiprows=6)
    id_conv_2 = pd.read_csv(file_paths["id_conv_path_2"], sep="\t", skiprows=6)

    # ID conv
    # SO sumo
    muscleForces_sumo_emptybar_0 = pd.read_csv(
        file_paths["muscle_forces_sumo_emptybar_path_0"], sep="\t", skiprows=14
    )
    muscleForces_sumo_1 = pd.read_csv(
        file_paths["muscle_forces_sumo_path_1"], sep="\t", skiprows=14
    )
    muscleForces_conv_2 = pd.read_csv(
        file_paths["muscle_forces_conv_path_2"], sep="\t", skiprows=14
    )

    # SO conv
    ## to do fix moment arms
    # print("\n PATH: ", file_paths["moment_arms_hip_flexion_r_sumo_path_1"])
    # athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
    # athlete_0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
    # momentArms_sumo = pd.read_csv(
    #   file_paths["moment_arms_hip_flexion_r_sumo_path_1"], sep="\t", skiprows=0
    # )
    # print("\n momentArms sumo: ", momentArms_sumo.columns)

    ### time normalise everything to 101 values
    ik_sumo_time_normalised_1 = time_normalise_df(ik_sumo_1)
    ik_conv_time_normalised_1 = time_normalise_df(ik_conv_1)
    ik_conv_time_normalised_2 = time_normalise_df(ik_conv_2)
    id_sumo_time_nomalised_1 = time_normalise_df(id_sumo_1)
    id_conv_time_normalised_2 = time_normalise_df(id_conv_2)
    ik_sumo_emptybar_time_normalised_0 = time_normalise_df(ik_sumo_emptybar_0)
    muscleForces_sumo_time_normalised_1 = time_normalise_df(muscleForces_sumo_1)
    muscleForces_conv_time_normalised_2 = time_normalise_df(muscleForces_conv_2)
    muscleForces_sumo_emptybar_time_normalised_0 = time_normalise_df(
        muscleForces_sumo_emptybar_0
    )

    ##################################################################################################

    if run_forces_plot:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 5
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics & Muscle Forces "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            muscle_interest = 0
            muscles_of_interest = [
                "recfem_r",
                "vaslat_r",
                "vasmed_r",
                "vasint_r",
                "glmax1_r",
                "glmax2_r",
                "glmax3_r",
                "semiten_r",
                "semimem_r",
                "bflh_r",
                "bfsh_r",
                "addmagMid_r",
            ]

            ## kinematics of hip, knee and ankle, and muscle forces
            for i in range(cols):
                for j in range(rows):
                    # i displays the columns, j the rows
                    if i == 0 and j == 0:  # hip angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["hip_flexion_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conv_time_normalised_1["hip_flexion_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Hip Flex [°]", color="grey")
                        plt.xlabel(x_label)
                    elif i == 0 and j == 1:  # knee angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["knee_angle_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conv_time_normalised_1["knee_angle_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Knee Flex [°]", color="grey")
                        plt.xlabel(x_label)
                    elif i == 0 and j == 2:  # ankle angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["ankle_angle_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conv_time_normalised_1["ankle_angle_r"],
                            label="Conventional 80%",
                        )
                        plt.ylabel("Ankle Flex [°]", color="grey")
                        plt.legend()
                        plt.xlabel(x_label)
                    elif muscle_interest < len(muscles_of_interest):
                        plt.sca(axs[i, j])
                        plt.plot(
                            muscleForces_sumo_time_normalised_1[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            muscleForces_conv_time_normalised_2[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Conventional 80%",
                        )
                        plt.ylabel(muscles_of_interest[muscle_interest] + " [N]")
                        muscle_interest += 1
                        plt.legend()
                        plt.xlabel(x_label)
                    else:
                        print("You can plot more curves, my master\n")

            plt.show()

        except Exception as e:
            print("Error in run_quadriceps_plot")
            print(e)

    # just for sumo currently avaiable
    if run_emptybar_comparison:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 5
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics & Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            muscle_interest = 0
            muscles_of_interest = [
                "recfem_r",
                "vaslat_r",
                "vasmed_r",
                "vasint_r",
                "glmax1_r",
                "glmax2_r",
                "glmax3_r",
                "semiten_r",
                "semimem_r",
                "bflh_r",
                "bfsh_r",
                "addmagMid_r",
            ]
            ## kinematics of hip, knee and ankle, and muscle forces
            for i in range(cols):
                for j in range(rows):
                    # i displays the columns, j the rows
                    if i == 0 and j == 0:  # hip angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["hip_flexion_r"],
                            label="Sumo",
                        )
                        plt.plot(
                            ik_sumo_emptybar_time_normalised_0["hip_flexion_r"],
                            label="Sumo emptybar",
                        )
                        plt.legend()
                        plt.ylabel("Hip Flex [°]", color="red")
                        plt.xlabel(x_label)
                    elif i == 0 and j == 1:  # knee angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["knee_angle_r"], label="Sumo"
                        )
                        plt.plot(
                            ik_sumo_emptybar_time_normalised_0["knee_angle_r"],
                            label="Sumo emptybar",
                        )
                        plt.legend()
                        plt.ylabel("Knee Flex [°]", color="red")
                        plt.xlabel(x_label)
                    elif i == 0 and j == 2:  # ankle angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised_1["ankle_angle_r"], label="Sumo"
                        )
                        plt.plot(
                            ik_sumo_emptybar_time_normalised_0["ankle_angle_r"],
                            label="Sumo emptybar",
                        )
                        plt.ylabel("Ankle Flex [°]", color="red")
                        plt.legend()
                        plt.xlabel(x_label)
                    elif muscle_interest < len(muscles_of_interest):
                        plt.sca(axs[i, j])
                        plt.plot(
                            muscleForces_sumo_time_normalised_1[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo",
                        )
                        plt.plot(
                            muscleForces_sumo_emptybar_time_normalised_0[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo emptybar",
                        )
                        plt.ylabel(muscles_of_interest[muscle_interest] + " [N]")
                        muscle_interest += 1
                        plt.legend()
                        plt.xlabel(x_label)
                    else:
                        print("You can plot more curves, my master\n")

            plt.show()

        except Exception as e:
            print("Error in run_emptybar_comparison")
            print(e)

    if run_muscle_force_sum_plot:
        # For the next plot:
        """
        1.⁠ ⁠Add a row below angles with the 3 joint moments
        2.⁠ ⁠Make them all same colors in all plots
        3.⁠ ⁠Split hams by medial (Semitend and Semimem) and lateral (biceps long and short heads)
        4.⁠ ⁠Add hip flexors as a muscle group (TFL, iliacus, psoas, and rectfem)
        5.⁠ ⁠Don't include rect fem on quads
        """
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 5
            color_row_0 = "red"
            color_row_1 = "lawngreen"
            color_row_2 = "orange"
            color_row_3 = "magenta"
            color_row_4 = "brown"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics, Kinetics & Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"
            # Hamstrings medial (Semitend and Semimem)
            hamstrings_medial_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,  # muscle force data
                "Hamstrings medial",  # Hamstrings medial
                "rl",
            )
            hamstrings_medial_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Hamstrings medial",
                "rl",
            )
            # Hamstrings lateral (biceps long and short heads)
            hamstrings_lateral_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,  # muscle force data
                "Hamstrings lateral",  # Hamstrings lateral
                "rl",
            )
            hamstrings_lateral_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,  # muscle force data
                "Hamstrings lateral",
                "rl",
            )
            vasti_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Vasti",  # Quadriceps
                "rl",
            )
            vasti_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Vasti",  # Quadriceps
                "rl",
            )
            gluteusmax_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Gluteus maximus",  # Gluteus Maximus
                "rl",
            )
            gluteusmax_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Gluteus maximus",  # Gluteus Maximus
                "rl",
            )
            # Gluteus Medius
            gluteusmed_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Gluteus medius",
                "rl",
            )
            gluteusmed_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Gluteus medius",
                "rl",
            )
            # Gluteus Minimus
            gluteusmin_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Gluteus minimus",
                "rl",
            )
            gluteusmin_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Gluteus minimus",
                "rl",
            )

            adductors_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Adductors",  # Adductors
                "rl",
            )
            adductors_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Adductors",  # Adductors
                "rl",
            )
            # Hip flexors
            hip_flexors_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Hip flexors",  # Adductors
                "rl",
            )
            hip_flexors_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Hip flexors",  # Adductors
                "rl",
            )

            # Triceps Surae
            triceps_surae_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,
                "Triceps surae",  # Adductors
                "rl",
            )
            triceps_surae_conve_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,
                "Triceps surae",  # Adductors
                "rl",
            )

            ## kinematics of hip, knee and ankle, and muscle forces
            plt.sca(axs[0, 0])
            plt.plot(
                ik_sumo_time_normalised_1["hip_flexion_r"],
                color=color_row_0,
                label="Sumo",
            )
            plt.plot(
                ik_conv_time_normalised_1["hip_flexion_r"],
                label="Conventional 80%",
            )
            plt.legend()
            plt.ylabel("Hip Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.plot(
                ik_sumo_time_normalised_1["knee_angle_r"],
                color=color_row_0,
                label="Sumo",
            )
            plt.plot(
                ik_conv_time_normalised_1["knee_angle_r"],
                label="Conventional 80%",
            )
            plt.legend()
            plt.ylabel("Knee Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(
                ik_sumo_time_normalised_1["ankle_angle_r"],
                label="Sumo",
                color=color_row_0,
            )
            plt.plot(
                ik_conv_time_normalised_1["ankle_angle_r"],
                label="Conventional 80%",
            )
            plt.ylabel("Ankle Flex [°]", color="grey")
            plt.legend()
            plt.xlabel(x_label)
            ## moments, just right leg
            # todo get mean of both
            # hip
            plt.sca(axs[1, 0])
            plt.plot(
                id_sumo_time_nomalised_1["hip_flexion_r_moment"],
                label="Sumo",
                color=color_row_1,
            )
            plt.plot(
                id_conv_time_normalised_2["hip_flexion_r_moment"],
                label="Conventional 80%",
            )
            plt.ylabel("Hip moment [Nm]", color="grey")
            plt.legend()
            plt.xlabel(x_label)
            # knee
            plt.sca(axs[1, 1])
            plt.plot(
                id_sumo_time_nomalised_1["knee_angle_r_moment"],
                label="Sumo",
                color=color_row_1,
            )
            plt.plot(
                id_conv_time_normalised_2["knee_angle_r_moment"],
                label="Conventional 80%",
            )
            plt.ylabel("Knee moment [Nm]", color="grey")
            plt.legend()
            plt.xlabel(x_label)
            # ankle
            plt.sca(axs[1, 2])
            plt.plot(
                id_sumo_time_nomalised_1["ankle_angle_r_moment"],
                label="Sumo",
                color=color_row_1,
            )
            plt.plot(
                id_conv_time_normalised_2["ankle_angle_r_moment"],
                label="Conventional 80%",
            )
            plt.ylabel("Ankle moment [Nm]", color="grey")
            plt.legend()
            plt.xlabel(x_label)

            # hamstrings medial
            plt.sca(axs[2, 0])
            plt.plot(
                hamstrings_medial_sumo_force,
                label="Sumo",
                color=color_row_2,
            )
            plt.plot(hamstrings_medial_conv_force, label="Conventional 80%")
            plt.ylabel("Hamstrings medial [N]")
            plt.legend()
            plt.xlabel(x_label)
            # hamstrings lateral
            plt.sca(axs[2, 1])
            plt.plot(hamstrings_lateral_sumo_force, label="Sumo", color=color_row_2)
            plt.plot(hamstrings_lateral_conv_force, label="Conventional 80%")
            plt.ylabel("Hamstrings lateral [N]")
            plt.legend()
            plt.xlabel(x_label)
            # vasti
            plt.sca(axs[2, 2])
            plt.plot(vasti_sumo_force, label="Sumo", color=color_row_2)
            plt.plot(vasti_conv_force, label="Conventional 80%")
            plt.ylabel("Vasti [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus maximus
            plt.sca(axs[3, 0])
            plt.plot(gluteusmax_sumo_force, label="Sumo", color=color_row_3)
            plt.plot(gluteusmax_conv_force, label="Conventional 80%")
            plt.ylabel("Gluteus maximus [N]")
            plt.legend()
            plt.xlabel(x_label)

            # adductors
            plt.sca(axs[3, 1])
            plt.plot(adductors_sumo_force, label="Sumo", color=color_row_3)
            plt.plot(adductors_conv_force, label="Conventional 80%")
            plt.ylabel("Adductors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus medius
            plt.sca(axs[3, 2])
            plt.plot(gluteusmed_sumo_force, label="Sumo", color=color_row_3)
            plt.plot(gluteusmed_conv_force, label="Conventional 80%")
            plt.ylabel("Gluteus medius [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Triceps surae
            plt.sca(axs[4, 0])
            plt.plot(triceps_surae_sumo_force, label="Sumo", color=color_row_4)
            plt.plot(triceps_surae_conve_force, label="Conventional 80%")
            plt.ylabel("Triceps surae [N]")
            plt.legend()
            plt.xlabel(x_label)

            # hip flexors
            plt.sca(axs[4, 1])
            plt.plot(hip_flexors_sumo_force, label="Sumo", color=color_row_4)
            plt.plot(hip_flexors_conv_force, label="Conventional 80%")
            plt.ylabel("Hip flexors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Gluteus minimus
            plt.sca(axs[4, 2])
            plt.plot(gluteusmin_sumo_force, label="Sumo", color=color_row_4)
            plt.plot(gluteusmin_conv_force, label="Conventional 80%")
            plt.ylabel("Gluteus minimus [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)

    if run_total_force_comparison:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            cols = 1
            fig, axs = plt.subplots(cols)
            fig.suptitle(
                "Total Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            # Total forces
            total_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised_1,  # muscle force data
                "All",  # All muscle groups
                "rl",
            )
            total_conv_force = sum_muscle_forces(
                muscleForces_conv_time_normalised_2,  # muscle force data
                "All",  # All muscle groups
                "rl",
            )
            # Total force
            plt.sca(axs[0])
            plt.plot(total_sumo_force, label="Sumo", color="red")
            plt.plot(total_conv_force, label="Conventional 80%")
            plt.ylabel("Total muscle force [N]")
            plt.legend()
            plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_total_force_comparison")
            print(e)

    if run_trail_comparison:
        ### get time normalised mean values of the trails
        ik_trail_0 = ik_conv_time_normalised_1
        ik_trail_1 = ik_conv_time_normalised_2
        ik_mean = ik_conv_mean_values = mean_trail_values(
            ik_conv_time_normalised_1,  # have to be time normalised
            ik_conv_time_normalised_2,
        )
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 2
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Trail Comparison Conventional"
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            # display mean, and trail values

            plot_data(
                axs[0, 0],  # axis
                ik_trail_0["hip_flexion_r"],  # data 1
                "1",  # label data 1
                "red",  # color data 1
                ik_trail_1["hip_flexion_r"],  # data 2
                "2",  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Hip Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(
                ik_mean["hip_flexion_r"], label="MEAN", color="gold"
            )  # add mean curve

            plt.sca(axs[0, 1])
            plt.plot(ik_trail_0["knee_angle_r"], label="1", color="red")
            plt.plot(ik_trail_1["knee_angle_r"], label="2", color="blue")
            plt.plot(ik_mean["knee_angle_r"], label="MEAN", color="gold")
            plt.ylabel("Knee Flexion [°]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(ik_trail_0["ankle_angle_r"], label="1", color="red")
            plt.plot(ik_trail_1["ankle_angle_r"], label="2", color="blue")
            plt.plot(ik_mean["ankle_angle_r"], label="MEAN", color="gold")
            plt.ylabel("Knee Flexion [°]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_trail_comparison")
            print(e)

# END
