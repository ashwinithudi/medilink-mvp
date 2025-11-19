from flask import Flask, jsonify
import random
import time
import hashlib

app = Flask(__name__)

# ---------------------------------------
# 🔹 Blockchain (Simple Implementation)
# ---------------------------------------
blockchain = []

def create_block(data):
    block = {
        "index": len(blockchain) + 1,
        "timestamp": time.time(),
        "data": data,
        "prev_hash": blockchain[-1]["hash"] if blockchain else "0"
    }
    block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
    blockchain.append(block)

# ---------------------------------------
# 🔹 Generate Fake Patient Data
# ---------------------------------------
cities = ["Karimnagar", "Warangal", "Nalgonda", "Khammam", "Hyderabad"]
hospitals = ["Yashoda", "Apollo", "KIMS", "Sunshine", "Care"]
names = ["Aditya", "Varun", "Pooja", "Aman", "Rohit", "Kiran", "Sita"]

def generate_patient():
    return {
        "age": random.randint(20, 80),
        "bp_diastolic": random.randint(70, 120),
        "bp_systolic": random.randint(120, 180),
        "city": random.choice(cities),
        "gender": random.choice(["M", "F"]),
        "heart_rate": random.randint(60, 160),
        "hospital": random.choice(hospitals),
        "name": random.choice(names),
        "oxygen": random.randint(85, 100),
        "patient_id": random.randint(1000, 9000)
    }

# ---------------------------------------
# 🔹 Simple ML Risk Logic
# ---------------------------------------
def predict_risk(patient):
    score = 0
    if patient["heart_rate"] > 140: score += 1
    if patient["bp_systolic"] > 160: score += 1
    if patient["oxygen"] < 92: score += 1
    if patient["age"] > 60: score += 1

    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    else:
        return "LOW"

# ---------------------------------------
# 🔹 API ROUTES
# ---------------------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "MediLink Backend Running"})

# ---------------------------------------
# 🔥 FIXED LIVE API (returns LIST of 10 patients)
# ---------------------------------------
@app.route("/live", methods=["GET"])
def live_api():
    patients = []

    for _ in range(10):
        patient = generate_patient()
        risk = predict_risk(patient)

        # Add to blockchain
        create_block({"patient": patient, "risk": risk})

        patients.append({
            "patient": patient,
            "predicted_risk": risk
        })

    return jsonify(patients)   # IMPORTANT: returning a LIST

# ---------------------------------------
# Blockchain length
# ---------------------------------------
@app.route("/chain", methods=["GET"])
def chain():
    return jsonify({"length": len(blockchain)})

# ---------------------------------------
# RUN SERVER
# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
