from local_functions import *
import pandas as pd


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
        "athlete_0_increased_force_3",
        "57",
        "athlete_0_scaled_increased_force_3",
        "conventional",
    ),
)
athletes.append(
    athlete(
        "athlete_1",
        "87",
        "athlete_1_scaled",
        "sumo",
    ),
)
file_paths = get_paths_athlete(athletes[0], athletes[0].model)

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
ik_sumo_0 = None
ik_sumo_1 = pd.read_csv(file_paths["ik_sumo_path_1"], sep="\t", skiprows=10)
ik_sumo_2 = None
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
id_conv_2 = pd.read_csv(file_paths["id_conv_path_2"], sep="\t", skiprows=6)

# ID conv
# SO sumo
muscleForces_sumo_emptybar_0 = pd.read_csv(
    file_paths["muscle_forces_sumo_emptybar_path_0"], sep="\t", skiprows=14
)
muscleForces_sumo_1 = pd.read_csv(
    file_paths["muscle_forces_sumo_path_1"], sep="\t", skiprows=14
)
muscleForces_conv_1 = pd.read_csv(
    file_paths["muscle_forces_conv_path_1"], sep="\t", skiprows=14
)
muscleForces_conv_2 = pd.read_csv(
    file_paths["muscle_forces_conv_path_2"], sep="\t", skiprows=14
)

# SO conv
## to do fix moment arms
# print("\n PATH: ", file_paths["moment_arms_hip_flexion_r_sumo_path_1"])
# athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
# athlete_0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
# momentArms_sumo = pd.read_csv(
#   file_paths["moment_arms_hip_flexion_r_sumo_path_1"], sep="\t", skiprows=0
# )
# print("\n momentArms sumo: ", momentArms_sumo.columns)

### time normalise everything to 101 values
ik_sumo_time_normalised_1 = time_normalise_df(ik_sumo_1)
ik_conv_time_normalised_1 = time_normalise_df(ik_conv_1)
ik_conv_time_normalised_2 = time_normalise_df(ik_conv_2)
id_sumo_time_nomalised_1 = time_normalise_df(id_sumo_1)
id_conv_time_normalised_2 = time_normalise_df(id_conv_2)
ik_sumo_emptybar_time_normalised_0 = time_normalise_df(ik_sumo_emptybar_0)
muscleForces_sumo_time_normalised_1 = time_normalise_df(muscleForces_sumo_1)
muscleForces_conv_time_normalised_1 = time_normalise_df(muscleForces_conv_1)
muscleForces_conv_time_normalised_2 = time_normalise_df(muscleForces_conv_2)
muscleForces_sumo_emptybar_time_normalised_0 = time_normalise_df(
    muscleForces_sumo_emptybar_0
)
##################################################################################################
