import opensim as osim
from src.imports import plt, athletes, dir_name, muscle_forces_sumo_mean

muscle_names = [
    "bflh_r",
    "bfsh_r",
    "semimem_r",
    "semiten_r",
    "bflh_l",
    "bfsh_l",
    "semimem_l",
    "semiten_l",
    "recfem_r",
    "recfem_l",
    "iliacus_r",
    "iliacus_l",
    "psoas_r",
    "psoas_l",
    "tfl_r",
    "tfl_l",
    "vaslat_r",
    "vasmed_r",
    "vasint_r",
    "vaslat_l",
    "vasmed_l",
    "vasint_l",
    "glmax1_r",
    "glmax2_r",
    "glmax3_r",
    "glmax1_l",
    "glmax2_l",
    "glmax3_l",
    "glmed1_r",
    "glmed2_r",
    "glmed3_r",
    "glmed1_l",
    "glmed2_l",
    "glmed3_l",
    "glmin1_r",
    "glmin2_r",
    "glmin3_r",
    "glmin1_l",
    "glmin2_l",
    "glmin3_l",
    "gaslat_r",
    "gasmed_r",
    "soleus_r",
    "gaslat_l",
    "gasmed_l",
    "soleus_l",
    "addbrev_r",
    "addlong_r",
    "addmagDist_r",
    "addmagIsch_r",
    "addmagMid_r",
    "addmagProx_r",
    "addbrev_l",
    "addlong_l",
    "addmagDist_l",
    "addmagIsch_l",
    "addmagMid_l",
    "addmagProx_l",
]


def normalize_Force(muscle_forces):
    """
    Normalize muscle force on maximum isometric force

    Return:
    Time normalized and normalized muscle forces of all lower body muscles
    """
    model_path = (
        dir_name + "/athlete_0_increased_force_3/athlete_0_increased_force_3.osim"
    )
    normalized_forces = muscle_forces.copy()

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in muscle_names:
        target = model.getMuscles().get(muscle)
        current_max_force = target.getMaxIsometricForce()
        print("\n MAXIMUM ISOMETRIC FORCE:", current_max_force)
        # time normalized muscle forces
        normalized_forces[muscle_names] = (
            muscle_forces[muscle_names] / current_max_force
        )

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
