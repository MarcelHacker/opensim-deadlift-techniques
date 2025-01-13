from src.imports import (
    plt,
    active_athlete,
    active_athlete_ik_sumo_time_normalised_0,
    active_athlete_ik_sumo_time_normalised_1,
)


def run_activations_comparison_from_emg(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 3
            cols = 2
            trial_color_0 = "red"
            trial_color_1 = "blue"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Activations Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Activations")
            x_label = "% concentric deadlift cycle"

            coordinates = [
                "hip_flexion_r",
                "knee_angle_r",
                "ankle_angle_r",
            ]
            ylabels = [
                "Hip Flex [°]",
                "Knee Flex [°]",
                "Ankle Flex [°]",
            ]

            for i in range(len(coordinates)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_0[coordinates[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_0[coordinates[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )

                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_activations_comparison_from_emg")
            print(e)
