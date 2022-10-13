import subprocess
import os
import glob
import cv2
from pathlib import Path
from pdf2jpg import pdf2jpg


def pdf2mp4(pdf_path):
    pdf_name = os.path.basename(pdf_path)
    output_dir = "./output/" + pdf_name + "_dir"
    video_name = pdf_name + "_vid"

    pdf2image(pdf_path)
    image2mp4(output_dir, video_name)
    remove_garbage(output_dir)
    return

def pdf2image(pdf_path):
    try:
        _ = pdf2jpg.convert_pdf2jpg(pdf_path, "./output/", dpi=300, pages="ALL")
        subprocess.run('explorer {}'.format(os.path.join(cwd, "output")))
        print("Done!")

    except Exception as e:
        print(e)

def image2mp4(output_dir, video_name):
    image_files = sorted(glob.glob(f"{output_dir}/*.jpg"))
    height, width, _ = cv2.imread(image_files[0]).shape[:3]
    video_writer = cv2.VideoWriter(
        f"{output_dir}/{video_name}.mp4",
        cv2.VideoWriter_fourcc('m','p','4','v'),
        1.0, (width, height))

    for image_file in image_files:
        img = cv2.imread(image_file)
        video_writer.write(img)
    video_writer.release()

def remove_garbage(output_dir):
    images = glob.glob(output_dir+'/*.jpg')
    for image in images:
        if os.path.isfile(image):
            os.remove(image)

if __name__ == "__main__":
    cwd = Path(__file__).resolve().parent
    os.chdir(cwd)
    file_path = input("Drag and Drop PDF File Here and Press \"Return\" \nFile Name MUST be English!\nFile Path: ")
    pdf2mp4(file_path)