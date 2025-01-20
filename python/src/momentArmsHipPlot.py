from .imports import (
    plt,
    active_athlete,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_0,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_1,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_1,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_2,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_2,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_0,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_1,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_1,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_2,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_2,
)


def run_moment_arms_hip_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            figure_prefix = "moment_arms_hip_flexion_"
            rows = 6
            cols = 2
            color_trial_0 = "red"
            color_trial_1 = "blue"
            color_trial_2 = "orange"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Moment Arms Hip Flexion Trails "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.743,
                hspace=0.324,
                top=0.904,
                right=0.91,
                left=0.067,
                bottom=0.073,
            )
            fig.set_label("Moment arms [m]")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "recfem_r",
                "semiten_r",
                "addmagIsch_r",
                "glmax1_r",
                "glmax2_r",
                "glmax3_r",
            ]
            coordinates_l = [
                "recfem_l",
                "semiten_l",
                "addmagIsch_l",
                "glmax1_l",
                "glmax2_l",
                "glmax3_l",
            ]
            ylabels = [
                "Rectus femoris [m]",
                "Semitendinosus [m]",
                "Adductor magnus isch [m]",
                "Gluteus maximus 1 [m]",
                "Gluteus maximus 2 [m]",
                "Gluteus maximus 3 [m]",
            ]
            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0[
                        coordinates_r[i]
                    ],
                    label="Trail 1 r",
                    color=color_trial_0,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_0[
                        coordinates_l[i]
                    ],
                    label="Trail 1 l",
                    color=color_trial_0,
                    linestyle="dotted",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_1[
                        coordinates_r[i]
                    ],
                    label="Trail 2 r",
                    color=color_trial_1,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_1[
                        coordinates_l[i]
                    ],
                    label="Trail 2 l",
                    color=color_trial_1,
                    linestyle="dotted",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_2[
                        coordinates_r[i]
                    ],
                    label="Trail 3 r",
                    color=color_trial_2,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_2[
                        coordinates_l[i]
                    ],
                    label="Trail 3 l",
                    color=color_trial_2,
                    linestyle="dotted",
                )
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for x in range(len(coordinates_r)):
                plt.sca(axs[1, x])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0[
                        coordinates_r[x]
                    ],
                    label="Trail 1 r",
                    color=color_trial_0,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_0[
                        coordinates_l[x]
                    ],
                    label="Trail 1 l",
                    color=color_trial_0,
                    linestyle="dotted",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_1[
                        coordinates_r[x]
                    ],
                    label="Trail 2 r",
                    color=color_trial_1,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_1[
                        coordinates_l[x]
                    ],
                    label="Trail 2 l",
                    color=color_trial_1,
                    linestyle="dotted",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_2[
                        coordinates_r[x]
                    ],
                    label="Trail 3 r",
                    color=color_trial_2,
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_2[
                        coordinates_l[x]
                    ],
                    label="Trail 3 l",
                    color=color_trial_2,
                    linestyle="dotted",
                )
                plt.ylabel(ylabels[x])
                plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            plt.savefig(
                "../results/ma/" + figure_prefix + active_athlete["name"] + ".png",
                transparent=None,
                dpi=300,
                format="png",
            )
            plt.show()

        except Exception as e:
            print("Error in run_moment_arms_hip_plot")
            print(e)
