import pandas as pd
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt
import os
import unittest
import msk_modelling_python as msk
import seaborn as sns

# the functions below assume that the CSV files have the same structure unless otherwise specified
# the first column in the py files should be named "time" or "frame"


class DataSet:
    # dataset is assumed to be a list of TimeSeries objects
    # each TimeSeries object is assumed to have a pandas dataframe with the first column named "time" or "frame"
    # usage: data = DataSet(files=[file1, file2, file3])

    def __init__(self, files=[]):

        self.module_path = os.path.dirname(os.path.abspath(__file__))

        if not files:
            self.files = select_multiple_files()
        elif files == "template":
            self.files = [
                os.path.join(self.module_path, "data", "template1.csv"),
                os.path.join(self.module_path, "data", "template2.csv"),
            ]
        else:
            self.files = files

        self.trials = []
        self.trial_names = []
        for file in self.files:
            if not os.path.basename(file).endswith(
                ".csv"
            ):  # check if the file is a CSV file
                Warning(f"File {file} is not a CSV file. Further errors may occur.")

            self.trials.append(TimeSeries(file))

    def plot_lines(self, show=True):

        for trial in self.trials:
            trial.plot_line(show=False)

        if show:
            plt.show()

    def correlation_matrix(self, show=True):

        try:
            sns.heatmap(self.df.corr(), annot=True)

            # save the plot
            plt.savefig(
                os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "correlation_matrix.png"
                )
            )
            if show:
                plt.show()
        except:
            msk.ut.pop_warning("Error: Could not plot the correlation matrix")

    def show(self):
        plt.show()


class TimeSeries:
    def __init__(self, file_path):
        self.name = os.path.splitext(os.path.basename(file_path))[0]
        self.file_path = file_path
        self.print = False
        self.read_csv(file_path)

    def read_csv(self, file):
        try:
            self.df = pd.read_csv(file)
            self.num_frames = len(self.data)
            self.num_columns = len(self.data.columns)
            self.columns = self.data.columns

            if self.columns[0].lower() in ["time", "frame"]:
                self.time = self.df[self.columns[0]]
                self.data = self.df.drop(columns=[self.columns[0]])
                self.header = self.columns[1]
            else:
                self.time = self.df["time"]
                self.data = self.df.drop(columns=["time"])
                self.header = self.df.columns[0]

            self.correlation_matrix = self.data.corr()

            if self.print:
                print(f"Data from {file} has been read successfully")

        except:
            self.data = None
            self.header = None
            self.num_frames = None

            if self.print:
                print("Error: Could not read the CSV file")

    def plot_line(self, show=True):
        plt.plot(self.df[self.header], label=f"{self.name}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.savefig(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{self.name}.png")
        )
        if show:
            try:
                plt.show(block=False)
                plt.gcf().canvas.manager.window.attributes("-topmost", 1)
                plt.gcf().canvas.manager.window.attributes("-topmost", 0)
            except:
                plt.show()
                Warning("waring! Could not show the plot using the canvas method")


def select_file(initialdir=os.path.dirname(os.path.abspath(__file__))):
    # select single file. Default directory is the directory of the script
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        initialdir=initialdir,
        title="Select file",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*")),
    )
    return file_path


def select_multiple_files(initialdir=os.path.dirname(os.path.abspath(__file__))):
    # select multiple files from same folder. Default directory is the directory of the script
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        initialdir=initialdir,
        title="Select multiple files",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*")),
    )
    return files


def plot_curves(file1, file2):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Get the header names
    header1 = df1.columns[0]
    header2 = df2.columns[0]

    # Check if the header names are "time" or "frame"
    if header1.lower() in ["time", "frame"] and header2.lower() in ["time", "frame"]:
        # Plot the curves
        plt.plot(df1[header1], label=f"{file1}_{header1}")
        plt.plot(df2[header2], label=f"{file2}_{header2}")

        # Add labels and legend
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()

        # Show the plot
        plt.show()
    else:
        print("The first column in both files should be named 'time' or 'frame.'")


def plot_multiple_curves(files):
    for file in files:
        df = pd.read_csv(file)
        header = df.columns[0]
        if header.lower() in ["time", "frame"]:
            plt.plot(df[header], label=f"{file}_{header}")
        else:
            print(f"The first column in {file} should be named 'time' or 'frame.'")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()


def calculate_joint_centres_modified(
    trc_filepath, new_filepath=None
):  # modified from lib
    """
    Calculates hip joint centers in a TRC file according to Harrington et al.

    Args:
        trc_filepath (str): Path to the TRC file.
        new_filepath (str, optional): Path to save the modified TRC file. Defaults to None.

    Returns:
        dict: Dictionary containing the modified TRC data.
    """
    trc = pd.read_csv(trc_filepath, sep="\t", skiprows=3)
    print("TRC: ", trc)
    print("TRC: ", trc["Time"][1])  # time [0] is NaN in this trc file
    print("TRC: ", trc["Time"][2])

    # Load TRC data
    # with open(trc_filepath, "r") as f:
    # ... (Implementation for loading TRC data using your preferred library)
    #   trc = ...

    # Set default output filepath
    if new_filepath is None:
        new_filepath = trc_filepath.replace(".trc", "_HJC.trc")

    # Sample rate (assuming data is evenly sampled)
    rate = round(1 / (trc["Time"][2] - trc["Time"][1]))  # time[0] is NaN in trc file

    # Add HJC using Harrington equations
    trc = add_hjc_harrington(trc)

    # Add knee and ankle joint centers (assuming markers exist)
    trc["RKJC"] = (trc["RKNE"] + trc["RKNM"]) / 2
    trc["LKJC"] = (trc["LKNE"] + trc["LKNM"]) / 2
    trc["RAJC"] = (trc["RANK"] + trc["RANM"]) / 2
    trc["LAJC"] = (trc["LANK"] + trc["LANM"]) / 2

    # Convert markers to separate data and labels (assuming specific format)
    markers_data = np.array([v for k, v in trc.items() if k != "Time"])
    marker_labels = list(trc.keys())[1:]

    # Save modified TRC data
    try:
        # ... (Implementation for saving TRC data using your preferred library)
        msk.write_trc_os4(markers_data, marker_labels, rate, new_filepath)
    except Exception as e:
        print(f"Error saving TRC file: {e}")
        # Handle potential issues (e.g., missing markers)

    return trc


def add_hjc_harrington(trc):
    """
    Calculates hip joint centers (HJC) using Harrington et al. (2006) formulas.

    Args:
        trc (dict): Dictionary containing TRC data.

    Returns:
        dict: Modified TRC data with added HJC markers.
    """

    lasis = trc["LASI"].T
    rasis = trc["RASI"].T

    # Handle missing SACRUM marker
    try:
        sacrum = trc["USACR"].T  # USACR markers exist in this model
    except KeyError:
        sacrum = (trc["LPSI"] + trc["RPSI"]) / 2
        trc["USACR"] = sacrum.T

    num_frames = len(rasis)
    hjc_left, hjc_right = np.empty((3, num_frames)), np.empty((3, num_frames))

    for i in range(num_frames):
        # Right-handed pelvis reference system definition
        pelvis_center = (lasis[:, i] + rasis[:, i]) / 2
        provv = (rasis[:, i] - sacrum[:, i]) / np.linalg.norm(
            rasis[:, i] - sacrum[:, i]
        )
        ib = (rasis[:, i] - lasis[:, i]) / np.linalg.norm(rasis[:, i] - lasis[:, i])
        kb = np.cross(ib, provv)
        kb /= np.linalg.norm(kb)
        jb = np.cross(kb, ib)
        jb /= np.linalg.norm(jb)

    pelvis_transform = np.array(
        [ib[0], jb[0], kb[0], pelvis_center[0]],
        [ib[1], jb[1], kb[1], pelvis_center[1], ib[2], jb[1]],
    )


def spider(files):
    # Read the CSV files

    for file in files:
        df = pd.read_csv(file)
        header = df.columns[0]
        if header.lower() in ["time", "frame"]:
            plt.plot(df[header], label=f"{file}_{header}")
        else:
            print(f"The first column in {file} should be named 'time' or 'frame.'")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    return None


# Testing the functions using unittest module when the script is run directly
class test(unittest.TestCase):
    # for each function assign True or false to run the test

    def test_plot_curves(self, run=False):
        if run:
            print("testing plot_curves ... ")
            file1 = select_file()
            plot_curves(file1, file1)

    def test_plot_multiple_curves(self, run=False):
        if run:
            print("testing plot_multiple_curves ... ")
            files = select_multiple_files()
            plot_multiple_curves(files)

    def test_spider(self, run=False):
        if run:
            print("testing spider ... ")
            files = select_multiple_files()
            spider(files)

    def show_plot(self, run=False):
        if run:
            plt.show()

    def test_DataSet(self, run=True):
        if run:
            print("testing DataSet ... ")
            data = DataSet()
            data.plot_lines(show=False)
            data.correlation_matrix(show=False)
            data.show()


if __name__ == "__main__":
    # create figute with 5x3 subplots
    fig, axs = plt.subplots(5, 3)
    fig.suptitle("Deadlift Sumo Technique Athlete_0")
    fig.set_label("Hip R")

    # calculate_joint_centres_modified(
    #   "/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/static_00.trc"
    # )

    # activate the subplots IK (first row)
    ik_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/ik.mot"

    ik_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/ik.mot"

    # activate the subplots ID (second row)
    id_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/inverse_dynamics.sto"

    id_conve_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/conventional_dl_80kg02/inverse_dynamics.sto"

    # activate the subplots Moment arms (third row)
    momentArmKnee_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_knee_angle_r.sto"

    momentArmAnkle_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_ankle_angle_r.sto"

    momentArmHip_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_increased_force_3_MuscleAnalysis_Moment_hip_flexion_r.sto"

    # activate the subplots muscle forces arms (fourth row)
    muscleForces_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_force.sto"

    # activate the subplots muscle forces arms (fith row)
    muscleActivation_sumo_path = r"/Users/marcelhacker/Documents/opensim-deadlift-techniques/athlete_0_increased_force_3/sumo_dl_80kg02/Athlete0_scaled_StaticOptimization_activation.sto"

    ik_sumo = pd.read_csv(ik_sumo_path, sep="\t", skiprows=10)
    ik_conv = pd.read_csv(ik_conve_path, sep="\t", skiprows=10)
    id_sumo = pd.read_csv(id_sumo_path, sep="\t", skiprows=6)
    id_conv = pd.read_csv(id_conve_path, sep="\t", skiprows=6)
    momentArmHip_sumo = pd.read_csv(momentArmHip_sumo_path, sep="\t", skiprows=11)
    momentArmKnee_sumo = pd.read_csv(momentArmKnee_sumo_path, sep="\t", skiprows=11)
    momentArmAnkle_sumo = pd.read_csv(momentArmAnkle_sumo_path, sep="\t", skiprows=11)
    muscleForces_sumo = pd.read_csv(muscleForces_sumo_path, sep="\t", skiprows=14)
    muscleActivation_sumo = pd.read_csv(
        muscleActivation_sumo_path, sep="\t", skiprows=8
    )
    # returns A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
    if ik_sumo.empty:  # check if file is empty
        print("File is empty:", ik_sumo_path)
    if ik_conv.empty:
        print("File is empty:", ik_conve_path)
    if id_sumo.empty:
        print("File is empty:", id_sumo_path)
    if id_conv.empty:
        print("File is empty:", id_conve_path)
    if momentArmHip_sumo.empty:
        print("File is empty:", momentArmHip_sumo_path)
    if momentArmKnee_sumo.empty:
        print("File is empty:", momentArmKnee_sumo_path)
    if momentArmAnkle_sumo.empty:
        print("File is empty:", momentArmAnkle_sumo_path)
    if muscleForces_sumo.empty:
        print("File is empty:", muscleForces_sumo_path)
    if muscleActivation_sumo.empty:
        print("File is empty:", muscleActivation_sumo_path)

    # check for desired columns in ik files
    if "hip_flexion_r" not in ik_sumo.columns:
        print("Desired column not found in file:", ik_sumo_path)

    if "hip_flexion_r" not in ik_conv.columns:
        print("Desired column not found in file:", ik_conve_path)

    # cut array to 500 items.
    item_count = 499
    ik_sumo = ik_sumo[0:item_count]
    ik_conv = ik_conv[0:item_count]

    # sumo deadlift curves, IK
    ## row 0, column 0
    plt.sca(axs[0, 0])
    plt.plot(ik_sumo["time"], ik_sumo["hip_flexion_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Flexion R Sumo")

    ## row 0, column 1, knee
    plt.sca(axs[0, 1])
    plt.plot(ik_sumo["time"], ik_sumo["knee_angle_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Angle R Sumo")

    ## row 0, column 2, ankle
    plt.sca(axs[0, 2])
    plt.plot(ik_sumo["time"], ik_sumo["ankle_angle_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Angle R Sumo")

    # sumo deadlift curves, ID, moments
    ## row 1, column 0, hip moments
    plt.sca(axs[1, 0])
    plt.plot(id_sumo["time"], id_sumo["hip_flexion_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Hip Flexion Moment R")

    ## row 1, column 1, knee moments
    plt.sca(axs[1, 1])
    plt.plot(id_sumo["time"], id_sumo["knee_angle_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Knee Angle Moment R")

    ## row 1, column 2, ankle moments
    plt.sca(axs[1, 2])
    plt.plot(id_sumo["time"], id_sumo["ankle_angle_r_moment"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Angle Moment R")

    # sumo deadlift curves, MA, Moment arms
    ## row 3, column 0, hip moment arms
    plt.sca(axs[2, 0])
    plt.plot(momentArmHip_sumo["time"], momentArmHip_sumo["semiten_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Moment arms R")

    ## row 3, column 1, knee moment arms
    plt.sca(axs[2, 1])
    plt.plot(momentArmKnee_sumo["time"], momentArmKnee_sumo["vaslat_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Moment arms R")

    ## row 3, column 2, ankle moment arms
    plt.sca(axs[2, 2])
    plt.plot(momentArmAnkle_sumo["time"], momentArmAnkle_sumo["soleus_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Moment arms R")

    # sumo deadlift curves, SO, muscle forces
    ## row 4, column 0, hip muscle forces
    plt.sca(axs[3, 0])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["semiten_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Muscle force R")

    ## row 4, column 1, knee muscle forces
    plt.sca(axs[3, 1])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["vaslat_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Muscle force R")

    ## row 4, column 2, ankle muscle forces
    plt.sca(axs[3, 2])
    plt.plot(muscleForces_sumo["time"], muscleForces_sumo["soleus_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Muscle force R")

    # sumo deadlift curves, SO, muscle forces
    ## row 4, column 0, hip muscle forces
    plt.sca(axs[4, 0])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["semiten_r"])
    plt.xlabel("Time")
    plt.ylabel("Hip Muscle activation R")

    ## row 4, column 1, knee muscle forces
    plt.sca(axs[4, 1])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["vaslat_r"])
    plt.xlabel("Time")
    plt.ylabel("Knee Muscle activation R")

    ## row 4, column 2, ankle muscle forces
    plt.sca(axs[4, 2])
    plt.plot(muscleActivation_sumo["time"], muscleActivation_sumo["soleus_r"])
    plt.xlabel("Time")
    plt.ylabel("Ankle Muscle activation R")

    # todo: insert also conventional deadlift curves
    plt.show()

# END
