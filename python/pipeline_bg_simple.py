"""
Code to run OpenSim analysis Marcel's data BSc
"""

from msk_modelling_python import *
import msk_modelling_python as msk

file = r"C:\Git\research_data\Projects\opensim-deadlift-techniques\simulations\athlete_1_increased_force_3\conv_dl_0\c3dfile\analog_filtered.csv"
df = msk.bops.import_file(file)

print(df.head())

df_time_normalised = msk.bops.time_normalise_df(df)
new_file = file.replace(".csv", "_time_normalised.csv")
df_time_normalised.to_csv(new_file)

exit()
run_setup = True
run_scale_model = False
run_increase_isom_force = False
run_ik = False
run_id = False
run_so = False

current_dir = os.path.dirname(__file__)
athlete_name = "athlete_1_increased_force_3"
athlete_path = os.path.join(os.path.dirname(current_dir), "simulations", athlete_name)
osim_model_path = os.path.join(athlete_path, "scaled_model.osim")

if not os.path.exists(osim_model_path):
    raise Exception("Model file not found: " + osim_model_path)

static_trc_file_path = None
max_isometric_force_scale_factor = 1

# motion files
trial_name = "conv_dl_0"
c3d_file_path = os.path.join(athlete_path, trial_name, "c3dfile.c3d")
motion_trc_file_path = os.path.join(athlete_path, trial_name, "ik.mot")
grf_mot_file_path = None
grf_xml_file_path = None
actuators_so_file_path = None

if motion_trc_file_path is not None:
    trial_path = os.path.dirname(motion_trc_file_path)
    ik_results_path = os.path.join(trial_path, "ik.mot")
    id_results_path = os.path.join(trial_path, "id.sto")

    error_log_path = os.path.join(trial_path, "error_log.txt")


# setup (to finish)
if run_setup:
    try:
        msk.bops.c3d_osim_export(c3d_file_path)
        file_name_no_ext = c3d_file_path.split("\\")[-1].replace(".c3d", "")
        grf_file = c3d_file_path.replace(
            ".c3d", "\\forces\\" + file_name_no_ext + "\\grf.mot"
        )
        msk.bops.create_grf_xml(
            grf_file,
            output_file="",
            apply_force_body_name="calcn_r",
            force_expressed_in_body_name="ground",
        )
        msk.log_error("Completed setup: c3d export", error_log_path)
    except Exception as e:
        print("Error in setup")
        print(e)
        msk.log_error("Error in setup: " + str(e), error_log_path)

# Scale model
if run_scale_model:
    try:
        msk.bops.scale_model(osim_model_path, static_trc_file_path)
        msk.log_error("Completed scaling model: " + str(e), error_log_path)
    except Exception as e:
        print("Error in scaling model")
        print(e)
        msk.log_error("Error in scaling model: " + str(e), error_log_path)

# change Max isometric force
if run_increase_isom_force:
    try:
        osimSetup = msk.classes.osimSetup()
        osimSetup.increase_max_isometric_force(
            osim_model_path, increase_factor=max_isometric_force_scale_factor
        )
        msk.log_error(
            "Completed changing Max isometric force: " + str(e), error_log_path
        )
    except Exception as e:
        print("Error in changing Max isometric force")
        print(e)
        msk.log_error(
            "Error in changing Max isometric force: " + str(e), error_log_path
        )

# Inverse kinematics
if run_ik:
    try:
        msk.bops.run_IK(osim_model_path, motion_trc_file_path, trial_path)
        msk.log_error("Completed inverse kinematics: " + str(e), error_log_path)
    except Exception as e:
        print("Error in inverse kinematics")
        print(e)
        msk.log_error("Error in inverse kinematics: " + str(e))

# Inverse dynamics
if run_id:
    try:
        msk.bops.run_ID(
            osim_model_path,
            ik_results_path,
            grf_mot_file_path,
            grf_xml_file_path,
            trial_path,
        )
        msk.log_error("Completed inverse dynamics: " + str(e), error_log_path)
    except Exception as e:
        print("Error in inverse dynamics")
        print(e)
        msk.log_error("Error in inverse dynamics: " + str(e))

# Static optimization
if run_so:
    try:
        msk.bops.run_SO(osim_model_path, trial_path, actuators_so_file_path)
        msk.log_error("Completed static optimization: " + str(e), error_log_path)
    except Exception as e:
        print("Error in static optimization")
        print(e)
        msk.log_error("Error in static optimization: " + str(e))
