# Tutorial Walkthrough - Brain MRI Segmentation

This walkthrough takes you from a raw MRI scan to a labelled 3D segmentation, step by step.

We will use the free **MRHead** sample dataset that ships with 3D Slicer.

---

## Part 1 - Load the Image

### Step 1.1 - Open 3D Slicer and load sample data

1. Launch 3D Slicer
2. Go to **File > Download Sample Data**
3. Click **MRHead** - it will download and open automatically
4. You will see the brain MRI appear in the three slice views (Axial, Sagittal, Coronal) and the 3D view

### Step 1.2 - Explore the image

- **Scroll** in any slice view to move through the brain
- **Left-click and drag** to pan
- **Right-click and drag** to zoom
- **Ctrl + scroll** to adjust window/level (brightness and contrast)

---

## Part 2 - Segment the Brain (Threshold Method)

### Step 2.1 - Open the Segment Editor

Go to **Modules dropdown > Segmentation > Segment Editor**

### Step 2.2 - Create a new segmentation

1. Click the **+ Add** button to add a new segment
2. Rename it **Brain** (double-click the name)

### Step 2.3 - Apply threshold segmentation

1. In the Effects panel, click **Threshold**
2. Set the range to approximately **20 to 220** (these values work well for MRHead)
3. Click **Apply**
4. The brain tissue should now be highlighted in the slice views

### Step 2.4 - Clean up with Island effect

1. Click **Islands** in the effects panel
2. Select **Keep largest island**
3. Click **Apply** - this removes small disconnected fragments

---

## Part 3 - View in 3D

### Step 3.1 - Enable 3D rendering

1. In the Segmentations panel (top of Segment Editor), click the **eye icon** next to your segment
2. OR click **Show 3D** button at the top of the Segment Editor

### Step 3.2 - Rotate the 3D view

- **Left-click and drag** in the 3D view to rotate
- **Right-click and drag** to zoom
- **Middle-click and drag** to pan

---

## Part 4 - Export the Result

### Step 4.1 - Export as STL (3D model)

1. Go to **File > Export Data**
2. Select your segmentation node
3. Choose format **STL**
4. Choose an output folder and click **Export**

### Step 4.2 - Export via Python script

Open the Python Interactor and run:

```python
exec(open('/path/to/scripts/export_model.py').read())

# Get the segmentation node from the scene
segNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")

# Export as STL
export_segmentation_as_stl(segNode, "/path/to/output/", file_prefix="brain")

# Export as NIfTI label map
export_segmentation_as_nifti(segNode, volumeNode, "/path/to/output/brain_seg.nii.gz")
```

---

## Part 5 - Try GrowCut (Optional - More Accurate)

For more precise segmentation of complex structures:

1. Open Python Interactor and run:

```python
exec(open('/path/to/scripts/segment_grow_cut.py').read())
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
grow_cut_segmentation(volumeNode)
```

2. In the Segment Editor:
   - Select **Foreground** segment, choose the **Paint** brush, and paint strokes INSIDE the brain
   - Select **Background** segment and paint strokes OUTSIDE the brain (skull, air)
   - Click **Apply** in the GrowCut panel
   - Wait for the algorithm to complete (may take 30-60 seconds)

---

## Summary

You have now:
- Loaded a medical image into 3D Slicer
- Segmented brain tissue using thresholding
- Visualized the result in 3D
- Exported the segmentation as an STL file and NIfTI label map

Take screenshots of your results and save them to the `results/` folder!
