from src.imports import (
    plt,
    athletes,
    normalize_Force,
    muscle_forces_sumo_mean,
    muscle_forces_conv_mean,
)


def run_normalized_muscle_force(bool):
    normalized_forces_sumo = normalize_Force(muscle_forces_sumo_mean)
    normalized_forces_conv = normalize_Force(muscle_forces_conv_mean)

    if bool:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conv"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(6, 3)
            fig.suptitle(
                "Muscle Force Sumo "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")

            plt.sca(axs[0, 0])
            plt.title("Gluteus maximus 1", fontsize=12)
            plt.plot(
                normalized_forces_sumo["glmax1_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["glmax1_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.title("Gluteus maximus 2", fontsize=12)
            plt.plot(
                normalized_forces_sumo["glmax2_r"],
                label="Sumo glmax2_r",
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["glmax2_r"],
                label="Conv glmax2_r",
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.title("Gluteus maximus 3", fontsize=12)
            plt.plot(
                normalized_forces_sumo["glmax3_r"],
                label="Sumo glmax3_r",
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["glmax3_r"],
                label="Conv glmax3_r",
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_normalized_muscle_force")
            print(e)
