import os
import opensim as osim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import msk_modelling_python as msk
from scipy import signal

current_directory = os.path.dirname(os.path.realpath(__file__))
dir_name = os.path.dirname(os.path.dirname(current_directory))

dir_name = "/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations"  # your dircetory


def get_paths_athlete(athlete, model_name=None):
    # todos include moment arm paths in the emptybar trails, not only in the weighted trails
    # todos recheck moment arms paths, and add moment arms to conv
    if model_name == None:
        print("No model name given, get_paths_athlete")
        return None
    else:
        print("\n model name:", model_name)
        print("\n athlete name:", athlete.name)

        data = {}
        # set athletes model and static trail
        data["osim"] = dir_name + "/" + athlete.name + "/" + model_name + ".osim"
        data["static_c3d"] = dir_name + "/" + athlete.name + "/static.c3d"
        data["static_trc"] = dir_name + "/" + athlete.name + "/static.trc"

        # sumo, emptybar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, emptybar trails
            trail_prefix = "sumo_emptybar_"  # folder prefix
            data["ik_sumo_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_sumo_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_sumo_emptybar_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["id_sumo_emptybar_path_" + str(i)])
            # print("\n", data["id_sumo_emptybar_path_" + str(i)])
            # print("\n", data["muscle_forces_sumo_emptybar_path_" + str(i)])

        # sumo, fullbar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, fullbar trails
            trail_prefix = "sumo_dl_"  # folder prefix
            data["ik_sumo_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_sumo_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto
            data["moment_arms_hip_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_hip_flexion_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_l.sto
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_hip_flexion_l.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_knee_angle_r.sto
            data["moment_arms_knee_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_knee_angle_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_knee_angle_l.sto
            data["moment_arms_knee_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_knee_angle_l.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_ankle_angle_r.sto
            data["moment_arms_ankle_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_ankle_angle_r.sto"
            )
            # e.g. athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_ankle_angle_l.sto
            data["moment_arms_ankle_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_Moment_ankle_angle_l.sto"
            )
            data["muscle_forces_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # moment_arms_hip_flexion_r_sumo_path_X
            data["moment_arms_hip_flexion_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_r.sto"
            )
            # moment_arms_hip_flexion_l_sumo_path_X
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # moment_arms_hip_flexion_l_sumo_path_X
            data["moment_arms_hip_flexion_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_r
            data["moment_arms_knee_angle_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_knee_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_l
            data["moment_arms_knee_angle_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_knee_angle_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_r
            data["moment_arms_ankle_angle_r_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_ankle_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_l
            data["moment_arms_ankle_angle_l_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_ankle_angle_l.sto"
            )

            # athlete_0_scaled_increased_force_3_MuscleAnalysis_NormalizedFiberLength.sto
            data["normalized_fiber_lengths_sumo_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_NormalizedFiberLength.sto"
            )
            # print("\n", data["id_sumo_path_" + str(i)])
            # print("\n", data["id_sumo_path_" + str(i)])
            # print("\n", data["muscle_forces_sumo_path_" + str(i)])

        # conv, emptybar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, emptybar trails
            trail_prefix = "conv_emptybar_"  # folder prefix
            data["ik_conv_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_conv_emptybar_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_conv_emptybar_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # print("\n", data["ik_conv_emptybar_path_" + str(i)])
            # print("\n", data["id_conv_emptybar_path_" + str(i)])
            # print("\n", data["muscle_forces_conv_emptybar_path_" + str(i)])

        # conv, fullbar
        for i in range(4):  # 4 trails per technique and load (weighted and emptybar)
            # ik, id and forces of sumo, fullbar trails
            trail_prefix = "conv_dl_"  # folder prefix
            data["ik_conv_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/ik.mot"
            )
            data["id_conv_path_" + str(i)] = (
                dir_name + "/" + athlete.name + "/" + trail_prefix + str(i) + "/id.sto"
            )
            data["muscle_forces_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_StaticOptimization_force.sto"
            )
            # moment_arms_hip_flexion_r_conv_path_X
            data["moment_arms_hip_flexion_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_r.sto"
            )
            # moment_arms_hip_flexion_l_conv_path_X
            data["moment_arms_hip_flexion_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # moment_arms_hip_flexion_l_conv_path_X
            data["moment_arms_hip_flexion_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_hip_flexion_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_r
            data["moment_arms_knee_angle_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_knee_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_knee_angle_l
            data["moment_arms_knee_angle_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_knee_angle_l.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_r
            data["moment_arms_ankle_angle_r_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_ankle_angle_r.sto"
            )
            # athlete_0_scaled_increased_force_3_MuscleAnalysis_MomentArm_ankle_angle_l
            data["moment_arms_ankle_angle_l_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_MomentArm_ankle_angle_l.sto"
            )
            data["normalized_fiber_lengths_conv_path_" + str(i)] = (
                dir_name
                + "/"
                + athlete.name
                + "/"
                + trail_prefix
                + str(i)
                + "/"
                + model_name
                + "_MuscleAnalysis_NormalizedFiberLength.sto"
            )
            # print("\n", data["ik_conv_path_" + str(i)])
            # print("\n", data["id_conv_path_" + str(i)])
            # print("\n", data["muscle_forces_conv_path_" + str(i)])

        return data


def calculateMuscleMoment(
    muscle_forces_so_file_time_normalised, moment_arms_ma_time_normalised
):
    muscle_moment_in_plane_time_normalised = (
        muscle_forces_so_file_time_normalised * moment_arms_ma_time_normalised
    )
    return muscle_moment_in_plane_time_normalised


def emg_filter(
    df, measurement_frequency=2000, band_lowcut=30, band_highcut=400, lowcut=6, order=4
):
    # analog data rate
    fs = measurement_frequency  # Hz
    if fs < band_highcut * 2:
        band_highcut = fs / 2
        print(
            "High pass frequency was too high. Using 1/2 *  sampling frequnecy instead"
        )

    analog_df = df.copy()

    nyq = 0.5 * fs
    normal_cutoff = lowcut / nyq
    b_low, a_low = signal.butter(order, normal_cutoff, btype="low", analog=False)

    low = band_lowcut / nyq
    high = band_highcut / nyq
    b_band, a_band = signal.butter(order, [low, high], btype="band")

    for col in analog_df.columns:
        if col == "time":
            continue
        raw_emg_signal = analog_df[col]
        bandpass_signal = signal.filtfilt(b_band, a_band, raw_emg_signal)
        detrend_signal = signal.detrend(bandpass_signal, type="linear")
        rectified_signal = np.abs(detrend_signal)
        linear_envelope = signal.filtfilt(b_low, a_low, rectified_signal)
        peak_maximum = np.max(linear_envelope)
        analog_df[col] = linear_envelope / peak_maximum

    return analog_df


def time_normalise_df(df, fs=""):

    if not type(df) == pd.core.frame.DataFrame:
        raise Exception("Input must be a pandas DataFrame")

    if not fs:
        try:
            fs = 1 / (df["time"][1] - df["time"][0])
        except KeyError as e:
            raise Exception('Input DataFrame must contain a column named "time"')

    normalised_df = pd.DataFrame(columns=df.columns)

    for column in df.columns:
        normalised_df[column] = np.zeros(101)

        currentData = df[column]
        currentData = currentData[~np.isnan(currentData)]

        timeTrial = np.arange(0, len(currentData) / fs, 1 / fs)
        Tnorm = np.arange(0, timeTrial[-1], timeTrial[-1] / 101)
        if len(Tnorm) == 102:
            Tnorm = Tnorm[:-1]
        normalised_df[column] = np.interp(Tnorm, timeTrial, currentData)

    return normalised_df


def get_mean_trail_values(
    data_1_time_normalised,
    data_2_time_normalised,
    data_3_time_normalised=None,
):
    """
    calculate the mean value of the given trails
    Input:
    Data Frame of the trail files, columns have to identical!

    Output:
    New data frame with the mean of values
    """
    data = pd.DataFrame()  # make a new dataFrame

    for column in data_1_time_normalised.columns:
        if data_3_time_normalised == None:
            data[column] = (
                data_1_time_normalised[column] + data_2_time_normalised[column]
            ) / 2
        else:
            data[column] = (
                data_1_time_normalised[column]
                + data_2_time_normalised[column]
                + data_3_time_normalised[column]
            ) / 3
    return data


def get_mean_array_values(
    array_1_time_normalised,
    array_2_time_normalised,
    array_3_time_normalised=None,
):
    """
    calculate the mean value of the given values in arrays
    Input:
    Array with values whit the same context!

    Output:
    Mean of the values in the arrays, as a array.
    """
    array = [0] * 101  # buffer
    i = 0
    if array_3_time_normalised == None:
        for value in array_1_time_normalised:
            array[i] = (value + array_2_time_normalised[i]) / 2  # made for 2 trails
            i += 1
    else:
        for value in array_1_time_normalised:
            array[i] = (
                value + array_2_time_normalised[i] + array_3_time_normalised[i]
            ) / 3  # made for 3 trails
            i += 1

    return array


def sum_both_limb_moments_and_mean_angles(
    ik_file_time_normalised, id_file_time_normalised
):
    # data should be the mean of all trails
    # and time normalised
    angles_and_moments = pd.DataFrame(
        {
            "hip_angle": [],
            "knee_angle": [],
            "ankle_angle": [],
            "hip_flexion_moment": [],
            "knee_flexion_moment": [],
            "ankle_flexion_moment": [],
        }
    )
    # angles
    angles_and_moments["hip_angle"] = (
        ik_file_time_normalised["hip_flexion_r"]
        + ik_file_time_normalised["hip_flexion_l"]
    ) / 2  # mean angle values of both limbs
    angles_and_moments["knee_angle"] = (
        ik_file_time_normalised["knee_angle_r"]
        + ik_file_time_normalised["knee_angle_l"]
    ) / 2  # mean angle values of both limbs
    angles_and_moments["ankle_angle"] = (
        ik_file_time_normalised["ankle_angle_r"]
        + ik_file_time_normalised["ankle_angle_l"]
    ) / 2  # mean angle values of both limbs

    # moments
    # now the sum of both limbs with the means
    # maybe for later the moments are for one leg, the sum of the means right and leg is divided by 2.
    angles_and_moments["hip_flexion_moment"] = (
        id_file_time_normalised["hip_flexion_r_moment"]
        + id_file_time_normalised["hip_flexion_l_moment"]
    )
    angles_and_moments["knee_flexion_moment"] = (
        id_file_time_normalised["knee_angle_r_moment"]
        + id_file_time_normalised["knee_angle_l_moment"]
    )
    angles_and_moments["ankle_flexion_moment"] = (
        id_file_time_normalised["ankle_angle_r_moment"]
        + id_file_time_normalised["ankle_angle_l_moment"]
    )

    return angles_and_moments


def sum_muscle_forces(muscleForces, muscle_group="Hamstrings", limbs="rl"):  #
    """sum_muscle_forces
    sum of intrested muscle forces

    Input:
    muscleForces must be time normalised to 101 values, data frame
    muscle_group = String e.g. "Hamstrings", "Quadriceps"
    limbs = "rl"  # rl for right and left, "r" or "l"
    Output:
    Array with the sum of the hole muscle forces
    """
    muscles_of_interest = []

    if limbs == "r" or limbs == "l":
        print("limb configuration not programmed, in sum_muscle_forces")

    if muscle_group == "Hip extensors" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "semimem_r",
            "semiten_r",
            "bflh_l",
            "bfsh_l",
            "semimem_l",
            "semiten_l",
            "glmax1_r",
            "glmax2_r",
            "glmax3_r",
            "glmax1_l",
            "glmax2_l",
            "glmax3_l",
        ]

    if muscle_group == "Knee extensors" and limbs == "rl":
        muscles_of_interest = [
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]

    if muscle_group == "Hamstrings" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "semimem_r",
            "semiten_r",
            "bflh_l",
            "bfsh_l",
            "semimem_l",
            "semiten_l",
        ]
    if muscle_group == "Hamstrings lateral" and limbs == "rl":
        muscles_of_interest = [
            "bflh_r",
            "bfsh_r",
            "bflh_l",
            "bfsh_l",
        ]
    if muscle_group == "Hamstrings medial" and limbs == "rl":
        muscles_of_interest = [
            "semimem_r",
            "semiten_r",
            "semimem_l",
            "semiten_l",
        ]

    if muscle_group == "Hip flexors" and limbs == "rl":  # rec fem added
        muscles_of_interest = [
            "recfem_r",
            "recfem_l",
            "iliacus_r",
            "iliacus_l",
            "psoas_r",
            "psoas_l",
            "tfl_r",
            "tfl_l",
        ]
    if muscle_group == "Vasti" and limbs == "rl":
        muscles_of_interest = [
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]

    if muscle_group == "vastus lateralis" and limbs == "rl":
        muscles_of_interest = [
            "vaslat_r",
            "vaslat_l",
        ]
    if muscle_group == "vastus medialis" and limbs == "rl":
        muscles_of_interest = [
            "vasmed_r",
            "vasmed_l",
        ]
    if muscle_group == "vastus intermedius" and limbs == "rl":
        muscles_of_interest = [
            "vasint_r",
            "vasint_l",
        ]
    if muscle_group == "rectus femoris" and limbs == "rl":
        muscles_of_interest = [
            "recfem_r",
            "recfem_l",
        ]

    if muscle_group == "Quadriceps" and limbs == "rl":
        muscles_of_interest = [
            "recfem_r",
            "recfem_l",
            "vaslat_r",
            "vasmed_r",
            "vasint_r",
            "vaslat_l",
            "vasmed_l",
            "vasint_l",
        ]
    if muscle_group == "Gluteus maximus" and limbs == "rl":
        muscles_of_interest = [
            "glmax1_r",
            "glmax2_r",
            "glmax3_r",
            "glmax1_l",
            "glmax2_l",
            "glmax3_l",
        ]
    if muscle_group == "Gluteus medius" and limbs == "rl":
        muscles_of_interest = [
            "glmed1_r",
            "glmed2_r",
            "glmed3_r",
            "glmed1_l",
            "glmed2_l",
            "glmed3_l",
        ]
    if muscle_group == "Gluteus minimus" and limbs == "rl":
        muscles_of_interest = [
            "glmin1_r",
            "glmin2_r",
            "glmin3_r",
            "glmin1_l",
            "glmin2_l",
            "glmin3_l",
        ]
    if muscle_group == "Triceps surae" and limbs == "rl":
        muscles_of_interest = [
            "gaslat_r",
            "gasmed_r",
            "soleus_r",
            "gaslat_l",
            "gasmed_l",
            "soleus_l",
        ]
    if muscle_group == "Adductors" and limbs == "rl":
        muscles_of_interest = [
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

    if muscle_group == "All" and limbs == "rl":
        muscles_of_interest = [
            "addbrev_r",
            "addbrev_l",
            "addlong_r",
            "addlong_l",
            "addmagDist_r",
            "addmagDist_l",
            "addmagIsch_r",
            "addmagIsch_l",
            "addmagMid_r",
            "addmagMid_l",
            "addmagProx_r",
            "addmagProx_l",
            "bflh_r",
            "bflh_l",
            "bfsh_r",
            "bfsh_l",
            "edl_r",
            "edl_l",
            "ehl_r",
            "ehl_l",
            "fdl_r",
            "fdl_l",
            "fhl_r",
            "fhl_l",
            "gaslat_r",
            "gaslat_l",
            "gasmed_r",
            "gasmed_l",
            "glmax1_r",
            "glmax1_l",
            "glmax2_r",
            "glmax2_l",
            "glmax3_r",
            "glmax3_l",
            "glmed1_r",
            "glmed1_l",
            "glmed2_r",
            "glmed2_l",
            "glmed3_r",
            "glmed3_l",
            "glmin1_r",
            "glmin1_l",
            "glmin2_r",
            "glmin2_l",
            "glmin3_r",
            "glmin3_l",
            "grac_r",
            "grac_l",
            "iliacus_r",
            "iliacus_l",
            "perbrev_r",
            "perbrev_l",
            "perlong_r",
            "perlong_l",
            "piri_r",
            "piri_l",
            "psoas_r",
            "psoas_l",
            "recfem_r",
            "recfem_l",
            "sart_r",
            "sart_l",
            "semimem_r",
            "semimem_l",
            "semiten_r",
            "semiten_l",
            "soleus_r",
            "soleus_l",
            "tfl_r",
            "tfl_l",
            "tibant_r",
            "tibant_l",
            "tibpost_r",
            "tibpost_l",
            "vasint_r",
            "vasint_l",
            "vaslat_r",
            "vaslat_l",
            "vasmed_r",
            "vasmed_l",
        ]
    if muscles_of_interest == []:
        print("no muscle sum choosen, in sum_muscle_forces")

    sum_forces = [0] * 101  # defined arry length

    for i in range(len(muscles_of_interest)):
        index = 0
        for value in muscleForces[muscles_of_interest[i]]:
            sum_forces[index] = sum_forces[index] + value
            index += 1
    return sum_forces


lower_body_muscles = [
    "addbrev_r",
    "addbrev_l",
    "addlong_r",
    "addlong_l",
    "addmagDist_r",
    "addmagDist_l",
    "addmagIsch_r",
    "addmagIsch_l",
    "addmagMid_r",
    "addmagMid_l",
    "addmagProx_r",
    "addmagProx_l",
    "bflh_r",
    "bflh_l",
    "bfsh_r",
    "bfsh_l",
    "edl_r",
    "edl_l",
    "ehl_r",
    "ehl_l",
    "fdl_r",
    "fdl_l",
    "fhl_r",
    "fhl_l",
    "gaslat_r",
    "gaslat_l",
    "gasmed_r",
    "gasmed_l",
    "glmax1_r",
    "glmax1_l",
    "glmax2_r",
    "glmax2_l",
    "glmax3_r",
    "glmax3_l",
    "glmed1_r",
    "glmed1_l",
    "glmed2_r",
    "glmed2_l",
    "glmed3_r",
    "glmed3_l",
    "glmin1_r",
    "glmin1_l",
    "glmin2_r",
    "glmin2_l",
    "glmin3_r",
    "glmin3_l",
    "grac_r",
    "grac_l",
    "iliacus_r",
    "iliacus_l",
    "perbrev_r",
    "perbrev_l",
    "perlong_r",
    "perlong_l",
    "piri_r",
    "piri_l",
    "psoas_r",
    "psoas_l",
    "recfem_r",
    "recfem_l",
    "sart_r",
    "sart_l",
    "semimem_r",
    "semimem_l",
    "semiten_r",
    "semiten_l",
    "soleus_r",
    "soleus_l",
    "tfl_r",
    "tfl_l",
    "tibant_r",
    "tibant_l",
    "tibpost_r",
    "tibpost_l",
    "vasint_r",
    "vasint_l",
    "vaslat_r",
    "vaslat_l",
    "vasmed_r",
    "vasmed_l",
]


def normalize_Force(muscle_forces, athlete_folder_path):
    """
    Normalize muscle force on maximum isometric force.

    Parameter:
    muscle_forces: time normalized data frame with muscle forces

    Return:
    Time normalized and normalized muscle forces of all lower body muscles
    """
    model_path = athlete_folder_path + "/scaled_model.osim"
    normalized_forces = muscle_forces.copy()

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in lower_body_muscles:
        target = model.getMuscles().get(muscle)
        current_max_force = target.getMaxIsometricForce()
        # time normalized muscle forces
        normalized_forces[lower_body_muscles] = (
            muscle_forces[lower_body_muscles] / current_max_force
        )
    return normalized_forces


def plot_data(
    axs,
    data_1,
    label_data_1,
    color_data_1,
    data_2,
    label_data_2,
    color_data_2,
    legend,
    y_label,
    x_label,
):
    plt.sca(axs)
    plt.plot(
        data_1,
        label=label_data_1,
        color=color_data_1,
    )
    plt.plot(
        data_2,
        label=label_data_2,
        color=color_data_2,
    )
    if legend:
        plt.legend()
    plt.ylabel(y_label)
    plt.xlabel(x_label)


def create_overall_csv(file_name, array_time_normalized, athlete):
    trial_postfix = "no_athlete_selected"
    if athlete == "athlete_0":
        trial_postfix = "A0"
    elif athlete == "athlete_1":
        trial_postfix = "A1"
    elif athlete == "athlete_2":
        trial_postfix = "A2"
    elif athlete == "athlete_3":
        trial_postfix = "A3"

    print(file_name)
    print(array_time_normalized)
    print(athlete)
    df = pd.DataFrame({})
    try:
        stored_csv = pd.read_csv(
            "/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/muscle_forces/"
            + file_name,
            sep="\t",
            skiprows=0,
        )
        print("STORED:", stored_csv.columns)
        print(type(stored_csv))
        df = stored_csv.copy()
    except Exception as e:
        print(f"Error reading: {e}")

    df["Trial1_" + str(trial_postfix)] = array_time_normalized[0]
    df["Trial2_" + str(trial_postfix)] = array_time_normalized[1]
    df["Trial3_" + str(trial_postfix)] = array_time_normalized[2]
    df["Trial4_" + str(trial_postfix)] = array_time_normalized[3]

    df.to_csv(
        "/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/muscle_forces/"
        + file_name,
        sep="\t",
        encoding="utf-8",
        index=False,
    )


def calculate_joint_centres_modified(
    trc_filepath, new_filepath=None
):  # modified from lib
    """
    Calculates hip joint centers in a TRC file according to Harrington et al.

    Args:
        trc_filepath (str): Path to the TRC file.
        new_filepath (str, optional): Path to save the modified TRC file. Defaults to None.

    Returns:
        dict: Dictionary containing the modified TRC data.
    """
    trc = pd.read_csv(trc_filepath, sep="\t", skiprows=3)
    print("TRC: ", trc)
    print("TRC: ", trc["Time"][1])  # time [0] is NaN in this trc file
    print("TRC: ", trc["Time"][2])

    # Load TRC data
    # with open(trc_filepath, "r") as f:
    # ... (Implementation for loading TRC data using your preferred library)
    #   trc = ...

    # Set default output filepath
    if new_filepath is None:
        new_filepath = trc_filepath.replace(".trc", "_HJC.trc")

    # Sample rate (assuming data is evenly sampled)
    rate = round(1 / (trc["Time"][2] - trc["Time"][1]))  # time[0] is NaN in trc file

    # Add HJC using Harrington equations
    trc = add_hjc_harrington(trc)

    # Add knee and ankle joint centers (assuming markers exist)
    trc["RKJC"] = (trc["RKNE"] + trc["RKNM"]) / 2
    trc["LKJC"] = (trc["LKNE"] + trc["LKNM"]) / 2
    trc["RAJC"] = (trc["RANK"] + trc["RANM"]) / 2
    trc["LAJC"] = (trc["LANK"] + trc["LANM"]) / 2

    # Convert markers to separate data and labels (assuming specific format)
    markers_data = np.array([v for k, v in trc.items() if k != "Time"])
    marker_labels = list(trc.keys())[1:]

    # Save modified TRC data
    try:
        # ... (Implementation for saving TRC data using your preferred library)
        msk.write_trc_os4(markers_data, marker_labels, rate, new_filepath)
    except Exception as e:
        print(f"Error saving TRC file: {e}")
        # Handle potential issues (e.g., missing markers)

    return trc


def add_hjc_harrington(trc):
    """
    Calculates hip joint centers (HJC) using Harrington et al. (2006) formulas.

    Args:
        trc (dict): Dictionary containing TRC data.

    Returns:
        dict: Modified TRC data with added HJC markers.
    """

    lasis = trc["LASI"].T
    rasis = trc["RASI"].T

    # Handle missing SACRUM marker
    try:
        sacrum = trc["USACR"].T  # USACR markers exist in this model
    except KeyError:
        sacrum = (trc["LPSI"] + trc["RPSI"]) / 2
        trc["USACR"] = sacrum.T

    num_frames = len(rasis)
    hjc_left, hjc_right = np.empty((3, num_frames)), np.empty((3, num_frames))

    for i in range(num_frames):
        # Right-handed pelvis reference system definition
        pelvis_center = (lasis[:, i] + rasis[:, i]) / 2
        provv = (rasis[:, i] - sacrum[:, i]) / np.linalg.norm(
            rasis[:, i] - sacrum[:, i]
        )
        ib = (rasis[:, i] - lasis[:, i]) / np.linalg.norm(rasis[:, i] - lasis[:, i])
        kb = np.cross(ib, provv)
        kb /= np.linalg.norm(kb)
        jb = np.cross(kb, ib)
        jb /= np.linalg.norm(jb)

    pelvis_transform = np.array(
        [ib[0], jb[0], kb[0], pelvis_center[0]],
        [ib[1], jb[1], kb[1], pelvis_center[1], ib[2], jb[1]],
    )
