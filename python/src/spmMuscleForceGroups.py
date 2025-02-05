import numpy as np
import spm1d
from .imports import (
    plt,
    active_athlete,
    active_athlete_bodymass,
    create_overall_csv,
    active_athlete_hip_extensors_sumo_r_force_0,
    active_athlete_hip_extensors_sumo_r_force_1,
    active_athlete_hip_extensors_sumo_r_force_2,
    active_athlete_hip_extensors_sumo_r_force_3,
    active_athlete_hip_extensors_sumo_l_force_0,
    active_athlete_hip_extensors_sumo_l_force_1,
    active_athlete_hip_extensors_sumo_l_force_2,
    active_athlete_hip_extensors_sumo_l_force_3,
    active_athlete_hip_extensors_conv_r_force_0,
    active_athlete_hip_extensors_conv_r_force_1,
    active_athlete_hip_extensors_conv_r_force_2,
    active_athlete_hip_extensors_conv_r_force_3,
    active_athlete_hip_extensors_conv_l_force_0,
    active_athlete_hip_extensors_conv_l_force_1,
    active_athlete_hip_extensors_conv_l_force_2,
    active_athlete_hip_extensors_conv_l_force_3,
    active_athlete_hip_flexors_sumo_r_force_0,
    active_athlete_hip_flexors_sumo_r_force_1,
    active_athlete_hip_flexors_sumo_r_force_2,
    active_athlete_hip_flexors_sumo_r_force_3,
    active_athlete_hip_flexors_sumo_l_force_0,
    active_athlete_hip_flexors_sumo_l_force_1,
    active_athlete_hip_flexors_sumo_l_force_2,
    active_athlete_hip_flexors_sumo_l_force_3,
    active_athlete_hip_flexors_conv_r_force_0,
    active_athlete_hip_flexors_conv_r_force_1,
    active_athlete_hip_flexors_conv_r_force_2,
    active_athlete_hip_flexors_conv_r_force_3,
    active_athlete_hip_flexors_conv_l_force_0,
    active_athlete_hip_flexors_conv_l_force_1,
    active_athlete_hip_flexors_conv_l_force_2,
    active_athlete_hip_flexors_conv_l_force_3,
    active_athlete_hip_adductors_sumo_r_force_0,
    active_athlete_hip_adductors_sumo_r_force_1,
    active_athlete_hip_adductors_sumo_r_force_2,
    active_athlete_hip_adductors_sumo_r_force_3,
    active_athlete_hip_adductors_sumo_l_force_0,
    active_athlete_hip_adductors_sumo_l_force_1,
    active_athlete_hip_adductors_sumo_l_force_2,
    active_athlete_hip_adductors_sumo_l_force_3,
    active_athlete_hip_adductors_conv_r_force_0,
    active_athlete_hip_adductors_conv_r_force_1,
    active_athlete_hip_adductors_conv_r_force_2,
    active_athlete_hip_adductors_conv_r_force_3,
    active_athlete_hip_adductors_conv_l_force_0,
    active_athlete_hip_adductors_conv_l_force_1,
    active_athlete_hip_adductors_conv_l_force_2,
    active_athlete_hip_adductors_conv_l_force_3,
    active_athlete_knee_extensors_sumo_r_force_0,
    active_athlete_knee_extensors_sumo_r_force_1,
    active_athlete_knee_extensors_sumo_r_force_2,
    active_athlete_knee_extensors_sumo_r_force_3,
    active_athlete_knee_extensors_sumo_l_force_0,
    active_athlete_knee_extensors_sumo_l_force_1,
    active_athlete_knee_extensors_sumo_l_force_2,
    active_athlete_knee_extensors_sumo_l_force_3,
    active_athlete_knee_extensors_conv_r_force_0,
    active_athlete_knee_extensors_conv_r_force_1,
    active_athlete_knee_extensors_conv_r_force_2,
    active_athlete_knee_extensors_conv_r_force_3,
    active_athlete_knee_extensors_conv_l_force_0,
    active_athlete_knee_extensors_conv_l_force_1,
    active_athlete_knee_extensors_conv_l_force_2,
    active_athlete_knee_extensors_conv_l_force_3,
)


def normalize_forces(array):
    normalized_array = []
    for value in array:
        normalized_array.append(value / active_athlete_bodymass)
    return normalized_array


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


def isSumoPreffered():
    if active_athlete["technique"] == "sumo":
        return True
    else:
        return False


def create_muscle_force_csv(
    array_sumo_time_normalized_r,
    array_sumo_time_normalized_l,
    array_conv_time_normalized_r,
    array_conv_time_normalized_l,
    muscle_group,
):
    create_overall_csv(
        ("sumo/" + str(muscle_group) + "_r.csv"),
        array_sumo_time_normalized_r,
        active_athlete["name"],
    )
    create_overall_csv(
        ("sumo/" + str(muscle_group) + "_l.csv"),
        array_sumo_time_normalized_l,
        active_athlete["name"],
    )
    create_overall_csv(
        ("conv/" + str(muscle_group) + "_r.csv"),
        array_conv_time_normalized_r,
        active_athlete["name"],
    )
    create_overall_csv(
        ("conv/" + str(muscle_group) + "_l.csv"),
        array_conv_time_normalized_l,
        active_athlete["name"],
    )


def createForceArray(technique, limb, muscle_group):
    array = [
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_0")
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_1")
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_2")
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_3")
        ),
    ]
    array = np.array(array)
    return array


"""
For the muscle forces sum of right and left leg of the trails was used.
"""


def run_muscle_force_groups_spm(bool, save_figures):
    if bool:
        try:
            figure_0_postfix = "_spm_muscle_group_summary"
            label_sumo = "SUMO"
            label_conv = "CONV"
            y_label = "Normalized muscle force [N/kg]"
            x_label = "% concentric deadlift cycle"

            fig_0, axs_0 = plt.subplots(2, 4)
            fig_0.suptitle(
                "Muscle Force Means "
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
            #  hip extensors
            hip_extensors_sumo_r = createForceArray("sumo", "r", "hip_extensors")
            print("\nHIP ex r\n", hip_extensors_sumo_r)
            hip_extensors_sumo_l = createForceArray("sumo", "l", "hip_extensors")
            print("\nHIP ex l\n", hip_extensors_sumo_l)
            hip_extensors_conv_r = createForceArray("conv", "r", "hip_extensors")
            hip_extensors_conv_l = createForceArray("conv", "l", "hip_extensors")

            # flexors
            hip_flexors_sumo_r = createForceArray("sumo", "r", "hip_flexors")
            hip_flexors_sumo_l = createForceArray("sumo", "l", "hip_flexors")
            hip_flexors_conv_r = createForceArray("conv", "r", "hip_flexors")
            hip_flexors_conv_l = createForceArray("conv", "l", "hip_flexors")

            # adductors
            hip_adductors_sumo_r = createForceArray("sumo", "r", "hip_adductors")
            hip_adductors_sumo_l = createForceArray("sumo", "l", "hip_adductors")
            hip_adductors_conv_r = createForceArray("conv", "r", "hip_adductors")
            hip_adductors_conv_l = createForceArray("conv", "l", "hip_adductors")

            # knee extensors
            knee_extensors_sumo_r = createForceArray("sumo", "r", "knee_extensors")
            knee_extensors_sumo_l = createForceArray("sumo", "l", "knee_extensors")
            knee_extensors_conv_r = createForceArray("conv", "r", "knee_extensors")
            knee_extensors_conv_l = createForceArray("conv", "l", "knee_extensors")

            hip_extensors_sumo = np.concatenate(
                (hip_extensors_sumo_r, hip_extensors_sumo_l)
            )
            hip_extensors_conv = np.concatenate(
                (hip_extensors_conv_r, hip_extensors_conv_l)
            )
            hip_flexors_sumo = np.concatenate((hip_flexors_sumo_r, hip_flexors_sumo_l))
            hip_flexors_conv = np.concatenate((hip_flexors_conv_r, hip_flexors_conv_l))
            hip_adductors_sumo = np.concatenate(
                (hip_adductors_sumo_r, hip_adductors_sumo_l)
            )
            hip_adductors_conv = np.concatenate(
                (hip_adductors_conv_r, hip_adductors_conv_l)
            )
            knee_extensors_sumo = np.concatenate(
                (knee_extensors_sumo_r, knee_extensors_sumo_l)
            )
            knee_extensors_conv = np.concatenate(
                (knee_extensors_conv_r, knee_extensors_conv_l)
            )
            create_muscle_force_csv(
                hip_extensors_sumo_r,
                hip_extensors_conv_l,
                hip_extensors_conv_r,
                hip_extensors_conv_l,
                "hip_extensors",
            )
            create_muscle_force_csv(
                hip_flexors_sumo_r,
                hip_flexors_sumo_l,
                hip_flexors_conv_r,
                hip_flexors_conv_l,
                "hip_flexors",
            )
            create_muscle_force_csv(
                hip_adductors_sumo_r,
                hip_adductors_sumo_l,
                hip_adductors_conv_r,
                hip_adductors_conv_l,
                "hip_adductors",
            )
            create_muscle_force_csv(
                knee_extensors_sumo_r,
                knee_extensors_sumo_l,
                knee_extensors_conv_r,
                knee_extensors_conv_l,
                "knee_extensors",
            )

            # hamstrings medial
            plt.sca(axs_0[0, 0])
            axs_0[0, 0].set_title(
                "Hip Extensors",
            )
            plot_means(hip_extensors_sumo, "r", label_sumo)
            plot_means(hip_extensors_conv, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 0])
            axs_0[1, 0].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(hip_extensors_sumo, hip_extensors_conv)

            # hamstrings lateral
            plt.sca(axs_0[0, 1])
            axs_0[0, 1].set_title(
                "Hip Flexors",
            )
            plot_means(hip_flexors_sumo, "r", label_sumo)
            plot_means(hip_flexors_conv, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 1])
            axs_0[1, 1].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(hip_flexors_sumo, hip_flexors_conv)

            # hamstrings lateral
            plt.sca(axs_0[0, 2])
            axs_0[0, 2].set_title(
                "Hip Adductors",
            )
            plot_means(hip_adductors_sumo, "r", label_sumo)
            plot_means(hip_adductors_conv, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 2])
            axs_0[1, 2].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)

            paired_ttest(hip_adductors_sumo, hip_adductors_conv)

            # gluteus maximus
            # row 0, column 3
            plt.sca(axs_0[0, 3])
            axs_0[0, 3].set_title(
                "Knee Extensors",
            )
            plot_means(knee_extensors_sumo, "r", label_sumo)
            plot_means(knee_extensors_conv, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)

            plt.sca(axs_0[1, 3])
            axs_0[1, 3].set_title(
                "Paired t-Test",
            )
            plt.xlabel(x_label)
            paired_ttest(knee_extensors_sumo, knee_extensors_conv)

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
