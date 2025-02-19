from src.imports import *
import datetime
from matplotlib.backends.backend_pdf import PdfPages


def plot_pelvis_checks(title, technique, data_moments, data_forces, save_path=None):
    trial_colors = ["red", "blue", "orange", "darkgreen"]
    x_label = "% concentric deadlift cycle"

    fig, axs = plt.subplots(2, 3)
    fig.suptitle(title, fontweight="bold")
    plt.subplots_adjust(
        wspace=0.277, hspace=0.126, top=0.914, right=0.92, left=0.05, bottom=0.064
    )

    coordinates = {
        "moments": [
            "pelvis_tilt_moment",
            "pelvis_list_moment",
            "pelvis_rotation_moment",
        ],
        "forces": ["pelvis_tx_force", "pelvis_ty_force", "pelvis_tz_force"],
    }
    labels = {
        "moments": ["Pelvis Tilt [Nm]", "Pelvis List [Nm]", "Pelvis Rotation [Nm]"],
        "forces": ["Pelvis tx [Nm]", "Pelvis ty [Nm]", "Pelvis tz [Nm]"],
    }

    for i, coord in enumerate(coordinates["moments"]):
        plt.sca(axs[0, i])
        axs[0, i].set_xlim(0, 100)
        plt.title(technique)
        for j, trial_data in enumerate(data_moments):
            plt.plot(trial_data[coord], label=f"Trial {j+1}", color=trial_colors[j])
        plt.ylabel(labels["moments"][i])

    for i, coord in enumerate(coordinates["forces"]):
        plt.sca(axs[1, i])
        axs[1, i].set_xlim(0, 100)
        for j, trial_data in enumerate(data_forces):
            plt.plot(trial_data[coord], label=f"Trial {j+1}", color=trial_colors[j])
        plt.ylabel(labels["forces"][i])
        plt.xlabel(x_label)

    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="center right")
    fig.set_size_inches(14, 7.5)

    if save_path:
        plt.savefig(save_path, dpi=300, format="png")
    plt.show()


def run_validation_athlete(run_validation, save_figures):
    if not run_validation:
        return

    try:
        plot_pelvis_checks(
            f"Pelvis Checks, SDL, Athlete {active_athlete['number']}; Model: {active_athlete['model']}; Preferred: {active_athlete['technique']}; Load: {active_athlete['load']} kg",
            "SDL",
            [
                active_athlete_id_sumo_time_normalised_0,
                active_athlete_id_sumo_time_normalised_1,
                active_athlete_id_sumo_time_normalised_2,
                active_athlete_id_sumo_time_normalised_3,
            ],
            [
                active_athlete_id_sumo_time_normalised_0,
                active_athlete_id_sumo_time_normalised_1,
                active_athlete_id_sumo_time_normalised_2,
                active_athlete_id_sumo_time_normalised_3,
            ],
            (
                f"../results/validation/{active_athlete['name']}_sdl.png"
                if save_figures
                else None
            ),
        )
    except Exception as e:
        print("Error in Pelvis Checks, SDL, Athlete", e)

    try:
        plot_pelvis_checks(
            f"Pelvis Checks, CDL, Athlete {active_athlete['number']}; Model: {active_athlete['model']}; Preferred: {active_athlete['technique']}; Load: {active_athlete['load']} kg",
            "CDL",
            [
                active_athlete_id_conv_time_normalised_0,
                active_athlete_id_conv_time_normalised_1,
                active_athlete_id_conv_time_normalised_2,
                active_athlete_id_conv_time_normalised_3,
            ],
            [
                active_athlete_id_conv_time_normalised_0,
                active_athlete_id_conv_time_normalised_1,
                active_athlete_id_conv_time_normalised_2,
                active_athlete_id_conv_time_normalised_3,
            ],
            (
                f"../results/validation/{active_athlete['name']}_cdl.png"
                if save_figures
                else None
            ),
        )
    except Exception as e:
        print("Error in Pelvis Checks, CDL, Athlete", e)
        ################## PDF ##################################################################################
        try:
            with PdfPages(
                f"/Users/marcelhacker/Documents/opensim-deadlift-techniques/results/pdf/{active_athlete['name']}_validation.pdf"
            ) as pdf:
                # first page
                firstPage = plt.figure(figsize=(11.69, 8.27))
                firstPage.clf()
                txt = (
                    "Validation Model Analysis Deadlift\n\n"
                    f"Athlete: {active_athlete['number']}\n"
                    f"Bodymass: {active_athlete['bodymass']} kg\n"
                    f"Preferred: {active_athlete['technique']}\n"
                    f"Load: {active_athlete['load']} kg\n"
                    f"e1RM: {active_athlete['fmax']} kg\n\n"
                    f"Test date: {active_athlete['testdate']}"
                )

                # Add text to the figure
                firstPage.text(
                    0.5,
                    0.6,
                    txt,
                    transform=firstPage.transFigure,
                    size=24,
                    ha="center",
                    va="center",
                )
                # Additional small text
                firstPage.text(
                    0.1,
                    0.1,
                    "Department of Sport and Human Movement Science, Biomechanics, Kinesiology and Computer Science in Sport\nVienna",
                    size=12,
                )
                # Save to PDF
                pdf.savefig()
                plt.close()

                pdf.savefig(fig_0)
                pdf.savefig(fig_1)
                pdf.savefig(fig_2)
                pdf.savefig(fig_3)

                # We can also set the file's metadata via the PdfPages object:
                d = pdf.infodict()
                d["Title"] = "Validation Model"
                d["Author"] = "Marcel Hacker"
                d["Subject"] = "Kinematics, Kinetics and Muscle Force Analysis"
                d["Keywords"] = "biomechanics"
                d["CreationDate"] = datetime.datetime(2025, 2, 16)
                d["ModDate"] = datetime.datetime.today()
        except Exception as e:
            print("Error in PDFs validation athlete")
            print(e)
