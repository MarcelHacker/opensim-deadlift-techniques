# test opensim

import struct 
print("Bit version of python:",struct.calcsize("P") * 8)

import opensim as osim

model = osim.Model()

print("Version and date:",osim.GetVersionAndDate())

print("OpenSim model created successfully!")