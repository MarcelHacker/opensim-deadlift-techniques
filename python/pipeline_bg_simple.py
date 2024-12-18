'''
Code to run OpenSim analysis Marcel's data BSc
'''

from msk_modelling_python import *
import msk_modelling_python as msk

run_setup = False
run_scale_model = False
run_increase_isom_force = False
run_ik = False
run_id = False
run_so = False

osim_model_path = None
static_trc_file_path = None
max_isometric_force_scale_factor = 1

# motion files
c3d_file_path = None
motion_trc_file_path = None
grf_mot_file_path = None
grf_xml_file_path = None    
actuators_so_file_path = None

trial_path = os.path.dirname(motion_trc_file_path)
ik_results_path = os.path.join(trial_path, 'ik.mot')
id_results_path = os.path.join(trial_path, 'id.sto')


# setup (to finish)
if run_setup:
    try:
        msk.bops.c3d_osim_export(c3d_file_path)
        file_name_no_ext = c3d_file_path.split('\\')[-1].replace('.c3d', '')
        grf_file = c3d_file_path.replace('.c3d', '\\forces\\' + file_name_no_ext + '\\grf.mot')
        msk.bops.create_grf_xml(grf_file, output_file= '', apply_force_body_name='calcn_r', force_expressed_in_body_name='ground')  
    except Exception as e:
        print('Error in setup')
        print(e)
        msk.log_error('Error in Marcel analysis setup: ' + str(e))
    
# Scale model
if run_scale_model:
    try:
        msk.bops.scale_model(osim_model_path, static_trc_file_path)
    except Exception as e:
        print('Error in scaling model')
        print(e)
        msk.log_error('Error in Marcel analysis scaling model: ' + str(e))

# change Max isometric force
if run_increase_isom_force:
    try:
        osimSetup = msk.classes.osimSetup()
        osimSetup.increase_max_isometric_force(osim_model_path, increase_factor = max_isometric_force_scale_factor)
    except Exception as e:
        print('Error in changing Max isometric force')
        print(e)
        msk.log_error('Error in Marcel analysis changing Max isometric force: ' + str(e))

# Inverse kinematics
if run_ik:
    try:
        msk.bops.run_IK(osim_model_path, motion_trc_file_path, trial_path)
    except Exception as e:
        print('Error in inverse kinematics')
        print(e)
        msk.log_error('Error in Marcel analysis inverse kinematics: ' + str(e))

# Inverse dynamics
if run_id:
    try:
        msk.bops.run_ID(osim_model_path, ik_results_path, grf_mot_file_path, grf_xml_file_path, trial_path)
    except Exception as e:
        print('Error in inverse dynamics')
        print(e)
        msk.log_error('Error in Marcel analysis inverse dynamics: ' + str(e))
        
# Static optimization
if run_so:
    try:
        msk.bops.run_SO(osim_model_path, trial_path, actuators_so_file_path)
    except Exception as e:
        print('Error in static optimization')
        print(e)
        msk.log_error('Error in Marcel analysis static optimization: ' + str(e))

