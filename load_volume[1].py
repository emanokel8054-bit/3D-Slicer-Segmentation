# load_volume.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Load a NIfTI or DICOM medical image into 3D Slicer

import slicer

def load_nifti_volume(file_path):
    """
    Load a NIfTI (.nii or .nii.gz) file into 3D Slicer.

    Parameters:
        file_path (str): Full path to the .nii or .nii.gz file

    Returns:
        volumeNode: The loaded volume node in Slicer's scene
    """
    print(f"Loading volume from: {file_path}")
    volumeNode = slicer.util.loadVolume(file_path)

    if volumeNode:
        print(f"Successfully loaded: {volumeNode.GetName()}")
        print(f"Image dimensions: {volumeNode.GetImageData().GetDimensions()}")
    else:
        print("ERROR: Could not load the file. Check the file path.")

    return volumeNode


def load_dicom_folder(folder_path):
    """
    Load a DICOM series from a folder into 3D Slicer.

    Parameters:
        folder_path (str): Path to the folder containing DICOM (.dcm) files
    """
    print(f"Importing DICOM from folder: {folder_path}")

    # Add the folder to the DICOM database
    dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser
    dicomBrowser.importDirectory(folder_path, dicomBrowser.ImportDirectoryAddLink)
    dicomBrowser.waitForImportFinished()

    print("DICOM import complete. Open the DICOM browser to load series.")


def reset_field_of_view():
    """Fit all slice views to show the loaded volume."""
    slicer.util.resetSliceViews()
    print("Slice views reset to fit loaded volume.")


# ----- Example Usage -----
# Uncomment and edit the path below to run:

# load_nifti_volume("/path/to/your/image.nii.gz")
# load_dicom_folder("/path/to/your/dicom_folder/")
