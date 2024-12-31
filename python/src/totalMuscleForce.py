from src.imports import (
    plt,
    athletes,
    total_muscle_forces_sumo_mean,
    total_muscle_forces_conv_mean,
)

"""
For the angles the mean of all right and left leg of the trails was used.
The joint moments are the sum of right and leg divided and then the mean of all trails
"""


def run_muscle_force_sum_plot(bool):
    if bool:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(1)
            fig.suptitle(
                "Total Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Total muscle force [N]")

            # Total force between two techniques
            plt.sca(axs)
            plt.plot(total_muscle_forces_sumo_mean, label=label_sumo, color=color_sumo)
            plt.plot(total_muscle_forces_conv_mean, label=label_conv, color=color_conv)
            plt.ylabel("Total muscle force [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_total_force_comparison")
            print(e)
