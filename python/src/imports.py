from src.local_functions import *
import pandas as pd

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


################################ CREATING ATHLETES ###########################################
athletes = []  # appending instances to athletes list
athletes.append(
    athlete(
        "athlete_0_increased_force_3",  #  folder name
        57.0,  # just for normalising
        "athlete_0_scaled_increased_force_3",  # model name in folder
        "sumo",  # preferred technique
    ),
)
athletes.append(
    athlete(
        "athlete_1",
        87.3,
        "athlete_1_scaled",
        "sumo",
    ),
)
file_paths = get_paths_athlete(
    athletes[0], athletes[0].model  # from which athlete
)  # gets array with specific file paths

##################################################################################################
# IK sumo
ik_sumo_emptybar_0 = pd.read_csv(
    file_paths["ik_sumo_emptybar_path_0"],
    sep="\t",
    skiprows=10,
)
ik_sumo_emptybar_1 = None
ik_sumo_emptybar_2 = None
ik_sumo_emptybar_3 = None
ik_sumo_0 = None  # pd.read_csv(file_paths["ik_sumo_path_0"], sep="\t", skiprows=10)
ik_sumo_1 = pd.read_csv(file_paths["ik_sumo_path_1"], sep="\t", skiprows=10)
ik_sumo_2 = pd.read_csv(file_paths["ik_sumo_path_2"], sep="\t", skiprows=10)
ik_sumo_3 = None
# IK conv
ik_conv_emptybar_0 = None
ik_conv_emptybar_1 = None
ik_conv_emptybar_2 = None
ik_conv_emptybar_3 = None
ik_conv_0 = None
ik_conv_1 = pd.read_csv(file_paths["ik_conv_path_1"], sep="\t", skiprows=10)
ik_conv_2 = pd.read_csv(file_paths["ik_conv_path_2"], sep="\t", skiprows=10)
ik_conv_3 = None
# ID sumo
id_sumo_1 = pd.read_csv(file_paths["id_sumo_path_1"], sep="\t", skiprows=6)
id_sumo_2 = pd.read_csv(file_paths["id_sumo_path_2"], sep="\t", skiprows=6)
# ID conv
id_conv_1 = pd.read_csv(file_paths["id_conv_path_1"], sep="\t", skiprows=6)
id_conv_2 = pd.read_csv(file_paths["id_conv_path_2"], sep="\t", skiprows=6)

# SO sumo
muscleForces_sumo_emptybar_0 = pd.read_csv(
    file_paths["muscle_forces_sumo_emptybar_path_0"], sep="\t", skiprows=14
)
muscleForces_sumo_0 = None

muscleForces_sumo_1 = pd.read_csv(
    file_paths["muscle_forces_sumo_path_1"], sep="\t", skiprows=14
)
muscleForces_sumo_2 = pd.read_csv(
    file_paths["muscle_forces_sumo_path_2"], sep="\t", skiprows=14
)
muscleForces_conv_1 = pd.read_csv(
    file_paths["muscle_forces_conv_path_1"], sep="\t", skiprows=14
)
muscleForces_conv_2 = pd.read_csv(
    file_paths["muscle_forces_conv_path_2"], sep="\t", skiprows=14
)

#################### MOMENT ARMS ################################################################
## SUMO
momentArms_hip_flexion_r_sumo_1 = pd.read_csv(
    file_paths["moment_arms_hip_flexion_r_sumo_path_1"], sep="\t", skiprows=11
)
momentArms_knee_flexion_r_sumo_1 = pd.read_csv(  # renamed the original
    file_paths["moment_arms_knee_angle_r_sumo_path_1"], sep="\t", skiprows=11
)
momentArms_ankle_flexion_r_sumo_1 = pd.read_csv(
    file_paths["moment_arms_ankle_angle_r_sumo_path_1"], sep="\t", skiprows=11
)

## CONVENTIONAL
momentArms_hip_flexion_r_conv_1 = pd.read_csv(
    file_paths["moment_arms_hip_flexion_r_conv_path_1"], sep="\t", skiprows=11
)
momentArms_knee_flexion_r_conv_1 = pd.read_csv(  # renamed the original
    file_paths["moment_arms_knee_angle_r_conv_path_1"], sep="\t", skiprows=11
)
momentArms_ankle_flexion_r_conv_1 = pd.read_csv(
    file_paths["moment_arms_ankle_angle_r_conv_path_1"], sep="\t", skiprows=11
)

#################### NORMALIZED FIBER LENGTHS ################################################################
# SUMO
normalized_fiber_lengths_sumo_0 = None
normalized_fiber_lengths_sumo_1 = pd.read_csv(
    file_paths["normalized_fiber_lengths_sumo_path_1"], sep="\t", skiprows=11
)
normalized_fiber_lengths_sumo_2 = pd.read_csv(
    file_paths["normalized_fiber_lengths_sumo_path_2"], sep="\t", skiprows=11
)

print(normalized_fiber_lengths_sumo_1)
print(normalized_fiber_lengths_sumo_2)


##################################################################################################

### time normalise everything to 101 values
# ik
ik_sumo_emptybar_time_normalised_0 = time_normalise_df(ik_sumo_emptybar_0)
ik_sumo_time_normalised_1 = time_normalise_df(ik_sumo_1)
ik_sumo_time_normalised_2 = time_normalise_df(ik_sumo_2)
ik_conv_time_normalised_1 = time_normalise_df(ik_conv_1)
ik_conv_time_normalised_2 = time_normalise_df(ik_conv_2)
# id
id_sumo_time_nomalised_1 = time_normalise_df(id_sumo_1)
id_sumo_time_nomalised_2 = time_normalise_df(id_sumo_2)
id_conv_time_normalised_1 = time_normalise_df(id_conv_1)
id_conv_time_normalised_2 = time_normalise_df(id_conv_2)
# muscle forces
muscleForces_sumo_time_normalised_0 = None  # time_normalise_df(muscleForces_sumo_0)
muscleForces_sumo_time_normalised_1 = time_normalise_df(muscleForces_sumo_1)
muscleForces_sumo_time_normalised_2 = time_normalise_df(muscleForces_sumo_2)
muscleForces_conv_time_normalised_1 = time_normalise_df(muscleForces_conv_1)
muscleForces_conv_time_normalised_2 = time_normalise_df(muscleForces_conv_2)
muscleForces_sumo_emptybar_time_normalised_0 = time_normalise_df(
    muscleForces_sumo_emptybar_0
)
## moment arms
# sumo
momentArms_hip_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    momentArms_hip_flexion_r_sumo_1
)
momentArms_knee_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    momentArms_knee_flexion_r_sumo_1
)
momentArms_ankle_flexion_r_sumo_time_normalised_1 = time_normalise_df(
    momentArms_ankle_flexion_r_sumo_1
)
# conv
momentArms_hip_flexion_r_conv_time_normalised_1 = time_normalise_df(
    momentArms_hip_flexion_r_conv_1
)
momentArms_knee_flexion_r_conv_time_normalised_1 = time_normalise_df(
    momentArms_knee_flexion_r_conv_1
)
momentArms_ankle_flexion_r_conv_time_normalised_1 = time_normalise_df(
    momentArms_ankle_flexion_r_conv_1
)

## normalized fiber lengths
# sumo
normalized_fiber_lengths_sumo_time_normalised_0 = None
normalized_fiber_lengths_sumo_time_normalised_1 = time_normalise_df(
    normalized_fiber_lengths_sumo_1
)
normalized_fiber_lengths_sumo_time_normalised_2 = time_normalise_df(
    normalized_fiber_lengths_sumo_2
)
##################################################################################################
# MUSCLE FORCES MUSCLE GROUPS, sum of both limbs, single trails
# Hamstrings medial (Semitend and Semimem)
hamstrings_medial_sumo_force_0 = None
hamstrings_medial_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,  # muscle force data
    "Hamstrings medial",  # Hamstrings medial
    "rl",
)
hamstrings_medial_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,  # muscle force data
    "Hamstrings medial",  # Hamstrings medial
    "rl",
)
hamstrings_medial_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Hamstrings medial",
    "rl",
)
hamstrings_medial_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Hamstrings medial",
    "rl",
)
# Hamstrings lateral (biceps long and short heads)
hamstrings_lateral_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,  # muscle force data
    "Hamstrings lateral",  # Hamstrings lateral
    "rl",
)
hamstrings_lateral_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,  # muscle force data
    "Hamstrings lateral",  # Hamstrings lateral
    "rl",
)
hamstrings_lateral_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,  # muscle force data
    "Hamstrings lateral",
    "rl",
)
hamstrings_lateral_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,  # muscle force data
    "Hamstrings lateral",
    "rl",
)

vasti_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Vasti",  # Quadriceps
    "rl",
)
vasti_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Vasti",  # Quadriceps
    "rl",
)
vasti_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Vasti",  # Quadriceps
    "rl",
)
vasti_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Vasti",  # Quadriceps
    "rl",
)

gluteusmax_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
gluteusmax_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
gluteusmax_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
gluteusmax_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Gluteus maximus",  # Gluteus Maximus
    "rl",
)
# Gluteus Medius
gluteusmed_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Gluteus medius",
    "rl",
)
gluteusmed_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Gluteus medius",
    "rl",
)
gluteusmed_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Gluteus medius",
    "rl",
)
gluteusmed_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Gluteus medius",
    "rl",
)
# Gluteus Minimus
gluteusmin_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Gluteus minimus",
    "rl",
)
gluteusmin_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Gluteus minimus",
    "rl",
)
gluteusmin_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Gluteus minimus",
    "rl",
)
gluteusmin_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Gluteus minimus",
    "rl",
)

adductors_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Adductors",  # Adductors
    "rl",
)
adductors_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Adductors",  # Adductors
    "rl",
)
adductors_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Adductors",  # Adductors
    "rl",
)
adductors_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Adductors",  # Adductors
    "rl",
)
# Hip flexors
hip_flexors_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Hip flexors",  # Adductors
    "rl",
)
hip_flexors_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Hip flexors",  # Adductors
    "rl",
)
hip_flexors_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Hip flexors",  # Adductors
    "rl",
)
hip_flexors_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Hip flexors",  # Adductors
    "rl",
)

# Triceps Surae
triceps_surae_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,
    "Triceps surae",  # Adductors
    "rl",
)
triceps_surae_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,
    "Triceps surae",  # Adductors
    "rl",
)
triceps_surae_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,
    "Triceps surae",  # Adductors
    "rl",
)
triceps_surae_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,
    "Triceps surae",  # Adductors
    "rl",
)

total_sumo_force_1 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_1,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
total_sumo_force_2 = sum_muscle_forces(
    muscleForces_sumo_time_normalised_2,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
total_conv_force_1 = sum_muscle_forces(
    muscleForces_conv_time_normalised_1,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
total_conv_force_2 = sum_muscle_forces(
    muscleForces_conv_time_normalised_2,  # muscle force data
    "All",  # All muscle groups
    "rl",
)
##################################################################################################
## MEAN VARIABLES, absolute mean values over all trails
# IMPORTANT: only calculate the mean with the time normalised vars
ik_sumo_mean = get_mean_trail_values(
    ik_sumo_time_normalised_1,  # have to be time normalised
    ik_sumo_time_normalised_2,  ##!!! to do change this, when having trail 2 ready
    ## todo add trail 3
)
id_sumo_mean = get_mean_trail_values(
    id_sumo_time_nomalised_1,  # have to be time normalised
    id_sumo_time_nomalised_2,  ##!!! to do change this, when having trail 2 ready
    ## todo add trail 3
)

ik_conv_mean = get_mean_trail_values(
    ik_conv_time_normalised_1,  # have to be time normalised
    ik_conv_time_normalised_2,
    ## todo add trail 3
)

id_conv_mean = get_mean_trail_values(
    id_conv_time_normalised_1,  # have to be time normalised
    id_conv_time_normalised_2,
    ## todo add trail 3
)

muscle_forces_sumo_mean = get_mean_trail_values(
    muscleForces_sumo_time_normalised_1,  # have to be time normalised
    muscleForces_sumo_time_normalised_2,  # have to be time normalised
    ## todo add trail 3
)

muscle_forces_conv_mean = get_mean_trail_values(
    muscleForces_conv_time_normalised_1,  # have to be time normalised
    muscleForces_conv_time_normalised_2,  # have to be time normalised
    ## todo add trail 3
)
######################## TOTAL MUSCLE FORCES ##############################
#
print("\n SUMO1:", total_sumo_force_1[0])
print("\n SUMO2:", total_sumo_force_2[0])
print("\n CONV1:", total_conv_force_1[0])
print("\n CONV2:", total_conv_force_2[0])
# get mean of array values get from muscle force sums
total_muscle_forces_sumo_mean = get_mean_array_values(
    total_sumo_force_1, total_sumo_force_2  # todo change this for 3 trails
)
total_muscle_forces_conv_mean = get_mean_array_values(
    total_conv_force_1, total_conv_force_2  # todo change this for 3 trails
)

###########################################################################

hamstrings_medial_sumo_force_mean = get_mean_array_values(
    hamstrings_medial_sumo_force_1,
    hamstrings_medial_sumo_force_2,  # todo change this for 3 trails
)
hamstrings_medial_conv_force_mean = get_mean_array_values(
    hamstrings_medial_conv_force_1, hamstrings_medial_conv_force_2  ## todo add 3 trail
)
hamstrings_lateral_sumo_force_mean = get_mean_array_values(
    hamstrings_lateral_sumo_force_1,
    hamstrings_lateral_sumo_force_2,  # todo change this for 3 trails
)
hamstrings_lateral_conv_force_mean = get_mean_array_values(
    hamstrings_lateral_conv_force_1,
    hamstrings_lateral_conv_force_2,  ## todo add 3 trail
)
vasti_sumo_force_mean = get_mean_array_values(
    vasti_sumo_force_1, vasti_sumo_force_2
)  ## todo add 3 trail
vasti_conv_force_mean = get_mean_array_values(
    vasti_sumo_force_1,  ## todo add 3 trail
    vasti_conv_force_2,
)
gluteusmax_sumo_force_mean = get_mean_array_values(
    gluteusmax_sumo_force_1, gluteusmax_sumo_force_2  # todo add 3 trail
)
gluteusmax_conv_force_mean = get_mean_array_values(
    gluteusmax_conv_force_1, gluteusmax_conv_force_2  ## todo add 3 trail
)
adductors_sumo_force_mean = get_mean_array_values(
    adductors_sumo_force_1, adductors_sumo_force_2
)  # todo add 3 trail
adductors_conv_force_mean = get_mean_array_values(
    adductors_conv_force_1, adductors_conv_force_2  ## todo add 3 trail
)
gluteusmed_sumo_force_mean = get_mean_array_values(
    gluteusmed_sumo_force_1, gluteusmed_sumo_force_2
)  # todo add 3 trail
gluteusmed_conv_force_mean = get_mean_array_values(
    gluteusmed_conv_force_1, gluteusmed_conv_force_2  ## todo add 3 trail
)
triceps_surae_sumo_force_mean = get_mean_array_values(
    triceps_surae_sumo_force_1, triceps_surae_sumo_force_2
)  # todo add 3 trail
triceps_surae_conv_force_mean = get_mean_array_values(
    triceps_surae_conv_force_1, triceps_surae_conv_force_2  ## todo add 3 trail
)
hip_flexors_sumo_force_mean = get_mean_array_values(
    hip_flexors_sumo_force_1, hip_flexors_sumo_force_2
)  # todo add 3 trail
hip_flexors_conv_force_mean = get_mean_array_values(
    hip_flexors_conv_force_1, hip_flexors_conv_force_2  ## todo add 3 trail
)
gluteusmin_sumo_force_mean = get_mean_array_values(
    gluteusmin_sumo_force_1, gluteusmin_sumo_force_2
)  # todo add 3 trail
gluteusmin_conv_force_mean = get_mean_array_values(
    gluteusmin_conv_force_1, gluteusmin_conv_force_2  ## todo add 3 trail
)

##################################################################################################
# ANGLES & MOMENTS of both limbs
## to do use here the mean time normalised trails ik and id, then rename vars to mean
mean_sumo_both_angles_and_moments = sum_both_limb_moments_and_mean_angles(
    ik_sumo_mean, id_sumo_mean  # use here means
)
mean_conv_both_angles_and_moments = sum_both_limb_moments_and_mean_angles(
    ik_conv_mean, id_conv_mean  # use here means
)
