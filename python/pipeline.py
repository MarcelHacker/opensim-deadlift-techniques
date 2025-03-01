import opensim as osim
import pandas as pd
import os


def import_trc_file(trcFilePath):
    """
    Input: trcFilePath(str) =  path to the trc file

    Output: trc_data(dict) = dictionary with the trc data
            trc_dataframe(pd.DataFrame) = DataFrame with the trc data
    """
    trc_data = pd.read_csv(
        trcFilePath,
        sep="\t",
        skiprows=2,
    )
    print("TRC: \n", trc_data)

    # convert data to DataFrame
    data_dict = {}
    headers = list(trc_data.keys())
    # only include columns from "Time" to "Markers" (i.e. labeled markers)
    data = list(trc_data.values())[headers.index("Time") : headers.index("Markers") - 1]
    headers = headers[headers.index("Time") : headers.index("Markers") - 1]

    for col_idx in range(1, len(data)):
        col_name = headers[col_idx]
        col_data = data[col_idx]
        col_dict = {"x": [], "y": [], "z": []}
        for i in range(len(col_data)):
            col_dict["x"].append(col_data[i][0])
            col_dict["y"].append(col_data[i][1])
            col_dict["z"].append(col_data[i][2])

        data_dict[col_name] = col_dict

    # convert data to DataFrame
    trc_dataframe = pd.DataFrame(data_dict)
    trc_dataframe.to_csv(os.path.join(os.path.dirname(trcFilePath), "test.csv"))

    return trc_data, trc_dataframe


def run_IK(osim_modelPath, trc_file, resultsDir):
    """
    Function to run Inverse Kinematics using the OpenSim API.

    Inputs:
            osim_modelPath(str): path to the OpenSim model file
            trc_file(str): path to the TRC file
            resultsDir(str): path to the directory where the results will be saved
    """

    # Load the TRC file
    # import pdb; pdb.set_trace()
    tuple_data = import_trc_file(trc_file)
    df = pd.DataFrame.from_records(tuple_data, columns=[x[0] for x in tuple_data])
    column_names = [x[0] for x in tuple_data]
    if len(set(column_names)) != len(column_names):
        print("Error: Duplicate column names found.")
    # Load the model
    osimModel = osim.Model(osim_modelPath)
    state = osimModel.initSystem()

    # Define the time range for the analysis
    initialTime = "0"
    finalTime = "12"

    # Create the inverse kinematics tool
    ikTool = osim.InverseKinematicsTool()
    ikTool.setModel(osimModel)
    ikTool.setStartTime(initialTime)
    ikTool.setEndTime(finalTime)
    ikTool.setMarkerDataFileName(trc_file)
    ikTool.setResultsDir(resultsDir)
    ikTool.set_accuracy(1e-6)
    ikTool.setOutputMotionFileName(os.path.join(resultsDir, "ik.mot"))

    # print setup
    ikTool.printToXML(os.path.join(resultsDir, "ik_setup.xml"))

    # Run inverse kinematics
    print("running ik...")
    ikTool.run()


run_IK(
    "/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_3_increased_force_14/scaled_model.osim",
    "/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_3_increased_force_14/conv_dl_0/markers_experimental.trc",
    "/Users/marcelhacker/Documents/opensim-deadlift-techniques/simulations/athlete_3_increased_force_14/",
)
