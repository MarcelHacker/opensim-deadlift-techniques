# Copyright (c) 2025 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
import unittest
from src.imports import *  # file paths of the athlete
from src.modules import *  # local modules for the project
from src.exportCSV import export_csv
from src.validateAthlete import run_validation_athlete
from src.processAthlete import run_process_athlete
from src.validateRRA import run_validation_rra_athlete


# from src.activationsComparison import run_activations_comparison_from_emg
# from src.rawEmgPlot import run_raw_emg_plot
# from src.normEmgPlot import run_norm_emg_plot

# from src.statisticsOverall import run_muscle_force_groups_overall
# from src.statisticsSummary import run_muscle_force_groups_summary
# from src.summaryPreferences import run_muscle_group_preferences


#####################################################################################
class test(unittest.TestCase):

    ##### TESTS WORKING ######
    def test_update_version(self):
        print("Test")


current_directory = os.path.dirname(os.path.realpath(__file__))
dir_name = os.path.dirname(os.path.dirname(current_directory))
dir_athletes = os.path.dirname(current_directory)  # change this to simulations folder
print("DIR athletes: ", dir_athletes)

if __name__ == "__main__":
    ## set athlete in imports.py
    ## unittest.main()
    # create_pdf_report(False)

    # todo fix athlete_2_increased_force_60/conv_dl_0

    save_figures = False
    run = True
    
    export_csv(run)  # export force data to csv
    #run_validation_rra_athlete(run, save_figures)
    run_validation_athlete(run, save_figures)
    run_process_athlete(run, save_figures)
    ################################## USED FUNCTIONS ###################################################
    run_total_muscle_force_plot_spm(run, save_figures)
    # run_total_muscle_force_plot_trails(False, save_figures)
    # run_muscle_moments_plot(False, save_figures)
    # run_norm_emg_plot(False)
    # run_raw_emg_plot(False)
    # run_activations_comparison_from_emg(False)

    # run_kinematics_plot(False, save_figures)
    # run_moments_plot(False, save_figures)
    # run_forces_plot(False, save_figures)
    # run_moment_arms_hip_plot(False, save_figures)
    ########################## MUSCLE FORCES ##############################################
    run_muscle_force_groups(run, save_figures)

    # run_muscle_force_groups_overall(run, save_figures)
    # run_muscle_force_groups_summary(run, save_figures)
    # run_muscle_group_preferences(run, save_figures)
    ########################## NORMALIZED MUSCLE FORCES ###################################
    # run_normalized_muscle_force(False)

    ##################### TOTAL MUSCLE FORCES #############################################
    # run_muscle_force_total_plot(False)  # total muscle forces between the techniques

    ########################## MOMENT ARMS ################################################
    # run_momentarms_plot(False)  # moments and moment arms between the techniques

    ########################## NORMALIZED FIBER LENGTHS ####################################
    # run_normalized_fibers(False)

    ##################################### testing #########################################
    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    # run_trail_comparison(False)  # plot for testing the mean values of angles and forces
    # run_emptybar_comparison(False)  # sumo dl with loaded and emptybar comparison
    # run_forces_plot(False)  # angles and single muscles right leg, refactor when needed
    # run_muscle_force_total_additional_plot(False)
    #######################################################################################
