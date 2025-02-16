from src.imports import *
import datetime

# from matplotlib.backends.backend_pdf import PdfPages


def run_process_athlete(bool, save_figures):
    if bool:
        trial_color_0 = "red"
        trial_color_1 = "blue"
        trial_color_2 = "orange"
        trial_color_3 = "darkgreen"
        x_label = "% concentric deadlift cycle"
        ###########################################  START IK #######################################################
        try:
            fig, axs = plt.subplots(2, 3)
            fig.suptitle(
                "Kinematics Trials Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.2,
                hspace=0.208,
                top=0.91,
                right=0.904,
                left=0.05,
                bottom=0.07,
            )
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
                    "../results/ik/" + active_athlete["name"] + "_trials.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete kinematics trials")
            print(e)

        try:
            fig, axs = plt.subplots(1, 3)
            fig.suptitle(
                "Kinematics Means Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.2,
                hspace=0.208,
                top=0.89,
                right=0.912,
                left=0.05,
                bottom=0.077,
            )

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

            hip_flexion_sumo_array = [
                active_athlete_ik_sumo_time_normalised_0["hip_flexion_r"],
                active_athlete_ik_sumo_time_normalised_0["hip_flexion_l"],
                active_athlete_ik_sumo_time_normalised_1["hip_flexion_r"],
                active_athlete_ik_sumo_time_normalised_1["hip_flexion_l"],
                active_athlete_ik_sumo_time_normalised_2["hip_flexion_r"],
                active_athlete_ik_sumo_time_normalised_2["hip_flexion_l"],
                active_athlete_ik_sumo_time_normalised_3["hip_flexion_r"],
                active_athlete_ik_sumo_time_normalised_3["hip_flexion_l"],
            ]

            hip_flexion_conv_array = [
                active_athlete_ik_conv_time_normalised_0["hip_flexion_r"],
                active_athlete_ik_conv_time_normalised_0["hip_flexion_l"],
                active_athlete_ik_conv_time_normalised_1["hip_flexion_r"],
                active_athlete_ik_conv_time_normalised_1["hip_flexion_l"],
                active_athlete_ik_conv_time_normalised_2["hip_flexion_r"],
                active_athlete_ik_conv_time_normalised_2["hip_flexion_l"],
                active_athlete_ik_conv_time_normalised_3["hip_flexion_r"],
                active_athlete_ik_conv_time_normalised_3["hip_flexion_l"],
            ]

            hip_flexion_sumo_array = np.array(hip_flexion_sumo_array)
            hip_flexion_conv_array = np.array(hip_flexion_conv_array)

            knee_flexion_sumo_array = [
                active_athlete_ik_sumo_time_normalised_0["knee_angle_r"],
                active_athlete_ik_sumo_time_normalised_0["knee_angle_l"],
                active_athlete_ik_sumo_time_normalised_1["knee_angle_r"],
                active_athlete_ik_sumo_time_normalised_1["knee_angle_l"],
                active_athlete_ik_sumo_time_normalised_2["knee_angle_r"],
                active_athlete_ik_sumo_time_normalised_2["knee_angle_l"],
                active_athlete_ik_sumo_time_normalised_3["knee_angle_r"],
                active_athlete_ik_sumo_time_normalised_3["knee_angle_l"],
            ]

            knee_flexion_conv_array = [
                active_athlete_ik_conv_time_normalised_0["knee_angle_r"],
                active_athlete_ik_conv_time_normalised_0["knee_angle_l"],
                active_athlete_ik_conv_time_normalised_1["knee_angle_r"],
                active_athlete_ik_conv_time_normalised_1["knee_angle_l"],
                active_athlete_ik_conv_time_normalised_2["knee_angle_r"],
                active_athlete_ik_conv_time_normalised_2["knee_angle_l"],
                active_athlete_ik_conv_time_normalised_3["knee_angle_r"],
                active_athlete_ik_conv_time_normalised_3["knee_angle_l"],
            ]

            knee_flexion_sumo_array = np.array(knee_flexion_sumo_array)
            knee_flexion_conv_array = np.array(knee_flexion_conv_array)

            ankle_flexion_sumo_array = [
                active_athlete_ik_sumo_time_normalised_0["ankle_angle_r"],
                active_athlete_ik_sumo_time_normalised_0["ankle_angle_l"],
                active_athlete_ik_sumo_time_normalised_1["ankle_angle_r"],
                active_athlete_ik_sumo_time_normalised_1["ankle_angle_l"],
                active_athlete_ik_sumo_time_normalised_2["ankle_angle_r"],
                active_athlete_ik_sumo_time_normalised_2["ankle_angle_l"],
                active_athlete_ik_sumo_time_normalised_3["ankle_angle_r"],
                active_athlete_ik_sumo_time_normalised_3["ankle_angle_l"],
            ]
            ankle_flexion_conv_array = [
                active_athlete_ik_conv_time_normalised_0["ankle_angle_r"],
                active_athlete_ik_conv_time_normalised_0["ankle_angle_l"],
                active_athlete_ik_conv_time_normalised_1["ankle_angle_r"],
                active_athlete_ik_conv_time_normalised_1["ankle_angle_l"],
                active_athlete_ik_conv_time_normalised_2["ankle_angle_r"],
                active_athlete_ik_conv_time_normalised_2["ankle_angle_l"],
                active_athlete_ik_conv_time_normalised_3["ankle_angle_r"],
                active_athlete_ik_conv_time_normalised_3["ankle_angle_l"],
            ]

            ankle_flexion_sumo_array = np.array(ankle_flexion_sumo_array)
            ankle_flexion_conv_array = np.array(ankle_flexion_conv_array)

            plt.sca(axs[0])
            plt.title("HIP")
            axs[0].set_xlim(left=0, right=100)
            plot_means(hip_flexion_sumo_array, "r", "SUMO")
            plot_means(hip_flexion_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(hip_flexion_sumo_array, hip_flexion_conv_array)
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -90),
                        1,
                        300,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[0].add_patch(rec)
            plt.ylabel("Hip Flex [°]")
            plt.xlabel(x_label)

            plt.sca(axs[1])
            plt.title("KNEE")
            axs[1].set_xlim(left=0, right=100)
            plot_means(knee_flexion_sumo_array, "r", "SUMO")
            plot_means(knee_flexion_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                knee_flexion_sumo_array, knee_flexion_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -90),
                        1,
                        200,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[1].add_patch(rec)
            plt.ylabel("Knee Flex [°]")
            plt.xlabel(x_label)

            plt.sca(axs[2])
            plt.title("ANKLE")
            axs[2].set_xlim(left=0, right=100)
            plot_means(ankle_flexion_sumo_array, "r", "SUMO")
            plot_means(ankle_flexion_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                ankle_flexion_sumo_array, ankle_flexion_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -90),
                        1,
                        200,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[2].add_patch(rec)
            plt.ylabel("Ankle Flex [°]")
            plt.xlabel(x_label)

            handles, labels = axs[
                0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(12, 6)
            if save_figures:
                plt.savefig(
                    "../results/ik/" + active_athlete["name"] + "_mean.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete kinematics means")
            print(e)
        ########################################### END IK #######################################################
        ###########################################  START ID #######################################################
        try:
            fig, axs = plt.subplots(2, 4)
            fig.suptitle(
                "Joint Moments Trials Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.318,
                hspace=0.183,
                top=0.904,
                right=0.91,
                left=0.051,
                bottom=0.064,
            )
            coordinates_r = [
                "hip_flexion_r_moment",
                "hip_adduction_r_moment",
                "knee_angle_r_moment",
                "ankle_angle_r_moment",
            ]
            coordinates_l = [
                "hip_flexion_l_moment",
                "hip_adduction_l_moment",
                "knee_angle_l_moment",
                "ankle_angle_l_moment",
            ]
            ylabels = [
                "Hip Flex Moment [Nm]",
                "Hip Add Moment [Nm]",
                "Knee Flex Moment [Nm]",
                "Ankle Flex Moment [Nm]",
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
            fig.set_size_inches(14, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/id/" + active_athlete["name"] + "_trials.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athletes joint moments trials")
            print(e)

        try:
            fig, axs = plt.subplots(1, 4)
            fig.suptitle(
                "Joint Moments Means Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.249,
                hspace=0.19,
                top=0.883,
                right=0.918,
                left=0.057,
                bottom=0.094,
            )
            hip_flexion_moment_sumo_array = [
                active_athlete_id_sumo_time_normalised_0["hip_flexion_r_moment"],
                active_athlete_id_sumo_time_normalised_0["hip_flexion_l_moment"],
                active_athlete_id_sumo_time_normalised_1["hip_flexion_r_moment"],
                active_athlete_id_sumo_time_normalised_1["hip_flexion_l_moment"],
                active_athlete_id_sumo_time_normalised_2["hip_flexion_r_moment"],
                active_athlete_id_sumo_time_normalised_2["hip_flexion_l_moment"],
                active_athlete_id_sumo_time_normalised_3["hip_flexion_r_moment"],
                active_athlete_id_sumo_time_normalised_3["hip_flexion_l_moment"],
            ]

            hip_flexion_moment_conv_array = [
                active_athlete_id_conv_time_normalised_0["hip_flexion_r_moment"],
                active_athlete_id_conv_time_normalised_0["hip_flexion_l_moment"],
                active_athlete_id_conv_time_normalised_1["hip_flexion_r_moment"],
                active_athlete_id_conv_time_normalised_1["hip_flexion_l_moment"],
                active_athlete_id_conv_time_normalised_2["hip_flexion_r_moment"],
                active_athlete_id_conv_time_normalised_2["hip_flexion_l_moment"],
                active_athlete_id_conv_time_normalised_3["hip_flexion_r_moment"],
                active_athlete_id_conv_time_normalised_3["hip_flexion_l_moment"],
            ]
            hip_flexion_moment_sumo_array = np.array(hip_flexion_moment_sumo_array)
            hip_flexion_moment_conv_array = np.array(hip_flexion_moment_conv_array)

            hip_adduction_moment_sumo_array = [
                active_athlete_id_sumo_time_normalised_0["hip_adduction_r_moment"],
                active_athlete_id_sumo_time_normalised_0["hip_adduction_l_moment"],
                active_athlete_id_sumo_time_normalised_1["hip_adduction_r_moment"],
                active_athlete_id_sumo_time_normalised_1["hip_adduction_l_moment"],
                active_athlete_id_sumo_time_normalised_2["hip_adduction_r_moment"],
                active_athlete_id_sumo_time_normalised_2["hip_adduction_l_moment"],
                active_athlete_id_sumo_time_normalised_3["hip_adduction_r_moment"],
                active_athlete_id_sumo_time_normalised_3["hip_adduction_l_moment"],
            ]
            hip_adduction_moment_conv_array = [
                active_athlete_id_conv_time_normalised_0["hip_adduction_r_moment"],
                active_athlete_id_conv_time_normalised_0["hip_adduction_l_moment"],
                active_athlete_id_conv_time_normalised_1["hip_adduction_r_moment"],
                active_athlete_id_conv_time_normalised_1["hip_adduction_l_moment"],
                active_athlete_id_conv_time_normalised_2["hip_adduction_r_moment"],
                active_athlete_id_conv_time_normalised_2["hip_adduction_l_moment"],
                active_athlete_id_conv_time_normalised_3["hip_adduction_r_moment"],
                active_athlete_id_conv_time_normalised_3["hip_adduction_l_moment"],
            ]
            hip_adduction_moment_sumo_array = np.array(hip_adduction_moment_sumo_array)
            hip_adduction_moment_conv_array = np.array(hip_adduction_moment_conv_array)

            knee_flexion_moment_sumo_array = [
                active_athlete_id_sumo_time_normalised_0["knee_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_0["knee_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_1["knee_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_1["knee_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_2["knee_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_2["knee_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_3["knee_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_3["knee_angle_l_moment"],
            ]
            knee_flexion_moment_conv_array = [
                active_athlete_id_conv_time_normalised_0["knee_angle_r_moment"],
                active_athlete_id_conv_time_normalised_0["knee_angle_l_moment"],
                active_athlete_id_conv_time_normalised_1["knee_angle_r_moment"],
                active_athlete_id_conv_time_normalised_1["knee_angle_l_moment"],
                active_athlete_id_conv_time_normalised_2["knee_angle_r_moment"],
                active_athlete_id_conv_time_normalised_2["knee_angle_l_moment"],
                active_athlete_id_conv_time_normalised_3["knee_angle_r_moment"],
                active_athlete_id_conv_time_normalised_3["knee_angle_l_moment"],
            ]
            knee_flexion_moment_sumo_array = np.array(knee_flexion_moment_sumo_array)
            knee_flexion_moment_conv_array = np.array(knee_flexion_moment_conv_array)

            ankle_flexion_moment_sumo_array = [
                active_athlete_id_sumo_time_normalised_0["ankle_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_0["ankle_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_1["ankle_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_1["ankle_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_2["ankle_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_2["ankle_angle_l_moment"],
                active_athlete_id_sumo_time_normalised_3["ankle_angle_r_moment"],
                active_athlete_id_sumo_time_normalised_3["ankle_angle_l_moment"],
            ]
            ankle_flexion_moment_conv_array = [
                active_athlete_id_conv_time_normalised_0["ankle_angle_r_moment"],
                active_athlete_id_conv_time_normalised_0["ankle_angle_l_moment"],
                active_athlete_id_conv_time_normalised_1["ankle_angle_r_moment"],
                active_athlete_id_conv_time_normalised_1["ankle_angle_l_moment"],
                active_athlete_id_conv_time_normalised_2["ankle_angle_r_moment"],
                active_athlete_id_conv_time_normalised_2["ankle_angle_l_moment"],
                active_athlete_id_conv_time_normalised_3["ankle_angle_r_moment"],
                active_athlete_id_conv_time_normalised_3["ankle_angle_l_moment"],
            ]
            ankle_flexion_moment_sumo_array = np.array(ankle_flexion_moment_sumo_array)
            ankle_flexion_moment_conv_array = np.array(ankle_flexion_moment_conv_array)

            plt.sca(axs[0])
            plt.title("HIP FLEXION")
            axs[0].set_xlim(left=0, right=100)
            plot_means(hip_flexion_moment_sumo_array, "r", "SUMO")
            plot_means(hip_flexion_moment_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                hip_flexion_moment_sumo_array, hip_flexion_moment_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -600),
                        1,
                        600,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[0].add_patch(rec)
            plt.ylabel("Hip Moment [Nm]")
            plt.xlabel(x_label)

            plt.sca(axs[1])
            plt.title("HIP ADDUCTION")
            axs[1].set_xlim(left=0, right=100)
            plot_means(hip_adduction_moment_sumo_array, "r", "SUMO")
            plot_means(hip_adduction_moment_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                hip_adduction_moment_sumo_array, hip_adduction_moment_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -600),
                        1,
                        600,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[1].add_patch(rec)
            plt.ylabel("Hip Moment [Nm]")
            plt.xlabel(x_label)

            plt.sca(axs[2])
            plt.title("KNEE")
            axs[2].set_xlim(left=0, right=100)
            plot_means(knee_flexion_moment_sumo_array, "r", "SUMO")
            plot_means(knee_flexion_moment_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                knee_flexion_moment_sumo_array, knee_flexion_moment_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -300),
                        1,
                        600,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[2].add_patch(rec)
            plt.ylabel("Knee Moment [Nm]")
            plt.xlabel(x_label)

            plt.sca(axs[3])
            plt.title("ANKLE")
            axs[3].set_xlim(left=0, right=100)
            plot_means(ankle_flexion_moment_sumo_array, "r", "SUMO")
            plot_means(ankle_flexion_moment_conv_array, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                ankle_flexion_moment_sumo_array, ankle_flexion_moment_conv_array
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -600),
                        1,
                        600,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[3].add_patch(rec)
            plt.ylabel("Ankle Moment [Nm]")
            plt.xlabel(x_label)

            handles, labels = axs[
                0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(14.5, 5.5)
            if save_figures:
                plt.savefig(
                    "../results/id/" + active_athlete["name"] + "_mean.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete dynamics means")
            print(e)
        ###########################################  END ID #######################################################
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
            fig, axs = plt.subplots(3, 3)
            fig.suptitle(
                "Muscle Force Groups Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.275,
                hspace=0.198,
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
                    "../results/muscle_forces/"
                    + active_athlete["name"]
                    + "_trials.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in process athlete muscle force groups trials")
            print(e)

        try:
            fig, axs = plt.subplots(3, 3)
            fig.suptitle(
                "Muscle Force Groups Means Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.275,
                hspace=0.198,
                top=0.935,
                right=0.921,
                left=0.06,
                bottom=0.06,
            )
            active_athlete_hamstrings_medial_sumo = [
                active_athlete_hamstrings_medial_sumo_force_0,
                active_athlete_hamstrings_medial_sumo_force_1,
                active_athlete_hamstrings_medial_sumo_force_2,
                active_athlete_hamstrings_medial_sumo_force_3,
            ]
            active_athlete_hamstrings_medial_conv = [
                active_athlete_hamstrings_medial_conv_force_0,
                active_athlete_hamstrings_medial_conv_force_1,
                active_athlete_hamstrings_medial_conv_force_2,
                active_athlete_hamstrings_medial_conv_force_3,
            ]
            active_athlete_hamstrings_medial_sumo = np.array(
                active_athlete_hamstrings_medial_sumo
            )
            active_athlete_hamstrings_medial_conv = np.array(
                active_athlete_hamstrings_medial_conv
            )

            # hamstrings medial
            plt.sca(axs[0, 0])
            axs[0, 0].set_xlim(left=0, right=100)
            plot_means(active_athlete_hamstrings_medial_sumo, "r", "SUMO")
            plot_means(active_athlete_hamstrings_medial_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_hamstrings_medial_sumo,
                active_athlete_hamstrings_medial_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[0, 0].add_patch(rec)
            plt.ylabel("Hamstrings medial [N]")

            active_athlete_hamstrings_lateral_sumo = [
                active_athlete_hamstrings_lateral_sumo_force_0,
                active_athlete_hamstrings_lateral_sumo_force_1,
                active_athlete_hamstrings_lateral_sumo_force_2,
                active_athlete_hamstrings_lateral_sumo_force_3,
            ]
            active_athlete_hamstrings_lateral_conv = [
                active_athlete_hamstrings_lateral_conv_force_0,
                active_athlete_hamstrings_lateral_conv_force_1,
                active_athlete_hamstrings_lateral_conv_force_2,
                active_athlete_hamstrings_lateral_conv_force_3,
            ]
            active_athlete_hamstrings_lateral_sumo = np.array(
                active_athlete_hamstrings_lateral_sumo
            )
            active_athlete_hamstrings_lateral_conv = np.array(
                active_athlete_hamstrings_lateral_conv
            )

            # hamstrings lateral
            plt.sca(axs[0, 1])
            axs[0, 1].set_xlim(left=0, right=100)
            plot_means(active_athlete_hamstrings_lateral_sumo, "r", "SUMO")
            plot_means(active_athlete_hamstrings_lateral_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_hamstrings_lateral_sumo,
                active_athlete_hamstrings_lateral_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[0, 1].add_patch(rec)
            plt.ylabel("Hamstrings lateral [N]")

            active_athlete_vasti_sumo = [
                active_athlete_vasti_sumo_force_0,
                active_athlete_vasti_sumo_force_1,
                active_athlete_vasti_sumo_force_2,
                active_athlete_vasti_sumo_force_3,
            ]
            active_athlete_vasti_conv = [
                active_athlete_vasti_conv_force_0,
                active_athlete_vasti_conv_force_1,
                active_athlete_vasti_conv_force_2,
                active_athlete_vasti_conv_force_3,
            ]
            active_athlete_vasti_sumo = np.array(active_athlete_vasti_sumo)
            active_athlete_vasti_conv = np.array(active_athlete_vasti_conv)

            # vasti
            plt.sca(axs[0, 2])
            axs[0, 2].set_xlim(left=0, right=100)
            axs[0, 2].set_ylim(bottom=0)
            plot_means(active_athlete_vasti_sumo, "r", "SUMO")
            plot_means(active_athlete_vasti_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_vasti_sumo,
                active_athlete_vasti_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -1000),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[0, 2].add_patch(rec)
            plt.ylabel("Vasti [N]")

            active_athlete_gluteusmax_sumo = [
                active_athlete_gluteusmax_sumo_force_0,
                active_athlete_gluteusmax_sumo_force_1,
                active_athlete_gluteusmax_sumo_force_2,
                active_athlete_gluteusmax_sumo_force_3,
            ]
            active_athlete_gluteusmax_conv = [
                active_athlete_gluteusmax_conv_force_0,
                active_athlete_gluteusmax_conv_force_1,
                active_athlete_gluteusmax_conv_force_2,
                active_athlete_gluteusmax_conv_force_3,
            ]
            active_athlete_gluteusmax_sumo = np.array(active_athlete_gluteusmax_sumo)
            active_athlete_gluteusmax_conv = np.array(active_athlete_gluteusmax_conv)

            # gluteus maximus
            plt.sca(axs[1, 0])
            axs[1, 0].set_xlim(left=0, right=100)
            axs[1, 0].set_ylim(bottom=0)
            plot_means(active_athlete_gluteusmax_sumo, "r", "SUMO")
            plot_means(active_athlete_gluteusmax_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_gluteusmax_sumo,
                active_athlete_gluteusmax_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -1000),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[1, 0].add_patch(rec)
            plt.ylabel("Gluteus maximus [N]")

            active_athlete_adductors_sumo = [
                active_athlete_adductors_sumo_force_0,
                active_athlete_adductors_sumo_force_1,
                active_athlete_adductors_sumo_force_2,
                active_athlete_adductors_sumo_force_3,
            ]
            active_athlete_adductors_conv = [
                active_athlete_adductors_conv_force_0,
                active_athlete_adductors_conv_force_1,
                active_athlete_adductors_conv_force_2,
                active_athlete_adductors_conv_force_3,
            ]
            active_athlete_adductors_sumo = np.array(active_athlete_adductors_sumo)
            active_athlete_adductors_conv = np.array(active_athlete_adductors_conv)

            # adductors
            plt.sca(axs[1, 1])
            axs[1, 1].set_xlim(left=0, right=100)
            plot_means(active_athlete_adductors_sumo, "r", "SUMO")
            plot_means(active_athlete_adductors_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_adductors_sumo,
                active_athlete_adductors_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[1, 1].add_patch(rec)
            plt.ylabel("Adductors [N]")

            active_athlete_gluteusmed_sumo = [
                active_athlete_gluteusmed_sumo_force_0,
                active_athlete_gluteusmed_sumo_force_1,
                active_athlete_gluteusmed_sumo_force_2,
                active_athlete_gluteusmed_sumo_force_3,
            ]
            active_athlete_gluteusmed_conv = [
                active_athlete_gluteusmed_conv_force_0,
                active_athlete_gluteusmed_conv_force_1,
                active_athlete_gluteusmed_conv_force_2,
                active_athlete_gluteusmed_conv_force_3,
            ]
            active_athlete_gluteusmed_sumo = np.array(active_athlete_gluteusmed_sumo)
            active_athlete_gluteusmed_conv = np.array(active_athlete_gluteusmed_conv)

            # gluteus medius
            plt.sca(axs[1, 2])
            axs[1, 2].set_xlim(left=0, right=100)
            plot_means(active_athlete_gluteusmed_sumo, "r", "SUMO")
            plot_means(active_athlete_gluteusmed_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_gluteusmed_sumo,
                active_athlete_gluteusmed_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[1, 2].add_patch(rec)
            plt.ylabel("Gluteus medius [N]")

            active_athlete_triceps_surae_sumo = [
                active_athlete_triceps_surae_sumo_force_0,
                active_athlete_triceps_surae_sumo_force_1,
                active_athlete_triceps_surae_sumo_force_2,
                active_athlete_triceps_surae_sumo_force_3,
            ]
            active_athlete_triceps_surae_conv = [
                active_athlete_triceps_surae_conv_force_0,
                active_athlete_triceps_surae_conv_force_1,
                active_athlete_triceps_surae_conv_force_2,
                active_athlete_triceps_surae_conv_force_3,
            ]
            active_athlete_triceps_surae_sumo = np.array(
                active_athlete_triceps_surae_sumo
            )
            active_athlete_triceps_surae_conv = np.array(
                active_athlete_triceps_surae_conv
            )

            # Triceps surae
            plt.sca(axs[2, 0])
            axs[2, 0].set_xlim(left=0, right=100)
            plot_means(active_athlete_triceps_surae_sumo, "r", "SUMO")
            plot_means(active_athlete_triceps_surae_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_triceps_surae_sumo,
                active_athlete_triceps_surae_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[2, 0].add_patch(rec)
            plt.ylabel("Triceps surae [N]")
            plt.xlabel(x_label)

            active_athlete_hip_flexors_sumo = [
                active_athlete_hip_flexors_sumo_force_0,
                active_athlete_hip_flexors_sumo_force_1,
                active_athlete_hip_flexors_sumo_force_2,
                active_athlete_hip_flexors_sumo_force_3,
            ]
            active_athlete_hip_flexors_conv = [
                active_athlete_hip_flexors_conv_force_0,
                active_athlete_hip_flexors_conv_force_1,
                active_athlete_hip_flexors_conv_force_2,
                active_athlete_hip_flexors_conv_force_3,
            ]
            active_athlete_hip_flexors_sumo = np.array(active_athlete_hip_flexors_sumo)
            active_athlete_hip_flexors_conv = np.array(active_athlete_hip_flexors_conv)
            # hip flexors
            plt.sca(axs[2, 1])
            axs[2, 1].set_xlim(left=0, right=100)
            plot_means(active_athlete_hip_flexors_sumo, "r", "SUMO")
            plot_means(active_athlete_hip_flexors_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_hip_flexors_sumo,
                active_athlete_hip_flexors_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[2, 1].add_patch(rec)
            plt.ylabel("Hip flexors [N]")
            plt.xlabel(x_label)

            active_athlete_gluteusmin_sumo = [
                active_athlete_gluteusmin_sumo_force_0,
                active_athlete_gluteusmin_sumo_force_1,
                active_athlete_gluteusmin_sumo_force_2,
                active_athlete_gluteusmin_sumo_force_3,
            ]
            active_athlete_gluteusmin_conv = [
                active_athlete_gluteusmin_conv_force_0,
                active_athlete_gluteusmin_conv_force_1,
                active_athlete_gluteusmin_conv_force_2,
                active_athlete_gluteusmin_conv_force_3,
            ]
            active_athlete_gluteusmin_sumo = np.array(active_athlete_gluteusmin_sumo)
            active_athlete_gluteusmin_conv = np.array(active_athlete_gluteusmin_conv)

            # Gluteus minimus
            plt.sca(axs[2, 2])
            axs[2, 2].set_xlim(left=0, right=100)
            plot_means(active_athlete_gluteusmin_sumo, "r", "SUMO")
            plot_means(active_athlete_gluteusmin_conv, "b", "CONV")
            t = spm1d.stats.ttest_paired(
                active_athlete_gluteusmin_sumo,
                active_athlete_gluteusmin_conv,
            )
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, -100),
                        1,
                        30000,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs[2, 2].add_patch(rec)
            plt.ylabel("Gluteus minimus [N]")
            plt.xlabel(x_label)

            handles, labels = axs[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig.legend(handles, labels, loc="center right")
            fig.set_size_inches(13, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/"
                    + active_athlete["name"]
                    + "_trials.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in process athlete muscle force groups means")
            print(e)
        ########################################### TOTAL FORCES ############################################
        try:
            color_sumo = "red"
            color_conv = "blue"
            linestyle_trail_1 = "dotted"
            linestyle_trail_2 = "dashed"
            linestyle_trail_3 = "dashdot"
            y_label = "Muscle force [N]"
            fig, axs = plt.subplots(2)
            fig.suptitle(
                "Total Muscle Force Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.373,
                hspace=0.262,
                top=0.89,
                right=0.988,
                left=0.076,
                bottom=0.088,
            )
            fig.set_label("Total Muscle Force [N]")

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
            fig.set_size_inches(11, 5.5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/total/"
                    + active_athlete["name"]
                    + "_trials.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in process athlete total muscle force trials")
            print(e)

        try:
            fig, axs = plt.subplots(1)
            fig.suptitle(
                "Total Muscle Force Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.386,
                hspace=0.362,
                top=0.902,
                right=0.985,
                left=0.06,
                bottom=0.083,
            )
            fig.set_label("Normalised Muscle Force [N/kg]")
            y_label = "Normalised Muscle Force [N/kg]"

            sumo_array = [
                normalize_forces(
                    active_athlete_total_sumo_force_0, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_sumo_force_1, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_sumo_force_2, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_sumo_force_3, active_athlete["bodymass"]
                ),
            ]
            conv_array = [
                normalize_forces(
                    active_athlete_total_conv_force_0, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_conv_force_1, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_conv_force_2, active_athlete["bodymass"]
                ),
                normalize_forces(
                    active_athlete_total_conv_force_3, active_athlete["bodymass"]
                ),
            ]
            sumo_array = np.array(sumo_array)
            conv_array = np.array(conv_array)

            axs.set_title(
                "Total Muscle Forces",
                fontweight="bold",
            )
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plot_means(sumo_array, "r", "SUMO")
            plot_means(conv_array, "b", "CONV")
            plt.legend(axs.lines, ["SDL", "CDL"])

            t = spm1d.stats.ttest_paired(sumo_array, conv_array)
            ti = t.inference(alpha=0.05, two_tailed=True)
            for index, value in enumerate(t.z):
                if value > ti.zstar or value < (-ti.zstar):
                    rec = plt.Rectangle(
                        (index, 0),
                        1,
                        800,
                        facecolor="lightsteelblue",
                        alpha=0.3,
                    )
                    axs.add_patch(rec)

            fig.set_size_inches(11, 6)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/total/"
                    + active_athlete["name"]
                    + "_mean.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
        except Exception as e:
            print("Error in process athlete total muscle force means with spm")
            print(e)

        try:
            label_sumo = "SDL"
            label_conv = "CDL"
            y_label = "Normalized muscle force [N/kg]"

            sumo_hip_extensors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_extensors_r", "sumo"
            )
            sumo_hip_extensors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_extensors_l", "sumo"
            )
            conv_hip_extensors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_extensors_r", "conv"
            )
            conv_hip_extensors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_extensors_l", "conv"
            )
            sumo_hip_flexors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_flexors_r", "sumo"
            )
            sumo_hip_flexors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_flexors_l", "sumo"
            )
            conv_hip_flexors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_flexors_r", "conv"
            )
            conv_hip_flexors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_flexors_l", "conv"
            )
            sumo_hip_adductors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_adductors_r", "sumo"
            )
            sumo_hip_adductors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_adductors_l", "sumo"
            )
            conv_hip_adductors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_adductors_r", "conv"
            )
            conv_hip_adductors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "hip_adductors_l", "conv"
            )
            sumo_knee_extensors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "knee_extensors_r", "sumo"
            )
            sumo_knee_extensors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "knee_extensors_l", "sumo"
            )
            conv_knee_extensors_r_active_athlete = getNormalizedForces(
                active_athlete["number"], "knee_extensors_r", "conv"
            )
            conv_knee_extensors_l_active_athlete = getNormalizedForces(
                active_athlete["number"], "knee_extensors_l", "conv"
            )
            sumo_hip_extensors_active_athlete = np.concatenate(
                (
                    sumo_hip_extensors_r_active_athlete,
                    sumo_hip_extensors_l_active_athlete,
                )
            )
            conv_hip_extensors_active_athlete = np.concatenate(
                (
                    conv_hip_extensors_r_active_athlete,
                    conv_hip_extensors_l_active_athlete,
                )
            )
            sumo_hip_flexors_active_athlete = np.concatenate(
                (sumo_hip_flexors_r_active_athlete, sumo_hip_flexors_l_active_athlete)
            )
            conv_hip_flexors_active_athlete = np.concatenate(
                (conv_hip_flexors_r_active_athlete, conv_hip_flexors_l_active_athlete)
            )
            sumo_hip_adductors_active_athlete = np.concatenate(
                (
                    sumo_hip_adductors_r_active_athlete,
                    sumo_hip_adductors_l_active_athlete,
                )
            )
            conv_hip_adductors_active_athlete = np.concatenate(
                (
                    conv_hip_adductors_r_active_athlete,
                    conv_hip_adductors_l_active_athlete,
                )
            )
            sumo_knee_extensors_active_athlete = np.concatenate(
                (
                    sumo_knee_extensors_r_active_athlete,
                    sumo_knee_extensors_l_active_athlete,
                )
            )
            conv_knee_extensors_active_athlete = np.concatenate(
                (
                    conv_knee_extensors_r_active_athlete,
                    conv_knee_extensors_l_active_athlete,
                )
            )
            fig_0, axs_0 = plt.subplots(1, 4)
            fig_0.suptitle(
                "Muscle Force Means Athlete " + str(active_athlete["number"]),
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.193,
                hspace=0.271,
                top=0.883,
                right=0.937,
                left=0.045,
                bottom=0.104,
            )

            # Hip extensors
            plt.sca(axs_0[0])
            axs_0[0].set_title(
                "Hip Extensors",
            )
            plot_means(sumo_hip_extensors_active_athlete, "r", label_sumo)
            plot_means(conv_hip_extensors_active_athlete, "b", label_conv)
            plt.ylabel(y_label)
            plt.xlabel(x_label)
            t = spm1d.stats.ttest_paired(
                sumo_hip_extensors_active_athlete, conv_hip_extensors_active_athlete
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
                    axs_0[0].add_patch(rec)

            # Hip flexors
            plt.sca(axs_0[1])
            axs_0[1].set_title(
                "Hip Flexors",
            )
            plt.xlabel(x_label)
            plot_means(sumo_hip_flexors_active_athlete, "r", label_sumo)
            plot_means(conv_hip_flexors_active_athlete, "b", label_conv)

            t = spm1d.stats.ttest_paired(
                sumo_hip_flexors_active_athlete, conv_hip_flexors_active_athlete
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
                    axs_0[1].add_patch(rec)

            # Hip adductors
            plt.sca(axs_0[2])
            axs_0[2].set_title(
                "Hip Adductors",
            )
            plt.xlabel(x_label)
            plot_means(sumo_hip_adductors_active_athlete, "r", label_sumo)
            plot_means(conv_hip_adductors_active_athlete, "b", label_conv)
            axs_0[2].set_ylim(ymin=0)

            t = spm1d.stats.ttest_paired(
                sumo_hip_adductors_active_athlete, conv_hip_adductors_active_athlete
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
                    axs_0[2].add_patch(rec)

            # row 0, column 3
            plt.sca(axs_0[3])
            axs_0[3].set_title(
                "Knee Extensors",
            )
            plt.xlabel(x_label)
            plot_means(sumo_knee_extensors_active_athlete, "r", label_sumo)
            plot_means(conv_knee_extensors_active_athlete, "b", label_conv)
            axs_0[3].set_ylim(ymin=0)

            t = spm1d.stats.ttest_paired(
                sumo_knee_extensors_active_athlete, conv_knee_extensors_active_athlete
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
                    axs_0[3].add_patch(rec)

            handles, labels = axs_0[
                0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_0.legend(handles, labels, loc="center right")
            fig_0.set_size_inches(15, 5)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/groups/"
                    + active_athlete["name"]
                    + "_mean.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
            ###############################################################################################################
        except Exception as e:
            print("Error in technique summary active athlete")
            print(e)

        try:
            y_label = "Normalized Peak Muscle Force [N/kg]"

            fig_0, axs_0 = plt.subplots(1, 4)
            fig_0.suptitle(
                "Peak Muscle Forces Athlete " + str(active_athlete["number"]),
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.33,
                hspace=0.293,
                top=0.898,
                right=0.988,
                left=0.05,
                bottom=0.044,
            )
            xlabel = ["Perferred", "Non-preferred"]
            # Hip extensors
            preferred_hip_extensors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_extensors", True
            )
            non_preferred_hip_extensors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_extensors", False
            )
            peak_forces_hip_extensors = [
                np.mean(preferred_hip_extensors_active_athlete),
                np.mean(non_preferred_hip_extensors_active_athlete),
            ]
            yerr_hip_extensors = [
                np.std(preferred_hip_extensors_active_athlete),
                np.std(non_preferred_hip_extensors_active_athlete),
            ]
            bar_labels = ["Preferred", "Non-preferred"]
            bar_colors = ["tab:red", "tab:blue"]
            rects = axs_0[0].bar(
                xlabel,
                peak_forces_hip_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[0].bar_label(rects, label_type="center", color="white")
            print(peak_forces_hip_extensors)
            axs_0[0].errorbar(
                xlabel,
                peak_forces_hip_extensors,
                yerr=yerr_hip_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            print("FRESH")
            axs_0[0].set_ylabel(y_label)
            axs_0[0].set_title("Hip Extensors")

            # Hip flexors
            preferred_hip_flexors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_flexors", True
            )
            non_preferred_hip_flexors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_flexors", False
            )
            peak_forces_hip_flexors = [
                np.mean(preferred_hip_flexors_active_athlete),
                np.mean(non_preferred_hip_flexors_active_athlete),
            ]
            yerr_hip_flexors = [
                np.std(preferred_hip_flexors_active_athlete),
                np.std(non_preferred_hip_flexors_active_athlete),
            ]
            rects = axs_0[1].bar(
                xlabel,
                peak_forces_hip_flexors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[1].bar_label(rects, label_type="center", color="white")
            axs_0[1].errorbar(
                xlabel,
                peak_forces_hip_flexors,
                yerr=yerr_hip_flexors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[1].set_ylabel(y_label)
            axs_0[1].set_title("Hip Flexors")

            preferred_hip_adductors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_adductors", True
            )
            non_preferred_sumo_hip_adductors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "hip_adductors", False
            )
            peak_forces_hip_adductors = [
                np.mean(preferred_hip_adductors_active_athlete),
                np.mean(non_preferred_sumo_hip_adductors_active_athlete),
            ]
            yerr_hip_adductors = [
                np.std(preferred_hip_adductors_active_athlete),
                np.std(non_preferred_sumo_hip_adductors_active_athlete),
            ]
            rects = axs_0[2].bar(
                xlabel,
                peak_forces_hip_adductors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[2].bar_label(rects, label_type="center", color="white")
            axs_0[2].errorbar(
                xlabel,
                peak_forces_hip_adductors,
                yerr=yerr_hip_adductors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[2].set_ylabel(y_label)
            axs_0[2].set_title("Hip Adductors")

            preferred_knee_extensors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "knee_extensors", True
            )
            non_preferred_knee_extensors_active_athlete = getNormalizedPeakForces(
                active_athlete["number"], "knee_extensors", False
            )
            peak_forces_knee_extensors = [
                np.mean(preferred_knee_extensors_active_athlete),
                np.mean(non_preferred_knee_extensors_active_athlete),
            ]
            yerr_knee_extensors = [
                np.std(preferred_knee_extensors_active_athlete),
                np.std(non_preferred_knee_extensors_active_athlete),
            ]
            rects = axs_0[3].bar(
                xlabel,
                peak_forces_knee_extensors,
                label=bar_labels,
                color=bar_colors,
            )
            axs_0[3].bar_label(rects, label_type="center", color="white")
            axs_0[3].errorbar(
                xlabel,
                peak_forces_knee_extensors,
                yerr=yerr_knee_extensors,
                fmt="o",
                color="black",
                elinewidth=3,
            )
            axs_0[3].set_ylabel(y_label)
            axs_0[3].set_title("Knee Extensors")

            fig_0.set_size_inches(12, 6)
            if save_figures:
                plt.savefig(
                    "../results/muscle_forces/peak/"
                    + active_athlete["name"]
                    + "_mean.png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()
            ###############################################################################################################
        except Exception as e:
            print("Error in process athlete peak muscle forces")
            print(e)
