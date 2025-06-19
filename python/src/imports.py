from src.modules import *
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


################################ CLASSES ###########################################
class Athlete:
    def __init__(
        self,
        name,
        age,
        gender,
        height,
        body_weight,
        technique,
        load,
        fmax,
        athlete_folder_path,
    ):
        # informations
        self.name = name  # "athlete_x", used for reading files
        self.age = age
        self.gender = gender
        self.height = height
        self.body_weight = body_weight  # "57"
        self.technique = technique  # "sumo" or "conventional", preffered deadlift
        self.load = load  # 275
        self.fmax = fmax  # 300
        self.athlete_folder_path = athlete_folder_path  # /Users/marcelhacker/Documents

    def create_athlete_json(self, athlete_folder_path):

        # warning not completed
        msk.ui.show_warning("Warning", "This function is not completed yet")

        athlete_dict = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "technique": self.technique,
            "load": self.load,
            "fmax": self.fmax,
            "paths": {
                "main": self.athlete_folder_path,
                "model_generic": "",
                "model_scaled": self.athlete_folder_path + "scaled_model.osim",
                "static": self.athlete_folder_path + "static_00.trc",
                "ik": {
                    "sumo_dl_0": self.athlete_folder_path + "/sumo_dl_0/ik.mot",
                    "sumo_dl_1": self.athlete_folder_path + "/sumo_dl_1/ik.mot",
                    "sumo_dl_2": self.athlete_folder_path + "/sumo_dl_2/ik.mot",
                    "sumo_dl_3": self.athlete_folder_path + "/sumo_dl_3/ik.mot",
                    "conv_dl_0": self.athlete_folder_path + "/conv_dl_0/ik.mot",
                    "conv_dl_1": self.athlete_folder_path + "/conv_dl_1/ik.mot",
                    "conv_dl_2": self.athlete_folder_path + "/conv_dl_2/ik.mot",
                    "conv_dl_3": self.athlete_folder_path + "/conv_dl_3/ik.mot",
                },
                "id": {
                    "sumo_dl_0": self.athlete_folder_path + "/sumo_dl_0/id.sto",
                    "sumo_dl_1": self.athlete_folder_path + "/sumo_dl_1/id.sto",
                    "sumo_dl_2": self.athlete_folder_path + "/sumo_dl_2/id.sto",
                    "sumo_dl_3": self.athlete_folder_path + "/sumo_dl_3/id.sto",
                    "conv_dl_0": self.athlete_folder_path + "/conv_dl_0/id.sto",
                    "conv_dl_1": self.athlete_folder_path + "/conv_dl_1/id.sto",
                    "conv_dl_2": self.athlete_folder_path + "/conv_dl_2/id.sto",
                    "conv_dl_3": self.athlete_folder_path + "/conv_dl_3/id.sto",
                },
                "so": {
                    "activations": {
                        "sumo_dl_0": self.athlete_folder_path
                        + "/sumo_dl_0/_StaticOptimization_activation.sto",
                        "sumo_dl_1": self.athlete_folder_path
                        + "/sumo_dl_1/_StaticOptimization_activation.sto",
                        "sumo_dl_2": self.athlete_folder_path
                        + "/sumo_dl_2/_StaticOptimization_activation.sto",
                        "sumo_dl_3": self.athlete_folder_path
                        + "/sumo_dl_3/_StaticOptimization_activation.sto",
                        "conv_dl_0": self.athlete_folder_path
                        + "/conv_dl_0/_StaticOptimization_activation.sto",
                        "conv_dl_1": self.athlete_folder_path
                        + "/conv_dl_1/_StaticOptimization_activation.sto",
                        "conv_dl_2": self.athlete_folder_path
                        + "/conv_dl_2/_StaticOptimization_activation.sto",
                        "conv_dl_3": self.athlete_folder_path
                        + "/conv_dl_3/_StaticOptimization_activation.sto",
                    },
                    "forces": {
                        "sumo_dl_0": self.athlete_folder_path
                        + "/sumo_dl_0/_StaticOptimization_force.sto",
                        "sumo_dl_1": self.athlete_folder_path
                        + "/sumo_dl_1/_StaticOptimization_force.sto",
                        "sumo_dl_2": self.athlete_folder_path
                        + "/sumo_dl_2/_StaticOptimization_force.sto",
                        "sumo_dl_3": self.athlete_folder_path
                        + "/sumo_dl_3/_StaticOptimization_force.sto",
                        "conv_dl_0": self.athlete_folder_path
                        + "/conv_dl_0/_StaticOptimization_force.sto",
                        "conv_dl_1": self.athlete_folder_path
                        + "/conv_dl_1/_StaticOptimization_force.sto",
                        "conv_dl_2": self.athlete_folder_path
                        + "/conv_dl_2/_StaticOptimization_force.sto",
                        "conv_dl_3": self.athlete_folder_path
                        + "/conv_dl_3/_StaticOptimization_force.sto",
                    },
                },
                "ma": {
                    "normalized_fiber_length": {},
                    "moment_arm": {
                        "hip_flexion_r": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_hip_flexion_r.sto",
                        },
                        "hip_flexion_l": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_hip_flexion_l.sto",
                        },
                        "knee_angle_r": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_knee_angle_r.sto",
                        },
                        "knee_angle_l": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_knee_angle_l.sto",
                        },
                        "ankle_angle_r": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_ankle_angle_r.sto",
                        },
                        "ankle_angle_l": {
                            "sumo_dl_0": self.athlete_folder_path
                            + "/sumo_dl_0/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "sumo_dl_1": self.athlete_folder_path
                            + "/sumo_dl_1/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "sumo_dl_2": self.athlete_folder_path
                            + "/sumo_dl_2/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "sumo_dl_3": self.athlete_folder_path
                            + "/sumo_dl_3/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "conv_dl_0": self.athlete_folder_path
                            + "/conv_dl_0/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "conv_dl_1": self.athlete_folder_path
                            + "/conv_dl_1/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "conv_dl_2": self.athlete_folder_path
                            + "/conv_dl_2/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                            "conv_dl_3": self.athlete_folder_path
                            + "/conv_dl_3/_MuscleAnalysis_MomentArm_ankle_angle_l.sto",
                        },
                    },
                },
            },
        }

        # save json file in the athlete folder
        with open(athlete_folder_path + "/settings.json", "w") as f:
            json.dump(athlete_dict, f)

        return athlete_dict


# set this name for the active folder
active_athlete_foldername = "athlete_0_increased_force_10"

################################ CREATING ATHLETE ###########################################
active_athlete = None  # define active_athlete
##################################################################################################

################################ GETTING ATHLETE JSON ###########################################
try:
    # fix this
    dirname = os.path.dirname(__file__)  # not used
    with open(dir_name + "/" + str(active_athlete_foldername) + "/settings.json") as f:
        active_athlete = json.load(f)
        print("\nACTIVE ATHLETE:\n", active_athlete["name"])
except Exception as e:
    print("\nError in getting active athlete json; src/imports.py\n")
    print(e)

##################################################################################################
# IK sumo
try:
    active_athlete_bodymass = active_athlete["bodymass"]
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
    active_athlete_ik_sumo_3 = pd.read_csv(
        active_athlete["paths"]["ik"]["sumo_dl_3"],
        sep="\t",
        skiprows=10,
    )
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
    active_athlete_ik_conv_3 = pd.read_csv(
        active_athlete["paths"]["ik"]["conv_dl_3"],
        sep="\t",
        skiprows=10,
    )

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
    active_athlete_id_sumo_3 = pd.read_csv(
        active_athlete["paths"]["id"]["sumo_dl_3"],
        sep="\t",
        skiprows=6,
    )
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
    active_athlete_id_conv_3 = pd.read_csv(
        active_athlete["paths"]["id"]["conv_dl_3"],
        sep="\t",
        skiprows=6,
    )
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
    active_athlete_muscleForces_sumo_3 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["sumo_dl_3"],
        sep="\t",
        skiprows=14,
    )
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
    active_athlete_muscleForces_conv_3 = pd.read_csv(
        active_athlete["paths"]["so"]["forces"]["conv_dl_3"],
        sep="\t",
        skiprows=14,
    )
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
    active_athlete_momentArms_hip_flexion_r_sumo_3 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["sumo_dl_3"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_sumo_3 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["sumo_dl_3"],
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
    active_athlete_momentArms_hip_flexion_r_conv_3 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_r"]["conv_dl_3"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_hip_flexion_l_conv_3 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["hip_flexion_l"]["conv_dl_3"],
        sep="\t",
        skiprows=11,
    )
    active_athlete_momentArms_knee_flexion_r_conv_0 = pd.read_csv(
        active_athlete["paths"]["ma"]["moment_arm"]["knee_angle_r"]["conv_dl_0"],
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
        skiprows=8,
    )
except Exception as e:
    print("Error in muscle activations files; src/imports.py")
    print(e)
    
##################################################################################################
# RRA sumo
try:
    active_athlete_rra_sumo_0 = pd.read_csv(
        active_athlete["paths"]["rra"]["sumo_dl_0"],
        sep="\t",
        skiprows=11, # fix this
    )
    active_athlete_rra_sumo_1 = pd.read_csv(
        active_athlete["paths"]["rra"]["sumo_dl_1"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_rra_sumo_2 = pd.read_csv(
        active_athlete["paths"]["rra"]["sumo_dl_2"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_rra_sumo_3 = pd.read_csv(
        active_athlete["paths"]["rra"]["sumo_dl_3"],
        sep="\t",
        skiprows=6,
    )
    # RRA conv
    active_athlete_rra_conv_0 = pd.read_csv(
        active_athlete["paths"]["rra"]["conv_dl_0"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_rra_conv_1 = pd.read_csv(
        active_athlete["paths"]["rra"]["conv_dl_1"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_rra_conv_2 = pd.read_csv(
        active_athlete["paths"]["rra"]["conv_dl_2"],
        sep="\t",
        skiprows=6,
    )
    active_athlete_rra_conv_3 = pd.read_csv(
        active_athlete["paths"]["rra"]["conv_dl_3"],
        sep="\t",
        skiprows=6,
    )
    
    ## normalise
    active_athlete_rra_conv_time_normalised_0 = (
        time_normalise_df(active_athlete_rra_conv_0)
    )
    active_athlete_rra_conv_time_normalised_1 = (
        time_normalise_df(active_athlete_rra_conv_1)
    )
    active_athlete_rra_conv_time_normalised_2 = (
        time_normalise_df(active_athlete_rra_conv_2)
    )
    active_athlete_rra_conv_time_normalised_3 = (
        time_normalise_df(active_athlete_rra_conv_3)
    )
    # sumo
    active_athlete_rra_sumo_time_normalised_0 = (
        time_normalise_df(active_athlete_rra_sumo_0)
    ) 
    active_athlete_rra_sumo_time_normalised_1 = (
        time_normalise_df(active_athlete_rra_sumo_1)
    )
    active_athlete_rra_sumo_time_normalised_2 = (
        time_normalise_df(active_athlete_rra_sumo_2)
    )
    active_athlete_rra_sumo_time_normalised_3 = (
        time_normalise_df(active_athlete_rra_sumo_3)
    )

except Exception as e:
    print("Error in RRA files; src/imports.py")
    print(e)
##################################################################################################
try:
    # active_athlete_emg_channels_order = active_athlete["paths"]["emg"]["channels_order"]
    # active_athlete_activations_emg_conv_0 = pd.read_csv(
    #   active_athlete["paths"]["emg"]["conv_dl_0"],
    #  sep=",",
    # skiprows=0,
    # )
    print("no emg data")
    # print("\nACTIVATIONS EMG conv 0:\n", active_athlete_activations_emg_conv_0)
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
    active_athlete_ik_sumo_time_normalised_3 = time_normalise_df(
        active_athlete_ik_sumo_3
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
    active_athlete_ik_conv_time_normalised_3 = time_normalise_df(
        active_athlete_ik_conv_3
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
    active_athlete_id_sumo_time_normalised_3 = time_normalise_df(
        active_athlete_id_sumo_3
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
    active_athlete_id_conv_time_normalised_3 = time_normalise_df(
        active_athlete_id_conv_3
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
    active_athlete_muscleForces_sumo_time_normalised_3 = time_normalise_df(
        active_athlete_muscleForces_sumo_3
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
    active_athlete_muscleForces_conv_time_normalised_3 = time_normalise_df(
        active_athlete_muscleForces_conv_3
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
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_3 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_sumo_3
    )
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_3 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_sumo_3
    )
    active_athlete_momentArms_knee_flexion_r_sumo_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_knee_flexion_r_sumo_0
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
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_3 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_r_conv_3
    )
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_3 = time_normalise_df(
        active_athlete_momentArms_hip_flexion_l_conv_3
    )
    active_athlete_momentArms_knee_flexion_r_conv_time_normalised_0 = time_normalise_df(
        active_athlete_momentArms_knee_flexion_r_conv_0
    )
    active_athlete_momentArms_knee_flexion_r_conv_time_normalised_1 = time_normalise_df(
        active_athlete_momentArms_knee_flexion_r_conv_1
    )
    active_athlete_momentArms_ankle_flexion_r_conv_time_normalised_1 = (
        time_normalise_df(active_athlete_momentArms_ankle_flexion_r_conv_1)
    )

    active_athlete_activations_conv_time_normalised_0 = time_normalise_df(
        active_athlete_activations_conv_0
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

    # active_athlete_activations_emg_conv_time_normalised_0 = time_normalise_df(
    #   active_athlete_activations_emg_conv_0
    # )
    print("no emg normalisation")
except Exception as e:
    print("Error in time normalisation emg activations files; src/imports.py")
    print(e)
##################################################################################################
# MUSCLE FORCES MUSCLE GROUPS, sum of both limbs, single trials
try:
    active_athlete_hip_extensors_sumo_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_sumo_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_sumo_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_sumo_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_sumo_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_sumo_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_sumo_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_sumo_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_conv_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_conv_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_conv_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_conv_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_conv_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_conv_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip extensors",
        "l",
    )
    active_athlete_hip_extensors_conv_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip extensors",
        "r",
    )
    active_athlete_hip_extensors_conv_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip extensors",
        "l",
    )
    ###############################
    active_athlete_hip_flexors_sumo_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_sumo_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_sumo_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_sumo_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_sumo_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_sumo_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_sumo_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_sumo_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_conv_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_conv_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_conv_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_conv_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_conv_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_conv_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip flexors",
        "l",
    )
    active_athlete_hip_flexors_conv_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip flexors",
        "r",
    )
    active_athlete_hip_flexors_conv_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip flexors",
        "l",
    )
    ###############################
    active_athlete_hip_adductors_sumo_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_sumo_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_sumo_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_sumo_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_sumo_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_sumo_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_sumo_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_sumo_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_conv_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_conv_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_conv_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_conv_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_conv_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_conv_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Hip adductors",
        "l",
    )
    active_athlete_hip_adductors_conv_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip adductors",
        "r",
    )
    active_athlete_hip_adductors_conv_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip adductors",
        "l",
    )
    ###############################
    active_athlete_knee_extensors_sumo_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_sumo_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_sumo_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_sumo_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,  # muscle force data
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_sumo_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_sumo_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,  # muscle force data
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_sumo_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_sumo_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_conv_r_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_conv_l_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_conv_r_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_conv_l_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_conv_r_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_conv_l_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Knee extensors",
        "l",
    )
    active_athlete_knee_extensors_conv_r_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Knee extensors",
        "r",
    )
    active_athlete_knee_extensors_conv_l_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Knee extensors",
        "l",
    )
    ###############################
    active_athlete_knee_extensors_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "Knee extensors",
        "rl",
    )
    active_athlete_knee_extensors_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Knee extensors",
        "rl",
    )
    #####################################################################
    # Hamstrings medial (Semitend and Semimem)
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
    active_athlete_hamstrings_medial_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
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
    active_athlete_hamstrings_medial_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hamstrings medial",
        "rl",
    )
    # Hamstrings lateral (biceps long and short heads)
    active_athlete_hamstrings_lateral_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "Hamstrings lateral",  # Hamstrings lateral
        "rl",
    )
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
    active_athlete_hamstrings_lateral_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "Hamstrings lateral",  # Hamstrings lateral
        "rl",
    )
    active_athlete_hamstrings_lateral_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,  # muscle force data
        "Hamstrings lateral",
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
    active_athlete_hamstrings_lateral_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,  # muscle force data
        "Hamstrings lateral",
        "rl",
    )
    active_athlete_vasti_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Vasti",  # Quadriceps
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
    active_athlete_vasti_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Vasti",  # Quadriceps
        "rl",
    )
    active_athlete_vasti_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_vasti_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Vasti",  # Quadriceps
        "rl",
    )
    active_athlete_vastus_lateralis_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_lateralis_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "vastus lateralis",
        "rl",
    )
    active_athlete_vastus_medialis_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_medialis_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "vastus medialis",
        "rl",
    )
    active_athlete_vastus_intermedius_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "vastus intermedius",
        "rl",
    )
    active_athlete_vastus_intermedius_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "vastus intermedius",
        "rl",
    )
    active_athlete_rectus_femoris_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_sumo_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_1,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_sumo_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_2,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_conv_force_1 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_1,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_conv_force_2 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_2,
        "rectus femoris",
        "rl",
    )
    active_athlete_rectus_femoris_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "rectus femoris",
        "rl",
    )

    active_athlete_gluteusmax_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Gluteus maximus",  # Gluteus Maximus
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
    active_athlete_gluteusmax_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    active_athlete_gluteusmax_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_gluteusmax_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Gluteus maximus",  # Gluteus Maximus
        "rl",
    )
    # Gluteus Medius
    active_athlete_gluteusmed_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Gluteus medius",
        "rl",
    )
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
    active_athlete_gluteusmed_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Gluteus medius",
        "rl",
    )
    active_athlete_gluteusmed_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_gluteusmed_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Gluteus medius",
        "rl",
    )
    # Gluteus Minimus
    active_athlete_gluteusmin_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Gluteus minimus",
        "rl",
    )
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
    active_athlete_gluteusmin_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Gluteus minimus",
        "rl",
    )
    active_athlete_gluteusmin_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_gluteusmin_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Gluteus minimus",
        "rl",
    )
    active_athlete_adductors_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Adductors",  # Adductors
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
    active_athlete_adductors_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Adductors",  # Adductors
        "rl",
    )
    active_athlete_adductors_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_adductors_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Adductors",  # Adductors
        "rl",
    )
    # Hip flexors
    active_athlete_hip_flexors_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Hip flexors",  # Adductors
        "rl",
    )
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
    active_athlete_hip_flexors_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Hip flexors",  # Adductors
        "rl",
    )
    active_athlete_hip_flexors_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_hip_flexors_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Hip flexors",  # Adductors
        "rl",
    )

    # Triceps Surae
    active_athlete_triceps_surae_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,
        "Triceps surae",  # Adductors
        "rl",
    )
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
    active_athlete_triceps_surae_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,
        "Triceps surae",  # Adductors
        "rl",
    )
    active_athlete_triceps_surae_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,
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
    active_athlete_triceps_surae_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,
        "Triceps surae",  # Adductors
        "rl",
    )

    active_athlete_total_sumo_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_0,  # muscle force data
        "All",  # All muscle groups
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
    active_athlete_total_sumo_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_sumo_time_normalised_3,  # muscle force data
        "All",  # All muscle groups
        "rl",
    )
    active_athlete_total_conv_force_0 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_0,  # muscle force data
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
    active_athlete_total_conv_force_3 = sum_muscle_forces(
        active_athlete_muscleForces_conv_time_normalised_3,  # muscle force data
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
        active_athlete_hamstrings_medial_sumo_force_0,
        active_athlete_hamstrings_medial_sumo_force_1,
        active_athlete_hamstrings_medial_sumo_force_2,  # todo change this for 4 trails
    )
    active_athlete_hamstrings_medial_conv_force_mean = get_mean_array_values(
        active_athlete_hamstrings_medial_conv_force_0,
        active_athlete_hamstrings_medial_conv_force_1,
        active_athlete_hamstrings_medial_conv_force_2,  ## todo add 4 trail
    )
    active_athlete_hamstrings_lateral_sumo_force_mean = get_mean_array_values(
        active_athlete_hamstrings_lateral_sumo_force_0,
        active_athlete_hamstrings_lateral_sumo_force_1,
        active_athlete_hamstrings_lateral_sumo_force_2,  # todo change this for 4 trails
    )
    active_athlete_hamstrings_lateral_conv_force_mean = get_mean_array_values(
        active_athlete_hamstrings_lateral_conv_force_0,
        active_athlete_hamstrings_lateral_conv_force_1,
        active_athlete_hamstrings_lateral_conv_force_2,  ## todo add 4 trail
    )
    active_athlete_vasti_sumo_force_mean = get_mean_array_values(
        active_athlete_vasti_sumo_force_0,
        active_athlete_vasti_sumo_force_1,
        active_athlete_vasti_sumo_force_2,
    )  ## todo add 4 trail
    active_athlete_vasti_conv_force_mean = get_mean_array_values(
        active_athlete_vasti_conv_force_0,
        active_athlete_vasti_conv_force_1,  ## todo add 4 trail
        active_athlete_vasti_conv_force_2,
    )
    active_athlete_gluteusmax_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmax_sumo_force_0,
        active_athlete_gluteusmax_sumo_force_1,
        active_athlete_gluteusmax_sumo_force_2,  # todo add 3 trail
    )
    active_athlete_gluteusmax_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmax_conv_force_0,
        active_athlete_gluteusmax_conv_force_1,
        active_athlete_gluteusmax_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_adductors_sumo_force_mean = get_mean_array_values(
        active_athlete_adductors_sumo_force_0,
        active_athlete_adductors_sumo_force_1,
        active_athlete_adductors_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_adductors_conv_force_mean = get_mean_array_values(
        active_athlete_adductors_conv_force_0,
        active_athlete_adductors_conv_force_1,
        active_athlete_adductors_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_gluteusmed_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmed_sumo_force_0,
        active_athlete_gluteusmed_sumo_force_1,
        active_athlete_gluteusmed_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_gluteusmed_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmed_conv_force_0,
        active_athlete_gluteusmed_conv_force_1,
        active_athlete_gluteusmed_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_triceps_surae_sumo_force_mean = get_mean_array_values(
        active_athlete_triceps_surae_sumo_force_0,
        active_athlete_triceps_surae_sumo_force_1,
        active_athlete_triceps_surae_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_triceps_surae_conv_force_mean = get_mean_array_values(
        active_athlete_triceps_surae_conv_force_0,
        active_athlete_triceps_surae_conv_force_1,
        active_athlete_triceps_surae_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_hip_flexors_sumo_force_mean = get_mean_array_values(
        active_athlete_hip_flexors_sumo_force_0,
        active_athlete_hip_flexors_sumo_force_1,
        active_athlete_hip_flexors_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_hip_flexors_conv_force_mean = get_mean_array_values(
        active_athlete_hip_flexors_conv_force_0,
        active_athlete_hip_flexors_conv_force_1,
        active_athlete_hip_flexors_conv_force_2,  ## todo add 3 trail
    )
    active_athlete_gluteusmin_sumo_force_mean = get_mean_array_values(
        active_athlete_gluteusmin_sumo_force_0,
        active_athlete_gluteusmin_sumo_force_1,
        active_athlete_gluteusmin_sumo_force_2,
    )  # todo add 3 trail
    active_athlete_gluteusmin_conv_force_mean = get_mean_array_values(
        active_athlete_gluteusmin_conv_force_0,
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


try:
    hip_flexion_r_muscle_moments_sumo_time_normalised_0 = calculateMuscleMoment(
        active_athlete_muscleForces_sumo_time_normalised_0,
        active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0,
    )

    hip_flexion_r_muscle_moments_conv_time_normalised_0 = calculateMuscleMoment(
        active_athlete_muscleForces_conv_time_normalised_0,
        active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0,
    )

    knee_flexion_r_muscle_moments_sumo_time_normalised_0 = calculateMuscleMoment(
        active_athlete_muscleForces_sumo_time_normalised_0,
        active_athlete_momentArms_knee_flexion_r_sumo_time_normalised_0,
    )

    knee_flexion_r_muscle_moments_conv_time_normalised_0 = calculateMuscleMoment(
        active_athlete_muscleForces_conv_time_normalised_0,
        active_athlete_momentArms_knee_flexion_r_conv_time_normalised_0,
    )

except Exception as e:
    print("Error in muscle moments; src/imports.py")
    print(e)
