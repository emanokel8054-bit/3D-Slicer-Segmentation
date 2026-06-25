# segment_threshold.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Segment a structure from a medical image using intensity thresholds
#
# How it works:
#   - You define a minimum and maximum intensity (HU value for CT, signal for MRI)
#   - All voxels within that range get labelled as the segmented structure
#   - Great for bone (CT ~400-3000 HU) or soft tissue (CT ~-100 to 200 HU)

import slicer


def threshold_segmentation(volume_node, segment_name, min_threshold, max_threshold):
    """
    Create a segmentation from a loaded volume using intensity thresholds.

    Parameters:
        volume_node   : The volume node loaded in Slicer (from load_volume.py)
        segment_name  : A label name for the segmented structure e.g. "Bone"
        min_threshold : Minimum intensity value to include
        max_threshold : Maximum intensity value to include

    Returns:
        segmentationNode: The resulting segmentation node
    """

    # Step 1 - Create a new segmentation node in the scene
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)

    # Step 2 - Add a segment (the structure we want to label)
    segmentId = segmentationNode.GetSegmentation().AddEmptySegment(segment_name)

    # Step 3 - Run the threshold effect using the Segment Editor
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volume_node)
    segmentEditorWidget.setCurrentSegmentID(segmentId)

    # Apply the Threshold effect
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold", str(min_threshold))
    effect.setParameter("MaximumThreshold", str(max_threshold))
    effect.self().onApply()

    # Clean up the editor node
    slicer.mrmlScene.RemoveNode(segmentEditorNode)

    print(f"Segmentation complete: '{segment_name}' | Threshold: {min_threshold} to {max_threshold}")
    return segmentationNode


def show_3d_rendering(segmentation_node):
    """Enable 3D surface rendering for a segmentation."""
    segmentation_node.CreateClosedSurfaceRepresentation()
    print("3D rendering enabled. Check the 3D view in Slicer.")


# ----- Common Threshold Ranges (CT in Hounsfield Units) -----
# Bone:         400  to 3000
# Soft tissue: -100  to  200
# Lung:        -1000 to -400
# Fat:          -200 to  -50

# ----- Example Usage -----
# First load a volume, then run:

# volumeNode = slicer.util.loadVolume("/path/to/image.nii.gz")
# seg = threshold_segmentation(volumeNode, "Bone", 400, 3000)
# show_3d_rendering(seg)
