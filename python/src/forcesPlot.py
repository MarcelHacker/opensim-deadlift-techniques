from src.imports import (
    plt,
    athletes,
    ik_sumo_time_normalised_1,
    ik_conv_time_normalised_1,
    muscleForces_sumo_time_normalised_1,
    muscleForces_conv_time_normalised_2,
)


def run_forces_plot(bool):
    if bool:
        try:
            rows = 3
            cols = 5
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics & Muscle Forces "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
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
