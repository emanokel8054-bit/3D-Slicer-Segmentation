# Tutorial Walkthrough - Brain MRI Segmentation

This walkthrough takes you from a raw MRI scan to a labelled 3D segmentation step by step.
We will use the free MRHead sample dataset that ships with 3D Slicer.

---

## Part 1 - Load the Image

1. Launch 3D Slicer
2. Go to **File > Download Sample Data**
3. Click **MRHead** - it downloads and opens automatically
4. You will see the brain MRI appear in three slice views and the 3D view

---

## Part 2 - Segment the Brain

1. Go to **Modules > Segmentation > Segment Editor**
2. Click **+ Add** to add a new segment, rename it **Brain**
3. Click **Threshold** in the Effects panel
4. Set range to **20 to 220**
5. Click **Apply**
6. Click **Islands** > **Keep largest island** > **Apply**

---

## Part 3 - View in 3D

1. Click the **eye icon** next to your segment in the panel
2. Rotate in the 3D view by left-click dragging

---

## Part 4 - Export the Result

Open the Python Interactor and run:

```python
exec(open('/path/to/scripts/export_model.py').read())
segNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
export_segmentation_as_stl(segNode, "/path/to/output/", file_prefix="brain")
```

---

## Part 5 - Try GrowCut (Optional)

```python
exec(open('/path/to/scripts/segment_grow_cut.py').read())
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
grow_cut_segmentation(volumeNode)
```

Then in the Segment Editor:
- Paint **green strokes** inside the brain (Foreground)
- Paint **red strokes** outside the brain (Background)
- Click **Apply** and wait 30-60 seconds
