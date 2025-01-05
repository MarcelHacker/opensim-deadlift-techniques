import opensim as osim
from src.imports import plt, athletes, dir_name, muscle_forces_sumo_mean


def normalize_Force(muscle_forces, muscle_name):
    # needs time normalized values
    model_path = (
        dir_name + "/athlete_0_increased_force_3/athlete_0_increased_force_3.osim"
    )
    # time normalized values
    normalized_force = [0] * 101

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in model.getMuscles():
        print(muscle)
        print(model.getMuscles())
        if muscle == muscle_name:
            current_max_force = muscle.getMaxIsometricForce()
            print(current_max_force)
            normalized_force = muscle_forces / current_max_force
    print(normalized_force)
    return normalized_force


def run_normalized_muscle_force(bool):
    normalized_force_glmax1_r = normalize_Force(muscle_forces_sumo_mean, "glmax1_r")

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
            plt.sca(axs)
            plt.plot(normalized_force_glmax1_r, label=label_sumo, color=color_sumo)
            plt.ylabel("Gluteus maximus 1 [N/N]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_normalized_muscle_force")
            print(e)
