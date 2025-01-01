import numpy as np
from src.imports import (
    plt,
    athletes,
    total_muscle_forces_sumo_mean,
    total_muscle_forces_conv_mean,
    vasti_sumo_force_mean,
    vasti_conv_force_mean,
    gluteusmax_sumo_force_mean,
    gluteusmax_conv_force_mean,
    hamstrings_medial_sumo_force_mean,
    hamstrings_medial_conv_force_mean,
)

"""
Plot the total muscle forces of the two techniques.
The joint moments are the sum of right and leg divided and then the mean of all trails
"""


def run_muscle_force_total_additional_plot(bool):
    if bool:
        try:
            color_sumo = "crimson"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(2)
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

            axs[0].set_yticks(np.arange(0, 26000.1, 3000))
            # Total force between two techniques
            plt.sca(axs[0])
            plt.plot(
                total_muscle_forces_sumo_mean,
                label=label_sumo,
                color=color_sumo,
                linewidth=2.0,
            )
            plt.plot(
                total_muscle_forces_conv_mean,
                label=label_conv,
                color=color_conv,
                linewidth=2.0,
            )
            plt.ylabel("Total muscle force [N]")
            plt.legend()
            plt.xlabel(x_label)

            # Total force between two techniques
            plt.sca(axs[1])
            plt.plot(
                vasti_sumo_force_mean,
                label="Vasti",
                color=color_sumo,
                linewidth=2.0,
            )
            plt.plot(
                gluteusmax_sumo_force_mean,
                label="Gluteus max",
                color="red",
                linewidth=2.0,
            )
            plt.plot(
                hamstrings_medial_sumo_force_mean,
                label="Hamstrings medial",
                color="darkred",
                linewidth=2.0,
            )
            plt.plot(vasti_conv_force_mean, label="Vasti", color="royalblue")
            plt.plot(gluteusmax_conv_force_mean, label="Gluteus max", color="navy")
            plt.plot(
                hamstrings_medial_conv_force_mean,
                label="Hamstrings medial",
                color="dodgerblue",
            )
            plt.ylabel("Muscle forces [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_total_force_comparison")
            print(e)
