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
from src.normalizedFibreLengths import run_normalized_fibres

#####################################################################################

if __name__ == "__main__":
    ########################## MUSCLE FORCES ##############################################
    run_muscle_force_sum_plot(False)  #

    ##################### TOTAL MUSCLE FORCES #############################################
    run_muscle_force_total_plot(False)  # total muscle forces between the techniques

    ########################## MOMENT ARMS ################################################
    run_momentarms_plot(False)  # moments and moment arms between the techniques

    ########################## NORMALIZED FIBRE LENGTHS ####################################
    run_normalized_fibres(False)

    ##################################### testing #########################################
    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_trail_comparison(False)  # plot for testing the mean values of angles and forces
    run_emptybar_comparison(False)  # sumo dl with loaded and emptybar comparison
    run_forces_plot(False)  # angles and single muscles right leg, refactor when needed
    run_muscle_force_total_additional_plot(False)
    #######################################################################################
