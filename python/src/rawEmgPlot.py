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
            # Create some mock data
            fig, ax1 = plt.subplots(cols, rows)
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
                wspace=0.96,
                hspace=0.282,
                top=0.901,
                right=0.96,
                left=0.06,
                bottom=0.065,
            )
            fig.set_label("EMG Data")  # backup label
            x_label = "Frame"

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
            for i in range(len(coordinates_r)):
                current_muscle = coordinates_r[i]
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.title(coordinates_r[i])
                            plt.xlabel(x_label)
                            ax1[0, i].plot(
                                active_athlete_activations_emg_conv_0[value],
                                color=color_emg_raw,
                            )
                            ax1[0, i].tick_params(axis="y", labelcolor=color_emg_raw)
                            ax1[0, i].set_xlabel(x_label)
                            ax1[0, i].set_ylabel("EMG raw", color=color_emg_raw)

                            ax2 = ax1[
                                0, i
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax2.plot(
                                filtered_emg[value],
                                color=color_emg_filtered,
                            )
                            ax2.tick_params(axis="y", labelcolor=color_emg_filtered)
                            ax2.set_ylabel(
                                "EMG filtered", color=color_emg_filtered
                            )  # we already handled the x-label with ax1

            for j in range(len(coordinates_l)):
                current_muscle = coordinates_l[j]
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.title(coordinates_l[j])
                            plt.xlabel(x_label)
                            ax1[1, j].plot(
                                active_athlete_activations_emg_conv_0[value],
                                color=color_emg_raw,
                            )
                            ax1[1, j].tick_params(axis="y", labelcolor=color_emg_raw)
                            ax1[1, j].set_xlabel(x_label)
                            ax1[1, j].set_ylabel("EMG raw", color=color_emg_raw)

                            ax2 = ax1[
                                1, j
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax2.plot(
                                filtered_emg[value],
                                color=color_emg_filtered,
                            )
                            ax2.tick_params(axis="y", labelcolor=color_emg_filtered)
                            ax2.set_ylabel(
                                "EMG filtered", color=color_emg_filtered
                            )  # we already handled the x-label with ax1

            fig.tight_layout()  # otherwise the right y-label is slightly clipped
            plt.show()

        except Exception as e:
            print("Error in run_raw_emg_plot")
            print(e)


"""
backup
coordinates_r = [
                "semiten_r",
                "glmax2_r",
                "recfem_r",
            ]

            ylabels = [
                "semiten",
                "glmax2",
                "recfem",
            ]

            for i in range(len(coordinates_r)):
                current_muscle = coordinates_r[i]
                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            # plt.sca(ax1[0, i])
                            plt.title("Conventional Deadlift R")
                            plt.xlabel(x_label)
                            ax1[0, i].plot(
                                active_athlete_activations_emg_conv_0[value],
                                color=color_emg_raw,
                            )
                            ax1[0, i].tick_params(axis="y", labelcolor=color_emg_raw)
                            ax1[0, i].set_xlabel(x_label)
                            ax1[0, i].set_ylabel("EMG raw", color=color_emg_raw)

                            ax2 = (
                                ax1.twinx()
                            )  # instantiate a second Axes that shares the same x-axis
                            ax2[0, i].plot(
                                filtered_emg[value],
                                color=color_emg_filtered,
                            )
                            ax2[0, i].tick_params(
                                axis="y", labelcolor=color_emg_filtered
                            )
                            ax2[0, i].set_ylabel(
                                "EMG filtered", color=color_emg_filtered
                            )  # we already handled the x-label with ax1
                            plt.title(ylabels[i])

            fig.tight_layout()  # otherwise the right y-label is slightly clipped
            plt.show()
"""
