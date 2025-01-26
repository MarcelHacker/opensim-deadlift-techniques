import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from .imports import (
    plt,
    active_athlete,
)


def create_pdf_report(bool):
    if bool:
        try:
            # Create the PdfPages object to which we will save the pages:
            # The with statement makes sure that the PdfPages object is closed properly at
            # the end of the block, even if an Exception occurs.
            with PdfPages("multipage_pdf.pdf") as pdf:
                plt.figure(figsize=(3, 3))
                plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], "r-o")
                plt.title("Page One")
                pdf.savefig()  # saves the current figure into a pdf page
                plt.close()

                # if LaTeX is not installed or error caught, change to `False`
                plt.rcParams["text.usetex"] = False
                plt.figure(figsize=(8, 6))
                x = np.arange(0, 5, 0.1)
                plt.plot(x, np.sin(x), "b-")
                plt.title("Page Two")
                pdf.attach_note(
                    "plot of sin(x)"
                )  # attach metadata (as pdf note) to page
                pdf.savefig()
                plt.close()

                plt.rcParams["text.usetex"] = False
                fig = plt.figure(figsize=(4, 5))
                plt.plot(x, x**2, "ko")
                plt.title("Page Three")
                pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
                plt.close()

                # We can also set the file's metadata via the PdfPages object:
                d = pdf.infodict()
                d["Title"] = "Multipage PDF Example"
                d["Author"] = "Marcel Hacker"
                d["Subject"] = "Biomechanics"
                d["Keywords"] = "Deadlift Analysis"
                d["CreationDate"] = datetime.datetime(2009, 11, 13)
                d["ModDate"] = datetime.datetime.today()

        except Exception as e:
            print("Error in create_pdf_report")
            print(e)
