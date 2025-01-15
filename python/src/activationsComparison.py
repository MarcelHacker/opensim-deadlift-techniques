import pandas as pd
import numpy as np
from scipy import signal
from src.imports import (
    plt,
    active_athlete,
    active_athlete_emg_channels_order,
    active_athlete_activations_conv_time_normalised_0,
    active_athlete_activations_emg_conv_time_normalised_0,
    active_athlete_activations_emg_conv_0,
)

# channels_order
# print("CHANNEL ORDER:", active_athlete_emg_channels_order)


def emg_filter(band_lowcut=30, band_highcut=400, lowcut=6, order=4):
    # analog data rate
    fs = 1000  # Hz
    if fs < band_highcut * 2:
        band_highcut = fs / 2
        print(
            "High pass frequency was too high. Using 1/2 *  sampling frequnecy instead"
        )

    analog_df = active_athlete_activations_emg_conv_time_normalised_0
    max_emg_list = []
    for col in analog_df.columns:
        max_rolling_average = np.max(
            pd.Series(analog_df[col]).rolling(200, min_periods=1).mean()
        )
        max_emg_list.append(max_rolling_average)

    nyq = 0.5 * fs
    normal_cutoff = lowcut / nyq
    b_low, a_low = signal.butter(order, normal_cutoff, btype="low", analog=False)

    low = band_lowcut / nyq
    high = band_highcut / nyq
    b_band, a_band = signal.butter(order, [low, high], btype="band")

    for col in analog_df.columns:
        top_3_values = analog_df[col].nlargest(3)  # get the 3 largest values
        print("TOP 3:", top_3_values)
        mean_maximum_signal = np.mean(top_3_values)  # cal mean of the 3 largest values
        print("MEAN MAX:", mean_maximum_signal)
        raw_emg_signal = analog_df[col]
        bandpass_signal = signal.filtfilt(b_band, a_band, raw_emg_signal)
        detrend_signal = signal.detrend(bandpass_signal, type="linear")
        rectified_signal = np.abs(detrend_signal)
        linear_envelope = signal.filtfilt(b_low, a_low, rectified_signal)
        analog_df[col] = linear_envelope / mean_maximum_signal

    return analog_df


# band_lowcut=30, band_highcut=400, lowcut=6, order=4
# filter emg data
filtered_emg = emg_filter(30, 400, 6, 4)
print(filtered_emg)


def run_activations_comparison_from_emg(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 6
            cols = 2
            color_emg = "red"
            color_computed = "blue"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Activations Trial CONV 0; "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
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
                plt.sca(axs[0, i])
                plt.title("Conventional Deadlift R")
                plt.plot(
                    active_athlete_activations_conv_time_normalised_0[current_muscle],
                    label="COMPUTED",
                    color=color_computed,
                )

                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        # print(f"{key}: {value}")
                        if key == current_muscle:
                            print(value)
                            curve = filtered_emg[value]
                            plt.plot(
                                curve,
                                label="EMG",
                                color=color_emg,
                                linestyle="dashed",
                            )

                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for j in range(len(coordinates_l)):
                current_muscle = coordinates_l[j]
                plt.sca(axs[1, j])
                plt.title("Conventional Deadlift L")
                plt.plot(
                    active_athlete_activations_conv_time_normalised_0[current_muscle],
                    label="COMPUTED",
                    color=color_computed,
                )
                # plt.plot(
                #   active_athlete_activations_emg_conv_0[current_muscle],
                #  label="COMPUTED no time norm",
                # color=color_computed,
                # )
                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            print(value)
                            curve = filtered_emg[value]
                            plt.plot(
                                curve,
                                label="EMG",
                                color=color_emg,
                                linestyle="dashed",
                            )

                plt.legend()
                plt.ylabel(ylabels[j])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_activations_comparison_from_emg")
            print(e)
