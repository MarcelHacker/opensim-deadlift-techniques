from .imports import (
    plt,
    active_athlete,
    active_athlete_id_sumo_time_normalised_0,
    active_athlete_id_sumo_time_normalised_1,
    active_athlete_id_sumo_time_normalised_2,
    active_athlete_id_sumo_time_normalised_3,
    active_athlete_id_conv_time_normalised_0,
    active_athlete_id_conv_time_normalised_1,
    active_athlete_id_conv_time_normalised_2,
    active_athlete_id_conv_time_normalised_3,
)


def run_moments_plot(bool):
    if bool:
        try:
            figure_postfix = "_moments_trials"
            rows = 3
            cols = 2
            trial_color_0 = "red"
            trial_color_1 = "blue"
            trial_color_2 = "orange"
            trial_color_3 = "magenta"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Joint Moments Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.285,
                hspace=0.298,
                top=0.904,
                right=0.91,
                left=0.067,
                bottom=0.067,
            )
            fig.set_label("Joint Moments [Nm]")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "hip_flexion_r_moment",
                "knee_angle_r_moment",
                "ankle_angle_r_moment",
            ]
            coordinates_l = [
                "hip_flexion_l_moment",
                "knee_angle_l_moment",
                "ankle_angle_l_moment",
            ]
            ylabels = [
                "Hip Moment [Nm]",
                "Knee Moment [Nm]",
                "Ankle Moment [Nm]",
            ]

            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            plt.savefig(
                "../results/id/" + active_athlete["name"] + figure_postfix + ".png",
                transparent=None,
                dpi=300,
                format="png",
            )
            plt.show()

        except Exception as e:
            print("Error in run_moments_plot")
            print(e)
