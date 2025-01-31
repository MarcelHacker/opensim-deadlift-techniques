import numpy as np
import spm1d
from .imports import (
    plt,
    active_athlete,
    active_athlete_hamstrings_medial_sumo_force_0,
    active_athlete_hamstrings_medial_sumo_force_1,
    active_athlete_hamstrings_medial_sumo_force_2,
    active_athlete_hamstrings_medial_sumo_force_3,
    active_athlete_hamstrings_medial_conv_force_0,
    active_athlete_hamstrings_medial_conv_force_1,
    active_athlete_hamstrings_medial_conv_force_2,
    active_athlete_hamstrings_medial_conv_force_3,
    active_athlete_hamstrings_lateral_sumo_force_0,
    active_athlete_hamstrings_lateral_sumo_force_1,
    active_athlete_hamstrings_lateral_sumo_force_2,
    active_athlete_hamstrings_lateral_sumo_force_3,
    active_athlete_hamstrings_lateral_conv_force_0,
    active_athlete_hamstrings_lateral_conv_force_1,
    active_athlete_hamstrings_lateral_conv_force_2,
    active_athlete_hamstrings_lateral_conv_force_3,
    active_athlete_vasti_sumo_force_0,
    active_athlete_vasti_sumo_force_1,
    active_athlete_vasti_sumo_force_2,
    active_athlete_vasti_sumo_force_3,
    active_athlete_vasti_conv_force_0,
    active_athlete_vasti_conv_force_1,
    active_athlete_vasti_conv_force_2,
    active_athlete_vasti_conv_force_3,
    active_athlete_gluteusmax_sumo_force_0,
    active_athlete_gluteusmax_sumo_force_1,
    active_athlete_gluteusmax_sumo_force_2,
    active_athlete_gluteusmax_sumo_force_3,
    active_athlete_gluteusmax_conv_force_0,
    active_athlete_gluteusmax_conv_force_1,
    active_athlete_gluteusmax_conv_force_2,
    active_athlete_gluteusmax_conv_force_3,
    active_athlete_adductors_sumo_force_0,
    active_athlete_adductors_sumo_force_1,
    active_athlete_adductors_sumo_force_2,
    active_athlete_adductors_sumo_force_3,
    active_athlete_adductors_conv_force_0,
    active_athlete_adductors_conv_force_1,
    active_athlete_adductors_conv_force_2,
    active_athlete_adductors_conv_force_3,
    active_athlete_gluteusmed_sumo_force_0,
    active_athlete_gluteusmed_sumo_force_1,
    active_athlete_gluteusmed_sumo_force_2,
    active_athlete_gluteusmed_sumo_force_3,
    active_athlete_gluteusmed_conv_force_0,
    active_athlete_gluteusmed_conv_force_1,
    active_athlete_gluteusmed_conv_force_2,
    active_athlete_gluteusmed_conv_force_3,
    active_athlete_triceps_surae_sumo_force_0,
    active_athlete_triceps_surae_sumo_force_1,
    active_athlete_triceps_surae_sumo_force_2,
    active_athlete_triceps_surae_sumo_force_3,
    active_athlete_triceps_surae_conv_force_0,
    active_athlete_triceps_surae_conv_force_1,
    active_athlete_triceps_surae_conv_force_2,
    active_athlete_triceps_surae_conv_force_3,
    active_athlete_hip_flexors_sumo_force_0,
    active_athlete_hip_flexors_sumo_force_1,
    active_athlete_hip_flexors_sumo_force_2,
    active_athlete_hip_flexors_sumo_force_3,
    active_athlete_hip_flexors_conv_force_0,
    active_athlete_hip_flexors_conv_force_1,
    active_athlete_hip_flexors_conv_force_2,
    active_athlete_hip_flexors_conv_force_3,
    active_athlete_gluteusmin_sumo_force_0,
    active_athlete_gluteusmin_sumo_force_1,
    active_athlete_gluteusmin_sumo_force_2,
    active_athlete_gluteusmin_sumo_force_3,
    active_athlete_gluteusmin_conv_force_0,
    active_athlete_gluteusmin_conv_force_1,
    active_athlete_gluteusmin_conv_force_2,
    active_athlete_gluteusmin_conv_force_3,
)

"""
For the muscle forces sum of right and left leg of the trails was used.
"""


def run_muscle_force_groups_spm(bool, save_figures):
    if bool:
        try:
            figure_0_postfix = "_spm_hip_extensors_muscle_force"
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "SUMO"
            label_conv = "CONV"
            y_label = "Muscle force [N]"
            x_label = "% concentric deadlift cycle"

            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Muscle Force Hip Extensors Means "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
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

            hamstrings_medial_sumo = [
                active_athlete_hamstrings_medial_sumo_force_0,
                active_athlete_hamstrings_medial_sumo_force_1,
                active_athlete_hamstrings_medial_sumo_force_2,
                active_athlete_hamstrings_medial_sumo_force_3,
            ]

            hamstrings_medial_conv = [
                active_athlete_hamstrings_medial_conv_force_0,
                active_athlete_hamstrings_medial_conv_force_1,
                active_athlete_hamstrings_medial_conv_force_2,
                active_athlete_hamstrings_medial_conv_force_3,
            ]
            hamstrings_medial_sumo = np.array(hamstrings_medial_sumo)
            hamstrings_medial_conv = np.array(hamstrings_medial_conv)

            # hamstrings medial
            plt.sca(axs_0[0, 0])
            axs_0[0, 0].set_title(
                "Hamstrings medial",
            )
            spm1d.plot.plot_mean_sd(
                hamstrings_medial_sumo,
                linecolor="r",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_sumo,
                autoset_ylim=True,
                roi=None,
            )
            spm1d.plot.plot_mean_sd(
                hamstrings_medial_conv,
                linecolor="b",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_conv,
                autoset_ylim=True,
                roi=None,
            )
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 0])
            axs_0[1, 0].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            t = spm1d.stats.ttest_paired(hamstrings_medial_sumo, hamstrings_medial_conv)
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()

            hamstrings_lateral_sumo = [
                active_athlete_hamstrings_lateral_sumo_force_0,
                active_athlete_hamstrings_lateral_sumo_force_1,
                active_athlete_hamstrings_lateral_sumo_force_2,
                active_athlete_hamstrings_lateral_sumo_force_3,
            ]

            hamstrings_lateral_conv = [
                active_athlete_hamstrings_lateral_conv_force_0,
                active_athlete_hamstrings_lateral_conv_force_1,
                active_athlete_hamstrings_lateral_conv_force_2,
                active_athlete_hamstrings_lateral_conv_force_3,
            ]
            hamstrings_lateral_sumo = np.array(hamstrings_lateral_sumo)
            hamstrings_lateral_conv = np.array(hamstrings_lateral_conv)

            # hamstrings lateral
            plt.sca(axs_0[0, 1])
            axs_0[0, 1].set_title(
                "Hamstrings lateral",
            )
            spm1d.plot.plot_mean_sd(
                hamstrings_lateral_sumo,
                linecolor="r",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_sumo,
                autoset_ylim=True,
                roi=None,
            )
            spm1d.plot.plot_mean_sd(
                hamstrings_lateral_conv,
                linecolor="b",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_conv,
                autoset_ylim=True,
                roi=None,
            )
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 1])
            axs_0[1, 1].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            t = spm1d.stats.ttest_paired(
                hamstrings_lateral_sumo, hamstrings_lateral_conv
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()

            adductors_sumo = [
                active_athlete_adductors_sumo_force_0,
                active_athlete_adductors_sumo_force_1,
                active_athlete_adductors_sumo_force_2,
                active_athlete_adductors_sumo_force_3,
            ]

            adductors_conv = [
                active_athlete_adductors_conv_force_0,
                active_athlete_adductors_conv_force_1,
                active_athlete_adductors_conv_force_2,
                active_athlete_adductors_conv_force_3,
            ]
            adductors_sumo = np.array(adductors_sumo)
            adductors_conv = np.array(adductors_conv)

            # hamstrings lateral
            plt.sca(axs_0[0, 2])
            axs_0[0, 2].set_title(
                "Adductors",
            )
            spm1d.plot.plot_mean_sd(
                adductors_sumo,
                linecolor="r",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_sumo,
                autoset_ylim=True,
                roi=None,
            )
            spm1d.plot.plot_mean_sd(
                adductors_conv,
                linecolor="b",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_conv,
                autoset_ylim=True,
                roi=None,
            )
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 2])
            axs_0[1, 2].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            t = spm1d.stats.ttest_paired(adductors_sumo, adductors_conv)
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()

            # active_athlete_gluteusmax_sumo_force_0

            gluteusmax_sumo = [
                active_athlete_gluteusmax_sumo_force_0,
                active_athlete_gluteusmax_sumo_force_1,
                active_athlete_gluteusmax_sumo_force_2,
                active_athlete_gluteusmax_sumo_force_3,
            ]

            gluteusmax_conv = [
                active_athlete_gluteusmax_conv_force_0,
                active_athlete_gluteusmax_conv_force_1,
                active_athlete_gluteusmax_conv_force_2,
                active_athlete_gluteusmax_conv_force_3,
            ]
            gluteusmax_sumo = np.array(gluteusmax_sumo)
            gluteusmax_conv = np.array(gluteusmax_conv)

            # gluteus maximus
            # row 0, column 3
            plt.sca(axs_0[0, 3])
            axs_0[0, 3].set_title(
                "Gluteus maximus",
            )
            spm1d.plot.plot_mean_sd(
                gluteusmax_sumo,
                linecolor="r",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_sumo,
                autoset_ylim=True,
                roi=None,
            )
            spm1d.plot.plot_mean_sd(
                gluteusmax_conv,
                linecolor="b",
                linestyle="-",
                facecolor="0.8",
                edgecolor="0.8",
                alpha=0.5,
                label=label_conv,
                autoset_ylim=True,
                roi=None,
            )
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 3])
            axs_0[1, 3].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            t = spm1d.stats.ttest_paired(gluteusmax_sumo, gluteusmax_conv)
            ti = t.inference(alpha=0.05, two_tailed=True)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()

            handles, labels = axs_0[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_0.legend(handles, labels, loc="center right")
            fig_0.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/so/mean/"
                    + active_athlete["name"]
                    + figure_0_postfix
                    + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_groups_spm")
            print(e)
