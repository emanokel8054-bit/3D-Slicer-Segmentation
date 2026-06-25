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

3D Slicer has Python built in - you do not need to install Python separately.

1. Open 3D Slicer
2. Go to **View > Python Interactor**
3. In the console at the bottom, type:
   ```python
   print("Hello from Slicer!")
   ```
4. You should see the output printed - Python is working.

---

## Step 3 - Clone This Repository

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux):

```bash
git clone https://github.com/YOUR_USERNAME/3d-slicer-segmentation.git
cd 3d-slicer-segmentation
```

If you do not have Git installed, you can also click **Code > Download ZIP** on GitHub.

---

## Step 4 - Download a Sample Dataset

See [`../samples/README.md`](../samples/README.md) for free datasets.

The easiest option: open Slicer and go to **File > Download Sample Data > MRHead**.

---

## Step 5 - Run Your First Script

1. Open 3D Slicer
2. Open the Python Interactor (View > Python Interactor)
3. Run the load script:

```python
exec(open('/full/path/to/scripts/load_volume.py').read())
volumeNode = load_nifti_volume('/full/path/to/MRHead.nii.gz')
```

4. You should see the MRI brain appear in all four views.

---

## Optional - Install SlicerJupyter

SlicerJupyter lets you run Slicer Python code in a Jupyter notebook interface.

1. In Slicer, open the **Extensions Manager** (View > Extensions Manager)
2. Search for **SlicerJupyter**
3. Install it and restart Slicer
4. Go to **JupyterKernel module** and click "Start Jupyter Server"
