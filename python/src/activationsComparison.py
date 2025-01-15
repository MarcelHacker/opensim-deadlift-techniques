import pandas as pd
import numpy as np
from scipy import signal
from src.imports import (
    plt,
    active_athlete,
    time_normalise_df,
    active_athlete_emg_channels_order,
    active_athlete_activations_conv_time_normalised_0,
    active_athlete_activations_emg_conv_time_normalised_0,
    active_athlete_activations_emg_conv_0,
)


def emg_filter(band_lowcut=30, band_highcut=400, lowcut=6, order=4):
    # analog data rate
    fs = 2000  # Hz
    if fs < band_highcut * 2:
        band_highcut = fs / 2
        print(
            "High pass frequency was too high. Using 1/2 *  sampling frequnecy instead"
        )

    analog_df = active_athlete_activations_emg_conv_0

    nyq = 0.5 * fs
    normal_cutoff = lowcut / nyq
    b_low, a_low = signal.butter(order, normal_cutoff, btype="low", analog=False)

    low = band_lowcut / nyq
    high = band_highcut / nyq
    b_band, a_band = signal.butter(order, [low, high], btype="band")

    for col in analog_df.columns:
        raw_emg_signal = analog_df[col]
        bandpass_signal = signal.filtfilt(b_band, a_band, raw_emg_signal)
        detrend_signal = signal.detrend(bandpass_signal, type="linear")
        rectified_signal = np.abs(detrend_signal)
        linear_envelope = signal.filtfilt(b_low, a_low, rectified_signal)
        peak_maximum = np.max(linear_envelope)
        print(col)
        print("\nMAX: \n", peak_maximum)
        analog_df[col] = linear_envelope / peak_maximum

    return analog_df


# band_lowcut=30, band_highcut=400, lowcut=6, order=4
# filter emg data
filtered_emg = emg_filter(30, 400, 6, 4)
filtered_emg.to_csv(
    "/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_1_increased_force_3/conv_dl_0/c3dfile/analog_filtered.csv"
)
filtered_emg_time_normalised_0 = time_normalise_df(filtered_emg)



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
                        if key == current_muscle:
                            # curve = filtered_emg[value]
                            plt.plot(
                                filtered_emg_time_normalised_0[value],
                                label="EMG filtered",
                                color=color_emg,
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
                # Durchlaufen der Liste und Abrufen der Werte
                for item in active_athlete_emg_channels_order:
                    for key, value in item.items():
                        if key == current_muscle:
                            print(value)
                            # curve = filtered_emg[value]
                            plt.plot(
                                filtered_emg_time_normalised_0[value],
                                label="EMG filtered",
                                color=color_emg,
                            )

                plt.legend()
                plt.ylabel(ylabels[j])
                plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_activations_comparison_from_emg")
            print(e)
