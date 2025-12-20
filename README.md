# 🛰️ NASA Nearest Earth Object (NEO)
## End-to-End Machine Learning Operations (MLOps) Project

---

## 📌 Pendahuluan

Proyek ini merupakan implementasi **Machine Learning Operations (MLOps) end-to-end** menggunakan dataset **NASA Nearest Earth Object (NEO)**.  
Tujuan utama proyek adalah membangun sistem Machine Learning yang **reproducible, scalable, dan observable**, sesuai dengan praktik industri modern.

Seluruh pipeline mencakup:

- Version control dan experiment tracking  
- Model development dan hyperparameter tuning  
- Workflow automation (Continuous Integration / CI)  
- Monitoring, logging, dan alerting tingkat lanjut  

---

## 📦 Dataset

Dataset yang digunakan adalah **NASA Nearest Earth Objects (NEO)** yang berisi informasi objek-objek terdekat dengan Bumi dari tahun 1910 hingga 2024. Dataset ini diambil dari sumber terbuka di Kaggle.

📥 **Download dataset:**  
🔗 https://www.kaggle.com/datasets/ivansher/nasa-nearest-earth-objects-1910-2024  

**Deskripsi singkat:**
- Tanggal dan waktu observasi NEO  
- Estimasi ukuran objek  
- Jarak terdekat terhadap Bumi  
- Kecepatan relatif objek  
- Informasi apakah objek diperkirakan berbahaya  

Silakan ekstrak isi dataset ke dalam folder yang sesuai untuk diproses oleh skrip model.

---

## 🧪 Experiment Management & Version Control  
**(Kriteria 1)**

Eksperimen Machine Learning dikelola menggunakan:

- **Git** untuk version control  
- **MLflow** untuk tracking parameter, metrik, dan artifact  
- **DagsHub** sebagai remote MLflow tracking server  

Seluruh eksperimen terdokumentasi dengan baik dan dapat direproduksi secara penuh.

📌 **Repository Eksperimen & Tracking MLflow:**  
🔗 https://github.com/MENSTRUE/Eksperimen_SML_wafa_bila_syaefurokhman.git

---

## 🤖 Model Development & Hyperparameter Tuning  
**(Kriteria 2)**

Model dibangun melalui tahapan berikut:

1. Training model baseline  
2. Evaluasi performa awal  
3. Hyperparameter tuning  
4. Logging model terbaik ke MLflow  

📂 **Folder:** `/Membangun_model`  
📄 **Script utama:**
- `modelling.py`  
- `modelling_tuning.py`  

---

## 🔄 Workflow Automation (Continuous Integration)  
**(Kriteria 3)**

Workflow Machine Learning diautomasi menggunakan **MLflow Projects** untuk memastikan:

- Eksekusi pipeline yang konsisten  
- Reproducibility environment  
- Integrasi dengan Docker image  

📂 **Folder:** `/Workflow-CI`  
📄 **File penting:**
- `MLProject`  
- `conda.yaml`  

📌 **Repository Workflow CI (Terpisah):**  
🔗 https://github.com/MENSTRUE/Workflow-CI.git

---

## 📊 Monitoring, Logging & Alerting (Advanced)  
**(Kriteria 4)**

Sistem monitoring real-time diimplementasikan untuk memantau:

- Performa model inference  
- Kesehatan sistem (CPU & RAM)  
- Kualitas prediksi model  

🛠️ **Stack Monitoring:**
- **Prometheus** sebagai time-series database  
- **Grafana** sebagai visualization dashboard  

📈 **Metrik yang Dimonitor (10):**
- Accuracy  
- Prediction Count  
- Error Rate  
- Request Throughput  
- CPU Usage  
- Memory Usage  
- dan metrik pendukung lainnya  

🚨 **Alerting Rules (3):**
- High Error Rate  
- Low Model Accuracy  
- High CPU Usage  

---

## 🛠️ Teknologi yang Digunakan

- **Python:** 3.10  
- **Machine Learning:** Scikit-Learn, Pandas  
- **MLOps:** MLflow, DagsHub  
- **Monitoring:** Prometheus, Grafana  
- **System Metrics:** Psutil  

---

## 🚀 Menjalankan Sistem Monitoring

```bash
python prometheus_exporter.py
python inference.py
