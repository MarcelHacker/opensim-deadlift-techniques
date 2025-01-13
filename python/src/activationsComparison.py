from src.imports import (
    plt,
    active_athlete,
    active_athlete_emg_channels_order,
    active_athlete_activations_conv_time_normalised_0,
    active_athlete_activations_emg_conv_time_normalised_0,
)

# channels_order
print("CHANNEL ORDER:", active_athlete_emg_channels_order)


def run_activations_comparison_from_emg(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            # create figure with 6x3 subplots (1 for sumo and 1 for conventional)
            rows = 5
            cols = 2
            color_emg = "red"
            color_computed = "blue"
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Activations Trials "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Activations")
            x_label = "% concentric deadlift cycle"

            coordinates = [
                "semiten_r",
                "glmax2_r",
                "recfem_r",
                "vaslat_r",
                "addmagIsch_r",
            ]

            ylabels = [
                "Hip Flex [°]",
                "Knee Flex [°]",
                "Ankle Flex [°]",
            ]
            for i in range(len(coordinates)):
                current_muscle = coordinates[i]
                print("currnt_muscle: ", coordinates[i])
                plt.sca(axs[0, i])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_activations_conv_time_normalised_0[current_muscle],
                    label="COMPUTED",
                    color=color_computed,
                )
                print(active_athlete_activations_conv_time_normalised_0[current_muscle])
                print(
                    active_athlete_activations_emg_conv_time_normalised_0[
                        "EMG Channels_EMG15"
                    ]
                )
                print(type(active_athlete_activations_emg_conv_time_normalised_0))
                current_channel = active_athlete_emg_channels_order[current_muscle]
                print("Current channel: ", current_channel)
                print(
                    "EMG: ",
                    active_athlete_activations_emg_conv_time_normalised_0[0],
                )
                plt.plot(
                    active_athlete_activations_emg_conv_time_normalised_0[
                        str(current_channel)
                    ],
                    label="EMG",
                    color=color_emg,
                    linestyle="dashed",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_activations_comparison_from_emg")
            print(e)
