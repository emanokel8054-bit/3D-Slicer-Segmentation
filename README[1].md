# 3D Slicer Medical Image Segmentation

A beginner-friendly project demonstrating **medical image segmentation** of MRI and CT scans using [3D Slicer](https://www.slicer.org/) and Python scripting.

---

## What This Project Does

This repository shows how to:
- Load DICOM / NIfTI medical images into 3D Slicer
- Segment anatomical structures (e.g. brain, liver, lungs) from MRI and CT scans
- Automate segmentation tasks using 3D Slicer's Python console
- Export segmentation masks and 3D models for visualization

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| [3D Slicer](https://www.slicer.org/) | Medical image viewing and segmentation |
| Python 3 | Scripting and automation inside Slicer |
| NIfTI / DICOM | Standard medical image formats |
| SlicerJupyter (optional) | Notebook-based interaction |

---

## Project Structure

```
3d-slicer-segmentation/
├── scripts/
│   ├── load_volume.py          # Load a medical image into 3D Slicer
│   ├── segment_threshold.py    # Threshold-based segmentation
│   ├── segment_grow_cut.py     # GrowCut semi-automatic segmentation
│   └── export_model.py         # Export segmentation as 3D model (.stl)
├── samples/
│   └── README.md               # Where to download free sample datasets
├── docs/
│   ├── setup.md                # Installation and setup guide
│   └── walkthrough.md          # Step-by-step tutorial with screenshots
├── results/
│   └── README.md               # Folder for your output screenshots/models
└── README.md
```

---

## Getting Started

### 1. Install 3D Slicer
Download the latest stable version from: https://download.slicer.org/

### 2. Clone This Repository
```bash
git clone https://github.com/YOUR_USERNAME/3d-slicer-segmentation.git
cd 3d-slicer-segmentation
```

### 3. Get a Sample Dataset
See [`samples/README.md`](samples/README.md) for free MRI/CT datasets you can use immediately.

### 4. Run a Script
Open 3D Slicer, go to the **Python Console** (View > Python Interactor), and run:
```python
exec(open('/path/to/scripts/load_volume.py').read())
```

---

## Key Concepts Covered

- **Threshold Segmentation** - Isolate structures by pixel intensity range
- **GrowCut Segmentation** - Semi-automatic region growing from seed points
- **3D Rendering** - Visualize segmented anatomy in 3D
- **Model Export** - Save segmentations as `.stl` files for 3D printing or analysis

---

## Sample Results

> Add your own screenshots to the `results/` folder after running the scripts.

---

## Learning Resources

- [3D Slicer Documentation](https://slicer.readthedocs.io/)
- [Slicer Python Scripting Guide](https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html)
- [Free Medical Image Datasets](https://www.cancerimagingarchive.net/)
- [Slicer Community Forum](https://discourse.slicer.org/)

---

## License

MIT License - feel free to use and adapt this project.
