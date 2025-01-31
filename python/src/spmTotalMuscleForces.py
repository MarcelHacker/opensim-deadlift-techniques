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


def run_total_muscle_force_plot_spm(bool, save_figures):
    # just for sumo currently avaiable
    if bool:
        try:
            figure_postfix = "_spm_total_muscle_forces"
            cols = 2
            fig, axs = plt.subplots(cols)
            fig.suptitle(
                "Total Muscle Force Means "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.386,
                hspace=0.362,
                top=0.902,
                right=0.988,
                left=0.076,
                bottom=0.07,
            )
            fig.set_label("Total Muscle Force [N]")
            x_label = "% concentric deadlift cycle"
            y_label = "Muscle Force [N]"

            sumo_array = [
                active_athlete_total_sumo_force_0,
                active_athlete_total_sumo_force_1,
                active_athlete_total_sumo_force_2,
                active_athlete_total_sumo_force_3,
            ]
            conv_array = [
                active_athlete_total_conv_force_0,
                active_athlete_total_conv_force_1,
                active_athlete_total_conv_force_2,
                active_athlete_total_conv_force_3,
            ]
            sumo_array = np.array(sumo_array)
            conv_array = np.array(conv_array)

            plt.sca(axs[0])
            axs[0].set_title(
                "Total Muscle Forces",
                fontweight="bold",
            )
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            spm1d.plot.plot_mean_sd(
                sumo_array,
                linecolor="r",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label="Sumo",
                autoset_ylim=True,
                roi=None,
            )
            spm1d.plot.plot_mean_sd(
                conv_array,
                linecolor="b",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label="Conv",
                autoset_ylim=True,
                roi=None,
            )
            # Add a legend
            plt.legend(axs[0].lines, ["SUMO", "CONV"])

            plt.sca(axs[1])
            axs[1].set_title(
                "Significance Tests",
                fontweight="bold",
            )
            plt.xlabel(x_label)

            t = spm1d.stats.ttest_paired(sumo_array, conv_array)
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()

            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/so/" + active_athlete["name"] + figure_postfix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in run_total_muscle_force_plot_spm")
            print(e)
