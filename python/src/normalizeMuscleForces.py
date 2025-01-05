import opensim as osim
from src.imports import plt, athletes


def normalize_Force(muscle):
    # needs time normalized values
    print(athletes[0].osim)
    model_path = athletes[0].osim
    print(model_path)
    # time normalized values
    normalized_force = [0] * 101

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in model.getMuscles():
        current_max_force = muscle.getMaxIsometricForce()

    normalize_force = normalize_force / current_max_force
    print(normalized_force)
    return normalized_force


def run_normalized_muscle_force(bool):
    muscles_of_interest = ["glmax1_r", ""]
    if bool:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional 80%"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(1)
            fig.suptitle(
                "Kinematics, Kinetics & Muscle Force Comparison "
                + athletes[0].name
                + "; Model: "
                + athletes[0].model
                + "; Preferred: "
                + athletes[0].technique,
                fontweight="bold",
            )
            fig.set_label("Muscle Forces R")

            ## kinematics of hip, knee and ankle, and muscle forces
            # angles from both and mean value
            plt.sca(axs[0])
            plt.plot(label=label_sumo, color=color_sumo)
            plt.plot(label=label_conv, color=color_conv)
            plt.ylabel("Gluteus minimus [N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_muscle_force_sum_plot")
            print(e)
