# segment_threshold.py
# Run this inside the 3D Slicer Python Console (View > Python Interactor)
# Purpose: Segment a structure from a medical image using intensity thresholds

import slicer

def threshold_segmentation(volume_node, segment_name, min_threshold, max_threshold):
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)

    segmentId = segmentationNode.GetSegmentation().AddEmptySegment(segment_name)

    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volume_node)
    segmentEditorWidget.setCurrentSegmentID(segmentId)

    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold", str(min_threshold))
    effect.setParameter("MaximumThreshold", str(max_threshold))
    effect.self().onApply()

    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    print(f"Segmentation complete: '{segment_name}' | Threshold: {min_threshold} to {max_threshold}")
    return segmentationNode

def show_3d_rendering(segmentation_node):
    segmentation_node.CreateClosedSurfaceRepresentation()
    print("3D rendering enabled. Check the 3D view in Slicer.")

# Common CT Threshold Ranges (Hounsfield Units):
# Bone:         400  to 3000
# Soft tissue: -100  to  200
# Lung:        -1000 to -400
# Fat:          -200 to  -50

# Example:
# volumeNode = slicer.util.loadVolume("/path/to/image.nii.gz")
# seg = threshold_segmentation(volumeNode, "Bone", 400, 3000)
# show_3d_rendering(seg)
