from pathlib import Path # pathlib for easy path handling
import pydicom # pydicom to handle dicom files
import matplotlib.pyplot as plt
import numpy as np
import dicom2nifti # to convert DICOM files to the NIftI format
import nibabel as nib # nibabel to handle nifti files
import pandas as pd  
from matplotlib import cm
%matplotlib inline
import cv2
import seaborn as sns
from tqdm import tqdm
from pprint import pprint
import glob
from pydicom.filereader import read_dicomdir
from pydicom.data import get_testdata_files
from os.path import dirname, join
import zipfile
from subprocess import check_output
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

Dataset = "Neurohacking_data-0.0"

# ファイルを解凍し、作業ディレクトリに配置します。
with zipfile.ZipFile("../input/neurohackinginrimages/" + Dataset + ".zip", "r") as z:
    z.extractall(".")

def dcm_to_nifti(input_dir:str,output_dir:str):
    """
    概要
        DICOMファイルからNIfTIファイルを生成
    
    詳細説明
        input_dirの中のDICOMファイルをNIfTIファイルに変換。NIfTIファイルはoutput_dirに生成します。
        output_dirが存在しない場合、ディレクトリを作ります。
    Args:
        input_dir : str 一人分のDICOMファイルが入ったディレクトリのパス
        output_dir : str 生成したNIfTIファイルを入れるディレクトリのパス

    Returns:
        なし

    """
    head_mri_dicom = Path(input_dir)
    output_dir = Path(output_dir)
    
    # 出力ディレクトリが存在しない場合は作成
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    
    dicom2nifti.convert_directory(head_mri_dicom, output_dir)

dcm_to_nifti("Neurohacking_data-0.0/BRAINIX/DICOM/T1","Neurohacking_data-0.0/BRAINIX/NIfTI/T1")

print(check_output(["ls", '-l', "Neurohacking_data-0.0/BRAINIX/NIfTI/T1/"]).decode("utf8"))