# Synthetic Heart Rate Dataset for Triage Simulation

This dataset contains simulated heart rate (HR) values for 1,000 virtual patients. It is intended for research and development of automated triage systems, particularly those using machine learning to detect anomalies or classify patient criticality based on HR alone.

## Dataset Description

- `patient_id`: Unique identifier for each synthetic patient
- `hr_clean`: Baseline HR sampled uniformly between 30–150 bpm
- `hr_noisy`: HR with Gaussian noise added (σ = 3 bpm) to simulate wearable sensor jitter

## Generation Method

The dataset was generated using NumPy to create uniformly distributed HR values and add Gaussian noise. It was saved to CSV using pandas.

## Usage

This dataset can be used for:
- Simulating emergency triage conditions
- Testing ML classification or fuzzy logic models for HR-based self-tagging
- Evaluating signal noise robustness

## License

This dataset is released under the CC BY 4.0 license. Please cite the original methodology source:

> Oliveira, R. C., Costa, C. A., Lima, C. D. S., & Silva, F. A. (2016). A fuzzy decision support system for health triage. *Expert Systems with Applications*, 45, 100–107. https://doi.org/10.1016/j.eswa.2015.09.039
