# segment_grow_cut.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Semi-automatic segmentation using the GrowCut algorithm
#
# How it works:
#   - You paint a few "seed" strokes on the target structure and background
#   - GrowCut propagates from those seeds to fill the full structure
#   - More accurate than threshold for complex soft-tissue structures

import slicer


def grow_cut_segmentation(volume_node):
    """
    Set up a GrowCut segmentation with two segments:
      - Segment 1 (Foreground): The structure you want to isolate
      - Segment 2 (Background): Surrounding tissue to exclude

    After running this function:
      1. In the Segment Editor, paint GREEN strokes inside your target structure
      2. Paint RED strokes on the background
      3. Then click "Apply" in the GrowCut effect panel

    Parameters:
        volume_node: The volume node loaded in Slicer
    """

    # Create segmentation node
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)

    # Add foreground and background segments
    seg = segmentationNode.GetSegmentation()
    foregroundId = seg.AddEmptySegment("Foreground")
    backgroundId = seg.AddEmptySegment("Background")

    # Set colors: green for foreground, red for background
    foregroundSegment = seg.GetSegment(foregroundId)
    backgroundSegment = seg.GetSegment(backgroundId)
    foregroundSegment.SetColor(0.0, 1.0, 0.0)  # Green
    backgroundSegment.SetColor(1.0, 0.0, 0.0)  # Red

    # Open the Segment Editor and activate GrowCut
    slicer.util.selectModule("SegmentEditor")
    segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor

    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volume_node)
    segmentEditorWidget.setCurrentSegmentID(foregroundId)
    segmentEditorWidget.setActiveEffectByName("GrowCut")

    print("GrowCut ready.")
    print("NEXT STEPS:")
    print("  1. Select 'Foreground' segment and paint green strokes on your target structure.")
    print("  2. Select 'Background' segment and paint red strokes on surrounding tissue.")
    print("  3. Click 'Apply' in the GrowCut panel.")

    return segmentationNode


# ----- Example Usage -----

# volumeNode = slicer.util.loadVolume("/path/to/image.nii.gz")
# grow_cut_segmentation(volumeNode)
