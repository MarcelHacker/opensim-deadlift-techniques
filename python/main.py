# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
import unittest
from src.imports import *  # file paths of the athlete

from src.local_functions import *  # local functions for the project

from src.kinematicsPlot import run_kinematics_plot
from src.momentsPlot import run_moments_plot
from src.forcesPlot import run_forces_plot
from src.momentArmsHipPlot import run_moment_arms_hip_plot

# from src.muscleForceSum import run_muscle_force_sum_plot
# from src.activationsComparison import run_activations_comparison_from_emg
# from src.rawEmgPlot import run_raw_emg_plot
# from src.normEmgPlot import run_norm_emg_plot
from src.totalMuslceForceTrails import run_total_muscle_force_plot_trails
from src.muslceMomentsPlot import run_muscle_moments_plot


#####################################################################################
class test(unittest.TestCase):

    ##### TESTS WORKING ######
    def test_update_version(self):
        print("Test")
        # run_muscle_force_sum_plot(False)


current_directory = os.path.dirname(os.path.realpath(__file__))
dir_name = os.path.dirname(os.path.dirname(current_directory))
dir_athletes = os.path.dirname(current_directory)  # change this to simulations folder
print("DIR athletes: ", dir_athletes)


if __name__ == "__main__":
    ## set athlete in imports.py
    ## unittest.main()
    created_athlete = Athlete(
        "athlete_2",
        25,
        "male",
        185,
        95,
        "conv",
        175,
        250,
        dir_athletes + "/simulations/athlete_2",
    )
    # Athlete.create_athlete_json(
    #   created_athlete, dir_athletes + "/simulations/athlete_2"
    # )

    ################################## USED FUNCTIONS ###################################################
    run_total_muscle_force_plot_trails(False)
    run_muscle_moments_plot(False)
    # run_norm_emg_plot(False)
    # run_raw_emg_plot(False)
    # run_activations_comparison_from_emg(False)

    run_kinematics_plot(False)
    run_moments_plot(False)
    run_forces_plot(True)
    run_moment_arms_hip_plot(False)
    ########################## MUSCLE FORCES ##############################################
    # run_muscle_force_sum_plot(False)

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
