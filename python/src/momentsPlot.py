from .imports import (
    plt,
    active_athlete,
    active_athlete_id_sumo_time_normalised_0,
    active_athlete_id_sumo_time_normalised_1,
    active_athlete_id_sumo_time_normalised_2,
    active_athlete_id_conv_time_normalised_0,
    active_athlete_id_conv_time_normalised_1,
    active_athlete_id_conv_time_normalised_2,
)


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
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")
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
                    label="Trail 1 r",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_l[i]],
                    label="Trail 1 l",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trail 2 r",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trail 2 l",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trail 3 r",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trail 3 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_r[i]],
                    label="Trail 1 r",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_l[i]],
                    label="Trail 1 l",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_r[i]],
                    label="Trail 2 r",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_l[i]],
                    label="Trail 2 l",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_r[i]],
                    label="Trail 3 r",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_l[i]],
                    label="Trail 3 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_moments_plot")
            print(e)