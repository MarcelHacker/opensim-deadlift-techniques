import numpy as np
import pandas as pd
import spm1d
from .imports import (
    plt,
    active_athlete,
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


def getNormalizedForces(muscle_group, isPreferred):
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
        print("STORED MUSCLE Groups:", muscle_group_csv.columns)
        print(type(muscle_group_csv))
        return muscle_group_csv
    except Exception as e:
        print(f"Error reading csv: {muscle_group},{e}")


"""
For the muscle forces sum of right and left leg of the trails was used.
"""


def run_muscle_force_groups_overall(bool, save_figures):
    if bool:
        try:
            figure_0_prefix = "overall_hip_extensors"
            label_preferred = "PREFERRED"
            label_non_preferred = "NON-PREFERRED"
            y_label = "Normalized muscle force [N/kg]"
            x_label = "% concentric deadlift cycle"

            preferred_hamstrings_medial = getNormalizedForces("hamstrings_medial", True)
            non_preferred_hamstrings_medial = getNormalizedForces(
                "hamstrings_medial", False
            )
            preferred_hamstrings_lateral = getNormalizedForces(
                "hamstrings_lateral", True
            )
            non_preferred_hamstrings_lateral = getNormalizedForces(
                "hamstrings_lateral", False
            )
            preferred_adductors = getNormalizedForces("adductors", True)
            non_preferred_adductors = getNormalizedForces("adductors", False)

            preferred_gluteus_maximus = getNormalizedForces("gluteus_maximus", True)
            non_preferred_gluteus_maximus = getNormalizedForces(
                "gluteus_maximus", False
            )

            preferred_vastus_lateralis = getNormalizedForces("vastus_lateralis", True)
            non_preferred_vastus_lateralis = getNormalizedForces(
                "vastus_lateralis", False
            )
            preferred_vastus_medialis = getNormalizedForces("vastus_medialis", True)
            non_preferred_vastus_medialis = getNormalizedForces(
                "vastus_medialis", False
            )
            preferred_vastus_intermedius = getNormalizedForces(
                "vastus_intermedius", True
            )
            non_preferred_vastus_intermedius = getNormalizedForces(
                "vastus_intermedius", False
            )
            preferred_rectus_femoris = getNormalizedForces("rectus_femoris", True)
            non_preferred_rectus_femoris = getNormalizedForces("rectus_femoris", False)

            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Muscle Force Means Hip Extensors Overall; " + "n = 2 (Athlete 0, 2)",
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

            # hamstrings medial
            plt.sca(axs_0[0, 0])
            axs_0[0, 0].set_title(
                "Hamstrings medial",
            )
            plot_means(preferred_hamstrings_medial, "r", label_preferred)
            plot_means(non_preferred_hamstrings_medial, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 0])
            axs_0[1, 0].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(preferred_hamstrings_medial, non_preferred_hamstrings_medial)

            # hamstrings lateral
            plt.sca(axs_0[0, 1])
            axs_0[0, 1].set_title(
                "Hamstrings lateral",
            )
            plot_means(preferred_hamstrings_lateral, "r", label_preferred)
            plot_means(non_preferred_hamstrings_lateral, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 1])
            axs_0[1, 1].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(preferred_hamstrings_lateral, non_preferred_hamstrings_lateral)

            # hamstrings lateral
            plt.sca(axs_0[0, 2])
            axs_0[0, 2].set_title(
                "Adductors",
            )
            plot_means(preferred_adductors, "r", label_preferred)
            plot_means(non_preferred_adductors, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 2])
            axs_0[1, 2].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(preferred_adductors, non_preferred_adductors)

            # gluteus maximus
            # row 0, column 3
            plt.sca(axs_0[0, 3])
            axs_0[0, 3].set_title(
                "Gluteus maximus",
            )
            plot_means(preferred_gluteus_maximus, "r", label_preferred)
            plot_means(non_preferred_gluteus_maximus, "b", label_non_preferred)

            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 3])
            axs_0[1, 3].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(preferred_gluteus_maximus, non_preferred_gluteus_maximus)

            handles, labels = axs_0[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_0.legend(handles, labels, loc="center right")
            fig_0.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/" + figure_0_prefix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
            ###############################################################################################################

            figure_1_prefix = "overall_knee_extensors"
            fig_1, axs_1 = plt.subplots(2, 4)
            fig_1.suptitle(
                "Muscle Force Means Knee Extensors Overall; " + "n = 2 (Athlete 0, 2)",
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

            # vastus lateralis
            # row 0, column 0
            plt.sca(axs_1[0, 0])
            axs_1[0, 0].set_title(
                "Vastus lateralis",
            )
            plot_means(preferred_vastus_lateralis, "r", label_preferred)
            plot_means(non_preferred_vastus_lateralis, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 0])
            axs_1[1, 0].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(preferred_vastus_lateralis, non_preferred_vastus_lateralis)

            # vastus medialis
            # row 0, column 1
            plt.sca(axs_1[0, 1])
            axs_1[0, 1].set_title(
                "Vastus medialis",
            )
            plot_means(preferred_vastus_medialis, "r", label_preferred)
            plot_means(non_preferred_vastus_medialis, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 1])
            axs_1[1, 1].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(preferred_vastus_medialis, non_preferred_vastus_medialis)

            # vastus intermedius
            # row 0, column 2
            plt.sca(axs_1[0, 2])
            axs_1[0, 2].set_title(
                "Vastus intermedius",
            )
            plot_means(preferred_vastus_intermedius, "r", label_preferred)
            plot_means(non_preferred_vastus_intermedius, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 2])
            axs_1[1, 2].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(preferred_vastus_intermedius, non_preferred_vastus_intermedius)

            # rectus femoris
            # row 0, column 3
            plt.sca(axs_1[0, 3])
            axs_1[0, 3].set_title(
                "Rectus femoris",
            )
            plot_means(preferred_rectus_femoris, "r", label_preferred)
            plot_means(non_preferred_rectus_femoris, "b", label_non_preferred)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 3])
            axs_1[1, 3].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(preferred_rectus_femoris, non_preferred_rectus_femoris)

            handles, labels = axs_1[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_1.legend(handles, labels, loc="center right")
            fig_1.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/" + figure_1_prefix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in statistics overall")
            print(e)
