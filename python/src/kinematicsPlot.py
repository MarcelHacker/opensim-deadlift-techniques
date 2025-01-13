from src.imports import (
    plt,
    active_athlete,
    active_athlete_ik_sumo_time_normalised_0,
    active_athlete_ik_sumo_time_normalised_1,
    active_athlete_ik_sumo_time_normalised_2,
    active_athlete_ik_conv_time_normalised_0,
    active_athlete_ik_conv_time_normalised_1,
    active_athlete_ik_conv_time_normalised_2,
)


def run_kinematics_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 2
            trial_color_0 = "red"
            trial_color_1 = "blue"
            trial_color_2 = "magenta"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics Trails "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Kinematics")
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
                    active_athlete_ik_sumo_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_ik_conv_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_kinematics_plot")
            print(e)
