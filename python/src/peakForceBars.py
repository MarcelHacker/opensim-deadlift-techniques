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

            figure_0_postfix = "peak_force_summary"
            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Peak Muscle Forces; n = 2 (Athlete 0, 2) ",
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.33,
                hspace=0.293,
                top=0.915,
                right=0.896,
                left=0.051,
                bottom=0.04,
            )
            xlabels_sumo = [
                "Athlete 0",
                "Athlete 2",
            ]
            # Hip extensors
            preferred_sumo_hip_extensors_athlete_0 = getNormalizedPeakForces(
                0, "hip_extensors", True
            )
            non_preferred_sumo_hip_extensors_athlete_2 = getNormalizedPeakForces(
                2, "hip_extensors", False
            )
            peak_forces_sumo_hip_extensors = [
                np.mean(preferred_sumo_hip_extensors_athlete_0),
                np.mean(non_preferred_sumo_hip_extensors_athlete_2),
            ]
            yerr_sumo_hip_extensors = [
                np.std(preferred_sumo_hip_extensors_athlete_0),
                np.std(non_preferred_sumo_hip_extensors_athlete_2),
            ]
            bar_labels = ["Preferred", "Non-preferred"]
            bar_colors = ["tab:red", "tab:blue"]
            rects = axs_0[0, 0].bar(
                xlabels_sumo,
                peak_forces_sumo_hip_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[0, 0].bar_label(rects, label_type="center", color="white")
            axs_0[0, 0].errorbar(
                xlabels_sumo,
                peak_forces_sumo_hip_extensors,
                yerr=yerr_sumo_hip_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[0, 0].set_ylabel(y_label)
            axs_0[0, 0].set_title("Hip Extensors, SDL")

            preferred_conv_hip_extensors_athlete_2 = getNormalizedPeakForces(
                2, "hip_extensors", True
            )
            non_preferred_conv_hip_extensors_athlete_0 = getNormalizedPeakForces(
                0, "hip_extensors", False
            )
            xlabels_conv = [
                "Athlete 2",
                "Athlete 0",
            ]
            peak_forces_conv_hip_extensors = [
                np.mean(preferred_conv_hip_extensors_athlete_2),
                np.mean(non_preferred_conv_hip_extensors_athlete_0),
            ]
            yerr_conv_hip_extensors = [
                np.std(preferred_conv_hip_extensors_athlete_2),
                np.std(non_preferred_conv_hip_extensors_athlete_0),
            ]
            bar_labels = ["Preferred", "Non-preferred"]
            bar_colors = ["tab:red", "tab:blue"]
            rects = axs_0[1, 0].bar(
                xlabels_conv,
                peak_forces_conv_hip_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[1, 0].bar_label(rects, label_type="center", color="white")
            axs_0[1, 0].errorbar(
                xlabels_conv,
                peak_forces_conv_hip_extensors,
                yerr=yerr_conv_hip_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[1, 0].set_ylabel(y_label)
            axs_0[1, 0].set_title("Hip Extensors, CDL")

            # Hip flexors
            preferred_sumo_hip_flexors_athlete_0 = getNormalizedPeakForces(
                0, "hip_flexors", True
            )
            non_preferred_sumo_hip_flexors_athlete_2 = getNormalizedPeakForces(
                2, "hip_flexors", False
            )
            peak_forces_sumo_hip_flexors = [
                np.mean(preferred_sumo_hip_flexors_athlete_0),
                np.mean(non_preferred_sumo_hip_flexors_athlete_2),
            ]
            yerr_sumo_hip_flexors = [
                np.std(preferred_sumo_hip_flexors_athlete_0),
                np.std(non_preferred_sumo_hip_flexors_athlete_2),
            ]
            rects = axs_0[0, 1].bar(
                xlabels_sumo,
                peak_forces_sumo_hip_flexors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[0, 1].bar_label(rects, label_type="center", color="white")
            axs_0[0, 1].errorbar(
                xlabels_sumo,
                peak_forces_sumo_hip_flexors,
                yerr=yerr_sumo_hip_flexors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[0, 1].set_ylabel(y_label)
            axs_0[0, 1].set_title("Hip Flexors, SDL")

            preferred_conv_hip_flexors_athlete_2 = getNormalizedPeakForces(
                2, "hip_flexors", True
            )
            non_preferred_conv_hip_flexors_athlete_0 = getNormalizedPeakForces(
                0, "hip_flexors", False
            )
            peak_forces_conv_hip_flexors = [
                np.mean(preferred_conv_hip_flexors_athlete_2),
                np.mean(non_preferred_conv_hip_flexors_athlete_0),
            ]
            yerr_conv_hip_flexors = [
                np.std(preferred_conv_hip_flexors_athlete_2),
                np.std(non_preferred_conv_hip_flexors_athlete_0),
            ]
            rects = axs_0[1, 1].bar(
                xlabels_conv,
                peak_forces_conv_hip_flexors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[1, 1].bar_label(rects, label_type="center", color="white")
            axs_0[1, 1].errorbar(
                xlabels_conv,
                peak_forces_conv_hip_flexors,
                yerr=yerr_conv_hip_flexors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[1, 1].set_ylabel(y_label)
            axs_0[1, 1].set_title("Hip Flexors, CDL")

            preferred_sumo_hip_adductors_athlete_0 = getNormalizedPeakForces(
                0, "hip_adductors", True
            )
            non_preferred_sumo_hip_adductors_athlete_2 = getNormalizedPeakForces(
                2, "hip_adductors", False
            )
            peak_forces_sumo_hip_adductors = [
                np.mean(preferred_sumo_hip_adductors_athlete_0),
                np.mean(non_preferred_sumo_hip_adductors_athlete_2),
            ]
            yerr_sumo_hip_adductors = [
                np.std(preferred_sumo_hip_adductors_athlete_0),
                np.std(non_preferred_sumo_hip_adductors_athlete_2),
            ]
            rects = axs_0[0, 2].bar(
                xlabels_sumo,
                peak_forces_sumo_hip_adductors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[0, 2].bar_label(rects, label_type="center", color="white")
            axs_0[0, 2].errorbar(
                xlabels_sumo,
                peak_forces_sumo_hip_adductors,
                yerr=yerr_sumo_hip_adductors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[0, 2].set_ylabel(y_label)
            axs_0[0, 2].set_title("Hip Adductors, SDL")

            preferred_conv_hip_adductors_athlete_2 = getNormalizedPeakForces(
                2, "hip_adductors", True
            )
            non_preferred_conv_hip_adductors_athlete_0 = getNormalizedPeakForces(
                0, "hip_adductors", False
            )
            peak_forces_conv_hip_adductors = [
                np.mean(preferred_conv_hip_adductors_athlete_2),
                np.mean(non_preferred_conv_hip_adductors_athlete_0),
            ]
            yerr_conv_hip_adductors = [
                np.std(preferred_conv_hip_adductors_athlete_2),
                np.std(non_preferred_conv_hip_adductors_athlete_0),
            ]
            rects = axs_0[1, 2].bar(
                xlabels_conv,
                peak_forces_conv_hip_adductors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[1, 2].bar_label(rects, label_type="center", color="white")
            axs_0[1, 2].errorbar(
                xlabels_conv,
                peak_forces_conv_hip_adductors,
                yerr=yerr_conv_hip_adductors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[1, 2].set_ylabel(y_label)
            axs_0[1, 2].set_title("Hip Adductors, CDL")

            preferred_sumo_knee_extensors_athlete_0 = getNormalizedPeakForces(
                0, "knee_extensors", True
            )
            non_preferred_sumo_knee_extensors_athlete_2 = getNormalizedPeakForces(
                2, "knee_extensors", False
            )
            peak_forces_sumo_knee_extensors = [
                np.mean(preferred_sumo_knee_extensors_athlete_0),
                np.mean(non_preferred_sumo_knee_extensors_athlete_2),
            ]
            yerr_sumo_knee_extensors = [
                np.std(preferred_sumo_knee_extensors_athlete_0),
                np.std(non_preferred_sumo_knee_extensors_athlete_2),
            ]
            rects = axs_0[0, 3].bar(
                xlabels_sumo,
                peak_forces_sumo_knee_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[0, 3].bar_label(rects, label_type="center", color="white")
            axs_0[0, 3].errorbar(
                xlabels_sumo,
                peak_forces_sumo_knee_extensors,
                yerr=yerr_sumo_knee_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[0, 3].set_ylabel(y_label)
            axs_0[0, 3].set_title("Knee Extensors, SDL")

            preferred_conv_knee_extensors_athlete_2 = getNormalizedPeakForces(
                2, "knee_extensors", True
            )
            non_preferred_conv_knee_extensors_athlete_0 = getNormalizedPeakForces(
                0, "knee_extensors", False
            )
            peak_forces_conv_knee_extensors = [
                np.mean(preferred_conv_knee_extensors_athlete_2),
                np.mean(non_preferred_conv_knee_extensors_athlete_0),
            ]
            yerr_conv_knee_extensors = [
                np.std(preferred_conv_knee_extensors_athlete_2),
                np.std(non_preferred_conv_knee_extensors_athlete_0),
            ]
            rects = axs_0[1, 3].bar(
                xlabels_conv,
                peak_forces_conv_knee_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[1, 3].bar_label(rects, label_type="center", color="white")
            axs_0[1, 3].errorbar(
                xlabels_conv,
                peak_forces_conv_knee_extensors,
                yerr=yerr_conv_knee_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[1, 3].set_ylabel(y_label)
            axs_0[1, 3].set_title("Knee Extensors, CDL")

            handles, labels = axs_0[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
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
