from msk_modelling_python.src.bops import *
import msk_modelling_python.src.bops as bp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
    column_1_time_normalised, column_2_time_normalised, column_3_time_normalised
):
    """
    calculate the mean value of the 3 trails
    Input:
    3 columns of the trail files, data frame


    Output:
    Array with the sum of the mean
    """
    mean = [0] * 101  # defined arry length of 101 values

    values_sum = 0
    index = 0
    for value in column_1_time_normalised:
        values_sum = sum(
            value,
            column_2_time_normalised[index],
            column_3_time_normalised[index],
        )
        mean[index] = values_sum / 3  # 3 trails
        index += 1
    print(mean)
    return mean


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
    if muscle_group == "Quadriceps" and limbs == "rl":
        muscles_of_interest = [
            "recfem_r",
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "recfem_l",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]
    if muscle_group == "Gluteus Maximus" and limbs == "rl":
        muscles_of_interest = [
            "glmax1_r",
            "glmax2_r",
            "glmax3_r",
            "glmax1_l",
            "glmax2_l",
            "glmax3_l",
        ]
    if muscle_group == "Gluteus Medius" and limbs == "rl":
        muscles_of_interest = [
            "glmed1_r",
            "glmed2_r",
            "glmed3_r",
            "glmed1_l",
            "glmed2_l",
            "glmed3_l",
        ]
    if muscle_group == "Triceps Surae" and limbs == "rl":
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
    if muscles_of_interest == []:
        print("no muscle sum choosen, in sum_muscle_forces")

    sum_forces = [0] * 101  # defined arry length

    for i in range(len(muscles_of_interest)):
        index = 0
        for value in muscleForces[muscles_of_interest[i]]:
            sum_forces[index] = sum_forces[index] + value
            index += 1
    print(sum_forces)
    return sum_forces


# creating class for athletes list
class athlete:
    def __init__(self, name, mass, model, technique, static_trc_path):
        self.name = name  # "athlete_x"
        self.mass = mass  # "57"
        self.model = model  # "athlete_x"
        self.technique = technique  # "sumo" or "conventional"
        self.static_trc_path = static_trc_path  # "./static_0.trc"


################################ IK files ###########################################
# sumo
ik_sumo_emptybar_path_0 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_emptybar/ik.mot"
ik_sumo_path_0 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"

# conventional
ik_conve_emptybar_path_0 = (
    None  # only emptybar trail in athlete_0 for sumo, not in conve
)
ik_conve_path_0 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg03/ik.mot"
ik_conve_path_1 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/ik.mot"


######################## SO files #####################################
# sumo
muscleForces_sumo_emptybar_path_0 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_emptybar/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"
muscleForces_sumo_path_2 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"
muscleForces_sumo_path_1 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg01/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"

# conventional
muscleForces_conve_path_1 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"
muscleForces_conve_path_2 = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg03/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"

####################################################################

if __name__ == "__main__":

    # todo check mean func
    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_forces_plot = False
    run_emptybar_comparison = False
    run_muscle_force_sum_plot = True

    # creating athlete list
    athletes = []
    # appending instances to list
    athletes.append(
        athlete(
            "athlete_0",
            "57",
            "athlete_0_increased_force_3",
            "conventional",
            "/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/static_00.trc",
        )
    )

    ik_sumo = pd.read_csv(ik_sumo_path_0, sep="\t", skiprows=10)
    ik_conve = pd.read_csv(ik_conve_path_0, sep="\t", skiprows=10)
    ik_sumo_emptybar = pd.read_csv(ik_sumo_emptybar_path_0, sep="\t", skiprows=10)

    muscleForces_sumo = pd.read_csv(muscleForces_sumo_path_2, sep="\t", skiprows=14)
    muscleForces_conve = pd.read_csv(muscleForces_conve_path_2, sep="\t", skiprows=14)
    muscleForces_sumo_emptybar = pd.read_csv(
        muscleForces_sumo_emptybar_path_0, sep="\t", skiprows=14
    )

    if ik_sumo.empty:  # check if file is empty
        print("File is empty:", ik_sumo_path_0)
    if ik_conve.empty:
        print("File is empty:", ik_conve_path_0)
    if muscleForces_sumo.empty:
        print("File is empty:", muscleForces_sumo_path_2)
    if muscleForces_conve.empty:
        print("File is empty:", muscleForces_conve_path_2)

    if "knee_angle_r" not in ik_sumo.columns:
        print("Desired column not found in file:", ik_sumo_path_0)
    if "knee_angle_r" not in ik_conve.columns:
        print("Desired column not found in file:", ik_conve_path_0)

    ### time normalise everything to 101 values
    ik_sumo_time_normalised = time_normalise_df(ik_sumo)
    ik_conve_time_normalised = time_normalise_df(ik_conve)
    ik_sumo_emptybar_time_normalised = time_normalise_df(ik_sumo_emptybar)
    muscleForces_sumo_time_normalised = time_normalise_df(muscleForces_sumo)
    muscleForces_conve_time_normalised = time_normalise_df(muscleForces_conve)
    muscleForces_sumo_emptybar_time_normalised = time_normalise_df(
        muscleForces_sumo_emptybar
    )

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
                            ik_sumo_time_normalised["hip_flexion_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conve_time_normalised["hip_flexion_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Hip Flex [°]", color="grey")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 1:  # knee angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised["knee_angle_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conve_time_normalised["knee_angle_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Knee Flex [°]", color="grey")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 2:  # ankle angles
                        plt.sca(axs[i, j])
                        plt.plot(
                            ik_sumo_time_normalised["ankle_angle_r"],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            ik_conve_time_normalised["ankle_angle_r"],
                            label="Conventional 80%",
                        )
                        plt.ylabel("Ankle Flex [°]", color="grey")
                        plt.legend()
                        plt.xlabel("% concentric deadlift cycle")
                    elif muscle_interest < len(muscles_of_interest):
                        plt.sca(axs[i, j])
                        plt.plot(
                            muscleForces_sumo_time_normalised[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo",
                            color="red",
                        )
                        plt.plot(
                            muscleForces_conve_time_normalised[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Conventional 80%",
                        )
                        plt.ylabel(muscles_of_interest[muscle_interest] + " [N]")
                        muscle_interest += 1
                        plt.legend()
                        plt.xlabel("% concentric deadlift cycle")
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
                            ik_sumo_time_normalised["hip_flexion_r"],
                            label="Sumo",
                        )
                        plt.plot(
                            ik_sumo_emptybar_time_normalised["hip_flexion_r"],
                            label="Sumo emptybar",
                        )
                        plt.legend()
                        plt.ylabel("Hip Flex [°]", color="red")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 1:  # knee angles
                        plt.sca(axs[i, j])
                        plt.plot(ik_sumo_time_normalised["knee_angle_r"], label="Sumo")
                        plt.plot(
                            ik_sumo_emptybar_time_normalised["knee_angle_r"],
                            label="Sumo emptybar",
                        )
                        plt.legend()
                        plt.ylabel("Knee Flex [°]", color="red")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 2:  # ankle angles
                        plt.sca(axs[i, j])
                        plt.plot(ik_sumo_time_normalised["ankle_angle_r"], label="Sumo")
                        plt.plot(
                            ik_sumo_emptybar_time_normalised["ankle_angle_r"],
                            label="Sumo emptybar",
                        )
                        plt.ylabel("Ankle Flex [°]", color="red")
                        plt.legend()
                        plt.xlabel("% concentric deadlift cycle")
                    elif muscle_interest < len(muscles_of_interest):
                        plt.sca(axs[i, j])
                        plt.plot(
                            muscleForces_sumo_time_normalised[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo",
                        )
                        plt.plot(
                            muscleForces_sumo_emptybar_time_normalised[
                                muscles_of_interest[muscle_interest]
                            ],
                            label="Sumo emptybar",
                        )
                        plt.ylabel(muscles_of_interest[muscle_interest] + " [N]")
                        muscle_interest += 1
                        plt.legend()
                        plt.xlabel("% concentric deadlift cycle")
                    else:
                        print("You can plot more curves, my master\n")

            plt.show()

        except Exception as e:
            print("Error in run_emptybar_comparison")
            print(e)

    if run_muscle_force_sum_plot:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 3
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

            hamstrings_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,  # muslce force data
                "Hamstrings",  # Hamstrings
                "rl",
            )
            hamstrings_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,  # muslce force data
                "Hamstrings",  # Hamstrings
                "rl",
            )
            quadriceps_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,
                "Quadriceps",  # Quadriceps
                "rl",
            )
            quadriceps_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,
                "Quadriceps",  # Quadriceps
                "rl",
            )
            gluteusmax_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,
                "Gluteus Maximus",  # Gluteus Maximus
                "rl",
            )
            gluteusmax_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,
                "Gluteus Maximus",  # Gluteus Maximus
                "rl",
            )
            # Gluteus Medius
            gluteusmed_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,
                "Gluteus Medius",
                "rl",
            )
            gluteusmed_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,
                "Gluteus Medius",
                "rl",
            )
            adductors_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,
                "Adductors",  # Adductors
                "rl",
            )
            adductors_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,
                "Adductors",  # Adductors
                "rl",
            )

            # Triceps Surae
            triceps_surae_sumo_force = sum_muscle_forces(
                muscleForces_sumo_time_normalised,
                "Triceps Surae",  # Adductors
                "rl",
            )
            triceps_surae_conve_force = sum_muscle_forces(
                muscleForces_conve_time_normalised,
                "Triceps Surae",  # Adductors
                "rl",
            )

            ## kinematics of hip, knee and ankle, and muscle forces
            plt.sca(axs[0, 0])
            plt.plot(
                ik_sumo_time_normalised["hip_flexion_r"],
                color="lime",
                label="Sumo",
            )
            plt.plot(
                ik_conve_time_normalised["hip_flexion_r"],
                label="Conventional 80%",
                color="darkgreen",
            )
            plt.legend()
            plt.ylabel("Hip Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.plot(
                ik_sumo_time_normalised["knee_angle_r"],
                color="navy",
                label="Sumo",
            )
            plt.plot(
                ik_conve_time_normalised["knee_angle_r"],
                label="Conventional 80%",
                color="peru",
            )
            plt.legend()
            plt.ylabel("Knee Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(
                ik_sumo_time_normalised["ankle_angle_r"], label="Sumo", color="khaki"
            )
            plt.plot(
                ik_conve_time_normalised["ankle_angle_r"],
                label="Conventional 80%",
                color="lightcoral",
            )
            plt.ylabel("Ankle Flex [°]", color="grey")
            plt.legend()
            plt.xlabel(x_label)
            # hamstrings
            plt.sca(axs[1, 0])
            plt.plot(hamstrings_sumo_force, label="Sumo")
            plt.plot(hamstrings_conve_force, label="Conventional 80%", color="blue")
            plt.ylabel("Hamstrings [N]")
            plt.legend()
            plt.xlabel(x_label)
            # quadricpes
            plt.sca(axs[1, 1])
            plt.plot(quadriceps_sumo_force, label="Sumo", color="red")
            plt.plot(quadriceps_conve_force, label="Conventional 80%", color="blue")
            plt.ylabel("Quadriceps [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus maximus
            plt.sca(axs[1, 2])
            plt.plot(gluteusmax_sumo_force, label="Sumo", color="pink")
            plt.plot(gluteusmax_conve_force, label="Conventional 80%", color="purple")
            plt.ylabel("Gluteus maximus [N]")
            plt.legend()
            plt.xlabel(x_label)

            # adductors
            plt.sca(axs[2, 0])
            plt.plot(adductors_sumo_force, label="Sumo", color="cyan")
            plt.plot(adductors_conve_force, label="Conventional 80%", color="olive")
            plt.ylabel("Adductors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus medius
            plt.sca(axs[2, 1])
            plt.plot(gluteusmed_sumo_force, label="Sumo", color="magenta")
            plt.plot(gluteusmed_conve_force, label="Conventional 80%", color="gold")
            plt.ylabel("Gluteus medius [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Triceps surae
            plt.sca(axs[2, 2])
            plt.plot(triceps_surae_sumo_force, label="Sumo", color="chartreuse")
            plt.plot(
                triceps_surae_conve_force, label="Conventional 80%", color="olivedrab"
            )
            plt.ylabel("Triceps surae [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)

# END
