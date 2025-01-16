import numpy as np
import matplotlib.pyplot as plt
from src.imports import (
    emg_filter,
    active_athlete,
    active_athlete_emg_channels_order,
    active_athlete_activations_emg_conv_0,
)

# emg_filter(df, measurement_frequency=2000, band_lowcut=30, band_highcut=400, lowcut=6, order=4)
# filter emg data without time normalisation. This comes only after the filtering not before.
filtered_emg = emg_filter(active_athlete_activations_emg_conv_0, 2000, 30, 400, 6, 4)
print("filtered:", filtered_emg)
print("EMG: ", active_athlete_activations_emg_conv_0)


def run_raw_emg_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 6
            cols = 2
            color_emg_filtered = "blue"
            color_emg_raw = "red"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "EMG Raw & Filtered CONV 0; "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.386,
                hspace=0.324,
                top=0.901,
                right=0.988,
                left=0.04,
                bottom=0.064,
            )
            fig.set_label("Activations")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "semiten_r",
                "glmax2_r",
                "recfem_r",
                "vaslat_r",
                "addmagIsch_r",
                "tibant_r",
            ]

            coordinates_l = [
                "semiten_l",
                "glmax2_l",
                "recfem_l",
                "vaslat_l",
                "addmagIsch_l",
                "tibant_l",
            ]

            ylabels = [
                "semiten",
                "glmax2",
                "recfem",
                "vaslat",
                "addmagIsch",
                "tibant",
            ]

            for i in range(len(coordinates_r)):
                current_muscle = coordinates_r[i]
                plt.title("Conventional Deadlift R")
                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.sca(axs[0, i])
                            plt.plot(
                                active_athlete_activations_emg_conv_0[value],
                                label="EMG raw",
                                color=color_emg_raw,
                            )
                            plt.secondary_yaxis(
                                filtered_emg[value],
                                label="EMG filtered",
                                color=color_emg_filtered,
                            )

                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for j in range(len(coordinates_l)):
                current_muscle = coordinates_l[j]
                plt.sca(axs[1, j])
                plt.title("Conventional Deadlift L")
                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.plot(
                                active_athlete_activations_emg_conv_0[value],
                                label="EMG raw",
                                color=color_emg_raw,
                            )
                            plt.plot(
                                filtered_emg[value] * 1000,
                                label="EMG filtered",
                                color=color_emg_filtered,
                            )

                plt.legend()
                plt.ylabel(ylabels[j])
                plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_raw_emg_plot")
            print(e)
