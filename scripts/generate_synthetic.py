import pandas as pd
import numpy as np
import os
from faker import Faker

fake = Faker()
os.makedirs("data", exist_ok=True)
np.random.seed(42)

def generate_node_csv(node_id, n=500):
    rows = []
    for i in range(n):
        patient_id = f"N{node_id}_{i:05d}"
        age = np.random.randint(20, 90)
        sex = np.random.choice(["M", "F"])
        hr_mean = np.clip(np.random.normal(80, 12), 40, 180)
        spo2_mean = np.clip(np.random.normal(97, 2), 70, 100)
        bp_sys = np.clip(np.random.normal(125, 15), 80, 220)
        creatinine = np.round(np.random.normal(1.0, 0.4), 2)
        wbc = int(np.clip(np.random.normal(8, 3), 1, 30))
        diabetes = np.random.choice([0, 1], p=[0.8, 0.2])
        hypertension = np.random.choice([0, 1], p=[0.6, 0.4])
        risk_score = (age / 90) + (hr_mean - 60) / 120 + diabetes * 0.2 + hypertension * 0.15
        readmit_30 = int(risk_score > 0.8)
        notes = fake.sentence(nb_words=12)

        rows.append({
            "patient_id": patient_id,
            "age": age,
            "sex": sex,
            "hr_mean": round(hr_mean, 1),
            "spo2_mean": round(spo2_mean, 1),
            "bp_sys": round(bp_sys, 1),
            "creatinine": creatinine,
            "wbc": wbc,
            "diabetes": diabetes,
            "hypertension": hypertension,
            "readmit_30": readmit_30,
            "clinical_notes": notes
        })
    return pd.DataFrame(rows)

for node in [1, 2, 3]:
    df = generate_node_csv(node, n=400)
    path = f"data/node{node}.csv"
    df.to_csv(path, index=False)
    print("Created:", path)
