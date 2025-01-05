from src.imports import plt, athletes, normalized_fiber_lengths_sumo_time_normalised_1


def run_normalized_fibres(bool):
    if bool:
        try:
            fig, axs = plt.subplots(2, 3)
            fig.suptitle(
                "Muscle Fiber Lengths Sumo "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")
            x_label = "% concentric deadlift cycle"

            plt.sca(axs[0, 0])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmax1_r"],
                label="Glmax 1",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmax2_r"],
                label="Glmax 2",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmax3_r"],
                label="Glmax 3",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[0, 1])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["vaslat_r"],
                label="Vastus lat",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["vasmed_r"],
                label="Vastus med",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["vasint_r"],
                label="Vastus int",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[0, 2])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["semiten_r"],
                label="Semiten",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["semimem_r"],
                label="Semimem",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["bflh_r"],
                label="BFLH",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["bfsh_r"],
                label="BFSH",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 0])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmed1_r"],
                label="glmed1_r",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmed2_r"],
                label="glmed2_r",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["glmed3_r"],
                label="glmed3_r",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 1])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["addbrev_r"],
                label="addbrev",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["addlong_r"],
                label="addlong",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["addmagDist_r"],
                label="addmagDist",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.sca(axs[1, 2])
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["gaslat_r"],
                label="gaslat_r",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["gasmed_r"],
                label="gasmed_r",
            )
            plt.plot(
                normalized_fiber_lengths_sumo_time_normalised_1["soleus_r"],
                label="soleus_r",
            )
            plt.ylabel("Normalized fiber length [l/l_opt]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()

        except Exception as e:
            print("Error in run_trail_comparison")
            print(e)
