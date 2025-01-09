##
# # Usage for VICON data static export:
# python increaseForce.py
##
import opensim as osim


def increase_max_isometric_force(model_path, factor):  # opensim API
    print(model_path)

    # Load the OpenSim model
    model = osim.Model(model_path)

    # Loop through muscles and update their maximum isometric force
    for muscle in model.getMuscles():
        current_max_force = muscle.getMaxIsometricForce()
        new_max_force = current_max_force * factor
        muscle.setMaxIsometricForce(new_max_force)

    # Save the modified model
    output_model_path = model_path.replace(".osim", f"_increased_force_{factor}.osim")
    model.printToXML(output_model_path)

    print(f"Model with increased forces saved to: {output_model_path}")
