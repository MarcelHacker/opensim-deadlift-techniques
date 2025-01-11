from src.local_functions import *
import pandas as pd
import json

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


# set the current athlete
# /Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_0_increased_force_3/settings.json
with open(dir_name + "/athlete_0_increased_force_3/settings.json") as f:
    athlete_0_parsed = json.load(f)

# set the current athlete
with open(dir_name + "/athlete_1_increased_force_3/settings.json") as f:
    athlete_1_parsed = json.load(f)

################################ CREATING ATHLETES ###########################################
athletes = []  # appending instances to athletes list

print(athlete_0_parsed)
print(athlete_1_parsed)
# file_paths = get_paths_athlete(
#   athlete_1_parsed, athlete_1_parsed["model"]  # from which athlete
# )  # gets array with specific file paths

##################################################################################################
# IK sumo
athlete_0_ik_sumo_emptybar_0 = pd.read_csv(
    athlete_0_parsed["paths"]["ik"]["sumo_emptybar_0"],
    sep="\t",
    skiprows=10,
)
print("ATHLETE 0:", athlete_0_ik_sumo_emptybar_0)
athlete_0_ik_sumo_emptybar_1 = None
athlete_0_ik_sumo_emptybar_2 = None
athlete_0_ik_sumo_emptybar_3 = None
athlete_0_ik_sumo_0 = (
    None  # pd.read_csv(file_paths["ik_sumo_path_0"], sep="\t", skiprows=10)
)
athlete_0_ik_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ik"]["sumo_dl_1"],
    sep="\t",
    skiprows=10,
)
athlete_0_ik_sumo_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ik"]["sumo_dl_2"],
    sep="\t",
    skiprows=10,
)
athlete_0_ik_sumo_3 = None
# IK conv
athlete_0_ik_conv_emptybar_0 = None
athlete_0_ik_conv_emptybar_1 = None
athlete_0_ik_conv_emptybar_2 = None
athlete_0_ik_conv_emptybar_3 = None
athlete_0_ik_conv_0 = None
athlete_0_ik_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ik"]["conv_dl_1"],
    sep="\t",
    skiprows=10,
)
athlete_0_ik_conv_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ik"]["conv_dl_2"],
    sep="\t",
    skiprows=10,
)
athlete_0_ik_conv_3 = None
# ID sumo
athlete_0_id_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["id"]["sumo_dl_1"],
    sep="\t",
    skiprows=6,
)
athlete_0_id_sumo_2 = pd.read_csv(
    athlete_0_parsed["paths"]["id"]["sumo_dl_2"],
    sep="\t",
    skiprows=6,
)
# ID conv
athlete_0_id_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["id"]["conv_dl_1"],
    sep="\t",
    skiprows=6,
)
athlete_0_id_conv_2 = pd.read_csv(
    athlete_0_parsed["paths"]["id"]["conv_dl_2"],
    sep="\t",
    skiprows=6,
)

# SO sumo
athlete_0_muscleForces_sumo_emptybar_0 = pd.read_csv(
    athlete_0_parsed["paths"]["so"]["forces"]["sumo_emptybar_0"],
    sep="\t",
    skiprows=14,
)
athlete_0_muscleForces_sumo_0 = None

athlete_0_muscleForces_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["so"]["forces"]["sumo_dl_1"],
    sep="\t",
    skiprows=14,
)
athlete_0_muscleForces_sumo_2 = pd.read_csv(
    athlete_0_parsed["paths"]["so"]["forces"]["sumo_dl_2"],
    sep="\t",
    skiprows=14,
)
athlete_0_muscleForces_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["so"]["forces"]["conv_dl_1"],
    sep="\t",
    skiprows=14,
)
athlete_0_muscleForces_conv_2 = pd.read_csv(
    athlete_0_parsed["paths"]["so"]["forces"]["conv_dl_2"],
    sep="\t",
    skiprows=14,
)
#################### MOMENT ARMS ################################################################
## SUMO
athlete_0_momentArms_hip_flexion_r_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_l_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_r_sumo_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_2"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_l_sumo_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_2"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_knee_flexion_r_sumo_1 = pd.read_csv(  # renamed the original
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["knee_angle_r"]["sumo_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_ankle_flexion_r_sumo_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["ankle_angle_r"]["sumo_dl_1"],
    sep="\t",
    skiprows=11,
)

## CONVENTIONAL
athlete_0_momentArms_hip_flexion_r_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_l_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_r_conv_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_2"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_hip_flexion_l_conv_2 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_2"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_knee_flexion_r_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["knee_angle_r"]["conv_dl_1"],
    sep="\t",
    skiprows=11,
)
athlete_0_momentArms_ankle_flexion_r_conv_1 = pd.read_csv(
    athlete_0_parsed["paths"]["ma"]["moment_arm"]["ankle_angle_r"]["conv_dl_1"],
    sep="\t",
    skiprows=11,
)
#################### NORMALIZED FIBER LENGTHS ################################################################
# SUMO
athlete_0_normalized_fiber_lengths_sumo_0 = None
athlete_0_normalized_fiber_lengths_sumo_1 = None
athlete_0_normalized_fiber_lengths_sumo_2 = None
##################################################################################################

### time normalise everything to 101 values
# ik
athlete_0_ik_sumo_emptybar_time_normalised_0 = time_normalise_df(
    athlete_0_ik_sumo_emptybar_0
)
athlete_0_ik_sumo_time_normalised_1 = time_normalise_df(athlete_0_ik_sumo_1)
athlete_0_ik_sumo_time_normalised_2 = time_normalise_df(athlete_0_ik_sumo_2)
athlete_0_ik_conv_time_normalised_1 = time_normalise_df(athlete_0_ik_conv_1)
athlete_0_ik_conv_time_normalised_2 = time_normalise_df(athlete_0_ik_conv_2)
# id
athlete_0_id_sumo_time_normalised_1 = time_normalise_df(athlete_0_id_sumo_1)
athlete_0_id_sumo_time_normalised_2 = time_normalise_df(athlete_0_id_sumo_2)
athlete_0_id_conv_time_normalised_1 = time_normalise_df(athlete_0_id_conv_1)
athlete_0_id_conv_time_normalised_2 = time_normalise_df(athlete_0_id_conv_2)
# muscle forces
athlete_0_muscleForces_sumo_time_normalised_0 = (
    None  # time_normalise_df(muscleForces_sumo_0)
)
athlete_0_muscleForces_sumo_time_normalised_1 = time_normalise_df(
    athlete_0_muscleForces_sumo_1
)
athlete_0_muscleForces_sumo_time_normalised_2 = time_normalise_df(
    athlete_0_muscleForces_sumo_2
)
athlete_0_muscleForces_conv_time_normalised_1 = time_normalise_df(
    athlete_0_muscleForces_conv_1
)
athlete_0_muscleForces_conv_time_normalised_2 = time_normalise_df(
    athlete_0_muscleForces_conv_2
)
athlete_0_muscleForces_sumo_emptybar_time_normalised_0 = time_normalise_df(
    athlete_0_muscleForces_sumo_emptybar_0
)
## moment arms
# sumo
athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_r_sumo_1
)
athlete_0_momentArms_hip_flexion_l_sumo_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_l_sumo_1
)
athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_2 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_r_sumo_2
)
athlete_0_momentArms_hip_flexion_l_sumo_time_normalised_2 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_l_sumo_2
)
athlete_0_momentArms_knee_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_knee_flexion_r_sumo_1
)
athlete_0_momentArms_ankle_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_ankle_flexion_r_sumo_1
)
# conv
athlete_0_momentArms_hip_flexion_r_conv_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_r_conv_1
)
athlete_0_momentArms_hip_flexion_l_conv_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_l_conv_1
)
athlete_0_momentArms_hip_flexion_r_conv_time_normalised_2 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_r_conv_2
)
athlete_0_momentArms_hip_flexion_l_conv_time_normalised_2 = time_normalise_df(
    athlete_0_momentArms_hip_flexion_l_conv_2
)
athlete_0_momentArms_knee_flexion_r_conv_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_knee_flexion_r_conv_1
)
athlete_0_momentArms_ankle_flexion_r_conv_time_normalised_1 = time_normalise_df(
    athlete_0_momentArms_ankle_flexion_r_conv_1
)

## normalized fiber lengths
# sumo
athlete_0_normalized_fiber_lengths_sumo_time_normalised_0 = None
athlete_0_normalized_fiber_lengths_sumo_time_normalised_1 = None
athlete_0_normalized_fiber_lengths_sumo_time_normalised_2 = None
##################################################################################################
# MUSCLE FORCES MUSCLE GROUPS, sum of both limbs, single trails
# Hamstrings medial (Semitend and Semimem)
athlete_0_hamstrings_medial_sumo_force_0 = None
athlete_0_hamstrings_medial_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,  # muscle force data
    "Hamstrings medial",  # Hamstrings medial
    "rl",
)
athlete_0_hamstrings_medial_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,  # muscle force data
    "Hamstrings medial",  # Hamstrings medial
    "rl",
)
athlete_0_hamstrings_medial_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Hamstrings medial",
    "rl",
)
athlete_0_hamstrings_medial_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Hamstrings medial",
    "rl",
)
# Hamstrings lateral (biceps long and short heads)
athlete_0_hamstrings_lateral_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,  # muscle force data
    "Hamstrings lateral",  # Hamstrings lateral
    "rl",
)
athlete_0_hamstrings_lateral_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,  # muscle force data
    "Hamstrings lateral",  # Hamstrings lateral
    "rl",
)
athlete_0_hamstrings_lateral_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,  # muscle force data
    "Hamstrings lateral",
    "rl",
)
athlete_0_hamstrings_lateral_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,  # muscle force data
    "Hamstrings lateral",
    "rl",
)

athlete_0_vasti_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Vasti",  # Quadriceps
    "rl",
)
athlete_0_vasti_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Vasti",  # Quadriceps
    "rl",
)
athlete_0_vasti_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Vasti",  # Quadriceps
    "rl",
)
athlete_0_vasti_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Vasti",  # Quadriceps
    "rl",
)

athlete_0_gluteusmax_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
athlete_0_gluteusmax_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
athlete_0_gluteusmax_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
athlete_0_gluteusmax_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
# Gluteus Medius
athlete_0_gluteusmed_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Gluteus medius",
    "rl",
)
athlete_0_gluteusmed_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Gluteus medius",
    "rl",
)
athlete_0_gluteusmed_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Gluteus medius",
    "rl",
)
athlete_0_gluteusmed_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Gluteus medius",
    "rl",
)
# Gluteus Minimus
athlete_0_gluteusmin_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Gluteus minimus",
    "rl",
)
athlete_0_gluteusmin_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Gluteus minimus",
    "rl",
)
athlete_0_gluteusmin_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Gluteus minimus",
    "rl",
)
athlete_0_gluteusmin_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Gluteus minimus",
    "rl",
)

athlete_0_adductors_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Adductors",  # Adductors
    "rl",
)
athlete_0_adductors_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Adductors",  # Adductors
    "rl",
)
athlete_0_adductors_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Adductors",  # Adductors
    "rl",
)
athlete_0_adductors_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Adductors",  # Adductors
    "rl",
)
# Hip flexors
athlete_0_hip_flexors_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Hip flexors",  # Adductors
    "rl",
)
athlete_0_hip_flexors_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Hip flexors",  # Adductors
    "rl",
)
athlete_0_hip_flexors_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Hip flexors",  # Adductors
    "rl",
)
athlete_0_hip_flexors_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Hip flexors",  # Adductors
    "rl",
)

# Triceps Surae
athlete_0_triceps_surae_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,
    "Triceps surae",  # Adductors
    "rl",
)
athlete_0_triceps_surae_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,
    "Triceps surae",  # Adductors
    "rl",
)
athlete_0_triceps_surae_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,
    "Triceps surae",  # Adductors
    "rl",
)
athlete_0_triceps_surae_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,
    "Triceps surae",  # Adductors
    "rl",
)

athlete_0_total_sumo_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_1,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
athlete_0_total_sumo_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_sumo_time_normalised_2,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
athlete_0_total_conv_force_1 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_1,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
athlete_0_total_conv_force_2 = sum_muscle_forces(
    athlete_0_muscleForces_conv_time_normalised_2,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
##################################################################################################
## MEAN VARIABLES, absolute mean values over all trails
# IMPORTANT: only calculate the mean with the time normalised vars
athlete_0_ik_sumo_mean = get_mean_trail_values(
    athlete_0_ik_sumo_time_normalised_1,  # have to be time normalised
    athlete_0_ik_sumo_time_normalised_2,  ##!!! to do change this, when having trail 2 ready
    ## todo add trail 3
)
athlete_0_id_sumo_mean = get_mean_trail_values(
    athlete_0_id_sumo_time_normalised_1,  # have to be time normalised
    athlete_0_id_sumo_time_normalised_2,  ##!!! to do change this, when having trail 2 ready
    ## todo add trail 3
)

athlete_0_ik_conv_mean = get_mean_trail_values(
    athlete_0_ik_conv_time_normalised_1,  # have to be time normalised
    athlete_0_ik_conv_time_normalised_2,
    ## todo add trail 3
)

athlete_0_id_conv_mean = get_mean_trail_values(
    athlete_0_id_conv_time_normalised_1,  # have to be time normalised
    athlete_0_id_conv_time_normalised_2,
    ## todo add trail 3
)

athlete_0_muscle_forces_sumo_mean = get_mean_trail_values(
    athlete_0_muscleForces_sumo_time_normalised_1,  # have to be time normalised
    athlete_0_muscleForces_sumo_time_normalised_2,  # have to be time normalised
    ## todo add trail 3
)

athlete_0_muscle_forces_conv_mean = get_mean_trail_values(
    athlete_0_muscleForces_conv_time_normalised_1,  # have to be time normalised
    athlete_0_muscleForces_conv_time_normalised_2,  # have to be time normalised
    ## todo add trail 3
)
######################## TOTAL MUSCLE FORCES ##############################
#
# get mean of array values get from muscle force sums
athlete_0_total_muscle_forces_sumo_mean = get_mean_array_values(
    athlete_0_total_sumo_force_1,
    athlete_0_total_sumo_force_2,  # todo change this for 3 trails
)
athlete_0_total_muscle_forces_conv_mean = get_mean_array_values(
    athlete_0_total_conv_force_1,
    athlete_0_total_conv_force_2,  # todo change this for 3 trails
)

###########################################################################

athlete_0_hamstrings_medial_sumo_force_mean = get_mean_array_values(
    athlete_0_hamstrings_medial_sumo_force_1,
    athlete_0_hamstrings_medial_sumo_force_2,  # todo change this for 3 trails
)
athlete_0_hamstrings_medial_conv_force_mean = get_mean_array_values(
    athlete_0_hamstrings_medial_conv_force_1,
    athlete_0_hamstrings_medial_conv_force_2,  ## todo add 3 trail
)
athlete_0_hamstrings_lateral_sumo_force_mean = get_mean_array_values(
    athlete_0_hamstrings_lateral_sumo_force_1,
    athlete_0_hamstrings_lateral_sumo_force_2,  # todo change this for 3 trails
)
athlete_0_hamstrings_lateral_conv_force_mean = get_mean_array_values(
    athlete_0_hamstrings_lateral_conv_force_1,
    athlete_0_hamstrings_lateral_conv_force_2,  ## todo add 3 trail
)
athlete_0_vasti_sumo_force_mean = get_mean_array_values(
    athlete_0_vasti_sumo_force_1, athlete_0_vasti_sumo_force_2
)  ## todo add 3 trail
athlete_0_vasti_conv_force_mean = get_mean_array_values(
    athlete_0_vasti_sumo_force_1,  ## todo add 3 trail
    athlete_0_vasti_conv_force_2,
)
athlete_0_gluteusmax_sumo_force_mean = get_mean_array_values(
    athlete_0_gluteusmax_sumo_force_1,
    athlete_0_gluteusmax_sumo_force_2,  # todo add 3 trail
)
athlete_0_gluteusmax_conv_force_mean = get_mean_array_values(
    athlete_0_gluteusmax_conv_force_1,
    athlete_0_gluteusmax_conv_force_2,  ## todo add 3 trail
)
athlete_0_adductors_sumo_force_mean = get_mean_array_values(
    athlete_0_adductors_sumo_force_1, athlete_0_adductors_sumo_force_2
)  # todo add 3 trail
athlete_0_adductors_conv_force_mean = get_mean_array_values(
    athlete_0_adductors_conv_force_1,
    athlete_0_adductors_conv_force_2,  ## todo add 3 trail
)
athlete_0_gluteusmed_sumo_force_mean = get_mean_array_values(
    athlete_0_gluteusmed_sumo_force_1, athlete_0_gluteusmed_sumo_force_2
)  # todo add 3 trail
athlete_0_gluteusmed_conv_force_mean = get_mean_array_values(
    athlete_0_gluteusmed_conv_force_1,
    athlete_0_gluteusmed_conv_force_2,  ## todo add 3 trail
)
athlete_0_triceps_surae_sumo_force_mean = get_mean_array_values(
    athlete_0_triceps_surae_sumo_force_1, athlete_0_triceps_surae_sumo_force_2
)  # todo add 3 trail
athlete_0_triceps_surae_conv_force_mean = get_mean_array_values(
    athlete_0_triceps_surae_conv_force_1,
    athlete_0_triceps_surae_conv_force_2,  ## todo add 3 trail
)
athlete_0_hip_flexors_sumo_force_mean = get_mean_array_values(
    athlete_0_hip_flexors_sumo_force_1, athlete_0_hip_flexors_sumo_force_2
)  # todo add 3 trail
athlete_0_hip_flexors_conv_force_mean = get_mean_array_values(
    athlete_0_hip_flexors_conv_force_1,
    athlete_0_hip_flexors_conv_force_2,  ## todo add 3 trail
)
athlete_0_gluteusmin_sumo_force_mean = get_mean_array_values(
    athlete_0_gluteusmin_sumo_force_1, athlete_0_gluteusmin_sumo_force_2
)  # todo add 3 trail
athlete_0_gluteusmin_conv_force_mean = get_mean_array_values(
    athlete_0_gluteusmin_conv_force_1,
    athlete_0_gluteusmin_conv_force_2,  ## todo add 3 trail
)

##################################################################################################
# ANGLES & MOMENTS of both limbs
## to do use here the mean time normalised trails ik and id, then rename vars to mean
athlete_0_mean_sumo_both_angles_and_moments = sum_both_limb_moments_and_mean_angles(
    athlete_0_ik_sumo_mean, athlete_0_id_sumo_mean  # use here means
)
athlete_0_mean_conv_both_angles_and_moments = sum_both_limb_moments_and_mean_angles(
    athlete_0_ik_conv_mean, athlete_0_id_conv_mean  # use here means
)
