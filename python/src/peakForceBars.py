import numpy as np
import pandas as pd
import spm1d
from .imports import (
    plt,
)


def plot_means(array, color_letter, label):
    spm1d.plot.plot_mean_sd(
        array,
        linecolor=color_letter,
        linestyle="-",
        facecolor="0.8",
        edgecolor="0.8",
        alpha=0.5,
        label=label,
        autoset_ylim=True,
        roi=None,
    )


def paired_ttest(varA, varB):
    t = spm1d.stats.ttest_paired(varA, varB)
    ti = t.inference(alpha=0.05, two_tailed=True)
    ti.plot()
    ti.plot_threshold_label()
    ti.plot_p_values()


def getNormalizedPeakForces(athlete_number, muscle_group, isPreferred):
    # read muscle group csv
    try:
        reduced_csv = []
        trial_names = [
            "R_A" + str(athlete_number),
            "L_A" + str(athlete_number),
        ]
        muscle_group_csv = pd.read_csv(
            "/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/muscle_forces/"
            + ("preferred" if isPreferred else "non-preferred")
            + "/"
            + muscle_group
            + ".csv",
            sep="\t",
            skiprows=0,
        )
        for trial in trial_names:
            reduced_csv.append(muscle_group_csv[trial])

        return reduced_csv
    except Exception as e:
        print(f"Error reading peak force csv: {muscle_group},{e}")


def run_peak_muscle_force_bars(bool, save_figures):
    if bool:
        try:
            y_label = "Normalized Peak Muscle Force [N/kg]"
            x_label = "% concentric deadlift cycle"

            figure_0_postfix = "peak_force_summary"
            fig_0, axs_0 = plt.subplots()
            fig_0.suptitle(
                "Peak Muscle Forces; n = 2 (Athlete 0, 2) ",
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.33,
                hspace=0.293,
                top=0.917,
                right=0.921,
                left=0.067,
                bottom=0.06,
            )
            preferred_hip_extensors_athlete_0 = getNormalizedPeakForces(
                0, "hip_extensors", True
            )
            preferred_hip_extensors_athlete_2 = getNormalizedPeakForces(
                2, "hip_extensors", True
            )
            non_preferred_hip_extensors_athlete_0 = getNormalizedPeakForces(
                0, "hip_extensors", False
            )
            non_preferred_hip_extensors_athlete_2 = getNormalizedPeakForces(
                2, "hip_extensors", False
            )

            # Hip extensors
            xlabels = [
                "Athlete 0 SUMO",
                "Athlete 2 SUMO",
                "Athlete 2 CONV",
                "Athlete 0 CONV",
            ]
            peak_forces = [
                np.mean(preferred_hip_extensors_athlete_0),
                np.mean(non_preferred_hip_extensors_athlete_2),
                np.mean(preferred_hip_extensors_athlete_2),
                np.mean(non_preferred_hip_extensors_athlete_0),
            ]
            yerr = [
                np.std(preferred_hip_extensors_athlete_0),
                np.std(non_preferred_hip_extensors_athlete_2),
                np.std(preferred_hip_extensors_athlete_2),
                np.std(non_preferred_hip_extensors_athlete_0),
            ]
            bar_labels = ["Preferred", "Non-preferred", "Preferred", "Non-preferred"]
            bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:blue"]

            axs_0.bar(xlabels, peak_forces, label=bar_labels, color=bar_colors)
            axs_0.errorbar(
                xlabels, peak_forces, yerr=yerr, fmt="o", color="black", elinewidth=3
            )
            axs_0.set_ylabel(y_label)
            axs_0.set_title("Hip Extensors")

            handles, labels = (
                axs_0.get_legend_handles_labels()
            )  # get legend from first plot
            fig_0.legend(handles, labels, loc="center right")
            fig_0.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/" + figure_0_postfix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
            ###############################################################################################################
        except Exception as e:
            print("Error in run_peak_muscle_force_bars")
            print(e)
