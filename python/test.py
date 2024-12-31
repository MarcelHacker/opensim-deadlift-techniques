# test opensim
import struct

print("Bit version of python:", struct.calcsize("P") * 8)

# activate your virtual environment
# cd penv
# cd bin
# source activate

import opensim as osim

model = osim.Model()

print("Version and date of opensim: ", osim.GetVersionAndDate())

print("OpenSim model created successfully!")

# solution was export PYTHONPATH=/Users/marcelhacker/Applications/OpenSim_4.5/sdk/Python:$PYTHONPATH

