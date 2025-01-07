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
            # figure 1
            fig, axs = plt.subplots(3)
            fig.suptitle(
                "Muscle Force Gluteus Maximus "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")

            plt.sca(axs[0])
            plt.title(
                "Gluteus maximus 1",
                fontweight="bold",
            )
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

            plt.sca(axs[1])
            plt.title("Gluteus maximus 2", fontsize=12)
            plt.plot(
                normalized_forces_sumo["glmax2_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["glmax2_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[2])
            plt.title("Gluteus maximus 3", fontsize=12)
            plt.plot(
                normalized_forces_sumo["glmax3_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["glmax3_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            # figure 2
            fig_2, axs_2 = plt.subplots(4)
            fig_2.suptitle(
                "Muscle Forces Hamstrings "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig_2.set_label("Muscle Forces R")

            plt.sca(axs_2[0])
            plt.title("Biceps Femoris longus", fontsize=12)
            plt.plot(
                normalized_forces_sumo["bflh_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["bflh_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_2[1])
            plt.title("Biceps Femoris breve", fontsize=12)
            plt.plot(
                normalized_forces_sumo["bfsh_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["bfsh_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_2[2])
            plt.title("Semitendinosus", fontsize=12)
            plt.plot(
                normalized_forces_sumo["semiten_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["semiten_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_2[3])
            plt.title("Semimembranosus", fontsize=12)
            plt.plot(
                normalized_forces_sumo["semimem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["semimem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            # figure 3
            fig_3, axs_3 = plt.subplots(4)
            fig_3.suptitle(
                "Muscle Forces Quadriceps "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig_2.set_label("Muscle Forces R")

            plt.sca(axs_3[0])
            plt.title("Vastus lateralis", fontsize=12)
            plt.plot(
                normalized_forces_sumo["vaslat_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["vaslat_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_3[1])
            plt.title("Vastus medialis", fontsize=12)
            plt.plot(
                normalized_forces_sumo["vasmed_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["vasmed_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_3[2])
            plt.title("Vastus intermedius", fontsize=12)
            plt.plot(
                normalized_forces_sumo["vasint_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["vasint_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs_3[3])
            plt.title("Rectus femoris", fontsize=12)
            plt.plot(
                normalized_forces_sumo["recfem_r"],
                label=label_sumo,
                color=color_sumo,
            )
            plt.plot(
                normalized_forces_conv["recfem_r"],
                label=label_conv,
                color=color_conv,
            )
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_normalized_muscle_force")
            print(e)
