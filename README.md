# 🎬 Sentiment Detection Web App (FastAPI + PyTorch + Frontend)

A full-stack machine learning project that predicts whether a given text (e.g., a movie review) is **positive or negative** using a trained RNN model.

---

## 🚀 Live Demo

* 🌐 **Frontend:** [https://your-frontend-url.com](https://sentiment-analysis-project-self.vercel.app/)
* ⚙️ **Backend API:** [https://your-backend-url.com](https://sentiment-analysis-project-75zy.onrender.com)

---

## 🧠 Features

* 🔍 Real-time sentiment prediction
* ⚡ FastAPI backend for high performance
* 🧠 PyTorch RNN model
* 📝 Text preprocessing using NLTK + TF-IDF
* 🌍 Deployable on cloud platforms

---

## 🧰 Tech Stack

### Backend

* FastAPI
* PyTorch
* Scikit-learn (TF-IDF)
* NLTK

### Frontend

* React (or your framework)
* Tailwind CSS

---

## ⚙️ Backend Setup

### 1. Navigate to backend

```id="6s1xjz"
cd backend
```

### 2. Install dependencies

```id="sxbh3w"
pip install -r requirements.txt
```

### 3. Download NLTK data

```python id="apn9bm"
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 4. Run FastAPI server

```id="v1d2k0"
uvicorn main:app --reload
```

Backend runs on:

```id="z8d7kq"
http://127.0.0.1:8000
```

---

## 🔮 API Endpoint

### POST `/predict`

#### Request

```json id="3e4n0o"
{
  "text": "This movie was amazing!"
}
```

#### Response

```json id="s7j2p9"
{
  "prediction": 1,
  "probability": 0.91
}
```

---

## 🎨 Frontend Setup

```id="9qk2lm"
cd frontend
npm install
npm run dev
```

Frontend runs on:

```id="l3x8pn"
http://localhost:3000
```

---

## 🔗 Connecting Frontend to Backend

Update API URL in your frontend:

```javascript id="7j2mqa"
const API_URL = "https://your-backend-url.com/predict";
```

---

## 🚀 Deployment

### Backend

* Deploy on Render / Railway
* Start command:

```id="8h1zxp"
uvicorn main:app --host 0.0.0.0 --port 10000
```

### Frontend

* Deploy on Vercel / Netlify

---

## ⚠️ Important Notes

* Uses pre-trained TF-IDF vectorizer (`vectorizer.pkl`)
* Do NOT use `fit_transform()` in inference
* Model input shape: `(batch_size, 1, 5000)`

---

## 📈 Future Improvements

* Replace RNN with LSTM/GRU
* Add user authentication
* Improve UI/UX
* Add batch predictions

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
