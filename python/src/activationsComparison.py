from src.imports import (
    plt,
    active_athlete,
)


def run_activations_comparison_from_emg(bool):

    if bool:
        try:
            color_sumo = "deeppink"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(4, 3)
            fig.suptitle(
                "Activations Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Moment arm [cm]")

            # Total force between two techniques
            ## moments, both legs
            # hip
            plt.sca(axs[0, 0])
            plt.title("Hip")
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
            plt.ylabel("Moment [Nm]")
            plt.legend()
            plt.xlabel(x_label)
            # knee
            plt.sca(axs[0, 1])
            plt.title("Knee")
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
            plt.sca(axs[0, 2])
            plt.title("Ankle")
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

            plt.sca(axs[1, 0])
            plt.title("Hip Flex")
            plt.plot(
                momentArms_hip_flexion_r_sumo_time_normalised_1["glmax1_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_hip_flexion_r_conv_time_normalised_1["glmax1_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Glmax1_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 1])
            plt.title("Hip Flex")
            plt.plot(
                momentArms_hip_flexion_r_sumo_time_normalised_1["glmax2_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_hip_flexion_r_conv_time_normalised_1["glmax2_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Glmax2_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 2])
            plt.title("Hip Flex")
            plt.plot(
                momentArms_hip_flexion_r_sumo_time_normalised_1["glmax3_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_hip_flexion_r_conv_time_normalised_1["glmax3_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Glmax3_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[2, 0])
            plt.title("Hip Flex")
            plt.plot(
                momentArms_hip_flexion_r_sumo_time_normalised_1["recfem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_hip_flexion_r_conv_time_normalised_1["recfem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Recfem_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[2, 1])
            plt.title("Knee Flex")
            plt.plot(
                momentArms_knee_flexion_r_sumo_time_normalised_1["recfem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_knee_flexion_r_conv_time_normalised_1["recfem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Recfem_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[2, 2])
            plt.title("Knee Flex")
            plt.plot(
                momentArms_knee_flexion_r_sumo_time_normalised_1["semiten_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_knee_flexion_r_conv_time_normalised_1["semiten_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("semiten_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[3, 0])
            plt.title("Knee Flex")
            plt.plot(
                momentArms_knee_flexion_r_sumo_time_normalised_1["vaslat_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_knee_flexion_r_conv_time_normalised_1["vaslat_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("vaslat_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[3, 1])
            plt.title("Knee Flex")
            plt.plot(
                momentArms_knee_flexion_r_sumo_time_normalised_1["vasmed_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_knee_flexion_r_conv_time_normalised_1["vasmed_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("vasmed_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[3, 2])
            plt.title("Ankle Flex")
            plt.plot(
                momentArms_ankle_flexion_r_sumo_time_normalised_1["soleus_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                momentArms_ankle_flexion_r_conv_time_normalised_1["soleus_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("soleus_r [m]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_complete_plot")
            print(e)
