# Copyright (c) 2024 Basilio Gonçalves & Marcel Hacker

################################ IMPORTS ###########################################
from src.imports import *  # file paths of the athlete
from src.local_functions import *  # local functions for the project
from src.forcesPlot import run_forces_plot
from src.emptyBarComparison import run_emptybar_comparison
from src.completePlot import run_complete_plot
from src.muscleForceSum import run_muscle_force_sum_plot
from src.totalMuscleForce import run_muscle_force_sum_plot
from src.seeTrailComparison import run_trail_comparison

#####################################################################################

if __name__ == "__main__":

    # todo add test_plot with angles, moments, moment arms, activations and forces for the data
    run_forces_plot(False)  # angles and single muscles
    run_emptybar_comparison(False)
    run_complete_plot(False)
    run_muscle_force_sum_plot(False)
    run_muscle_force_sum_plot(False)
    run_trail_comparison(True)
