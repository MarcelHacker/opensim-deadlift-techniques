from src.imports import *
from .imports import *

# Simple Python func:

# All the coordinates From the RRA, Kinematics and inverse kinematics.
# For each coordinates one line.
# Subplot to See. 

def plot_rra_coordinates(title, technique, data_ik, data_rra, save_path=None):
    trial_colors = ["red", "blue", "orange", "darkgreen"]
    x_label = "% concentric deadlift cycle"

    fig, axs = plt.subplots(4, 3)
    fig.suptitle(title, fontweight="bold")
    plt.subplots_adjust(
        wspace=0.277, hspace=0.126, top=0.914, right=0.92, left=0.05, bottom=0.064
    )

    coordinates = {
        "coordinates_0": [
            "pelvis_tilt",
            "pelvis_list",
            "pelvis_rotation",
        ],
        "coordinates_1": [
            "pelvis_tx",
            "pelvis_ty",
            "pelvis_tz",
        ],
        "coordinates_2": [
            "hip_flexion_r",
            "knee_angle_r",
            "ankle_angle_r",
        ],
        "coordinates_3": [
            "hip_flexion_l",
            "knee_angle_l",
            "ankle_angle_l",
        ],
    }
    labels = {
        "coordinates_0": [
            "pelvis_tilt [°]",
            "pelvis_list [°]",
            "pelvis_rotation [°]",
        ],
        "coordinates_1": [
            "pelvis_tx [°]",
            "pelvis_ty [°]",
            "pelvis_tz [°]",
        ],
        "coordinates_2": [
            "hip_flexion_r [°]",
            "knee_angle_r [°]",
            "ankle_angle_r [°]",
        ],
        "coordinates_3": [
            "hip_flexion_l [°]",
            "knee_angle_l [°]",
            "ankle_angle_l [°]",
        ],
    }

    for i, coord in enumerate(coordinates["coordinates_0"]):
        plt.sca(axs[0, i])
        axs[0, i].set_xlim(0, 100)
        #plt.title("Pelvis 1")
        for j, trial_data in enumerate(data_ik):
            plt.plot(trial_data[coord], label=f"Trial_ik {j+1}", color=trial_colors[j], linestyle="dashed")
        for j, trial_data in enumerate(data_rra):
            plt.plot(trial_data[coord], label=f"Trial_rra {j+1}", color=trial_colors[j])
        plt.ylabel(labels["coordinates_0"][i])
        
    for i, coord in enumerate(coordinates["coordinates_1"]):
        plt.sca(axs[1, i])
        axs[1, i].set_xlim(0, 100)
        #plt.title("Pelvis 2")
        for j, trial_data in enumerate(data_ik):
            plt.plot(trial_data[coord], label=f"Trial_ik {j+1}", color=trial_colors[j], linestyle="dashed")
        for j, trial_data in enumerate(data_rra):
            plt.plot(trial_data[coord], label=f"Trial_rra {j+1}", color=trial_colors[j])
        plt.ylabel(labels["coordinates_1"][i])
        
    for i, coord in enumerate(coordinates["coordinates_2"]):
        plt.sca(axs[2, i])
        axs[2, i].set_xlim(0, 100)
        #plt.title("Joints right")
        for j, trial_data in enumerate(data_ik):
            plt.plot(trial_data[coord], label=f"Trial_ik {j+1}", color=trial_colors[j], linestyle="dashed")
        for j, trial_data in enumerate(data_rra):
            plt.plot(trial_data[coord], label=f"Trial_rra {j+1}", color=trial_colors[j])
        plt.ylabel(labels["coordinates_2"][i])
        
    for i, coord in enumerate(coordinates["coordinates_3"]):
        plt.sca(axs[3, i])
        axs[3, i].set_xlim(0, 100)
        #plt.title("Joints right")
        for j, trial_data in enumerate(data_ik):
            plt.plot(trial_data[coord], label=f"Trial_ik {j+1}", color=trial_colors[j], linestyle="dashed")
        for j, trial_data in enumerate(data_rra):
            plt.plot(trial_data[coord], label=f"Trial_rra {j+1}", color=trial_colors[j])
        plt.ylabel(labels["coordinates_3"][i])

    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="center right")
    fig.set_size_inches(14, 7.5)

    if save_path:
        plt.savefig(save_path, dpi=300, format="png")
    plt.show()


def run_validation_rra_athlete(run_validation, save_figures):
    if not run_validation:
        return

    try:
        plot_rra_coordinates(
            f"RRA, SDL, Athlete {active_athlete['number']}; Model: {active_athlete['model']}; Preferred: {active_athlete['technique']}; Load: {active_athlete['load']} kg",
            "SDL",
            [
                active_athlete_ik_sumo_time_normalised_0,
                active_athlete_ik_sumo_time_normalised_1,
                active_athlete_ik_sumo_time_normalised_2,
                active_athlete_ik_sumo_time_normalised_3,
            ],
            [
                active_athlete_rra_sumo_time_normalised_0,
                active_athlete_rra_sumo_time_normalised_1,
                active_athlete_rra_sumo_time_normalised_2,
                active_athlete_rra_sumo_time_normalised_3,
            ],
            (
                f"../results/validation/rra/{active_athlete['name']}_sdl.png"
                if save_figures
                else None
            ),
        )
    except Exception as e:
        print("Error in RRA Checks, SDL, Athlete", e)

    try:
        plot_rra_coordinates(
            f"RRA, CDL, Athlete {active_athlete['number']}; Model: {active_athlete['model']}; Preferred: {active_athlete['technique']}; Load: {active_athlete['load']} kg",
            "CDL",
            [
                active_athlete_ik_conv_time_normalised_0,
                active_athlete_ik_conv_time_normalised_1,
                active_athlete_ik_conv_time_normalised_2,
                active_athlete_ik_conv_time_normalised_3,
            ],
            [
                active_athlete_rra_conv_time_normalised_0,
                active_athlete_rra_conv_time_normalised_1,
                active_athlete_rra_conv_time_normalised_2,
                active_athlete_rra_conv_time_normalised_3,
            ],
            (
                f"../results/validation/rra/{active_athlete['name']}_cdl.png"
                if save_figures
                else None
            ),
        )
    except Exception as e:
        print("Error in RRA Checks, CDL, Athlete", e)
