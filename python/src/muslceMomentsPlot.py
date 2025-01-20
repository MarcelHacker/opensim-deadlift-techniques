import pandas as pd
from .imports import (
    plt,
    active_athlete,
    hip_flexion_r_muscle_moments_sumo_time_normalised_0,
    hip_flexion_r_muscle_moments_conv_time_normalised_0,
    knee_flexion_r_muscle_moments_sumo_time_normalised_0,
    knee_flexion_r_muscle_moments_conv_time_normalised_0,
)


def run_muscle_moments_plot(bool):

    if bool:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conv"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(2)
            fig.suptitle(
                "Muscle Moment Analysis "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle moment [Nm]")

            # hip
            plt.sca(axs[0])
            plt.title("Hip Flexion recfem_r")
            plt.plot(
                hip_flexion_r_muscle_moments_sumo_time_normalised_0["recfem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                hip_flexion_r_muscle_moments_conv_time_normalised_0["recfem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Muscle moment [Nm]")
            plt.xlabel(x_label)

            plt.sca(axs[1])
            plt.title("Knee Flexion recfem_r")
            plt.plot(
                knee_flexion_r_muscle_moments_sumo_time_normalised_0["recfem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                knee_flexion_r_muscle_moments_conv_time_normalised_0["recfem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Muscle moment [Nm]")
            plt.xlabel(x_label)
            plt.legend()

            plt.show()
        except Exception as e:
            print("Error in run_muscle_moments_plot")
            print(e)
