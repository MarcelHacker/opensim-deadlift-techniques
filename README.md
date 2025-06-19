# opensim-deadlift-techniques

## FOR MAC

Important:

```md
export PYTHONPATH=/Users/marcelhacker/Applications/OpenSim_4.5/sdk/Python:$PYTHONPATH
```

1. Activate env and nagivate to project:

```md
cd "/Users/marcelhacker/penv/bin"
source activate
cd "/Users/marcelhacker/Documents/opensim-deadlift-techniques"
cd python
```

## FOR WINDOWS

1. Activate env and navigate to project:

```md
cd "C:\Users\ihack\Documents\penv\Scripts"
activate
cd "C:\Users\ihack\Documents\opensim-deadlift-techniques"
```

## Install opensim python

```md
e:
cd "E:\OpenSim 4.5\sdk\Python"
python setup_win_python38.py
python -m pip install .
```

# WORKFLOW

Important: Add the external weight to the hands to account for barbell.

1. Export .c3d and .trc from VICON data.
2. Extract .TRC for markers, and .MOT for ground reaction force data.
3. Add and Calculate joint centers in MOKKA, for now.
4. Scaling the generic model.
5. Inverse Kinematics.
6. Inverse Dynamics.
7. Static Optimisation with Sum of Activations _SQUARED_.

# Current Problems

TRC files are crashing when joint centers are calculated manualy.

Pelvis_rotation xml -> zu ändern zu -180 bis 180 Grad oder Radiant

## MAC path for python packages:

Macintosh HD/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/side-packages

```md
export PYTHONPATH=/Users/marcelhacker/Applications/OpenSim_4.5/sdk/Python:$PYTHONPATH
```

## Python alias for terminal

alias python=python3
source ~/.bashrc

## VICON Export

Select only the labelled markers and export those only to trc. TRC Version 4. The scaling pose and the dynamic markerpositions have to match the model (generic) pose! DO not move the placed remaining markers after the static trial.

## Citations

Mainly to Basilio Goncalves from University of Vienna which made all this possible. Thanks!

Package msk_modelling_python (pre-release) from Basilio Goncalves, PhD, University of Vienna, 2024

Rajagopal, A., Dembia, C. L., DeMers, M. S., Delp, D. D., Hicks, J. L., & Delp, S. L. (2016). Full-Body Musculoskeletal Model for Muscle-Driven Simulation of Human Gait. IEEE transactions on bio-medical engineering, 63(10), 2068–2079. https://doi.org/10.1109/TBME.2016.2586891

Harrington, M. E., Zavatsky, A. B., Lawson, S. E., Yuan, Z., & Theologis, T. N. (2007). Prediction of the hip joint centre in adults, children, and patients with cerebral palsy based on magnetic resonance imaging. Journal of biomechanics, 40(3), 595–602. https://doi.org/10.1016/j.jbiomech.2006.02.003

### Aditional:

If remote hungs up run:

```md
git config http.postBuffer 524288000
```

also include PYTHON in the path of terminal:

```md
PYTHONPATH=/Users/marcelhacker/Applications/OpenSim_4.5/sdk/Python:$PYTHONPATH
```

Create Alias for python command in terminal:

```md
alias python=python3
source ~/.bashrc
```
