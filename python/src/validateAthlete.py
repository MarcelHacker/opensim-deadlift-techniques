from src.imports import *
import datetime

from matplotlib.backends.backend_pdf import PdfPages


def run_validation_athlete(bool, save_figures):
    if bool:
        trial_color_0 = "red"
        trial_color_1 = "blue"
        trial_color_2 = "orange"
        trial_color_3 = "darkgreen"
        x_label = "% concentric deadlift cycle"
        try:
            fig_0, axs_0 = plt.subplots(2, 3)
            fig_0.suptitle(
                "Pelvis Checks, SDL, Athlete "
                + str(active_athlete["number"])
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            plt.subplots_adjust(
                wspace=0.277,
                hspace=0.126,
                top=0.914,
                right=0.92,
                left=0.05,
                bottom=0.064,
            )
            coordinates_moments = [
                "pelvis_tilt_moment",
                "pelvis_list_moment",
                "pelvis_rotation_moment",
            ]
            coordinates_forces = [
                "pelvis_tx_force",
                "pelvis_ty_force",
                "pelvis_tz_force",
            ]
            labels_moments = [
                "Pelvis Tilt [Nm]",
                "Pelvis List [Nm]",
                "Pelvis Rotation [Nm]",
            ]
            labels_force = [
                "Pelvis tx [Nm]",
                "Pelvis ty [Nm]",
                "Pelvis tz [Nm]",
            ]

            for i in range(len(coordinates_moments)):
                plt.sca(axs_0[0, i])
                axs_0[0, i].set_xlim(left=0, right=100)
                plt.title("SDL")
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_moments[i]],
                    label="Trial 1",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_moments[i]],
                    label="Trial 2",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_moments[i]],
                    label="Trial 3",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_moments[i]],
                    label="Trial 4",
                    color=trial_color_3,
                )
                plt.ylabel(labels_moments[i])

            for i in range(len(coordinates_forces)):
                plt.sca(axs_0[1, i])
                axs_0[1, i].set_xlim(left=0, right=100)
                plt.plot(
                    active_athlete_id_sumo_time_normalised_0[coordinates_forces[i]],
                    label="Trial 1",
                    color=trial_color_0,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_1[coordinates_forces[i]],
                    label="Trial 2",
                    color=trial_color_1,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_2[coordinates_forces[i]],
                    label="Trial 3",
                    color=trial_color_2,
                )
                plt.plot(
                    active_athlete_id_sumo_time_normalised_3[coordinates_forces[i]],
                    label="Trial 4",
                    color=trial_color_3,
                )
                plt.ylabel(labels_force[i])
                plt.xlabel(x_label)

            handles, labels = axs_0[
                0, 0
            ].get_legend_handles_labels()  # get legend from first plot
            fig_0.legend(handles, labels, loc="center right")
            fig_0.set_size_inches(14, 7.5)
            if save_figures:
                plt.savefig(
                    "../results/validation/" + active_athlete["name"] + ".png",
                    transparent=None,
                    dpi=300,
                    format="png",
                )
            plt.show()

        except Exception as e:
            print("Error in Pelvis Checks, SDL, Athlete")
            print(e)
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
