# 🌿 Plant Species Identifier

A deep learning-powered web application that identifies plant species based on leaf images. Built using Python, Flask, and PyTorch, the model classifies 10 native Indian plant species and provides detailed botanical descriptions.

---

## 🚀 Features

- 🔍 **Image-based classification** using a custom-trained CNN model
- 🧠 **PyTorch-powered ResNet18 architecture**
- 🌱 Identifies **10 Indian plant species** from leaf images
- 🧾 Returns **scientific name and ecological description**
- 📸 Simple web interface for uploading leaf images
- ⚡ Real-time prediction with Flask backend

---

## 🖼️ Example Classes

- Apta *(Bauhinia racemosa)*
- Indian Rubber Tree *(Ficus elastica)*
- Karanj *(Pongamia pinnata)*
- Kashid *(Cassia fistula)*
- Nilgiri *(Eucalyptus globulus)*
- Pimpal *(Ficus religiosa)*
- Sita Ashok *(Saraca asoca)*
- Sonmohar *(Peltophorum pterocarpum)*
- Vad *(Ficus benghalensis)*
- Vilayati Chinch *(Pithecellobium dulce)*

---

## 📂 Project Structure
plant-identifier/
│
├── app.py # Flask app entry point
├── model.py # Model loading & prediction logic
├── utils.py # Species descriptions and helper functions
├── requirements.txt # Python dependencies
│
├── Models/
│ └── best_leaf_cnn_model.pt # Trained PyTorch model
│
├── templates/
│ ├── index.html # Upload form UI
│ └── display.html # Prediction results page
│
├── static/
│ ├── styles/
│ │ └── style.css # Custom CSS styles
│ └── images/
│ └── 4.jpg # Background & UI images
