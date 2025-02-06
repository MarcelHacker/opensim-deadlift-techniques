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


def getNormalizedForces(athlete_number, muscle_group, technique):
    # read muscle group csv
    try:
        reduced_csv = []
        trial_names = [
            "Trial1_A" + str(athlete_number),
            "Trial2_A" + str(athlete_number),
            "Trial3_A" + str(athlete_number),
            "Trial4_A" + str(athlete_number),
        ]
        muscle_group_csv = pd.read_csv(
            "/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/muscle_forces/"
            + technique
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
        print(f"Error reading csv: {muscle_group},{e}")


def run_muscle_force_groups_summary(bool, save_figures):
    if bool:
        try:
            figure_0_postfix = "spm_check_athlete_0"
            label_sumo = "SUMO"
            label_conv = "CONV"
            y_label = "Normalized muscle force [N/kg]"
            x_label = "% concentric deadlift cycle"

            sumo_hip_extensors_r_athlete_0 = getNormalizedForces(
                0, "hip_extensors_r", "sumo"
            )
            sumo_hip_extensors_r_athlete_2 = getNormalizedForces(
                2, "hip_extensors_r", "sumo"
            )
            sumo_hip_extensors_l_athlete_0 = getNormalizedForces(
                0, "hip_extensors_l", "sumo"
            )
            sumo_hip_extensors_l_athlete_2 = getNormalizedForces(
                2, "hip_extensors_l", "sumo"
            )
            conv_hip_extensors_r_athlete_0 = getNormalizedForces(
                0, "hip_extensors_r", "conv"
            )
            conv_hip_extensors_r_athlete_2 = getNormalizedForces(
                2, "hip_extensors_r", "conv"
            )
            conv_hip_extensors_l_athlete_0 = getNormalizedForces(
                0, "hip_extensors_l", "conv"
            )
            conv_hip_extensors_l_athlete_2 = getNormalizedForces(
                2, "hip_extensors_l", "conv"
            )
            sumo_hip_flexors_r_athlete_0 = getNormalizedForces(
                0, "hip_flexors_r", "sumo"
            )
            sumo_hip_flexors_r_athlete_2 = getNormalizedForces(
                2, "hip_flexors_r", "sumo"
            )
            sumo_hip_flexors_l_athlete_0 = getNormalizedForces(
                0, "hip_flexors_l", "sumo"
            )
            sumo_hip_flexors_l_athlete_2 = getNormalizedForces(
                2, "hip_flexors_l", "sumo"
            )
            conv_hip_flexors_r_athlete_0 = getNormalizedForces(
                0, "hip_flexors_r", "conv"
            )
            conv_hip_flexors_r_athlete_2 = getNormalizedForces(
                2, "hip_flexors_r", "conv"
            )
            conv_hip_flexors_l_athlete_0 = getNormalizedForces(
                0, "hip_flexors_l", "conv"
            )
            conv_hip_flexors_l_athlete_2 = getNormalizedForces(
                2, "hip_flexors_l", "conv"
            )
            sumo_hip_adductors_r_athlete_0 = getNormalizedForces(
                0, "hip_adductors_r", "sumo"
            )
            sumo_hip_adductors_r_athlete_2 = getNormalizedForces(
                2, "hip_adductors_r", "sumo"
            )
            sumo_hip_adductors_l_athlete_0 = getNormalizedForces(
                0, "hip_adductors_l", "sumo"
            )
            sumo_hip_adductors_l_athlete_2 = getNormalizedForces(
                2, "hip_adductors_l", "sumo"
            )
            conv_hip_adductors_r_athlete_0 = getNormalizedForces(
                0, "hip_adductors_r", "conv"
            )
            conv_hip_adductors_r_athlete_2 = getNormalizedForces(
                2, "hip_adductors_r", "conv"
            )
            conv_hip_adductors_l_athlete_0 = getNormalizedForces(
                0, "hip_adductors_l", "conv"
            )
            conv_hip_adductors_l_athlete_2 = getNormalizedForces(
                2, "hip_adductors_l", "conv"
            )
            sumo_knee_extensors_r_athlete_0 = getNormalizedForces(
                0, "knee_extensors_r", "sumo"
            )
            sumo_knee_extensors_r_athlete_2 = getNormalizedForces(
                2, "knee_extensors_r", "sumo"
            )
            sumo_knee_extensors_l_athlete_0 = getNormalizedForces(
                0, "knee_extensors_l", "sumo"
            )
            sumo_knee_extensors_l_athlete_2 = getNormalizedForces(
                2, "knee_extensors_l", "sumo"
            )
            conv_knee_extensors_r_athlete_0 = getNormalizedForces(
                0, "knee_extensors_r", "conv"
            )
            conv_knee_extensors_r_athlete_2 = getNormalizedForces(
                2, "knee_extensors_r", "conv"
            )
            conv_knee_extensors_l_athlete_0 = getNormalizedForces(
                0, "knee_extensors_l", "conv"
            )
            conv_knee_extensors_l_athlete_2 = getNormalizedForces(
                2, "knee_extensors_l", "conv"
            )
            sumo_hip_extensors_athlete_0 = np.concatenate(
                (sumo_hip_extensors_r_athlete_0, sumo_hip_extensors_l_athlete_0)
            )
            sumo_hip_extensors_athlete_2 = np.concatenate(
                (sumo_hip_extensors_r_athlete_2, sumo_hip_extensors_l_athlete_2)
            )
            conv_hip_extensors_athlete_0 = np.concatenate(
                (conv_hip_extensors_r_athlete_0, conv_hip_extensors_l_athlete_0)
            )
            conv_hip_extensors_athlete_2 = np.concatenate(
                (conv_hip_extensors_r_athlete_2, conv_hip_extensors_l_athlete_2)
            )
            sumo_hip_flexors_athlete_0 = np.concatenate(
                (sumo_hip_flexors_r_athlete_0, sumo_hip_flexors_l_athlete_0)
            )
            sumo_hip_flexors_athlete_2 = np.concatenate(
                (sumo_hip_flexors_r_athlete_2, sumo_hip_flexors_l_athlete_2)
            )
            conv_hip_flexors_athlete_0 = np.concatenate(
                (conv_hip_flexors_r_athlete_0, conv_hip_flexors_l_athlete_0)
            )
            conv_hip_flexors_athlete_2 = np.concatenate(
                (conv_hip_flexors_r_athlete_2, conv_hip_flexors_l_athlete_2)
            )
            sumo_hip_adductors_athlete_0 = np.concatenate(
                (sumo_hip_adductors_r_athlete_0, sumo_hip_adductors_l_athlete_0)
            )
            sumo_hip_adductors_athlete_2 = np.concatenate(
                (sumo_hip_adductors_r_athlete_2, sumo_hip_adductors_l_athlete_2)
            )
            conv_hip_adductors_athlete_0 = np.concatenate(
                (conv_hip_adductors_r_athlete_0, conv_hip_adductors_l_athlete_0)
            )
            conv_hip_adductors_athlete_2 = np.concatenate(
                (conv_hip_adductors_r_athlete_2, conv_hip_adductors_l_athlete_2)
            )
            sumo_knee_extensors_athlete_0 = np.concatenate(
                (sumo_knee_extensors_r_athlete_0, sumo_knee_extensors_l_athlete_0)
            )
            sumo_knee_extensors_athlete_2 = np.concatenate(
                (sumo_knee_extensors_r_athlete_2, sumo_knee_extensors_l_athlete_2)
            )
            conv_knee_extensors_athlete_0 = np.concatenate(
                (conv_knee_extensors_r_athlete_0, conv_knee_extensors_l_athlete_0)
            )
            conv_knee_extensors_athlete_2 = np.concatenate(
                (conv_knee_extensors_r_athlete_2, conv_knee_extensors_l_athlete_2)
            )
            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Muscle Force Means " + "Athlete 0" + "; preferred: SUMO",
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
            plot_means(sumo_hip_extensors_athlete_0, "r", label_sumo)
            plot_means(conv_hip_extensors_athlete_0, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 0])
            axs_0[1, 0].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_extensors_athlete_0, conv_hip_extensors_athlete_0
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        200,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_0[0, 0].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # Hip flexors
            plt.sca(axs_0[0, 1])
            axs_0[0, 1].set_title(
                "Hip flexors",
            )
            plot_means(sumo_hip_flexors_athlete_0, "r", label_sumo)
            plot_means(conv_hip_flexors_athlete_0, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 1])
            axs_0[1, 1].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_flexors_athlete_0, conv_hip_flexors_athlete_0
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        100,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_0[0, 1].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # Hip adductors
            plt.sca(axs_0[0, 2])
            axs_0[0, 2].set_title(
                "Hip adductors",
            )
            plot_means(sumo_hip_adductors_athlete_0, "r", label_sumo)
            plot_means(conv_hip_adductors_athlete_0, "b", label_conv)
            axs_0[0, 2].set_ylim(ymin=0)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 2])
            axs_0[1, 2].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_adductors_athlete_0, conv_hip_adductors_athlete_0
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        100,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_0[0, 2].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # row 0, column 3
            plt.sca(axs_0[0, 3])
            axs_0[0, 3].set_title(
                "Knee extensors",
            )
            plot_means(sumo_knee_extensors_athlete_0, "r", label_sumo)
            plot_means(conv_knee_extensors_athlete_0, "b", label_conv)
            axs_0[0, 3].set_ylim(ymin=0)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 3])
            axs_0[1, 3].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_knee_extensors_athlete_0, conv_knee_extensors_athlete_0
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        300,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_0[0, 3].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

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

            figure_1_postfix = "spm_check_athlete_2"
            fig_1, axs_1 = plt.subplots(2, 4)
            fig_1.suptitle(
                "Muscle Force Means " + "Athlete 2" + "; preferred: CONV",
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
            plt.sca(axs_1[0, 0])
            axs_1[0, 0].set_title(
                "Hip extensors",
            )
            plot_means(sumo_hip_extensors_athlete_2, "r", label_sumo)
            plot_means(conv_hip_extensors_athlete_2, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 0])
            axs_1[1, 0].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_extensors_athlete_2, conv_hip_extensors_athlete_2
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        200,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_1[0, 0].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # Hip flexors
            plt.sca(axs_1[0, 1])
            axs_1[0, 1].set_title(
                "Hip flexors",
            )
            plot_means(sumo_hip_flexors_athlete_2, "r", label_sumo)
            plot_means(conv_hip_flexors_athlete_2, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 1])
            axs_1[1, 1].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_flexors_athlete_2, conv_hip_flexors_athlete_2
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        100,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_1[0, 1].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # Hip adductors
            plt.sca(axs_1[0, 2])
            axs_1[0, 2].set_title(
                "Hip adductors",
            )
            plot_means(sumo_hip_adductors_athlete_2, "r", label_sumo)
            plot_means(conv_hip_adductors_athlete_2, "b", label_conv)
            axs_1[0, 2].set_ylim(ymin=0)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 2])
            axs_1[1, 2].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_hip_adductors_athlete_2, conv_hip_adductors_athlete_2
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        100,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_1[0, 2].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            # row 0, column 3
            plt.sca(axs_1[0, 3])
            axs_1[0, 3].set_title(
                "Knee extensors",
            )
            plot_means(sumo_knee_extensors_athlete_2, "r", label_sumo)
            plot_means(conv_knee_extensors_athlete_2, "b", label_conv)
            axs_1[0, 3].set_ylim(ymin=0)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_1[1, 3])
            axs_1[1, 3].set_title(
                "Paired t-Test",
            )
            t = spm1d.stats.ttest_paired(
                sumo_knee_extensors_athlete_2, conv_knee_extensors_athlete_2
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        300,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs_1[0, 3].add_patch(rec)
            ti.plot()
            ti.plot_threshold_label()
            ti.plot_p_values()
            plt.xlabel(x_label)

            handles, labels = axs_1[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_1.legend(handles, labels, loc="center right")
            fig_1.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/" + figure_1_postfix + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
            ###############################################################################################################
        except Exception as e:
            print("Error in statistics summary")
            print(e)
