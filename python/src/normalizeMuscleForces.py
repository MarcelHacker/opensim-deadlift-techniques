import opensim as osim
from src.imports import plt, athletes, dir_name, muscle_forces_sumo_mean


def normalize_Force(muscle_forces):
    """
    Normalize muscle force on maximum isometric force

    Return:
    Time normalized and normalized muscle forces
    """
    muscle_name = ["glmax1_r", "glmax2_r", "glmax3_r"]
    model_path = (
        dir_name + "/athlete_0_increased_force_3/athlete_0_increased_force_3.osim"
    )
    normalized_forces = muscle_forces.copy()

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in muscle_name:
        target = model.getMuscles().get(muscle)
        current_max_force = target.getMaxIsometricForce()
        print("\n MAXIMUM ISOMETRIC FORCE:", current_max_force)
        # time normalized muscle forces
        normalized_forces[muscle_name] = muscle_forces[muscle_name] / current_max_force

    return normalized_forces


def run_normalized_muscle_force(bool):
    normalized_forces = normalize_Force(
        muscle_forces_sumo_mean
    )  # refactor for all muscles

    if bool:
        try:
            color_sumo = "red"
            color_conv = "blue"
            label_sumo = "Sumo"
            label_conv = "Conventional 80%"
            x_label = "% concentric deadlift cycle"
            fig, axs = plt.subplots(1)
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

            # print(normalized_forces)

            ## kinematics of hip, knee and ankle, and muscle forces
            # angles from both and mean value
            plt.sca(axs)
            plt.plot(normalized_forces["glmax1_r"], label="glmax1_r")
            plt.plot(normalized_forces["glmax2_r"], label="glmax2_r")
            plt.plot(normalized_forces["glmax3_r"], label="glmax3_r")
            plt.ylabel("Normalized muscle force [1]")
            plt.legend()
            plt.xlabel(x_label)

            plt.show()
        except Exception as e:
            print("Error in run_normalized_muscle_force")
            print(e)
