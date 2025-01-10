from src.imports import plt, athletes, athlete_0_ik_sumo_1, athlete_0_ik_sumo_2


def run_kinematics_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 5
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics Trails "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            coordinates = [
                "hip_flexion_r",
                "knee_angle_r",
                "ankle_angle_r",
            ]
            ylabels = ["Hip Flex [°]", "Knee Flex [°]", "Ankle Flex [°]"]
            ## kinematics of hip, knee and ankle, and muscle forces
            for i in range(cols):
                for j in range(rows):
                    plt.sca(axs[i, j])
                    plt.plot(
                        athlete_0_ik_sumo_1[coordinates[j]],
                        label="Sumo",
                        color="red",
                    )
                    plt.plot(
                        athlete_0_ik_sumo_2[coordinates[j]],
                        label="Sumo",
                        color="red",
                    )
                    #  plt.plot(
                    #         athlete_0_ik_sumo_2["hip_flexion_r"],
                    #        label="Conventional 80%",
                    # )
                    plt.legend()
                    plt.ylabel([ylabels[j]], color="grey")
                    plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_emptybar_comparison")
            print(e)
