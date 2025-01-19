from .imports import (
    plt,
    active_athlete,
    active_athlete_total_sumo_force_0,
    active_athlete_total_sumo_force_1,
    active_athlete_total_sumo_force_2,
    active_athlete_total_conv_force_0,
    active_athlete_total_conv_force_1,
    active_athlete_total_conv_force_2,
)


def run_total_muscle_force_plot_trails(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            cols = 2
            color_sumo = "red"
            color_conv = "blue"
            fig, axs = plt.subplots(cols)
            fig.suptitle(
                "Total Muscle Force Trials; "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.386,
                hspace=0.324,
                top=0.901,
                right=0.988,
                left=0.04,
                bottom=0.064,
            )
            fig.set_label("Total Muscle Force [N]")
            x_label = "% concentric deadlift cycle"

            plt.sca(axs[0])
            plt.title("Sumo Deadlift")
            plt.plot(
                active_athlete_total_sumo_force_0,
                label="Trail 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_total_sumo_force_1,
                label="Trail 2",
            )
            plt.plot(
                active_athlete_total_sumo_force_2,
                label="Trail 3",
            )

            plt.sca(axs[1])
            plt.title("Conventional Deadlift")
            plt.plot(
                active_athlete_total_conv_force_0,
                label="Trail 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_total_conv_force_1,
                label="Trail 2",
            )
            plt.plot(
                active_athlete_total_conv_force_2,
                label="Trail 3",
            )

            plt.legend()
            plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_total_muscle_force_plot_trails")
            print(e)
