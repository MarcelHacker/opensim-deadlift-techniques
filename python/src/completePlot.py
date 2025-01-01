from src.imports import (
    plt,
    athletes,
    mean_sumo_both_angles_and_moments,
    mean_conv_both_angles_and_moments,
    momentArms_hip_flexion_r_sumo_time_normalised_1,
    momentArms_knee_flexion_r_sumo_time_normalised_1,
    momentArms_ankle_flexion_r_sumo_time_normalised_1,
    momentArms_hip_flexion_r_conv_time_normalised_1,
)


def run_complete_plot(bool):

    if bool:
        """
        Row 1: Hip, knee and ankle joint moments single leg
        Row 2: Hip, knee and ankle moment arms single leg
        Row 3: Hip, knee and ankle moment arms single leg
        """
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(6, 3)
            fig.suptitle(
                "Moment Arms Analysis "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Moment arm [cm]")

            # Total force between two techniques
            ## moments, both legs
            # hip
            plt.sca(axs[0, 0])
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
            plt.sca(axs[0, 1])
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
            plt.ylabel("Glmax1_r [cm]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 1])
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
            plt.ylabel("Glmax2_r [cm]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 2])
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
            plt.ylabel("Glmax3_r [cm]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[2, 0])
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
            plt.ylabel("Recfem_r [cm]")
            plt.legend()
            plt.xlabel(x_label)
            plt.sca(axs[2, 0])
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
            plt.ylabel("Recfem_r [cm]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_complete_plot")
            print(e)
