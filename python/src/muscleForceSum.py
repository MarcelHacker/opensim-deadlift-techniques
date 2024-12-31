from src.imports import (
    plt,
    athletes,
    mean_sumo_both_angles_and_moments,
    mean_conv_both_angles_and_moments,
    hamstrings_medial_sumo_force_mean,
    hamstrings_medial_conv_force_mean,
    hamstrings_lateral_sumo_force_mean,
    hamstrings_lateral_conv_force_mean,
    vasti_sumo_force_mean,
    vasti_conv_force_mean,
    gluteusmax_sumo_force_mean,
    gluteusmax_conv_force_mean,
    adductors_sumo_force_mean,
    adductors_conv_force_mean,
    gluteusmed_sumo_force_mean,
    gluteusmed_conv_force_mean,
    triceps_surae_sumo_force_mean,
    triceps_surae_conv_force_mean,
    hip_flexors_sumo_force_mean,
    hip_flexors_conv_force_mean,
    gluteusmin_sumo_force_mean,
    gluteusmin_conv_force_mean,
)

"""
For the angles the mean of all right and left leg of the trails was used.
The joint moments are the sum of right and leg divided and then the mean of all trails
"""


def run_muscle_force_sum_plot(bool):
    if bool:
        # For the next plot:
        # muscle forces are from one single limb
        # moments from both limbs
        """
        1.⁠ ⁠Add a row below angles with the 3 joint moments
        2.⁠ ⁠Make them all same colors in all plots
        3.⁠ ⁠Split hams by medial (Semitend and Semimem) and lateral (biceps long and short heads)
        4.⁠ ⁠Add hip flexors as a muscle group (TFL, iliacus, psoas, and rectfem)
        5.⁠ ⁠Don't include rect fem on quads
        """
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional 80%"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(5, 3)
            fig.suptitle(
                "Kinematics, Kinetics & Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")

            ## kinematics of hip, knee and ankle, and muscle forces
            # angles from both and mean value
            plt.sca(axs[0, 0])
            plt.plot(
                mean_sumo_both_angles_and_moments["hip_angle"],
                color=color_sumo,
                label=label_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["hip_angle"],
                color=color_conv,
                label=label_conv,
            )
            plt.legend()
            plt.ylabel("Hip Flex [°]")
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.plot(
                mean_sumo_both_angles_and_moments["knee_angle"],
                color=color_sumo,
                label=label_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["knee_angle"],
                color=color_conv,
                label=label_conv,
            )
            plt.legend()
            plt.ylabel("Knee Flex [°]")
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(
                mean_sumo_both_angles_and_moments["ankle_angle"],
                color=color_sumo,
                label=label_sumo,
            )
            plt.plot(
                mean_conv_both_angles_and_moments["ankle_angle"],
                color=color_conv,
                label=label_conv,
            )
            plt.ylabel("Ankle Flex [°]")
            plt.legend()
            plt.xlabel(x_label)

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

            # hamstrings medial
            plt.sca(axs[2, 0])
            plt.plot(
                hamstrings_medial_sumo_force_mean,  # mean of all trails
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                hamstrings_medial_conv_force_mean,
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Hamstrings medial [N]")
            plt.legend()
            plt.xlabel(x_label)
            # hamstrings lateral
            plt.sca(axs[2, 1])
            plt.plot(
                hamstrings_lateral_sumo_force_mean,
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                hamstrings_lateral_conv_force_mean,
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Hamstrings lateral [N]")
            plt.legend()
            plt.xlabel(x_label)

            # vasti
            plt.sca(axs[2, 2])
            plt.plot(vasti_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(vasti_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Vasti [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus maximus
            plt.sca(axs[3, 0])
            plt.plot(gluteusmax_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(gluteusmax_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Gluteus maximus [N]")
            plt.legend()
            plt.xlabel(x_label)

            # adductors
            plt.sca(axs[3, 1])
            plt.plot(adductors_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(adductors_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Adductors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # gluteus medius
            plt.sca(axs[3, 2])
            plt.plot(gluteusmed_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(gluteusmed_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Gluteus medius [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Triceps surae
            plt.sca(axs[4, 0])
            plt.plot(triceps_surae_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(triceps_surae_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Triceps surae [N]")
            plt.legend()
            plt.xlabel(x_label)

            # hip flexors
            plt.sca(axs[4, 1])
            plt.plot(hip_flexors_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(hip_flexors_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Hip flexors [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Gluteus minimus
            plt.sca(axs[4, 2])
            plt.plot(gluteusmin_sumo_force_mean, label=label_sumo, color=color_sumo)
            plt.plot(gluteusmin_conv_force_mean, label=label_conv, color=color_conv)
            plt.ylabel("Gluteus minimus [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)
