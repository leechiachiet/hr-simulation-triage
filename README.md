# 🫀 Real-Time Heart Rate Anomaly Detection for Mass Casualty Triage  
### A Machine Learning and Fuzzy Logic Hybrid Approach

---

## 📖 Project Overview

This repository supports the research dissertation **"Real-Time Heart Rate Anomaly Detection for Mass Casualty Triage — A Machine Learning Approach"**  
conducted as part of the **Master of Science (Data Science)** program at **Universiti Teknologi PETRONAS (UTP)**.

The project aims to design a **real-time intelligent triage system** capable of detecting abnormal heart rate (HR) patterns during **mass casualty incidents (MCI)** using a **hybrid Fuzzy Logic + Machine Learning (ML)** model.  
A custom **synthetic heart rate dataset** was developed to complement publicly available datasets (MIMIC-IV and PPG-Dalia) for model training and evaluation.

---

## 🧬 Dataset Description

### Hybrid Dataset Component
1. **Synthetic HR Dataset (Lee, 2025)** — Simulated vital signs for 1,000 patients based on the START triage system

The synthetic dataset is generated following the framework of **Ullah et al. (2013)**,  
_"Towards automated self-tagging in emergency health cases,"_  
*International Journal of Distributed Sensor Networks*, 9(9), 1–11.  
Heart rate values are sampled using Gaussian distributions representing four triage classes.

| Triage Category | Label | Description | Typical HR Range (bpm) |
|-----------------|--------|-------------|-------------------------|
| Immediate | Red | Critical (life-threatening) | >130 or <40 |
| Delayed | Yellow | Serious but stable | 110–130 |
| Minor | Green | Stable, walking wounded | 60–110 |
| Deceased | Black | No pulse or unresponsive | <30 |

---

## ⚙️ Synthetic Dataset Generator

### 📁 File: `generate_synthetic_hr_dataset.py`
This script creates a **synthetic heart rate triage dataset** for 1,000 virtual patients,  
introducing Gaussian noise to emulate sensor jitter and timestamped readings for time-series analysis.

#### Key Features
- 1,000 synthetic patient records  
- Four triage classes based on START protocol  
- Gaussian noise (σ = 3 bpm) for realism  
- Timestamped data at 1-second intervals  
- Output format: CSV (`synthetic_hr_triage_dataset.csv`)

#### Example Output
| Patient_ID | Heart_Rate_bpm | Triage_Level | Timestamp |
|-------------|----------------|---------------|------------|
| 1 | 148.5 | Immediate | 2025-01-01 00:00:00 |
| 2 | 142.1 | Immediate | 2025-01-01 00:00:01 |
| 3 | 150.3 | Immediate | 2025-01-01 00:00:02 |

---
