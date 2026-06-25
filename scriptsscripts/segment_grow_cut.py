# segment_grow_cut.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Semi-automatic segmentation using the GrowCut algorithm

import slicer

def grow_cut_segmentation(volume_node):
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)

    seg = segmentationNode.GetSegmentation()
    foregroundId = seg.AddEmptySegment("Foreground")
    backgroundId = seg.AddEmptySegment("Background")

    foregroundSegment = seg.GetSegment(foregroundId)
    backgroundSegment = seg.GetSegment(backgroundId)
    foregroundSegment.SetColor(0.0, 1.0, 0.0)  # Green
    backgroundSegment.SetColor(1.0, 0.0, 0.0)  # Red

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
    print("  1. Select Foreground segment and paint green strokes on your target structure.")
    print("  2. Select Background segment and paint red strokes on surrounding tissue.")
    print("  3. Click Apply in the GrowCut panel.")

    return segmentationNode

# Example:
# volumeNode = slicer.util.loadVolume("/path/to/image.nii.gz")
# grow_cut_segmentation(volumeNode)
