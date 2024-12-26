import pandas as pd
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt
import os
import unittest
import msk_modelling_python as msk
import seaborn as sns


if __name__ == "__main__":

    run_quadriceps_plot = True

    # activate the subplots IK
    ik_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"
    ik_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"

    # activate the subplots muscle forces
    muscleForces_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_force.sto"
    muscleForces_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/Athlete0_scaled_StaticOptimization_force.sto"

    ik_sumo = pd.read_csv(ik_sumo_path, sep="\t", skiprows=10)
    ik_conve = pd.read_csv(ik_conve_path, sep="\t", skiprows=10)

    muscleForces_sumo = pd.read_csv(muscleForces_sumo_path, sep="\t", skiprows=14)
    muscleForces_conve = pd.read_csv(muscleForces_conve_path, sep="\t", skiprows=14)

    if run_quadriceps_plot:
        try:
            # create figure with 5x2 subplots (1 for sumo and 1 for conventional)
            fig, axs = plt.subplots(5, 2)
            fig.suptitle(
                "Deadlift Quadriceps Forces Athlete_0; Model: athlete_0_increased_force_3 "
            )
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

            plt.show()

        except Exception as e:
            print("Error in run_quadriceps_plot")
            print(e)

# END
