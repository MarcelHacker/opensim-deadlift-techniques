import pandas as pd
from .imports import (
    plt,
    active_athlete,
    active_athlete_muscleForces_sumo_0,
    active_athlete_momentArms_hip_flexion_r_sumo_0,
)


def calculateMuscleMoment(
    muscle_forces_so_file_time_normalised, moment_arms_ma_time_normalised
):
    muscle_moment_in_plane_time_normalised = (
        muscle_forces_so_file_time_normalised * moment_arms_ma_time_normalised
    )
    return muscle_moment_in_plane_time_normalised


hip_flexion_r_muscle_moments_sumo_time_normalised_0 = calculateMuscleMoment(
    active_athlete_muscleForces_sumo_0, active_athlete_momentArms_hip_flexion_r_sumo_0
)

print(hip_flexion_r_muscle_moments_sumo_time_normalised_0)


def run_muscle_moments_plot(bool):

    if bool:
        try:
            color_sumo = "red"
            label_sumo = "Sumo"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(1)
            fig.suptitle(
                "Muslce moment Analysis "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Muslce moment [Nm]")

            # hip
            plt.sca(axs[0])
            plt.title("Hip")
            plt.plot(
                hip_flexion_r_muscle_moments_time_normalised_0["hip_flexion_moment"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.ylabel("Muscle moment [Nm]")
            plt.xlabel(x_label)
            plt.legend()

            plt.show()
        except Exception as e:
            print("Error in run_muscle_moments_plot")
            print(e)
