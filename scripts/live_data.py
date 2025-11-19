import pandas as pd
import numpy as np
import time
import random

names = ["Ravi", "Anita", "Suresh", "Priya", "Aman", "Kavya", "Rahul"]
hospitals = ["Apollo", "Yashoda", "KIMS", "CARE", "NIMS"]

cities = [
    "Hyderabad", "Warangal", "Karimnagar", "Nizamabad", "Khammam",
    "Nalgonda", "Mahabubnagar", "Adilabad", "Siddipet", "Sangareddy",
    "Jagitial", "Mancherial", "Vikarabad", "Wanaparthy", "Suryapet"
]

while True:
    row = {
        "patient_id": random.randint(1000, 9999),
        "name": random.choice(names),
        "age": np.random.randint(20, 85),
        "gender": np.random.choice(["M", "F"]),
        "hospital": random.choice(hospitals),
        "city": random.choice(cities),
        "heart_rate": np.random.randint(60, 150),
        "bp_systolic": np.random.randint(110, 180),
        "bp_diastolic": np.random.randint(60, 120),
        "oxygen": np.random.randint(85, 100)
    }

    df = pd.DataFrame([row])
    df.to_csv("data/live_patient.csv", index=False)

    print("Updated:", row)
    time.sleep(2)
