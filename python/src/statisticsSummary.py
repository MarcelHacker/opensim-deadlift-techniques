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


def getNormalizedForces(athlete_number, muscle_group, isPreferred):
    # read muscle group csv
    try:
        muscle_group_csv = pd.read_csv(
            "/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/muscle_forces/"
            + ("preferred" if isPreferred else "non-preferred")
            + "/"
            + muscle_group
            + ".csv",
            sep="\t",
            skiprows=0,
        )
        print("STORED cols:", muscle_group_csv.columns)
        reduced_csv = muscle_group_csv[
            [
                "Trial1_A" + str(athlete_number),
                "Trial2_A" + str(athlete_number),
                "Trial3_A" + str(athlete_number),
                "Trial4_A" + str(athlete_number),
            ]
        ]
        print("returned: ", muscle_group, reduced_csv)
        return reduced_csv
    except Exception as e:
        print(f"Error reading csv: {muscle_group},{e}")


"""
For the muscle forces sum of right and left leg of the trials was used.
"""


def run_muscle_force_groups_summary(bool, save_figures):
    if bool:
        try:
            figure_0_postfix = "_summary"
            label_preferred = "PREFERRED"
            label_non_preferred = "NON-PREFERRED"
            y_label = "Normalized muscle force [N/kg]"
            x_label = "% concentric deadlift cycle"

            preferred_hip_extensors_athlete_0 = getNormalizedForces(
                0, "hip_extensors", True
            )
            non_preferred_hip_extensors_athlete_0 = getNormalizedForces(
                0, "hip_extensors", False
            )
            preferred_hip_flexors_athlete_0 = getNormalizedForces(
                0, "hip_flexors", True
            )
            non_preferred_hip_flexors_athlete_0 = getNormalizedForces(
                0, "hip_flexors", False
            )
            preferred_hip_adductors_athlete_0 = getNormalizedForces(
                0, "hip_adductors", True
            )
            non_preferred_hip_adductors_athlete_0 = getNormalizedForces(
                0, "hip_adductors", False
            )
            preferred_knee_extensors_athlete_0 = getNormalizedForces(
                0, "knee_extensors", True
            )
            non_preferred_knee_extensors_athlete_0 = getNormalizedForces(
                0, "knee_extensors", False
            )

            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Muscle Force Means " + "Athlete 1",
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

            # Hip extensors
            plt.sca(axs_0[0, 0])
            axs_0[0, 0].set_title(
                "Hip extensors",
            )
            plot_means(preferred_hip_extensors_athlete_0, "r", label_preferred)
            plot_means(non_preferred_hip_extensors_athlete_0, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 0])
            axs_0[1, 0].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(
                preferred_hip_extensors_athlete_0, non_preferred_hip_extensors_athlete_0
            )

            # Hip flexors
            plt.sca(axs_0[0, 1])
            axs_0[0, 1].set_title(
                "Hip flexors",
            )
            plot_means(preferred_hip_flexors_athlete_0, "r", label_preferred)
            plot_means(non_preferred_hip_flexors_athlete_0, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 1])
            axs_0[1, 1].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(
                preferred_hip_flexors_athlete_0, non_preferred_hip_flexors_athlete_0
            )

            # Hip adductors
            plt.sca(axs_0[0, 2])
            axs_0[0, 2].set_title(
                "Hip adductors",
            )
            plot_means(preferred_hip_adductors_athlete_0, "r", label_preferred)
            plot_means(non_preferred_hip_adductors_athlete_0, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 2])
            axs_0[1, 2].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(
                preferred_hip_adductors_athlete_0, non_preferred_hip_adductors_athlete_0
            )

            # row 0, column 3
            plt.sca(axs_0[0, 3])
            axs_0[0, 3].set_title(
                "Knee extensors",
            )
            plot_means(preferred_knee_extensors_athlete_0, "r", label_preferred)
            plot_means(non_preferred_knee_extensors_athlete_0, "b", label_non_preferred)

            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 3])
            axs_0[1, 3].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(
                preferred_knee_extensors_athlete_0,
                non_preferred_knee_extensors_athlete_0,
            )

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
            print("Error in statistics summary")
            print(e)
