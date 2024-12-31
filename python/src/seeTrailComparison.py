from src.local_functions import plot_data
from src.imports import (
    plt,
    athletes,
    ik_conv_mean,
    muscleForces_conv_time_normalised_1,
    muscleForces_conv_time_normalised_2,
    muscle_forces_conv_mean,
    ik_conv_time_normalised_1,
    ik_conv_time_normalised_2,
)


def run_trail_comparison(bool):
    if bool:
        try:
            fig, axs = plt.subplots(2, 3)
            fig.suptitle(
                "Trail Comparison Conventional "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"
            label_data_1 = "1 conv trail"
            label_data_2 = "2 conv trail"

            # display mean, and trail values
            plot_data(
                axs[0, 0],  # axis
                ik_conv_time_normalised_1["hip_flexion_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                ik_conv_time_normalised_2["hip_flexion_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Hip Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(
                ik_conv_mean["hip_flexion_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[0, 1],  # axis
                ik_conv_time_normalised_1["knee_angle_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                ik_conv_time_normalised_2["knee_angle_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Knee Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(ik_conv_mean["knee_angle_r"], label="MEAN", color="gold")

            plot_data(
                axs[0, 2],  # axis
                ik_conv_time_normalised_1["ankle_angle_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                ik_conv_time_normalised_2["ankle_angle_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "Ankle Flexion [°]",  # y label
                x_label,
            ),
            plt.plot(ik_conv_mean["ankle_angle_r"], label="MEAN", color="gold")

            plot_data(
                axs[1, 0],  # axis
                muscleForces_conv_time_normalised_1["vaslat_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["vaslat_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "vaslat_r [N]",  # y label
                x_label,
            ),
            plt.plot(
                muscle_forces_conv_mean["vaslat_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[1, 1],  # axis
                muscleForces_conv_time_normalised_1["semiten_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["semiten_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "semiten_r [N]",  # y label
                x_label,
            ),
            plt.plot(
                muscle_forces_conv_mean["semiten_r"], label="MEAN", color="gold"
            )  # add mean curve

            plot_data(
                axs[1, 2],  # axis
                muscleForces_conv_time_normalised_1["glmax3_r"],  # data 1
                label_data_1,  # label data 1
                "red",  # color data 1
                muscleForces_conv_time_normalised_2["glmax3_r"],  # data 2
                label_data_2,  # label data 2
                "blue",  # color data 2
                True,  # legend
                "glmax3_r [N]",  # y label
                x_label,
            ),
            plt.sca(axs[1, 2])
            plt.plot(
                muscle_forces_conv_mean["glmax3_r"], label="MEAN", color="gold"
            )  # add mean curve

            plt.show()

        except Exception as e:
            print("Error in run_trail_comparison")
            print(e)
