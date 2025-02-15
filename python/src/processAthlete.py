from src.imports import *


def run_process_athlete(bool, save_figures):
    if bool:
        try:
            rows = 3
            cols = 2
            trial_color_0 = "red"
            trial_color_1 = "blue"
            trial_color_2 = "orange"
            trial_color_3 = "darkgreen"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Kinematics Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.2,
                hspace=0.285,
                top=0.893,
                right=0.912,
                left=0.05,
                bottom=0.07,
            )
            fig.set_label("Kinematics")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "hip_flexion_r",
                "knee_angle_r",
                "ankle_angle_r",
            ]
            coordinates_l = [
                "hip_flexion_l",
                "knee_angle_l",
                "ankle_angle_l",
            ]
            ylabels = [
                "Hip Flex [°]",
                "Knee Flex [°]",
                "Ankle Flex [°]",
            ]

            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("SDL")
                axs[0, i].set_xlim(left=0, right=100)
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_ik_sumo_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                axs[1, i].set_xlim(left=0, right=100)
                plt.title("CDL")
                plt.plot(
                    active_athlete_ik_conv_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_ik_conv_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/ik/" + active_athlete["name"] + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete kinematics")
            print(e)

        try:
            rows = 3
            cols = 2
            trial_color_0 = "red"
            trial_color_1 = "blue"
            trial_color_2 = "orange"
            trial_color_3 = "darkgreen"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Joint Moments Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.285,
                hspace=0.298,
                top=0.904,
                right=0.91,
                left=0.067,
                bottom=0.067,
            )
            fig.set_label("Joint Moments [Nm]")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "hip_flexion_r_moment",
                "knee_angle_r_moment",
                "ankle_angle_r_moment",
            ]
            coordinates_l = [
                "hip_flexion_l_moment",
                "knee_angle_l_moment",
                "ankle_angle_l_moment",
            ]
            ylabels = [
                "Hip Moment [Nm]",
                "Knee Moment [Nm]",
                "Ankle Moment [Nm]",
            ]

            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                axs[0, i].set_xlim(left=0, right=100)
                plt.title("SDL")
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])

            for i in range(len(coordinates_r)):
                plt.sca(axs[1, i])
                axs[1, i].set_xlim(left=0, right=100)
                plt.title("CDL")
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_r[i]],
                    label="Trial 1 r",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_0[coordinates_l[i]],
                    label="Trial 1 l",
                    color=trial_color_0,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_r[i]],
                    label="Trial 2 r",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_1[coordinates_l[i]],
                    label="Trial 2 l",
                    color=trial_color_1,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_r[i]],
                    label="Trial 3 r",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_2[coordinates_l[i]],
                    label="Trial 3 l",
                    color=trial_color_2,
                    linestyle="dashed",
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_3[coordinates_r[i]],
                    label="Trial 4 r",
                    color=trial_color_3,
                )
                plt.plot(
                    active_athlete_id_conv_time_normalised_3[coordinates_l[i]],
                    label="Trial 4 l",
                    color=trial_color_3,
                    linestyle="dashed",
                )
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/id/" + active_athlete["name"] + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athletes joint moments")
            print(e)

        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo_trial_0 = "SDL 1"
            label_sumo_trial_1 = "SDL 2"
            label_sumo_trial_2 = "SDL 3"
            label_sumo_trial_3 = "SDL 4"
            label_conv_trial_0 = "CDL 1"
            label_conv_trial_1 = "CDL 2"
            label_conv_trial_2 = "CDL 3"
            label_conv_trial_3 = "CDL 4"
            linestyle_trial_1 = "dashed"
            linestyle_trial_2 = "dotted"
            linestyle_trial_3 = "dashdot"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(3, 3)
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
                wspace=0.275,
                hspace=0.293,
                top=0.935,
                right=0.921,
                left=0.06,
                bottom=0.06,
            )

            # hamstrings medial
            plt.sca(axs[0, 0])
            axs[0, 0].set_xlim(left=0, right=100)
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hamstrings_medial_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_0,  # mean of all trails
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_1,  # mean of all trails
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_2,  # mean of all trails
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hamstrings_medial_conv_force_3,  # mean of all trails
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Hamstrings medial [N]")
            # hamstrings lateral
            plt.sca(axs[0, 1])
            axs[0, 1].set_xlim(left=0, right=100)
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle="dashed",
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle="dotted",
            )
            plt.plot(
                active_athlete_hamstrings_lateral_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Hamstrings lateral [N]")

            # vasti
            plt.sca(axs[0, 2])
            axs[0, 2].set_xlim(left=0, right=100)
            plt.plot(
                active_athlete_vasti_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_vasti_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_vasti_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_vasti_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_vasti_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_vasti_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_vasti_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_vasti_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Vasti [N]")

            # gluteus maximus
            plt.sca(axs[1, 0])
            axs[1, 0].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_gluteusmax_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmax_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmax_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmax_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmax_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Gluteus maximus [N]")

            # adductors
            plt.sca(axs[1, 1])
            axs[1, 1].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_adductors_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_adductors_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_adductors_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_adductors_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_adductors_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_adductors_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_adductors_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_adductors_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Adductors [N]")

            # gluteus medius
            plt.sca(axs[1, 2])
            axs[1, 2].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_gluteusmed_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmed_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmed_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmed_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmed_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Gluteus medius [N]")

            # Triceps surae
            plt.sca(axs[2, 0])
            axs[2, 0].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_triceps_surae_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_triceps_surae_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_triceps_surae_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_triceps_surae_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_triceps_surae_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Triceps surae [N]")
            plt.xlabel(x_label)

            # hip flexors
            plt.sca(axs[2, 1])
            axs[2, 1].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_hip_flexors_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_hip_flexors_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hip_flexors_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hip_flexors_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_hip_flexors_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Hip flexors [N]")
            plt.xlabel(x_label)

            # Gluteus minimus
            plt.sca(axs[2, 2])
            axs[2, 2].set_xlim(left=0, right=100)

            plt.plot(
                active_athlete_gluteusmin_sumo_force_0,
                label=label_sumo_trial_0,
                color=color_sumo,
            )
            plt.plot(
                active_athlete_gluteusmin_sumo_force_1,
                label=label_sumo_trial_1,
                color=color_sumo,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmin_sumo_force_2,
                label=label_sumo_trial_2,
                color=color_sumo,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmin_sumo_force_3,
                label=label_sumo_trial_3,
                color=color_sumo,
                linestyle=linestyle_trial_3,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_0,
                label=label_conv_trial_0,
                color=color_conv,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_1,
                label=label_conv_trial_1,
                color=color_conv,
                linestyle=linestyle_trial_1,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_2,
                label=label_conv_trial_2,
                color=color_conv,
                linestyle=linestyle_trial_2,
            )
            plt.plot(
                active_athlete_gluteusmin_conv_force_3,
                label=label_conv_trial_3,
                color=color_conv,
                linestyle=linestyle_trial_3,
            )
            plt.ylabel("Gluteus minimus [N]")
            plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/so/" + active_athlete["name"] + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in process athlete muscle force groups")
            print(e)

        try:
            cols = 2
            color_sumo = "red"
            color_conv = "blue"
            linestyle_trail_1 = "dotted"
            linestyle_trail_2 = "dashed"
            linestyle_trail_3 = "dashdot"
            fig, axs = plt.subplots(cols)
            fig.suptitle(
                "Total Muscle Force Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.385,
                hspace=0.213,
                top=0.902,
                right=0.988,
                left=0.064,
                bottom=0.06,
            )
            fig.set_label("Total Muscle Force [N]")
            x_label = "% concentric deadlift cycle"
            y_label = "Muscle force [N]"

            plt.sca(axs[0])
            plt.title(
                "SDL",
                fontweight="bold",
            )
            plt.plot(
                active_athlete_total_sumo_force_0,
                label="Trial 1",
                color=color_sumo,
            )
            plt.plot(
                active_athlete_total_sumo_force_1,
                label="Trial 2",
                color=color_sumo,
                linestyle=linestyle_trail_1,
            )
            plt.plot(
                active_athlete_total_sumo_force_2,
                label="Trial 3",
                color=color_sumo,
                linestyle=linestyle_trail_2,
            )
            plt.plot(
                active_athlete_total_sumo_force_3,
                label="Trial 4",
                color=color_sumo,
                linestyle=linestyle_trail_3,
            )
            # axs[0].set_yticks(np.arange(10000, 38000, 3000))
            axs[0].set_xticks(np.arange(0, 101, 5))
            axs[0].set_xlim(left=0, right=100)
            plt.legend()
            plt.ylabel(y_label)

            plt.sca(axs[1])
            plt.title(
                "CDL",
                fontweight="bold",
            )
            plt.plot(
                active_athlete_total_conv_force_0,
                label="Trial 1",
                color=color_conv,
            )
            plt.plot(
                active_athlete_total_conv_force_1,
                label="Trial 2",
                color=color_conv,
                linestyle=linestyle_trail_1,
            )
            plt.plot(
                active_athlete_total_conv_force_2,
                label="Trial 3",
                color=color_conv,
                linestyle=linestyle_trail_2,
            )
            plt.plot(
                active_athlete_total_conv_force_3,
                label="Trial 4",
                color=color_conv,
                linestyle=linestyle_trail_3,
            )
            # axs[1].set_yticks(np.arange(10000, 38000, 3000))
            axs[1].set_xticks(np.arange(0, 101, 5))
            axs[1].set_xlim(left=0, right=100)
            plt.legend()
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/so/" + active_athlete["name"] + "_total" + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete total muscle force")
            print(e)
