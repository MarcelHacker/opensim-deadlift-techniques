import numpy as np
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
                top=0.902,
                right=0.988,
                left=0.076,
                bottom=0.07,
            )
            fig.set_label("Total Muscle Force [N]")
            x_label = "% concentric deadlift cycle"
            y_label = "Muscle force [N]"

            plt.sca(axs[0])
            plt.title(
                "Sumo Deadlift",
                fontweight="bold",
            )
            plt.plot(
                active_athlete_total_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_total_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_total_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle="dashdot",
            )
            axs[0].set_yticks(np.arange(10000, 38000, 3000))
            axs[0].set_xticks(np.arange(0, 101, 5))
            axs[0].set_xlim(left=0, right=100)
            plt.legend()
            plt.xlabel(x_label)
            plt.ylabel(y_label)

            plt.sca(axs[1])
            plt.title(
                "Conventional Deadlift",
                fontweight="bold",
            )
            plt.plot(
                active_athlete_total_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_total_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_total_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle="dashdot",
            )
            axs[1].set_yticks(np.arange(10000, 38000, 3000))
            axs[1].set_xticks(np.arange(0, 101, 5))
            axs[1].set_xlim(left=0, right=100)
            plt.legend()
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

        except Exception as e:
            print("Error in run_total_muscle_force_plot_trails")
            print(e)
