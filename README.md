# 🛠️ AeroSound-FaultNet  
**Noise-Robust Acoustic Fault Recognition for Aircraft Engines**

AeroSound-FaultNet is a deep learning pipeline designed to detect and classify **aircraft engine anomalies** from acoustic signatures.  
It leverages **spectrogram-based feature extraction**, **contrastive learning**, and **spectral explainability** to achieve fault detection even under high background noise.  
The model integrates two open datasets — **AeroSonicDB** and **ESC-50** — for realistic, noise-robust training.

---

## 🚀 Overview

Traditional aircraft maintenance relies on scheduled inspections and sensor telemetry.  
AeroSound-FaultNet enables **condition-based monitoring** using only audio — a scalable, low-cost diagnostic method.

### Key Features
- Robust classification of **healthy vs. faulty** engine sounds  
- Noise augmentation using **ESC-50 environmental audio** (10–30 dB SNR)  
- Automated preprocessing pipeline (trimming, normalization, noise injection, split generation)  
- Supports **CNN, YAMNet**, and **Autoencoder** models for supervised or unsupervised learning  
- **Explainability layer** (Grad-CAM) over spectrograms to highlight fault frequencies  

---

## 📦 Datasets

The full datasets are too large (≈ 27 GB+) to host on GitHub.  
Only small sample clips are included for quick testing.  
Use the provided `download_data.sh` script to fetch the complete data automatically.

### 1️⃣ **AeroSonicDB (Aircraft Engine Audio)**
- **Source:** [Kaggle – Audio Dataset of Low-Flying Aircraft (AeroSonicDB)](https://www.kaggle.com/datasets/gray8ed/audio-dataset-of-low-flying-aircraft-aerosonicdb)  
- **Size:** ~27 GB  
- **Description:** Real-world recordings of low-flying aircraft and helicopter engines. Includes various engine types and flight conditions.  
- **Usage:** Core dataset for detecting tonal and vibrational fault patterns.  
- **License:** Free for research/non-commercial use (see Kaggle dataset terms).  

### 2️⃣ **ESC-50 (Environmental Sound Classification)**
- **Source:** [GitHub – ESC-50 by Karol Piczak](https://github.com/karolpiczak/ESC-50)  
- **Size:** ~1.3 GB  
- **Description:** 2,000 labeled 5-second environmental recordings across 50 categories (wind, rain, thunder, machinery, traffic, etc.).  
- **Usage:** Used to simulate realistic environmental noise during training (SNR 30 / 20 / 10 dB) for robustness evaluation.  
- **License:** CC BY 4.0 — open for research and education.  

---

## ⚙️ Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AeroSound-FaultNet.git
cd AeroSound-FaultNet
