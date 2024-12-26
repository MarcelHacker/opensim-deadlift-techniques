import pandas as pd
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt
import os
import unittest
import msk_modelling_python as msk
import seaborn as sns


if __name__ == "__main__":
    # create figute with 5x3 subplots
    fig, axs = plt.subplots(3, 3)
    fig.suptitle("Deadlift Sumo Forces Athlete_0")
    fig.set_label("Forces R")

    # activate the subplots IK (first row)
    ik_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"

    # activate the subplots muscle forces arms (fourth row)
    muscleForces_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_force.sto"

    # activate the subplots muscle forces arms (fith row)
    muscleActivation_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_activation.sto"

    ik_sumo = pd.read_csv(ik_sumo_path, sep="\t", skiprows=10)
    muscleForces_sumo = pd.read_csv(muscleForces_sumo_path, sep="\t", skiprows=14)
    muscleActivation_sumo = pd.read_csv(
        muscleActivation_sumo_path, sep="\t", skiprows=8
    )
    # returns A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
    if ik_sumo.empty:  # check if file is empty
        print("File is empty:", ik_sumo_path)
    if muscleForces_sumo.empty:
        print("File is empty:", muscleForces_sumo_path)
    if muscleActivation_sumo.empty:
        print("File is empty:", muscleActivation_sumo_path)

    # check for desired columns in ik files
    if "hip_flexion_r" not in ik_sumo.columns:
        print("Desired column not found in file:", ik_sumo_path)

    # sumo deadlift curves, IK
    ## row 0, column 0
    plt.sca(axs[0, 0])
    plt.plot(ik_sumo["time"], ik_sumo["hip_flexion_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Flexion")

    ## row 0, column 1, knee
    plt.sca(axs[0, 1])
    plt.plot(ik_sumo["time"], ik_sumo["knee_angle_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Flexion")

    ## row 0, column 2, ankle
    plt.sca(axs[0, 2])
    plt.plot(ik_sumo["time"], ik_sumo["ankle_angle_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Flexion")

    # sumo deadlift curves, SO, muscle forces
    ## row 1, column 0, hip muscle forces
    plt.sca(axs[1, 0])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["hip_flexion_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Hip Flexion Moment R")

    ## row 1, column 1, knee moments
    plt.sca(axs[1, 1])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["knee_angle_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Knee Angle Moment R")

    ## row 1, column 2, ankle moments
    plt.sca(axs[1, 2])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["ankle_angle_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Angle Moment R")

    # sumo deadlift curves, SO, Muscle activations
    ## row 3, column 0, hip moment arms
    plt.sca(axs[2, 0])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["semiten_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Moment arms R")

    ## row 3, column 1, knee moment arms
    plt.sca(axs[2, 1])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["vaslat_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Moment arms R")

    ## row 3, column 2, ankle moment arms
    plt.sca(axs[2, 2])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["soleus_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Moment arms R")

    plt.show()

# END
