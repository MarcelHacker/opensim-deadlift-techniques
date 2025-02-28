"""
Code to run OpenSim analysis Marcel's data BSc
"""

from msk_modelling_python import *
import msk_modelling_python as msk


# setup (to finish)
def setup():
    try:
        c3d_path = r"C:\Git\research_documents\students\marcel_BSc_vienna\data\pilot01\sumo_dl_80kg01_try_bg.c3d"
        msk.bops.c3d_osim_export(c3d_path)
        file_name_no_ext = c3d_path.split("\\")[-1].replace(".c3d", "")
        grf_file = c3d_path.replace(
            ".c3d", "\\forces\\" + file_name_no_ext + "\\grf.mot"
        )
        msk.bops.create_grf_xml(
            grf_file,
            output_file="",
            apply_force_body_name="calcn_r",
            force_expressed_in_body_name="ground",
        )
    except Exception as e:
        print("Error in setup")
        print(e)
        msk.log_error("Error in Marcel analysis setup: " + str(e))


# Scale model
def scale_model(osim_model_path, trial_path):
    try:
        trial = msk.bops.Trial(trial_path)
        msk.bops.scale_model(osim_model_path, trial.markers)
    except Exception as e:
        print("Error in scaling model")
        print(e)
        msk.log_error("Error in Marcel analysis scaling model: " + str(e))


# change Max isometric force
def increase_isom_force(osim_model_path, increase_factor=1):
    try:
        print(osim_model_path)
        print(increase_factor)
        osimSetup = msk.classes.osimSetup()
        osimSetup.increase_max_isometric_force(osim_model_path, increase_factor)
    except Exception as e:
        print("Error in changing Max isometric force")
        print(e)
        msk.log_error(
            "Error in Marcel analysis changing Max isometric force: " + str(e)
        )


# Inverse kinematics
def run_ik(osim_model_path, trial_path):
    try:
        trial = msk.bops.Trial(trial_path)
        msk.bops.run_IK(osim_model_path, trial.markers, trial.ik)
    except Exception as e:
        print("Error in inverse kinematics")
        print(e)
        msk.log_error("Error in Marcel analysis inverse kinematics: " + str(e))


# Inverse dynamics
def run_id(osim_model_path, trial_path):
    try:
        trial = msk.bops.Trial(trial_path)
        msk.bops.run_ID(osim_model_path, trial.markers, trial.ik, trial.id)
    except Exception as e:
        print("Error in inverse dynamics")
        print(e)
        msk.log_error("Error in Marcel analysis inverse dynamics: " + str(e))


# Static optimization
def run_so(osim_model_path, trial_path):
    try:
        trial = msk.bops.Trial(trial_path)
        msk.bops.run_SO(
            osim_model_path, trial.markers, trial.ik, trial.id, trial.so_force
        )
    except Exception as e:
        print("Error in static optimization")
        print(e)
        msk.log_error("Error in Marcel analysis static optimization: " + str(e))


if __name__ == "__main__":
    trial_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_2_increased_force_55/conv_dl_0/"
    model_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_2_increased_force_55/scaled_model.osim"
    # trial = msk.bops.Trial(trial_path)

    # if not trial.check_files():
    #     msk.log_error('Error in Marcel analysis files not found in ' + trial_path)

    # increase_isom_force(osim_model_path, 3)
    # increase_isom_force(osim_model_path, 3)

    # ikfile = r"C:\Git\research_documents\students\marcel_BSc_vienna\opensim-deadlift-techniques\athlete_0\motion\sumo_dl_80kg02\IK\ik.mot"
    # bops.checkMuscleMomentArms(osim_model_path, ik_file_path=ikfile, leg="l")
    run_ik(model_path, trial_path)

    print("Script completed successfully!")
# %% END
