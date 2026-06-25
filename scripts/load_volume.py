# load_volume.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Load a NIfTI or DICOM medical image into 3D Slicer

import slicer

def load_nifti_volume(file_path):
    print(f"Loading volume from: {file_path}")
    volumeNode = slicer.util.loadVolume(file_path)
    if volumeNode:
        print(f"Successfully loaded: {volumeNode.GetName()}")
        print(f"Image dimensions: {volumeNode.GetImageData().GetDimensions()}")
    else:
        print("ERROR: Could not load the file. Check the file path.")
    return volumeNode

def load_dicom_folder(folder_path):
    print(f"Importing DICOM from folder: {folder_path}")
    dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser
    dicomBrowser.importDirectory(folder_path, dicomBrowser.ImportDirectoryAddLink)
    dicomBrowser.waitForImportFinished()
    print("DICOM import complete. Open the DICOM browser to load series.")

def reset_field_of_view():
    slicer.util.resetSliceViews()
    print("Slice views reset to fit loaded volume.")

# load_nifti_volume("/path/to/your/image.nii.gz")
# load_dicom_folder("/path/to/your/dicom_folder/")
