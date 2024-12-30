# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
from msk_modelling_python.src.bops import *
from imports import *  # file paths of the athlete
from local_functions import *  # local functions for the project
import pandas as pd
import matplotlib.pyplot as plt

#####################################################################################

if __name__ == "__main__":

    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_forces_plot = False
    run_emptybar_comparison = False
    run_muscle_force_sum_plot = False
    run_total_force_comparison = True
    run_trail_comparison = False

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
            color_sumo = "red"
            color_conv = "blue"
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

            ## kinematics of hip, knee and ankle, and muscle forces
            plt.sca(axs[0, 0])
            plt.plot(
                ik_sumo_time_normalised_1["hip_flexion_r"],
                color=color_sumo,
                label="Sumo",
            )
            plt.plot(
                ik_conv_time_normalised_1["hip_flexion_r"],
                color=color_conv,
                label="Conventional 80%",
            )
            plt.legend()
            plt.ylabel("Hip Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.plot(
                ik_sumo_time_normalised_1["knee_angle_r"],
                color=color_sumo,
                label="Sumo",
            )
            plt.plot(
                ik_conv_time_normalised_1["knee_angle_r"],
                color=color_conv,
                label="Conventional 80%",
            )
            plt.legend()
            plt.ylabel("Knee Flex [°]", color="grey")
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(
                ik_sumo_time_normalised_1["ankle_angle_r"],
                color=color_sumo,
                label="Sumo",
            )
            plt.plot(
                ik_conv_time_normalised_1["ankle_angle_r"],
                color=color_conv,
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
                color=color_sumo,
            )
            plt.plot(
                id_conv_time_normalised_2["hip_flexion_r_moment"],
                color=color_conv,
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
                color=color_sumo,
            )
            plt.plot(
                id_conv_time_normalised_2["knee_angle_r_moment"],
                color=color_conv,
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
                color=color_sumo,
            )
            plt.plot(
                id_conv_time_normalised_2["ankle_angle_r_moment"],
                color=color_conv,
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
                color=color_sumo,
            )
            plt.plot(
                hamstrings_medial_conv_force, label="Conventional 80%", color=color_conv
            )
            plt.ylabel("Hamstrings medial [N]")
            plt.legend()
            plt.xlabel(x_label)
            # hamstrings lateral
            plt.sca(axs[2, 1])
            plt.plot(
                hamstrings_lateral_sumo_force,
                label="Sumo",
                color=color_sumo,
            )
            plt.plot(
                hamstrings_lateral_conv_force,
                label="Conventional 80%",
                color=color_conv,
            )
            plt.ylabel("Hamstrings lateral [N]")
            plt.legend()
            plt.xlabel(x_label)
            # vasti
            plt.sca(axs[2, 2])
            plt.plot(vasti_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(vasti_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Vasti [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus maximus
            plt.sca(axs[3, 0])
            plt.plot(gluteusmax_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(gluteusmax_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Gluteus maximus [N]")
            plt.legend()
            plt.xlabel(x_label)

            # adductors
            plt.sca(axs[3, 1])
            plt.plot(adductors_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(adductors_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Adductors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus medius
            plt.sca(axs[3, 2])
            plt.plot(gluteusmed_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(gluteusmed_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Gluteus medius [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Triceps surae
            plt.sca(axs[4, 0])
            plt.plot(triceps_surae_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(
                triceps_surae_conve_force, label="Conventional 80%", color=color_conv
            )
            plt.ylabel("Triceps surae [N]")
            plt.legend()
            plt.xlabel(x_label)

            # hip flexors
            plt.sca(axs[4, 1])
            plt.plot(hip_flexors_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(hip_flexors_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Hip flexors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Gluteus minimus
            plt.sca(axs[4, 2])
            plt.plot(gluteusmin_sumo_force, label="Sumo", color=color_sumo)
            plt.plot(gluteusmin_conv_force, label="Conventional 80%", color=color_conv)
            plt.ylabel("Gluteus minimus [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)

    if run_total_force_comparison:
        try:
            fig, axs = plt.subplots(2)
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

            mean_total_force_conv = [0] * 101
            index = 0
            # mean total for two trail files
            for value in total_conv_force_1:
                mean_total_force_conv[index] = (value + total_conv_force_2[index]) / 2
                index += 1

            # Total force between two techniques
            plt.sca(axs[0])
            plt.plot(total_sumo_force_1, label="Sumo", color="red")
            plt.plot(total_conv_force_2, label="Conventional 80%")
            plt.ylabel("Total muscle force [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1])
            plt.plot(total_conv_force_1, label="Conv 1", color="red")
            plt.plot(total_conv_force_2, label="Conv 2", color="blue")
            plt.plot(mean_total_force_conv, label="MEAN", color="magenta")
            plt.ylabel("Total muscle force CONV [N]")
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

# END
