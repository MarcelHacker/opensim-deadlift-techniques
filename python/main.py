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
from src.activationsComparison import run_activations_comparison_from_emg


#####################################################################################
class test(unittest.TestCase):

    ##### TESTS WORKING ######
    def test_update_version(self):
        print("Test")
        # run_muscle_force_sum_plot(False)


if __name__ == "__main__":
    ## set athlete in imports.py    unittest.main()
    run_activations_comparison_from_emg(True)

    run_kinematics_plot(False)
    run_moments_plot(False)
    run_forces_plot(False)
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
