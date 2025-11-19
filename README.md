🧠 MediLink — Borderless AI Health Network (MVP)

AI-powered real-time cross-hospital patient monitoring with ML risk prediction, Federated Learning, and Blockchain-based data integrity.

🚑 Problem Overview

Hospitals work in isolation, causing delays in emergency responses.

Real-time vitals and early-risk detection systems are missing.

Medical data is not securely shared or trustable across hospitals.

💡 Solution Overview

MediLink provides a unified AI-driven platform that:

Streams real-time vitals from multiple hospitals

Predicts patient risk using MLPClassifier (ML model)

Uses Federated Learning to train models without sharing data

Ensures tamper-proof records using Blockchain

Displays everything on a Streamlit dashboard

🏗 System Architecture

(Add your HD architecture image here after uploading)

<img width="1213" height="478" alt="Screenshot 2025-11-19 220742" src="https://github.com/user-attachments/assets/5d666d29-982d-4752-ba57-cd9e7aca961b" />


⚙️ Features

🔴 Real-time IoT vitals simulation

🤖 ML-based risk prediction

🔐 Federated Learning (FedAvg)

🔗 Blockchain integrity verification

📡 Flask REST API for data exchange

📊 Streamlit dashboard (auto-refresh every 5s)

🚨 High-risk alerts

🧰 Tech Stack

Backend: Flask, Python, Pandas, NumPy
AI: Scikit-Learn (MLP), Federated Learning
Security: Blockchain Layer
Frontend: Streamlit
Other: Git, VS Code

📁 Folder Structure
medilink-mvp/
│── api/
│── data/
│── models/
│── scripts/
│── dashboard.py
│── app.py
│── requirements.txt
│── README.md

▶️ How to Run
1. Create a virtual environment
python -m venv venv

venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Start Flask API
python app.py


API runs at: http://localhost:5000

4. Start Streamlit Dashboard
streamlit run dashboard.py


Dashboard: http://localhost:8505

<img width="1919" height="850" alt="Screenshot 2025-11-19 223500" src="https://github.com/user-attachments/assets/915858e0-78f0-4720-a86a-2c597d942498" />
<img width="546" height="338" alt="Screenshot 2025-11-19 223911" src="https://github.com/user-attachments/assets/2a088313-3504-4ef1-8ba9-5a6d88f9e13c" />



🚀 Future Enhancements

Real IoT device integration

Cloud deployment

Doctor mobile app

Smart diagnosis assistance

👩‍💻 Developer

Ashwini Thudi
GitHub: https://github.com/ashwinithudi

LinkedIn: https://www.linkedin.com/in/ashwini-thudi

⭐ Star this repo if you found it useful!
