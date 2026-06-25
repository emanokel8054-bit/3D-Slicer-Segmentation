# Setup Guide

## Step 1 - Install 3D Slicer

1. Go to https://download.slicer.org/
2. Download the **Stable Release** for your operating system (Windows, macOS, or Linux)
3. Install it like any normal application

**Minimum requirements:**
- 4 GB RAM (8 GB recommended)
- OpenGL-capable graphics card
- Windows 10 / macOS 10.13+ / Ubuntu 18.04+

---

## Step 2 - Verify Python Works in Slicer

1. Open 3D Slicer
2. Go to **View > Python Interactor**
3. In the console at the bottom, type:
```python
   print("Hello from Slicer!")
```
4. You should see the output printed - Python is working.

---

## Step 3 - Clone This Repository

```bash
git clone https://github.com/emanokel8054-bit/3D-Slicer-Segmentation.git
```

Or click **Code > Download ZIP** on GitHub.

---

## Step 4 - Download a Sample Dataset

See `samples/README.md` for free datasets.

The easiest option: open Slicer and go to **File > Download Sample Data > MRHead**.

---

## Step 5 - Run Your First Script

1. Open 3D Slicer
2. Open the Python Interactor (View > Python Interactor)
3. Run:

```python
exec(open('/full/path/to/scripts/load_volume.py').read())
volumeNode = load_nifti_volume('/full/path/to/MRHead.nii.gz')
```

You should see the MRI brain appear in all four views.
