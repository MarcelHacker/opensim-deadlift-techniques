from src.imports import (
    plt,
    athlete_0_ik_sumo_time_normalised_1,
    athlete_0_ik_sumo_time_normalised_2,
)


def run_kinematics_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 3
            fig, axs = plt.subplots(rows)
            fig.suptitle(
                "Kinematics Trails "
                + "athletes[0].name"
                + "; Model: "
                + "athletes[0].model"
                + "; Preferred: "
                + "athletes[0].technique"
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            coordinates = [
                "hip_flexion_r",
                "knee_angle_r",
                "ankle_angle_r",
            ]
            ylabels = ["Hip Flex [°]", "Knee Flex [°]", "Ankle Flex [°]"]
            x = 0
            ## kinematics of hip, knee and ankle, and muscle forces
            for i in range(len(coordinates)):
                print(i)
                plt.sca(axs[i])
                print("hi")
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_1[coordinates[i]],
                    label="Trail 1",
                    color="red",
                )
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_2[coordinates[i]],
                    label="Trail 2",
                    color="blue",
                )
                #  plt.plot(
                #         athlete_0_ik_sumo_2["hip_flexion_r"],
                #        label="Conventional 80%",
                # )
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_kinematics_plot")
            print(e)
