🖥️ Docker Practice: Laptop Price Predictor (ML + Streamlit)
This project is part of my learning journey into Docker. It demonstrates how to containerize a machine learning regression model that predicts laptop prices using a Streamlit app.

📦 Project Overview
🧠 ML Model: Trained using scikit-learn with features like brand, processor, RAM, etc.

🎯 Goal: Predict the price of a laptop based on user input.

🐳 Dockerized: Easily build and run the app in a container.

🖼️ Interface: Built using Streamlit for an interactive UI.

🗂️ Project Structure
bash
Copy
Edit
├── app.py                  # Main Streamlit app
├── Dockerfile              # Docker build instructions
├── requirements.txt        # Python dependencies
├── pipe.pkl                # Preprocessing pipeline
├── df.pkl                  # Dataset/model-related file
├── laptop_data.csv         # Dataset
├── .gitignore
└── README.md
🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Mangesh-Maurya/Docker-Practice-Laptop-Price-Predictor-ML-Streamlit
cd laptop-price-predictor-docker
2. Build the Docker Image
bash
Copy
Edit
docker build -t laptop-predictor .
3. Run the Container
bash
Copy
Edit
docker run -p 8501:8501 laptop-predictor
4. View the App
Open your browser and go to:

arduino
Copy
Edit
http://localhost:8501
🧾 Sample Prediction Screenshot
![Screenshot (51)](https://github.com/user-attachments/assets/ee0a10f4-1936-475e-970f-dd3e3a5d0d94)
![Screenshot (50)](https://github.com/user-attachments/assets/b02ed65d-4da9-4eb2-9e70-65edb07557ea)
![Screenshot (49)](https://github.com/user-attachments/assets/08a2752d-1bbb-44da-a1cc-c21fedb44f2e)
![Screenshot (48)](https://github.com/user-attachments/assets/0f978cad-7012-4e6a-ae4c-41081e734971)
![Screenshot (46)](https://github.com/user-attachments/assets/f8833095-6a63-45f9-8a67-7d12fc46f827)
![Screenshot (45)](https://github.com/user-attachments/assets/ffb9df7b-3778-4a19-8dcd-f1804d03abf8)
![Screenshot (44)](https://github.com/user-attachments/assets/39df8a58-2681-490f-ab45-396703800722)
![Screenshot (43)](https://github.com/user-attachments/assets/42057548-1f98-4cae-8b25-0acc15be606e)


📚 What I Learned
Writing Dockerfiles from scratch

Using COPY, WORKDIR, RUN, and CMD instructions

Containerizing Streamlit apps

Running ML models in isolated environments

🛠️ Tech Stack
Python 3.9

Streamlit

Scikit-learn

Pandas, NumPy

Docker

📌 Future Goals
Add form validation and error handling

Deploy on cloud (Render, Heroku, or AWS)
