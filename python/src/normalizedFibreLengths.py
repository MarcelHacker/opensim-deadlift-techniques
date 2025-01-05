from src.imports import (
    plt,
    athletes,
)


def run_normalized_fibres(bool):
    if bool:
        try:
            fig, axs = plt.subplots(2, 3)
            fig.suptitle(
                "Trail Comparison Conventional "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"
            label_data_1 = "1 conv trail"
            label_data_2 = "2 conv trail"

            plt.plot()  # add mean curve

            plt.show()

        except Exception as e:
            print("Error in run_trail_comparison")
            print(e)
