import spm1d
import numpy as np
from .imports import (
    plt,
    active_athlete,
    active_athlete_total_sumo_force_0,
    active_athlete_total_sumo_force_1,
    active_athlete_total_sumo_force_2,
    active_athlete_total_sumo_force_3,
    active_athlete_total_conv_force_0,
    active_athlete_total_conv_force_1,
    active_athlete_total_conv_force_2,
    active_athlete_total_conv_force_3,
)


def run_total_muscle_force_plot_trails(bool, save_figures):
    # just for sumo currently avaiable
    if bool:
        try:
            figure_postfix = "_total_muscle_forces_trials"
            cols = 2
            color_sumo = "red"
            color_conv = "blue"
            linestyle_trail_1 = "dotted"
            linestyle_trail_2 = "dashed"
            linestyle_trail_3 = "dashdot"
            fig, axs = plt.subplots(cols)
            fig.suptitle(
                "Total Muscle Force Trials "
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
                linestyle=linestyle_trail_1,
            )
            plt.plot(
                active_athlete_total_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trail_2,
            )
            plt.plot(
                active_athlete_total_sumo_force_3,
                label="Trial 4",
                color=color_sumo,
                linestyle=linestyle_trail_3,
            )
            # axs[0].set_yticks(np.arange(10000, 38000, 3000))
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
                linestyle=linestyle_trail_1,
            )
            plt.plot(
                active_athlete_total_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trail_2,
            )
            plt.plot(
                active_athlete_total_conv_force_3,
                label="Trial 4",
                color=color_conv,
                linestyle=linestyle_trail_3,
            )
            # axs[1].set_yticks(np.arange(10000, 38000, 3000))
            axs[1].set_xticks(np.arange(0, 101, 5))
            axs[1].set_xlim(left=0, right=100)
            plt.legend()
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/so/" + active_athlete["name"] + figure_postfix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            Y = np.random.randn(8, 101)
            Y = spm1d.util.smooth(Y, fwhm=15)
            t = spm1d.stats.ttest(Y)
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            plt.show()

        except Exception as e:
            print("Error in run_total_muscle_force_plot_trails")
            print(e)
