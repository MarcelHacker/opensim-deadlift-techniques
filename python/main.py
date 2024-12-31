# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
from msk_modelling_python.src.bops import *
from src.imports import *  # file paths of the athlete
from src.local_functions import *  # local functions for the project
from src.forcesPlot import run_forces_plot
from src.emptyBarComparison import run_emptybar_comparison
from src.completePlot import run_complete_plot
from src.muscleForceSum import run_muscle_force_sum_plot
import pandas as pd
import matplotlib.pyplot as plt

#####################################################################################

if __name__ == "__main__":

    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_total_force_comparison = False
    run_trail_comparison = False

    run_forces_plot(False)  # angles and single muscles
    run_emptybar_comparison(False)
    run_complete_plot(False)
    run_muscle_force_sum_plot(True)

    if run_total_force_comparison:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(1)
            fig.suptitle(
                "Total Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Total muscle force [N]")

            # Total force between two techniques
            plt.sca(axs)
            plt.plot(total_muscle_forces_sumo_mean, label=label_sumo, color=color_sumo)
            plt.plot(total_muscle_forces_conv_mean, label=label_conv, color=color_conv)
            plt.ylabel("Total muscle force [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_total_force_comparison")
            print(e)

    if run_trail_comparison:
        try:
            fig, axs = plt.subplots(2, 3)
            fig.suptitle(
                "Trail Comparison Conventional "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"
            label_data_1 = "1 conv trail"
            label_data_2 = "2 conv trail"

            # display mean, and trail values
            plot_data(
                axs[0, 0],  # axis
                muscleForces_conv_time_normalised_1["hip_flexion_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["hip_flexion_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Hip Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(
                ik_conv_mean["hip_flexion_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[0, 1],  # axis
                muscleForces_conv_time_normalised_1["knee_angle_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["knee_angle_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Knee Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(ik_conv_mean["knee_angle_r"], label="MEAN", color="gold")

            plot_data(
                axs[0, 2],  # axis
                muscleForces_conv_time_normalised_1["ankle_angle_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["ankle_angle_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Ankle Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(ik_conv_mean["ankle_angle_r"], label="MEAN", color="gold")

            plot_data(
                axs[1, 0],  # axis
                muscleForces_conv_time_normalised_1["vaslat_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["vaslat_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "vaslat_r [N]",  # y label
                x_label,
            ),
            plt.plot(
                muscle_forces_conv_mean["vaslat_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[1, 1],  # axis
                muscleForces_conv_time_normalised_1["semiten_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["semiten_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "semiten_r [N]",  # y label
                x_label,
            ),
            plt.plot(
                muscle_forces_conv_mean["semiten_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[1, 2],  # axis
                muscleForces_conv_time_normalised_1["glmax3_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["glmax3_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "glmax3_r [N]",  # y label
                x_label,
            ),
            plt.sca(axs[1, 2])
            plt.plot(
                muscle_forces_conv_mean["glmax3_r"], label="MEAN", color="gold"
            )  # add mean curve

            plt.show()

        except Exception as e:
            print("Error in run_trail_comparison")
            print(e)
