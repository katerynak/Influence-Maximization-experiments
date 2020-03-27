import os
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger
import time


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


experiment_dirs = get_immediate_subdirectories(".")

for exp_dir in experiment_dirs:
    experiment = exp_dir
    exp_dir = "./" + exp_dir + "/plots"
    dirs = get_immediate_subdirectories(exp_dir)
    experiment_pdf = []
    for dir in dirs:
        dataset = dir
        dir = exp_dir + "/" + dir + "/"
        # os.remove(dir + "result.pdf")
        filePath = dir + "result.pdf"
        if os.path.exists(filePath):
            os.remove(filePath)
        onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
        onlyfiles = sorted(onlyfiles)
        print(onlyfiles)

        merger = PdfFileMerger()

        for pdf in onlyfiles:
            merger.append(dir + pdf)

        print(len(onlyfiles))

        merger.write(dir + "result.pdf")
        merger.close()
        os.system(f"pdfnup --nup 2x2 --landscape --suffix multiple_{dataset}_{experiment} {dir}result.pdf")
        experiment_pdf.append(f"result-multiple_{dataset}_{experiment}.pdf")
    # fare merge qui per esperimento
    merger = PdfFileMerger()
    experiment_pdf = sorted(experiment_pdf)

    for pdf in experiment_pdf:
        merger.append(pdf)

    merger.write(f"{experiment}.pdf")
    merger.close()

    # remove tmp files
    for pdf in experiment_pdf:
        os.remove(pdf)
