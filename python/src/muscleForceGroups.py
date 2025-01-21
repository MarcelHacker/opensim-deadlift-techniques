from .imports import (
    plt,
    active_athlete,
    active_athlete_hamstrings_medial_sumo_force_0,
    active_athlete_hamstrings_medial_sumo_force_1,
    active_athlete_hamstrings_medial_sumo_force_2,
    active_athlete_hamstrings_medial_conv_force_0,
    active_athlete_hamstrings_medial_conv_force_1,
    active_athlete_hamstrings_medial_conv_force_2,
    active_athlete_hamstrings_lateral_sumo_force_0,
    active_athlete_hamstrings_lateral_sumo_force_1,
    active_athlete_hamstrings_lateral_sumo_force_2,
    active_athlete_hamstrings_lateral_conv_force_0,
    active_athlete_hamstrings_lateral_conv_force_1,
    active_athlete_hamstrings_lateral_conv_force_2,
    active_athlete_vasti_sumo_force_0,
    active_athlete_vasti_sumo_force_1,
    active_athlete_vasti_sumo_force_2,
    active_athlete_vasti_conv_force_0,
    active_athlete_vasti_conv_force_1,
    active_athlete_vasti_conv_force_2,
    active_athlete_gluteusmax_sumo_force_0,
    active_athlete_gluteusmax_sumo_force_1,
    active_athlete_gluteusmax_sumo_force_2,
    active_athlete_gluteusmax_conv_force_0,
    active_athlete_gluteusmax_conv_force_1,
    active_athlete_gluteusmax_conv_force_2,
    active_athlete_adductors_sumo_force_0,
    active_athlete_adductors_sumo_force_1,
    active_athlete_adductors_sumo_force_2,
    active_athlete_adductors_conv_force_0,
    active_athlete_adductors_conv_force_1,
    active_athlete_adductors_conv_force_2,
    active_athlete_gluteusmed_sumo_force_0,
    active_athlete_gluteusmed_sumo_force_1,
    active_athlete_gluteusmed_sumo_force_2,
    active_athlete_gluteusmed_conv_force_0,
    active_athlete_gluteusmed_conv_force_1,
    active_athlete_gluteusmed_conv_force_2,
    active_athlete_triceps_surae_sumo_force_0,
    active_athlete_triceps_surae_sumo_force_1,
    active_athlete_triceps_surae_sumo_force_2,
    active_athlete_triceps_surae_conv_force_0,
    active_athlete_triceps_surae_conv_force_1,
    active_athlete_triceps_surae_conv_force_2,
    active_athlete_hip_flexors_sumo_force_0,
    active_athlete_hip_flexors_sumo_force_1,
    active_athlete_hip_flexors_sumo_force_2,
    active_athlete_hip_flexors_conv_force_0,
    active_athlete_hip_flexors_conv_force_1,
    active_athlete_hip_flexors_conv_force_2,
    active_athlete_gluteusmin_sumo_force_0,
    active_athlete_gluteusmin_sumo_force_1,
    active_athlete_gluteusmin_sumo_force_2,
    active_athlete_gluteusmin_conv_force_0,
    active_athlete_gluteusmin_conv_force_1,
    active_athlete_gluteusmin_conv_force_2,
)

"""
For the muscle forces sum of right and left leg of the trails was used.
"""


def run_muscle_force_groups(bool):
    if bool:
        try:
            figure_prefix = "muscle_force_groups_"
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "SUMO"
            label_conv = "CONV"
            linestyle_trial_1 = "dashed"
            linestyle_trial_2 = "dotted"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(5, 3)
            fig.suptitle(
                "Muscle Force Groups "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle Force Groups")
            plt.subplots_adjust(
                wspace=0.285,
                hspace=0.298,
                top=0.904,
                right=0.91,
                left=0.067,
                bottom=0.067,
            )
            """
            ## moments, both legs
            # hip
            plt.sca(axs[1, 0])
            plt.plot(
                mean_sumo_both_angles_and_moments["hip_flexion_moment"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["hip_flexion_moment"],
                color=color_conv,
                label=label_conv,
            )
            plt.ylabel("Hip moment [Nm]")
            plt.legend()
            plt.xlabel(x_label)
            # knee
            plt.sca(axs[1, 1])
            plt.plot(
                mean_sumo_both_angles_and_moments["knee_flexion_moment"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["knee_flexion_moment"],
                color=color_conv,
                label=label_conv,
            )
            plt.ylabel("Knee moment [Nm]")
            plt.legend()
            plt.xlabel(x_label)
            # ankle
            plt.sca(axs[1, 2])
            plt.plot(
                mean_sumo_both_angles_and_moments["ankle_flexion_moment"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["ankle_flexion_moment"],
                color=color_conv,
                label=label_conv,
            )
            plt.ylabel("Ankle moment [Nm]")
            plt.legend()
            plt.xlabel(x_label)
            """
            # hamstrings medial
            plt.sca(axs[2, 0])
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_0,  # mean of all trails
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_1,  # mean of all trails
                label="Trial 2",
                color=color_conv,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_2,  # mean of all trails
                label="Trial 3",
                color=color_conv,
                linestyle="dotted",
            )
            plt.ylabel("Hamstrings medial [N]")
            plt.legend()
            plt.xlabel(x_label)
            # hamstrings lateral
            plt.sca(axs[2, 1])
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle="dotted",
            )
            plt.ylabel("Hamstrings lateral [N]")
            plt.legend()
            plt.xlabel(x_label)

            # vasti
            plt.sca(axs[2, 2])
            plt.plot(
                active_athlete_vasti_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_vasti_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_vasti_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_vasti_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_vasti_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_vasti_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle="dotted",
            )
            plt.ylabel("Vasti [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus maximus
            plt.sca(axs[3, 0])
            plt.plot(
                active_athlete_gluteusmax_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmax_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmax_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Gluteus maximus [N]")
            plt.legend()
            plt.xlabel(x_label)

            # adductors
            plt.sca(axs[3, 1])
            plt.plot(
                active_athlete_adductors_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_adductors_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_adductors_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_adductors_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_adductors_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_adductors_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Adductors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus medius
            plt.sca(axs[3, 2])
            plt.plot(
                active_athlete_gluteusmed_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmed_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmed_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Gluteus medius [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Triceps surae
            plt.sca(axs[4, 0])
            plt.plot(
                active_athlete_triceps_surae_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_triceps_surae_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_triceps_surae_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Triceps surae [N]")
            plt.legend()
            plt.xlabel(x_label)

            # hip flexors
            plt.sca(axs[4, 1])
            plt.plot(
                active_athlete_hip_flexors_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hip_flexors_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hip_flexors_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Hip flexors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Gluteus minimus
            plt.sca(axs[4, 2])
            plt.plot(
                active_athlete_gluteusmin_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmin_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmin_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.ylabel("Gluteus minimus [N]")
            plt.legend()
            plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            plt.savefig(
                "../results/so/" + figure_prefix + active_athlete["name"] + ".png",
                transparent=None,
                dpi=300,
                format="png",
            )
            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_groups")
            print(e)
