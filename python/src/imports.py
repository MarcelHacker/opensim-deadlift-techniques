from src.local_functions import *
import pandas as pd
import json
import os

"""
structure:
1. class athlete
2. athletes initialisation
3. IK, ID and SO files definitions
4. Time normalisation 
5. Muscle group force sums
6. Mean value definitions
7. Angles and Moments
"""
# file_paths func parameters say which athlete is active


################################ CLASSES ###########################################
class athlete:
    def __init__(self, name, mass, model, technique):
        # informations
        self.name = name  # "athlete_x", used for reading files
        self.mass = mass  # "57"
        self.model = model  # "athlete_x_scaled"
        self.technique = technique  # "sumo" or "conventional", preffered deadlift

    def create_athlete_json(self, athlete_folder_path):

        # warning not completed
        msk.ui.show_warning("Warning", "This function is not completed yet")

        athlete_dict = {
            "paths": athlete_folder_path,
            "name": self.name,
            "mass": self.mass,
            "model": self.model,
            "technique": self.technique,
        }

        # save json file in the athlete folder
        with open(athlete_folder_path + "/settings.json", "w") as f:
            json.dump(athlete_dict, f)

        return athlete_dict


active_athlete_folder = "athlete_1_increased_force_3"

################################ CREATING ATHLETES ###########################################
active_athlete = None
athletes = []  # appending instances to athletes list
##################################################################################################

################################ GETTING ATHLETE JSON ###########################################
try:
    # fix this
    dirname = os.path.dirname(__file__)  # not used
    with open(dir_name + "/" + str(active_athlete_folder) + "/settings.json") as f:
        active_athlete = json.load(f)
        print("\nACTIVE ATHLETE:\n", active_athlete["name"])
except Exception as e:
    print("\nError in setting active_athlete; src/imports.py\n")
    print(e)

##################################################################################################
# IK sumo
try:
    active_athlete_ik_sumo_emptybar_0 = None
    active_athlete_ik_sumo_emptybar_1 = None
    active_athlete_ik_sumo_emptybar_2 = None
    active_athlete_ik_sumo_emptybar_3 = None
    active_athlete_ik_sumo_0 = pd.read_csv(
        active_athlete["paths"]["ik"]["sumo_dl_0"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_sumo_1 = pd.read_csv(
        active_athlete["paths"]["ik"]["sumo_dl_1"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_sumo_2 = pd.read_csv(
        active_athlete["paths"]["ik"]["sumo_dl_2"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_sumo_3 = None
    # IK conv
    active_athlete_ik_conv_emptybar_0 = None
    active_athlete_ik_conv_emptybar_1 = None
    active_athlete_ik_conv_emptybar_2 = None
    active_athlete_ik_conv_emptybar_3 = None
    active_athlete_ik_conv_0 = pd.read_csv(
        active_athlete["paths"]["ik"]["conv_dl_0"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_conv_1 = pd.read_csv(
        active_athlete["paths"]["ik"]["conv_dl_1"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_conv_2 = pd.read_csv(
        active_athlete["paths"]["ik"]["conv_dl_2"],
        sep="\t",
        skiprows=10,
    )
    active_athlete_ik_conv_3 = None

except Exception as e:
    print("Error in IK files; src/imports.py")
    print(e)
# ID sumo
try:
    active_athlete_id_sumo_0 = pd.read_csv(
        active_athlete["paths"]["id"]["sumo_dl_0"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_sumo_1 = pd.read_csv(
        active_athlete["paths"]["id"]["sumo_dl_1"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_sumo_2 = pd.read_csv(
        active_athlete["paths"]["id"]["sumo_dl_2"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_sumo_3 = None
    # ID conv
    active_athlete_id_conv_0 = pd.read_csv(
        active_athlete["paths"]["id"]["conv_dl_0"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_conv_1 = pd.read_csv(
        active_athlete["paths"]["id"]["conv_dl_1"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_conv_2 = pd.read_csv(
        active_athlete["paths"]["id"]["conv_dl_2"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_id_conv_3 = None
except Exception as e:
    print("Error in ID files; src/imports.py")
    print(e)

# SO muscle forces
try:
    active_athlete_muscleForces_sumo_emptybar_0 = None
    active_athlete_muscleForces_sumo_0 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["sumo_dl_0"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_sumo_1 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["sumo_dl_1"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_sumo_2 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["sumo_dl_2"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_sumo_3 = None
    active_athlete_muscleForces_conv_0 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["conv_dl_0"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_conv_1 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["conv_dl_1"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_conv_2 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["conv_dl_2"],
        sep="\t",
        skiprows=14,
    )
    active_athlete_muscleForces_conv_3 = None
except Exception as e:
    print("Error in SO muscle forces files; src/imports.py")
    print(e)
#################### MOMENT ARMS ################################################################
## SUMO
try:
    active_athlete_momentArms_hip_flexion_r_sumo_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_sumo_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_r_sumo_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_1"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_sumo_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_1"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_r_sumo_2 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_2"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_sumo_2 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_2"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_knee_flexion_r_sumo_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["knee_angle_r"]["sumo_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_knee_flexion_r_sumo_1 = (
        pd.read_csv(  # renamed the original
            active_athlete["paths"]["ma"]["moment_arm"]["knee_angle_r"]["sumo_dl_1"],
            sep="\t",
            skiprows=11,
        )
    )
    active_athlete_momentArms_ankle_flexion_r_sumo_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["ankle_angle_r"]["sumo_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_ankle_flexion_r_sumo_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["ankle_angle_r"]["sumo_dl_1"],
        sep="\t",
        skiprows=11,
    )

    ## CONVENTIONAL
    active_athlete_momentArms_hip_flexion_r_conv_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_conv_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_0"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_r_conv_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_1"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_conv_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_1"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_r_conv_2 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_2"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_conv_2 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_2"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_knee_flexion_r_conv_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["knee_angle_r"]["conv_dl_1"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_ankle_flexion_r_conv_1 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["ankle_angle_r"]["conv_dl_1"],
        sep="\t",
        skiprows=11,
    )

except Exception as e:
    print("Error in MA moment arm files; src/imports.py")
    print(e)
#################### NORMALIZED FIBER LENGTHS ################################################################
# SUMO
try:
    active_athlete_normalized_fiber_lengths_sumo_0 = None
    active_athlete_normalized_fiber_lengths_sumo_1 = None
    active_athlete_normalized_fiber_lengths_sumo_2 = None
except Exception as e:
    print("Error in MA normalized fiber lengths files; src/imports.py")
    print(e)
##################################################################################################
try:
    print("path: ", active_athlete["paths"]["so"]["activations"]["conv_dl_0"])
    active_athlete_activations_conv_0 = pd.read_csv(
        active_athlete["paths"]["so"]["activations"]["conv_dl_0"],
        sep="\t",
        skiprows=10,
    )
    print("\nACTIVATIONS muscle conv 0:\n", active_athlete_activations_conv_0)
except Exception as e:
    print("Error in muscle activations files; src/imports.py")
    print(e)
##################################################################################################
try:
    active_athlete_activations_emg_conv_0 = pd.read_csv(
        active_athlete["paths"]["emg"]["conv_dl_0"],
        sep=",",
        skiprows=0,
    )
    print("\nACTIVATIONS EMG conv 0:\n", active_athlete_activations_emg_conv_0)
except Exception as e:
    print("Error in emg activations files; src/imports.py")
    print(e)
##################################################################################################

### time normalise everything to 101 values
# ik
try:
    active_athlete_ik_sumo_emptybar_time_normalised_0 = None
    active_athlete_ik_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_ik_sumo_0
    )
    active_athlete_ik_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_ik_sumo_1
    )
    active_athlete_ik_sumo_time_normalised_2 = time_normalise_df(
        active_athlete_ik_sumo_2
    )
    active_athlete_ik_conv_time_normalised_0 = time_normalise_df(
        active_athlete_ik_conv_0
    )
    active_athlete_ik_conv_time_normalised_1 = time_normalise_df(
        active_athlete_ik_conv_1
    )
    active_athlete_ik_conv_time_normalised_2 = time_normalise_df(
        active_athlete_ik_conv_2
    )
    # id
    active_athlete_id_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_id_sumo_0
    )
    active_athlete_id_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_id_sumo_1
    )
    active_athlete_id_sumo_time_normalised_2 = time_normalise_df(
        active_athlete_id_sumo_2
    )
    active_athlete_id_conv_time_normalised_0 = time_normalise_df(
        active_athlete_id_conv_0
    )
    active_athlete_id_conv_time_normalised_1 = time_normalise_df(
        active_athlete_id_conv_1
    )
    active_athlete_id_conv_time_normalised_2 = time_normalise_df(
        active_athlete_id_conv_2
    )
    # muscle forces
    active_athlete_muscleForces_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_muscleForces_sumo_0
    )
    active_athlete_muscleForces_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_muscleForces_sumo_1
    )
    active_athlete_muscleForces_sumo_time_normalised_2 = time_normalise_df(
        active_athlete_muscleForces_sumo_2
    )
    active_athlete_muscleForces_conv_time_normalised_0 = time_normalise_df(
        active_athlete_muscleForces_conv_0
    )
    active_athlete_muscleForces_conv_time_normalised_1 = time_normalise_df(
        active_athlete_muscleForces_conv_1
    )
    active_athlete_muscleForces_conv_time_normalised_2 = time_normalise_df(
        active_athlete_muscleForces_conv_2
    )
    active_athlete_muscleForces_sumo_emptybar_time_normalised_0 = None
except Exception as e:
    print("Error in time normalisation id,ik and muscle force files; src/imports.py")
    print(e)
    ## moment arms
    # sumo
try:
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_sumo_0
    )
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_sumo_0
    )
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_sumo_1
    )
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_sumo_1
    )
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_2 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_sumo_2
    )
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_2 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_sumo_2
    )
    active_athlete_momentArms_knee_flexion_r_sumo_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_knee_flexion_r_sumo_1
    )
    active_athlete_momentArms_ankle_flexion_r_sumo_time_normalised_1 = (
        time_normalise_df(active_athlete_momentArms_ankle_flexion_r_sumo_1)
    )
    # conv
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_conv_0
    )
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_conv_0
    )
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_conv_1
    )
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_conv_1
    )
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_2 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_conv_2
    )
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_2 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_conv_2
    )
    active_athlete_momentArms_knee_flexion_r_conv_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_knee_flexion_r_conv_1
    )
    active_athlete_momentArms_ankle_flexion_r_conv_time_normalised_1 = (
        time_normalise_df(active_athlete_momentArms_ankle_flexion_r_conv_1)
    )
    ## normalized fiber lengths
    # sumo
    active_athlete_normalized_fiber_lengths_sumo_time_normalised_0 = None
    active_athlete_normalized_fiber_lengths_sumo_time_normalised_1 = None
    active_athlete_normalized_fiber_lengths_sumo_time_normalised_2 = None

except Exception as e:
    print("Error in time normalisation ma files; src/imports.py")
    print(e)

try:
    active_athlete_activations_emg_conv_time_normalised_0 = time_normalise_df(
        active_athlete_activations_emg_conv_0
    )
except Exception as e:
    print("Error in time normalisation emg activations files; src/imports.py")
    print(e)
##################################################################################################
# MUSCLE FORCES MUSCLE GROUPS, sum of both limbs, single trails
# Hamstrings medial (Semitend and Semimem)
try:
    active_athlete_hamstrings_medial_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hamstrings medial",  # Hamstrings medial
        "rl",
    )
    active_athlete_hamstrings_medial_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hamstrings medial",  # Hamstrings medial
        "rl",
    )
    active_athlete_hamstrings_medial_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hamstrings medial",  # Hamstrings medial
        "rl",
    )
    active_athlete_hamstrings_medial_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hamstrings medial",
        "rl",
    )
    active_athlete_hamstrings_medial_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hamstrings medial",
        "rl",
    )
    active_athlete_hamstrings_medial_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hamstrings medial",
        "rl",
    )
    # Hamstrings lateral (biceps long and short heads)
    active_athlete_hamstrings_lateral_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hamstrings lateral",  # Hamstrings lateral
        "rl",
    )
    active_athlete_hamstrings_lateral_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hamstrings lateral",  # Hamstrings lateral
        "rl",
    )
    active_athlete_hamstrings_lateral_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,  # muscle force data
        "Hamstrings lateral",
        "rl",
    )
    active_athlete_hamstrings_lateral_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,  # muscle force data
        "Hamstrings lateral",
        "rl",
    )

    active_athlete_vasti_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Vasti",  # Quadriceps
        "rl",
    )
    active_athlete_vasti_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Vasti",  # Quadriceps
        "rl",
    )
    active_athlete_vasti_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Vasti",  # Quadriceps
        "rl",
    )
    active_athlete_vasti_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Vasti",  # Quadriceps
        "rl",
    )

    active_athlete_gluteusmax_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    active_athlete_gluteusmax_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    active_athlete_gluteusmax_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    active_athlete_gluteusmax_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    # Gluteus Medius
    active_athlete_gluteusmed_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Gluteus medius",
        "rl",
    )
    active_athlete_gluteusmed_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Gluteus medius",
        "rl",
    )
    active_athlete_gluteusmed_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Gluteus medius",
        "rl",
    )
    active_athlete_gluteusmed_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Gluteus medius",
        "rl",
    )
    # Gluteus Minimus
    active_athlete_gluteusmin_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Gluteus minimus",
        "rl",
    )
    active_athlete_gluteusmin_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Gluteus minimus",
        "rl",
    )
    active_athlete_gluteusmin_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Gluteus minimus",
        "rl",
    )
    active_athlete_gluteusmin_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Gluteus minimus",
        "rl",
    )

    active_athlete_adductors_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Adductors",  # Adductors
        "rl",
    )
    active_athlete_adductors_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Adductors",  # Adductors
        "rl",
    )
    active_athlete_adductors_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Adductors",  # Adductors
        "rl",
    )
    active_athlete_adductors_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Adductors",  # Adductors
        "rl",
    )
    # Hip flexors
    active_athlete_hip_flexors_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Hip flexors",  # Adductors
        "rl",
    )
    active_athlete_hip_flexors_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Hip flexors",  # Adductors
        "rl",
    )
    active_athlete_hip_flexors_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip flexors",  # Adductors
        "rl",
    )
    active_athlete_hip_flexors_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip flexors",  # Adductors
        "rl",
    )

    # Triceps Surae
    active_athlete_triceps_surae_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Triceps surae",  # Adductors
        "rl",
    )
    active_athlete_triceps_surae_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Triceps surae",  # Adductors
        "rl",
    )
    active_athlete_triceps_surae_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Triceps surae",  # Adductors
        "rl",
    )
    active_athlete_triceps_surae_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Triceps surae",  # Adductors
        "rl",
    )

    active_athlete_total_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "All",  # All muscle groups
        "rl",
    )
    active_athlete_total_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "All",  # All muscle groups
        "rl",
    )
    active_athlete_total_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,  # muscle force data
        "All",  # All muscle groups
        "rl",
    )
    active_athlete_total_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,  # muscle force data
        "All",  # All muscle groups
        "rl",
    )
except Exception as e:
    print("Error in muscle force grouping files; src/imports.py")
    print(e)
##################################################################################################
##################################################################################################
## MEAN VARIABLES, absolute mean values over all trails
# IMPORTANT: only calculate the mean with the time normalised vars
try:
    active_athlete_ik_sumo_mean = get_mean_trail_values(
        active_athlete_ik_sumo_time_normalised_1,  # have to be time normalised
        active_athlete_ik_sumo_time_normalised_2,  ##!!! to do change this, when having trail 2 ready
        ## todo add trail 3
    )
    active_athlete_id_sumo_mean = get_mean_trail_values(
        active_athlete_id_sumo_time_normalised_1,  # have to be time normalised
        active_athlete_id_sumo_time_normalised_2,  ##!!! to do change this, when having trail 2 ready
        ## todo add trail 3
    )

    active_athlete_ik_conv_mean = get_mean_trail_values(
        active_athlete_ik_conv_time_normalised_1,  # have to be time normalised
        active_athlete_ik_conv_time_normalised_2,
        ## todo add trail 3
    )

    active_athlete_id_conv_mean = get_mean_trail_values(
        active_athlete_id_conv_time_normalised_1,  # have to be time normalised
        active_athlete_id_conv_time_normalised_2,
        ## todo add trail 3
    )

    active_athlete_muscle_forces_sumo_mean = get_mean_trail_values(
        active_athlete_muscleForces_sumo_time_normalised_1,  # have to be time normalised
        active_athlete_muscleForces_sumo_time_normalised_2,  # have to be time normalised
        ## todo add trail 3
    )

    active_athlete_muscle_forces_conv_mean = get_mean_trail_values(
        active_athlete_muscleForces_conv_time_normalised_1,  # have to be time normalised
        active_athlete_muscleForces_conv_time_normalised_2,  # have to be time normalised
        ## todo add trail 3
    )
except Exception as e:
    print("Error in MUSCLE FORCES MEANS; src/imports.py")
    print(e)
######################## TOTAL MUSCLE FORCES ##############################
# get mean of array values get from muscle force sums
try:
    active_athlete_total_muscle_forces_sumo_mean = get_mean_array_values(
        active_athlete_total_sumo_force_1,
        active_athlete_total_sumo_force_2,  # todo change this for 3 trails
    )
    active_athlete_total_muscle_forces_conv_mean = get_mean_array_values(
        active_athlete_total_conv_force_1,
        active_athlete_total_conv_force_2,  # todo change this for 3 trails
    )
except Exception as e:
    print("Error in TOTAL MUSCLE FORCES MEANS; src/imports.py")
    print(e)

###########################################################################
try:
    active_athlete_hamstrings_medial_sumo_force_mean = get_mean_array_values(
        active_athlete_hamstrings_medial_sumo_force_1,
        active_athlete_hamstrings_medial_sumo_force_2,  # todo change this for 3 trails
    )
    active_athlete_hamstrings_medial_conv_force_mean = get_mean_array_values(
        active_athlete_hamstrings_medial_conv_force_1,
        active_athlete_hamstrings_medial_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_hamstrings_lateral_sumo_force_mean = get_mean_array_values(
        active_athlete_hamstrings_lateral_sumo_force_1,
        active_athlete_hamstrings_lateral_sumo_force_2,  # todo change this for 3 trails
    )
    active_athlete_hamstrings_lateral_conv_force_mean = get_mean_array_values(
        active_athlete_hamstrings_lateral_conv_force_1,
        active_athlete_hamstrings_lateral_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_vasti_sumo_force_mean = get_mean_array_values(
        active_athlete_vasti_sumo_force_1, active_athlete_vasti_sumo_force_2
    )  ## todo add 3 trail
    active_athlete_vasti_conv_force_mean = get_mean_array_values(
        active_athlete_vasti_sumo_force_1,  ## todo add 3 trail
        active_athlete_vasti_conv_force_2,
    )
    active_athlete_gluteusmax_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmax_sumo_force_1,
        active_athlete_gluteusmax_sumo_force_2,  # todo add 3 trail
    )
    active_athlete_gluteusmax_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmax_conv_force_1,
        active_athlete_gluteusmax_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_adductors_sumo_force_mean = get_mean_array_values(
        active_athlete_adductors_sumo_force_1, active_athlete_adductors_sumo_force_2
    )  # todo add 3 trail
    active_athlete_adductors_conv_force_mean = get_mean_array_values(
        active_athlete_adductors_conv_force_1,
        active_athlete_adductors_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_gluteusmed_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmed_sumo_force_1, active_athlete_gluteusmed_sumo_force_2
    )  # todo add 3 trail
    active_athlete_gluteusmed_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmed_conv_force_1,
        active_athlete_gluteusmed_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_triceps_surae_sumo_force_mean = get_mean_array_values(
        active_athlete_triceps_surae_sumo_force_1,
        active_athlete_triceps_surae_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_triceps_surae_conv_force_mean = get_mean_array_values(
        active_athlete_triceps_surae_conv_force_1,
        active_athlete_triceps_surae_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_hip_flexors_sumo_force_mean = get_mean_array_values(
        active_athlete_hip_flexors_sumo_force_1, active_athlete_hip_flexors_sumo_force_2
    )  # todo add 3 trail
    active_athlete_hip_flexors_conv_force_mean = get_mean_array_values(
        active_athlete_hip_flexors_conv_force_1,
        active_athlete_hip_flexors_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_gluteusmin_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmin_sumo_force_1, active_athlete_gluteusmin_sumo_force_2
    )  # todo add 3 trail
    active_athlete_gluteusmin_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmin_conv_force_1,
        active_athlete_gluteusmin_conv_force_2,  ## todo add 3 trail
    )

except Exception as e:
    print("Error in MEAN Muscle forces; src/imports.py")
    print(e)

##################################################################################################
# ANGLES & MOMENTS of both limbs
## to do use here the mean time normalised trails ik and id, then rename vars to mean
try:
    active_athlete_mean_sumo_both_angles_and_moments = (
        sum_both_limb_moments_and_mean_angles(
            active_athlete_ik_sumo_mean, active_athlete_id_sumo_mean  # use here means
        )
    )
    active_athlete_mean_conv_both_angles_and_moments = (
        sum_both_limb_moments_and_mean_angles(
            active_athlete_ik_conv_mean, active_athlete_id_conv_mean  # use here means
        )
    )

except Exception as e:
    print("Error in ANGLES & MOMENTS of both limbs; src/imports.py")
    print(e)
