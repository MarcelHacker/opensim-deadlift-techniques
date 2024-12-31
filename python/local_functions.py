import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dir_name = "/Users/marcelhacker/Documents/opensim-deadlift-techniques"  # your dircetory


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
            # moment_arms_hip_flexion_r_sumo_path_X
            data["moment_arms_hip_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_r.sto"
            )
            # moment_arms_hip_flexion_l_sumo_path_X
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # moment_arms_hip_flexion_l_sumo_path_X
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_r
            data["moment_arms_knee_angle_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_knee_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_l
            data["moment_arms_knee_angle_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_knee_angle_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_r
            data["moment_arms_ankle_angle_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_ankle_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_l
            data["moment_arms_ankle_angle_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_ankle_angle_l.sto"
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
            # moment_arms_hip_flexion_r_conv_path_X
            data["moment_arms_hip_flexion_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_r.sto"
            )
            # moment_arms_hip_flexion_l_conv_path_X
            data["moment_arms_hip_flexion_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # moment_arms_hip_flexion_l_conv_path_X
            data["moment_arms_hip_flexion_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_r
            data["moment_arms_knee_angle_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_knee_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_l
            data["moment_arms_knee_angle_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_knee_angle_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_r
            data["moment_arms_ankle_angle_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_ankle_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_l
            data["moment_arms_ankle_angle_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "__MuscleAnalysis_MomentArm_ankle_angle_l.sto"
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


def get_mean_trail_values(
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
    data = pd.DataFrame()  # make a new dataFrame

    for column in data_1_time_normalised.columns:
        if data_3_time_normalised == None:
            data[column] = (
                data_1_time_normalised[column] + data_2_time_normalised[column]
            ) / 2
        else:
            data[column] = (
                data_1_time_normalised[column]
                + data_2_time_normalised[column]
                + data_3_time_normalised[column]
            ) / 3
    return data


def get_mean_array_values(
    array_1_time_normalised,
    array_2_time_normalised,
    array_3_time_normalised=None,
):
    """
    calculate the mean value of the given values in arrays
    Input:
    Array with values whit the same context!

    Output:
    Mean of the values in the arrays, as a array.
    """
    array = [0] * 101  # buffer
    i = 0
    if array_3_time_normalised == None:
        for value in array_1_time_normalised:
            array[i] = (value + array_2_time_normalised[i]) / 2  # made for 2 trails
            i += 1
    else:
        for value in array_1_time_normalised:
            array[i] = (
                value + array_2_time_normalised[i] + array_3_time_normalised[i]
            ) / 3  # made for 3 trails
            i += 1

    return array


def sum_both_limb_moments_and_mean_angles(
    ik_file_time_normalised, id_file_time_normalised
):
    angles_and_moments = pd.DataFrame(
        {
            "hip_angle": [],
            "knee_angle": [],
            "ankle_angle": [],
            "hip_flexion_moment": [],
            "knee_flexion_moment": [],
            "ankle_flexion_moment": [],
        }
    )
    # angles
    angles_and_moments["hip_angle"] = (
        ik_file_time_normalised["hip_flexion_r"]
        + ik_file_time_normalised["hip_flexion_l"]
    ) / 2  # mean angle values of both limbs
    angles_and_moments["knee_angle"] = (
        ik_file_time_normalised["knee_angle_r"]
        + ik_file_time_normalised["knee_angle_l"]
    ) / 2  # mean angle values of both limbs
    angles_and_moments["ankle_angle"] = (
        ik_file_time_normalised["ankle_angle_r"]
        + ik_file_time_normalised["ankle_angle_l"]
    ) / 2  # mean angle values of both limbs

    # moments
    angles_and_moments["hip_flexion_moment"] = (
        id_file_time_normalised["hip_flexion_r_moment"]
        + id_file_time_normalised["hip_flexion_l_moment"]
    )
    angles_and_moments["knee_flexion_moment"] = (
        id_file_time_normalised["knee_angle_r_moment"]
        + id_file_time_normalised["knee_angle_l_moment"]
    )
    angles_and_moments["ankle_flexion_moment"] = (
        id_file_time_normalised["ankle_angle_r_moment"]
        + id_file_time_normalised["ankle_angle_l_moment"]
    )

    return angles_and_moments


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
