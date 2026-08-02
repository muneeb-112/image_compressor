# image_compressor
# Smart Image Compressor (Dynamic Target Sizing)

## 📌 Project Overview
Web applications, machine learning pipelines, and storage architectures often require images to fit strict file size constraints (KB/MB) without completely destroying visual quality. Standard compression tools only offer static quality scales (1-100), making it a guessing game to reach a specific target size.

This project implements a **Smart Image Compressor** built with **Python**, **Pillow**, and **Streamlit**. It solves the sizing dilemma by using a dynamic **Binary Search Algorithm** to iteratively adjust compression levels until the output image matches the exact target file size (KB/MB) requested by the user.

---

## 🚀 Key Features
* **Adaptive Sizing Control**: Users can input their desired maximum file size in either **KB** or **MB** formats.
* **Intelligent Optimization Loop**: Leverages a fast binary search layout to calculate the most optimal quality bit-rate within 7 computational rounds.
* **Format-Aware Processing**: Seamlessly handles RGBA (transparent PNG) channel conversions to RGB JPEG without breaking metadata.
* **Side-by-Side Visual Anchor**: Live comparison dashboard showcasing the original image vs. the optimized compressed variant along with real-time metrics.
* **Instant Native Downloader**: Pure memory buffer implementation (`io.BytesIO`) that lets users download the compressed output instantly without writing temporary cache files to disk.

---

## 🛠️ Architecture & Algorithm Design
The underlying automation bypasses standard trial-and-error by implementing a search bounds system:

```python
low, high = 1, 95
# Iteratively tests the midpoint quality to find the threshold closest 
# to the user's targeted byte-size constraint.
for _ in range(7):
    mid = (low + high) // 2
    # Compresses to an in-memory buffer to verify current size
```
This ensures high-speed execution and ensures the user always gets the highest possible image quality that safely fits their specified target storage limit.

---

## 📦 Local Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment (Streamlit Community Cloud)
This application is fully production-ready and configured for instant deployment on the **Streamlit Community Cloud**. It relies on `requirements.txt` to safely spin up the headless environment and expose the public link for production web use.
