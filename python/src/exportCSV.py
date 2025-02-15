from src.imports import *


def create_muscle_force_csv(
    array_sumo_time_normalized_r,
    array_sumo_time_normalized_l,
    array_conv_time_normalized_r,
    array_conv_time_normalized_l,
    muscle_group,
):
    create_overall_csv(
        ("sumo/" + str(muscle_group) + "_r.csv"),
        array_sumo_time_normalized_r,
        active_athlete["name"],
    )
    create_overall_csv(
        ("sumo/" + str(muscle_group) + "_l.csv"),
        array_sumo_time_normalized_l,
        active_athlete["name"],
    )
    create_overall_csv(
        ("conv/" + str(muscle_group) + "_r.csv"),
        array_conv_time_normalized_r,
        active_athlete["name"],
    )
    create_overall_csv(
        ("conv/" + str(muscle_group) + "_l.csv"),
        array_conv_time_normalized_l,
        active_athlete["name"],
    )


def create_peak_muscle_force_csv(
    array_sumo_peak_time_normalized_r,
    array_sumo_peak_time_normalized_l,
    array_conv_peak_time_normalized_r,
    array_conv_peak_time_normalized_l,
    muscle_group,
):

    create_peak_forces_csv(
        (
            "preferred/" + str(muscle_group) + ".csv"
            if active_athlete["technique"] == "sumo"
            else "non-preferred/" + str(muscle_group) + ".csv"
        ),
        array_sumo_peak_time_normalized_r,
        array_sumo_peak_time_normalized_l,
        active_athlete["name"],
    )
    create_peak_forces_csv(
        (
            "preferred/" + str(muscle_group) + ".csv"
            if active_athlete["technique"] == "conv"
            else "non-preferred/" + str(muscle_group) + ".csv"
        ),
        array_conv_peak_time_normalized_r,
        array_conv_peak_time_normalized_l,
        active_athlete["name"],
    )


def createForceArray(technique, limb, muscle_group):
    array = [
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_0"),
            active_athlete["bodymass"],
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_1"),
            active_athlete["bodymass"],
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_2"),
            active_athlete["bodymass"],
        ),
        normalize_forces(
            eval(f"active_athlete_{muscle_group}_{technique}_{limb}_force_3"),
            active_athlete["bodymass"],
        ),
    ]
    array = np.array(array)
    return array


def export_csv(bool):
    if bool:
        try:
            #  hip extensors
            hip_extensors_sumo_r = createForceArray("sumo", "r", "hip_extensors")
            hip_extensors_sumo_l = createForceArray("sumo", "l", "hip_extensors")
            hip_extensors_conv_r = createForceArray("conv", "r", "hip_extensors")
            hip_extensors_conv_l = createForceArray("conv", "l", "hip_extensors")

            # flexors
            hip_flexors_sumo_r = createForceArray("sumo", "r", "hip_flexors")
            hip_flexors_sumo_l = createForceArray("sumo", "l", "hip_flexors")
            hip_flexors_conv_r = createForceArray("conv", "r", "hip_flexors")
            hip_flexors_conv_l = createForceArray("conv", "l", "hip_flexors")

            # adductors
            hip_adductors_sumo_r = createForceArray("sumo", "r", "hip_adductors")
            hip_adductors_sumo_l = createForceArray("sumo", "l", "hip_adductors")
            hip_adductors_conv_r = createForceArray("conv", "r", "hip_adductors")
            hip_adductors_conv_l = createForceArray("conv", "l", "hip_adductors")

            # knee extensors
            knee_extensors_sumo_r = createForceArray("sumo", "r", "knee_extensors")
            knee_extensors_sumo_l = createForceArray("sumo", "l", "knee_extensors")
            knee_extensors_conv_r = createForceArray("conv", "r", "knee_extensors")
            knee_extensors_conv_l = createForceArray("conv", "l", "knee_extensors")

            create_muscle_force_csv(
                hip_extensors_sumo_r,
                hip_extensors_conv_l,
                hip_extensors_conv_r,
                hip_extensors_conv_l,
                "hip_extensors",
            )
            create_muscle_force_csv(
                hip_flexors_sumo_r,
                hip_flexors_sumo_l,
                hip_flexors_conv_r,
                hip_flexors_conv_l,
                "hip_flexors",
            )
            create_muscle_force_csv(
                hip_adductors_sumo_r,
                hip_adductors_sumo_l,
                hip_adductors_conv_r,
                hip_adductors_conv_l,
                "hip_adductors",
            )
            create_muscle_force_csv(
                knee_extensors_sumo_r,
                knee_extensors_sumo_l,
                knee_extensors_conv_r,
                knee_extensors_conv_l,
                "knee_extensors",
            )
            ############### PEAK FORCES ######################
            hip_extensors_sumo_r_peaks = [
                np.max(hip_extensors_sumo_r[0]),
                np.max(hip_extensors_sumo_r[1]),
                np.max(hip_extensors_sumo_r[2]),
                np.max(hip_extensors_sumo_r[3]),
            ]
            print(hip_extensors_sumo_r_peaks)
            hip_extensors_sumo_l_peaks = [
                np.max(hip_extensors_sumo_l[0]),
                np.max(hip_extensors_sumo_l[1]),
                np.max(hip_extensors_sumo_l[2]),
                np.max(hip_extensors_sumo_l[3]),
            ]
            hip_extensors_conv_r_peaks = [
                np.max(hip_extensors_conv_r[0]),
                np.max(hip_extensors_conv_r[1]),
                np.max(hip_extensors_conv_r[2]),
                np.max(hip_extensors_conv_r[3]),
            ]
            hip_extensors_conv_l_peaks = [
                np.max(hip_extensors_conv_l[0]),
                np.max(hip_extensors_conv_l[1]),
                np.max(hip_extensors_conv_l[2]),
                np.max(hip_extensors_conv_l[3]),
            ]
            create_peak_muscle_force_csv(
                hip_extensors_sumo_r_peaks,
                hip_extensors_sumo_l_peaks,
                hip_extensors_conv_r_peaks,
                hip_extensors_conv_l_peaks,
                "hip_extensors",
            )
            hip_flexors_sumo_r_peaks = [
                np.max(hip_flexors_sumo_r[0]),
                np.max(hip_flexors_sumo_r[1]),
                np.max(hip_flexors_sumo_r[2]),
                np.max(hip_flexors_sumo_r[3]),
            ]
            hip_flexors_sumo_l_peaks = [
                np.max(hip_flexors_sumo_l[0]),
                np.max(hip_flexors_sumo_l[1]),
                np.max(hip_flexors_sumo_l[2]),
                np.max(hip_flexors_sumo_l[3]),
            ]
            hip_flexors_conv_r_peaks = [
                np.max(hip_flexors_conv_r[0]),
                np.max(hip_flexors_conv_r[1]),
                np.max(hip_flexors_conv_r[2]),
                np.max(hip_flexors_conv_r[3]),
            ]
            hip_flexors_conv_l_peaks = [
                np.max(hip_flexors_conv_l[0]),
                np.max(hip_flexors_conv_l[1]),
                np.max(hip_flexors_conv_l[2]),
                np.max(hip_flexors_conv_l[3]),
            ]
            create_peak_muscle_force_csv(
                hip_flexors_sumo_r_peaks,
                hip_flexors_sumo_l_peaks,
                hip_flexors_conv_r_peaks,
                hip_flexors_conv_l_peaks,
                "hip_flexors",
            )
            hip_adductors_sumo_r_peaks = [
                np.max(hip_adductors_sumo_r[0]),
                np.max(hip_adductors_sumo_r[1]),
                np.max(hip_adductors_sumo_r[2]),
                np.max(hip_adductors_sumo_r[3]),
            ]
            print(hip_adductors_sumo_r_peaks)
            hip_adductors_sumo_l_peaks = [
                np.max(hip_adductors_sumo_l[0]),
                np.max(hip_adductors_sumo_l[1]),
                np.max(hip_adductors_sumo_l[2]),
                np.max(hip_adductors_sumo_l[3]),
            ]
            hip_adductors_conv_r_peaks = [
                np.max(hip_adductors_conv_r[0]),
                np.max(hip_adductors_conv_r[1]),
                np.max(hip_adductors_conv_r[2]),
                np.max(hip_adductors_conv_r[3]),
            ]
            hip_adductors_conv_l_peaks = [
                np.max(hip_adductors_conv_l[0]),
                np.max(hip_adductors_conv_l[1]),
                np.max(hip_adductors_conv_l[2]),
                np.max(hip_adductors_conv_l[3]),
            ]
            create_peak_muscle_force_csv(
                hip_adductors_sumo_r_peaks,
                hip_adductors_sumo_l_peaks,
                hip_adductors_conv_r_peaks,
                hip_adductors_conv_l_peaks,
                "hip_adductors",
            )
            knee_extensors_sumo_r_peaks = [
                np.max(knee_extensors_sumo_r[0]),
                np.max(knee_extensors_sumo_r[1]),
                np.max(knee_extensors_sumo_r[2]),
                np.max(knee_extensors_sumo_r[3]),
            ]
            print(knee_extensors_sumo_r_peaks)
            knee_extensors_sumo_l_peaks = [
                np.max(knee_extensors_sumo_l[0]),
                np.max(knee_extensors_sumo_l[1]),
                np.max(knee_extensors_sumo_l[2]),
                np.max(knee_extensors_sumo_l[3]),
            ]
            knee_extensors_conv_r_peaks = [
                np.max(knee_extensors_conv_r[0]),
                np.max(knee_extensors_conv_r[1]),
                np.max(knee_extensors_conv_r[2]),
                np.max(knee_extensors_conv_r[3]),
            ]
            knee_extensors_conv_l_peaks = [
                np.max(knee_extensors_conv_l[0]),
                np.max(knee_extensors_conv_l[1]),
                np.max(knee_extensors_conv_l[2]),
                np.max(knee_extensors_conv_l[3]),
            ]
            create_peak_muscle_force_csv(
                knee_extensors_sumo_r_peaks,
                knee_extensors_sumo_l_peaks,
                knee_extensors_conv_r_peaks,
                knee_extensors_conv_l_peaks,
                "knee_extensors",
            )
            #################################################
        except Exception as e:
            print("Error in export csv")
            print(e)
