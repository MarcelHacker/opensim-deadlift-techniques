from .imports import (
    plt,
    active_athlete,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_0,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_1,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_1,
    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_2,
    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_2,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_0,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_1,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_1,
    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_2,
    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_2,
)


def run_moment_arms_hip_plot(bool):
    # just for sumo currently avaiable
    if bool:
        try:
            rows = 6
            cols = 2
            fig, axs = plt.subplots(cols, rows)
            fig.suptitle(
                "Moment Arms Hip Flexion Trails "
                + active_athlete["name"]
                + "; Model: "
                + active_athlete["model"]
                + "; Preferred: "
                + active_athlete["technique"],
                fontweight="bold",
            )
            fig.set_label("Muscle Forces")
            x_label = "% concentric deadlift cycle"

            coordinates_r = [
                "recfem_r",
                "semiten_r",
                "addmagIsch_r",
                "glmax1_r",
                "glmax2_r",
                "glmax3_r",
            ]
            coordinates_l = [
                "recfem_l",
                "semiten_l",
                "addmagIsch_l",
                "glmax1_l",
                "glmax2_l",
                "glmax3_l",
            ]
            ylabels = [
                "Rectus femoris [m]",
                "Semitendinosus [m]",
                "Adductor magnus isch [m]",
                "Gluteus maximus 1 [m]",
                "Gluteus maximus 2 [m]",
                "Gluteus maximus 3 [m]",
            ]
            for i in range(len(coordinates_r)):
                plt.sca(axs[0, i])
                plt.title("Sumo Deadlift")
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_0[
                        coordinates_r[i]
                    ],
                    label="Trail 1 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_0[
                        coordinates_l[i]
                    ],
                    label="Trail 1 l",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_1[
                        coordinates_r[i]
                    ],
                    label="Trail 2 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_1[
                        coordinates_l[i]
                    ],
                    label="Trail 2 l",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_sumo_time_normalised_2[
                        coordinates_r[i]
                    ],
                    label="Trail 3 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_sumo_time_normalised_2[
                        coordinates_l[i]
                    ],
                    label="Trail 3 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[i])
                plt.xlabel(x_label)

            for x in range(len(coordinates_r)):
                plt.sca(axs[1, x])
                plt.title("Conventional Deadlift")
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_0[
                        coordinates_r[x]
                    ],
                    label="Trail 1 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_0[
                        coordinates_l[x]
                    ],
                    label="Trail 1 l",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_1[
                        coordinates_r[x]
                    ],
                    label="Trail 2 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_1[
                        coordinates_l[x]
                    ],
                    label="Trail 2 l",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_r_conv_time_normalised_2[
                        coordinates_r[x]
                    ],
                    label="Trail 3 r",
                )
                plt.plot(
                    active_athlete_momentArms_hip_flexion_l_conv_time_normalised_2[
                        coordinates_l[x]
                    ],
                    label="Trail 3 l",
                )
                #  add third trail
                plt.legend()
                plt.ylabel(ylabels[x])
                plt.xlabel(x_label)
            plt.show()

        except Exception as e:
            print("Error in run_moment_arms_hip_plot")
            print(e)
