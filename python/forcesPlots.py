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


# Python3 code here creating class
class athlete:
    def __init__(self, name, mass, model, technique):
        self.name = name
        self.mass = mass
        self.model = model
        self.technique = technique  # or conventional


if __name__ == "__main__":

    run_forces_plot = True
    run_muscle_force_sum_plot = False

    # creating athlete list
    athletes = []
    # appending instances to list
    athletes.append(
        athlete("athlete_0", "57", "athlete_0_increased_force_3", "conventional")
    )

    # activate the subplots IK
    ik_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"
    ik_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/ik.mot"

    # activate the subplots muscle forces
    muscleForces_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_force.sto"
    muscleForces_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/Athlete0_scaled_increased_force_3_StaticOptimization_force.sto"

    ik_sumo = pd.read_csv(ik_sumo_path, sep="\t", skiprows=10)
    ik_conve = pd.read_csv(ik_conve_path, sep="\t", skiprows=10)

    muscleForces_sumo = pd.read_csv(muscleForces_sumo_path, sep="\t", skiprows=14)
    muscleForces_conve = pd.read_csv(muscleForces_conve_path, sep="\t", skiprows=14)

    if ik_sumo.empty:  # check if file is empty
        print("File is empty:", ik_sumo_path)
    if ik_conve.empty:
        print("File is empty:", ik_conve_path)
    if muscleForces_sumo.empty:
        print("File is empty:", muscleForces_sumo_path)
    if muscleForces_conve.empty:
        print("File is empty:", muscleForces_conve_path)

    if "knee_angle_r" not in ik_sumo.columns:
        print("Desired column not found in file:", ik_sumo_path)
    if "knee_angle_r" not in ik_conve.columns:
        print("Desired column not found in file:", ik_conve_path)

    ### time normalise everything to 101 values
    ik_sumo_time_normalised = time_normalise_df(ik_sumo)
    ik_conve_time_normalised = time_normalise_df(ik_conve)
    muscleForces_sumo_time_normalised = time_normalise_df(muscleForces_sumo)
    muscleForces_conve_time_normalised = time_normalise_df(muscleForces_conve)

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
                        )
                        plt.plot(
                            ik_conve_time_normalised["hip_flexion_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Hip Flex [°]", color="red")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 1:  # knee angles
                        plt.sca(axs[i, j])
                        plt.plot(ik_sumo_time_normalised["knee_angle_r"], label="Sumo")
                        plt.plot(
                            ik_conve_time_normalised["knee_angle_r"],
                            label="Conventional 80%",
                        )
                        plt.legend()
                        plt.ylabel("Knee Flex [°]", color="red")
                        plt.xlabel("% concentric deadlift cycle")
                    elif i == 0 and j == 2:  # ankle angles
                        plt.sca(axs[i, j])
                        plt.plot(ik_sumo_time_normalised["ankle_angle_r"], label="Sumo")
                        plt.plot(
                            ik_conve_time_normalised["ankle_angle_r"],
                            label="Conventional 80%",
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

    if run_muscle_force_sum_plot:
        try:
            # create figure with 5x2 subplots (1 for sumo and 1 for conventional)
            fig, axs = plt.subplots(5, 2)
            fig.suptitle("Muscle Forces Athlete_0; Model: athlete_0_increased_force_3 ")
            fig.set_label("Muscle Forces R")

            if ik_sumo.empty:  # check if file is empty
                print("File is empty:", ik_sumo_path)
            if ik_conve.empty:
                print("File is empty:", ik_conve_path)
            if muscleForces_sumo.empty:
                print("File is empty:", muscleForces_sumo_path)
            if muscleForces_conve.empty:
                print("File is empty:", muscleForces_conve_path)

            if "knee_angle_r" not in ik_sumo.columns:
                print("Desired column not found in file:", ik_sumo_path)
            if "knee_angle_r" not in ik_conve.columns:
                print("Desired column not found in file:", ik_conve_path)

            # create muscle sum arrays
            # initialize data of lists.
            muscle_forces_data = {
                "hamstrings_r": [],
                "gluteus_maximus_r": [],
                "quadriceps_r": [],
                "adductors_r": [],
            }

            for val in muscleForces_sumo["recfem_r"]:
                muscle_forces_data["quadriceps_r"] += val

            print(muscleForces_sumo["recfem_r"])
            print(muscle_forces_data["quadriceps_r"])

            # Create DataFrame
            sum_muscle_forces = pd.DataFrame(muscle_forces_data)
            ## row 0
            axs[0, 0].set_title("Sumo Deadlift 80kg")
            plt.sca(axs[0, 0])
            plt.plot(ik_sumo["time"], ik_sumo["knee_angle_r"])
            plt.xlabel("Time")
            plt.ylabel("Knee Flexion")

            axs[0, 1].set_title("Conventional Deadlift 80kg", color="red")
            plt.sca(axs[0, 1])
            plt.plot(ik_conve["time"], ik_conve["knee_angle_r"])
            plt.title("Conventional Deadlift 80kg")
            plt.xlabel("Time")
            plt.ylabel("Knee Flexion")

            plt.sca(axs[1, 0])
            plt.plot(muscleForces_sumo["time"], muscleForces_sumo["recfem_r"])
            plt.xlabel("Time")
            plt.ylabel("Recfem_r")

            plt.sca(axs[1, 1])
            plt.plot(muscleForces_conve["time"], muscleForces_conve["recfem_r"])
            plt.xlabel("Time")
            plt.ylabel("Recfem_r")

            plt.sca(axs[2, 0])
            plt.plot(muscleForces_sumo["time"], muscleForces_sumo["vaslat_r"])
            plt.xlabel("Time")
            plt.ylabel("Vaslat_r")

            plt.sca(axs[2, 1])
            plt.plot(muscleForces_conve["time"], muscleForces_conve["vaslat_r"])
            plt.xlabel("Time")
            plt.ylabel("Vaslat_r")

            plt.sca(axs[3, 0])
            plt.plot(muscleForces_sumo["time"], muscleForces_sumo["vasmed_r"])
            plt.xlabel("Time")
            plt.ylabel("Vasmed_r")

            plt.sca(axs[3, 1])
            plt.plot(muscleForces_conve["time"], muscleForces_conve["vasmed_r"])
            plt.xlabel("Time")
            plt.ylabel("Vasmed_r")

            plt.sca(axs[4, 0])
            plt.plot(muscleForces_sumo["time"], muscleForces_sumo["vasint_r"])
            plt.xlabel("Time")
            plt.ylabel("Vasint_r")

            plt.sca(axs[4, 1])
            plt.plot(muscleForces_conve["time"], muscleForces_conve["vasint_r"])
            plt.xlabel("Time")
            plt.ylabel("Vasint_r")

            # plt.show()

        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)

# END
