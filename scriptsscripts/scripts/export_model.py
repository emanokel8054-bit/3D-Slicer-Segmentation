# export_model.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Export a completed segmentation as a 3D model (.stl or .nii.gz)

import slicer
import os

def export_segmentation_as_stl(segmentation_node, output_folder, file_prefix="segmentation"):
    os.makedirs(output_folder, exist_ok=True)
    segmentation_node.CreateClosedSurfaceRepresentation()

    seg = segmentation_node.GetSegmentation()
    num_segments = seg.GetNumberOfSegments()

    print(f"Exporting {num_segments} segment(s) to: {output_folder}")

    for i in range(num_segments):
        segmentId = seg.GetNthSegmentID(i)
        segmentName = seg.GetSegment(segmentId).GetName()
        safe_name = segmentName.replace(" ", "_")
        output_path = os.path.join(output_folder, f"{file_prefix}_{safe_name}.stl")

        slicer.util.exportNode(
            segmentation_node,
            output_path,
            {"fileType": "STL", "segmentIds": segmentId}
        )
        print(f"  Exported: {output_path}")

    print("Export complete.")


def export_segmentation_as_nifti(segmentation_node, volume_node, output_path):
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(
        segmentation_node, labelmapVolumeNode, volume_node
    )
    slicer.util.exportNode(labelmapVolumeNode, output_path)
    print(f"Label map exported to: {output_path}")
    slicer.mrmlScene.RemoveNode(labelmapVolumeNode)

# Example:
# export_segmentation_as_stl(seg, "/path/to/output/", file_prefix="brain")
# export_segmentation_as_nifti(seg, volumeNode, "/path/to/output/brain_seg.nii.gz")
