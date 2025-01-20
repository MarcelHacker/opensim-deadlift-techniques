import numpy as np
import matplotlib.pyplot as plt
from src.imports import (
    emg_filter,
    time_normalise_df,
    active_athlete,
    active_athlete_emg_channels_order,
    active_athlete_activations_emg_conv_0,
    active_athlete_activations_conv_time_normalised_0,
)

# emg_filter(df, measurement_frequency=2000, band_lowcut=30, band_highcut=400, lowcut=6, order=4)
# filter emg data without time normalisation. This comes only after the filtering not before.
filtered_emg = emg_filter(active_athlete_activations_emg_conv_0, 2000, 30, 400, 6, 4)
print("filtered:", filtered_emg)
print("EMG: ", active_athlete_activations_emg_conv_0)

filtered_emg_conv_time_normalised_0 = time_normalise_df(filtered_emg)
active_athlete_activations_emg_conv_time_normalised_0 = time_normalise_df(
    active_athlete_activations_emg_conv_0
)


def run_norm_emg_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            figure_prefix = "emg_comparison_conv_0_"
            rows = 6
            cols = 2
            color_opensim_activations = "black"
            color_emg_filtered = "blue"
            color_emg_raw = "red"
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
                wspace=0.98,
                hspace=0.315,
                top=0.901,
                right=0.942,
                left=0.049,
                bottom=0.065,
            )
            fig.set_label("EMG Data")  # backup label
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
            for i in range(len(coordinates_r)):
                current_muscle = coordinates_r[i]
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.title(coordinates_r[i])
                            plt.xlabel(x_label)
                            ax1[0, i].set_ylabel(
                                "Activation", color=color_opensim_activations
                            )
                            ax1[0, i].plot(
                                active_athlete_activations_conv_time_normalised_0[
                                    coordinates_r[i]
                                ],
                                color=color_opensim_activations,
                            )
                            ax1[0, i].tick_params(
                                axis="y", labelcolor=color_opensim_activations
                            )
                            ax1[0, i].set_xlabel(x_label)

                            ax2 = ax1[
                                0, i
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax2.plot(
                                active_athlete_activations_emg_conv_time_normalised_0[
                                    value
                                ],
                                color=color_emg_raw,
                            )
                            ax2.tick_params(axis="y", labelcolor=color_emg_raw)
                            ax3 = ax1[
                                0, i
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax3.plot(
                                filtered_emg_conv_time_normalised_0[value],
                                color=color_emg_filtered,
                            )
                            ax3.tick_params(axis="y", labelcolor=color_emg_filtered)

            for j in range(len(coordinates_l)):
                current_muscle = coordinates_l[j]
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            plt.title(coordinates_l[j])
                            plt.xlabel(x_label)
                            ax1[1, j].set_xlabel(x_label)
                            ax1[1, j].set_ylabel(
                                "Activation"
                            )  # we already handled the x-label with ax1
                            ax1[1, j].plot(
                                active_athlete_activations_conv_time_normalised_0[
                                    coordinates_l[j]
                                ],
                                color=color_opensim_activations,
                                label="COMPUTED",
                            )
                            ax1[1, j].tick_params(
                                axis="y", labelcolor=color_opensim_activations
                            )
                            ax2 = ax1[
                                1, j
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax2.plot(
                                active_athlete_activations_emg_conv_time_normalised_0[
                                    value
                                ],
                                color=color_emg_raw,
                                label="EMG raw",
                            )
                            ax2.tick_params(axis="y", labelcolor=color_emg_raw)
                            ax3 = ax1[
                                1, j
                            ].twinx()  # instantiate a second Axes that shares the same x-axis
                            ax3.plot(
                                filtered_emg_conv_time_normalised_0[value],
                                color=color_emg_filtered,
                                label="EMG filtered",
                            )
                            ax3.tick_params(axis="y", labelcolor=color_emg_filtered)

            fig.set_size_inches(13, 7.5)
            plt.savefig(
                "../results/so/" + figure_prefix + active_athlete["name"] + ".png",
                transparent=None,
                dpi=300,
                format="png",
            )
            plt.show()

        except Exception as e:
            print("Error in run_norm_emg_plot")
            print(e)
