# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
from src.imports import *  # file paths of the athlete
from src.local_functions import *  # local functions for the project
from src.forcesPlot import run_forces_plot
from src.emptyBarComparison import run_emptybar_comparison
from src.completePlot import run_momentarms_plot
from src.muscleForceSum import run_muscle_force_sum_plot
from src.totalMuscleForce import run_muscle_force_total_plot
from src.totalMuscleForceAdditional import run_muscle_force_total_additional_plot
from src.seeTrailComparison import run_trail_comparison
from src.normalizedFiberLengths import run_normalized_fibers
from src.normalizeMuscleForces import run_normalized_muscle_force
from src.increaseForce import increase_max_isometric_force

#####################################################################################

if __name__ == "__main__":

    increase_max_isometric_force(
        "/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_1_increased_force_3/athlete_1_scaled.osim",
        4,
    )
    # trc_filepath = "/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_1/static_00.trc"
    # calculate_joint_centres_modified(
    #   trc_filepath,
    #  "/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_1/static_00_hjc.trc",
    # )
    ########################## MUSCLE FORCES ##############################################
    run_muscle_force_sum_plot(False)

    ########################## NORMALIZED MUSCLE FORCES ###################################
    run_normalized_muscle_force(False)

    ##################### TOTAL MUSCLE FORCES #############################################
    run_muscle_force_total_plot(False)  # total muscle forces between the techniques

    ########################## MOMENT ARMS ################################################
    run_momentarms_plot(False)  # moments and moment arms between the techniques

    ########################## NORMALIZED FIBER LENGTHS ####################################
    run_normalized_fibers(False)

    ##################################### testing #########################################
    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_trail_comparison(False)  # plot for testing the mean values of angles and forces
    run_emptybar_comparison(False)  # sumo dl with loaded and emptybar comparison
    run_forces_plot(False)  # angles and single muscles right leg, refactor when needed
    run_muscle_force_total_additional_plot(False)
    #######################################################################################
