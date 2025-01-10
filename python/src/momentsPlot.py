from src.imports import (
    plt,
    athlete_0_parsed,
    athlete_0_ik_sumo_time_normalised_1,
    athlete_0_ik_sumo_time_normalised_2,
    athlete_0_ik_conv_time_normalised_1,
    athlete_0_ik_conv_time_normalised_2,
)

active_athlete_json = athlete_0_parsed


def run_moments_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 2
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Joint Moments Trails "
                + active_athlete_json["name"]
                + "; Model: "
                + active_athlete_json["model_name"]
                + "; Preferred: "
                + active_athlete_json["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "hip_flexion_r",
                "knee_angle_r",
                "ankle_angle_r",
            ]
            coordinates_l = [
                "hip_flexion_l",
                "knee_angle_l",
                "ankle_angle_l",
            ]
            ylabels = [
                "Hip Flex [°]",
                "Knee Flex [°]",
                "Ankle Flex [°]",
            ]

            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trail 1 r",
                )
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trail 1 l",
                )
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trail 2 r",
                )
                plt.plot(
                    athlete_0_ik_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trail 2 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                plt.title("Conventional Deadlift")
                plt.plot(
                    athlete_0_ik_conv_time_normalised_1[coordinates_r[i]],
                    label="Trail 1 r",
                )
                plt.plot(
                    athlete_0_ik_conv_time_normalised_1[coordinates_l[i]],
                    label="Trail 1 l",
                )
                plt.plot(
                    athlete_0_ik_conv_time_normalised_2[coordinates_r[i]],
                    label="Trail 2 r",
                )
                plt.plot(
                    athlete_0_ik_conv_time_normalised_2[coordinates_l[i]],
                    label="Trail 2 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_moments_plot")
            print(e)
