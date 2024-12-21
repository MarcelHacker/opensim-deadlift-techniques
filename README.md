# opensim-deadlift-techniques

# 1. Activate env

cd "/Users/marcelhacker/penv/bin"
source activate

# 2. Navigate to project

cd "/Users/marcelhacker/Documents/opensim-deadlift-techniques"

# Current Problems

TRC files are crashing when joint centers are calculated manualy.

Pelvis_rotation xml -> zu ändern zu -180 bis 180 Grad oder Radiant

# WORKFLOW

1. Export c3d from VICON.
2. Extract TRC for markers, and MOT for ground reaction force data.
3. Add and Calculate joint centers
4. Transform the data, when needed with extractMarkers.py
5. Scaling the generic model
6. Inverse Kinematics
7. Inverse Daynamics
8. Static optimisation

# MAC path for python packages:

Macintosh HD/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/side-packages

# Opensim path for python

export PYTHONPATH=/Users/marcelhacker/Applications/OpenSim_4.5/sdk/Python:$PYTHONPATH

# Python alias for terminal

alias python=python3
source ~/.bashrc

# CONDA deactivation (deinstall it):

conda deactivate

# Learnings

The scaling pose and the dynamic markerpositions have to match the model (generic) pose!

# VICON Export

Select only the labelled markers and export those only to trc.

## Citations

Mainly to Basilio Goncalves from University of Vienna which made all this possible. Thanks!

Package msk_modelling_python (pre-release) from Basilio Goncalves, PhD, University of Vienna, 2024

Rajagopal, A., Dembia, C. L., DeMers, M. S., Delp, D. D., Hicks, J. L., & Delp, S. L. (2016). Full-Body Musculoskeletal Model for Muscle-Driven Simulation of Human Gait. IEEE transactions on bio-medical engineering, 63(10), 2068–2079. https://doi.org/10.1109/TBME.2016.2586891

Harrington, M. E., Zavatsky, A. B., Lawson, S. E., Yuan, Z., & Theologis, T. N. (2007). Prediction of the hip joint centre in adults, children, and patients with cerebral palsy based on magnetic resonance imaging. Journal of biomechanics, 40(3), 595–602. https://doi.org/10.1016/j.jbiomech.2006.02.003

# if remote hungs up run

git config http.postBuffer 524288000
