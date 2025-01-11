from .imports import (
    plt,
    athlete_0_parsed,
    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_1,
    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_2,
    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_1,
    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_2,
)

active_athlete_json = athlete_0_parsed


def run_moment_arms_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            rows = 6
            cols = 2
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Moment Arms Trails "
                + active_athlete_json["name"]
                + "; Model: "
                + active_athlete_json["model_name"]
                + "; Preferred: "
                + active_athlete_json["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle Forces")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "recfem_r",
                "vaslat_r",
                "vasmed_r",
                "glmax1_r",
                "glmax2_r",
                "glmax3_r",
            ]
            coordinates_l = [
                "recfem_l",
                "vaslat_l",
                "vasmed_l",
                "glmax1_l",
                "glmax2_l",
                "glmax3_l",
            ]
            ylabels = [
                "Rectus femoris [N]",
                "Vastus laterlis [N]",
                "Vastus medialis [N]",
                "Gluteus maximus 1 [N]",
                "Gluteus maximus 2 [N]",
                "Gluteus maximus 3 [N]",
            ]
            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_1[
                        coordinates_r[i]
                    ],
                    label="Trail 1 r",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_1[
                        coordinates_l[i]
                    ],
                    label="Trail 1 l",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_2[
                        coordinates_r[i]
                    ],
                    label="Trail 2 r",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_sumo_time_normalised_2[
                        coordinates_l[i]
                    ],
                    label="Trail 2 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for x in range(len(coordinates_r)):
                plt.sca(axs[1, x])
                plt.title("Conventional Deadlift")
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_1[
                        coordinates_r[x]
                    ],
                    label="Trail 1 r",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_1[
                        coordinates_l[x]
                    ],
                    label="Trail 1 l",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_2[
                        coordinates_r[x]
                    ],
                    label="Trail 2 r",
                )
                plt.plot(
                    athlete_0_momentArms_hip_flexion_r_conv_time_normalised_2[
                        coordinates_l[x]
                    ],
                    label="Trail 2 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[x])
                plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_moment_arms_plot")
            print(e)
