import random

def predict_risk(data):
    hr = data["heart_rate"]
    sys = data["bp_systolic"]
    dio = data["bp_diastolic"]
    oxy = data["oxygen"]

    score = 0
    if hr > 120: score += 1
    if sys > 150: score += 1
    if dio > 100: score += 1
    if oxy < 90: score += 1

    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    else:
        return "LOW"
