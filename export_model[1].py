# export_model.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Export a completed segmentation as a 3D model (.stl or .obj)
#          suitable for 3D printing, analysis, or sharing

import slicer
import os


def export_segmentation_as_stl(segmentation_node, output_folder, file_prefix="segmentation"):
    """
    Export each segment in a segmentation node as a separate .stl file.

    Parameters:
        segmentation_node : The segmentation node to export
        output_folder     : Path to the folder where .stl files will be saved
        file_prefix       : Prefix for the output filenames (default: "segmentation")
    """

    # Make sure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Ensure the segmentation has a closed surface representation
    segmentation_node.CreateClosedSurfaceRepresentation()

    seg = segmentation_node.GetSegmentation()
    num_segments = seg.GetNumberOfSegments()

    print(f"Exporting {num_segments} segment(s) to: {output_folder}")

    for i in range(num_segments):
        segmentId = seg.GetNthSegmentID(i)
        segmentName = seg.GetSegment(segmentId).GetName()

        # Build the output path
        safe_name = segmentName.replace(" ", "_")
        output_path = os.path.join(output_folder, f"{file_prefix}_{safe_name}.stl")

        # Export as STL
        slicer.util.exportNode(
            segmentation_node,
            output_path,
            {"fileType": "STL", "segmentIds": segmentId}
        )

        print(f"  Exported: {output_path}")

    print("Export complete.")


def export_segmentation_as_nifti(segmentation_node, volume_node, output_path):
    """
    Export a segmentation as a NIfTI label map (.nii.gz).
    Useful for sharing with other tools (ITK-SNAP, FSL, etc.)

    Parameters:
        segmentation_node : The segmentation node
        volume_node       : The reference volume (sets geometry of output)
        output_path       : Full path for the output .nii.gz file
    """

    # Convert segmentation to a label map volume
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(
        segmentation_node, labelmapVolumeNode, volume_node
    )

    # Save to NIfTI
    slicer.util.exportNode(labelmapVolumeNode, output_path)
    print(f"Label map exported to: {output_path}")

    # Clean up temporary node
    slicer.mrmlScene.RemoveNode(labelmapVolumeNode)


# ----- Example Usage -----

# Export as STL (3D model):
# export_segmentation_as_stl(seg, "/path/to/output/folder/", file_prefix="brain")

# Export as NIfTI label map:
# export_segmentation_as_nifti(seg, volumeNode, "/path/to/output/segmentation.nii.gz")
