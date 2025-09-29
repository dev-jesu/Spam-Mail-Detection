# 🔒 AI-Powered Spam Mail Detection System

A modern web application powered by machine learning to detect spam emails with high accuracy using Logistic Regression algorithm. This is a complete full-stack implementation with FastAPI backend and React frontend.

![Spam Detection](https://img.shields.io/badge/ML-Logistic%20Regression-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![React](https://img.shields.io/badge/Frontend-React-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)

## 🌟 Features

- **🎯 High Accuracy**: 96.58% accuracy in spam detection
- **⚡ Real-time Analysis**: Instant email analysis and classification
- **📊 Data Visualization**: Interactive charts showing dataset statistics and model performance
- **🎨 Modern UI/UX**: Beautiful, responsive design with professional styling
- **📱 Mobile Friendly**: Optimized for desktop, tablet, and mobile devices
- **🔧 Easy Setup**: Simple installation and configuration process

## 📊 Model Performance

- **Total Dataset**: 517,401 emails
- **Ham (Legitimate)**: 312,770 emails
- **Spam**: 204,631 emails
- **Accuracy**: 96.58%
- **Precision**: 98.41%
- **Recall**: 92.86%
- **F1-Score**: 95.55%

## 🚀 Live Demo

[Try the live demo here!](#)

## 📸 Screenshots

### Homepage - Spam Detection Interface
![Homepage](docs/screenshots/homepage.png)

### Analytics - Model Performance Dashboard
![Analytics](docs/screenshots/analytics.png)

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **FastAPI** - Modern, fast web framework
- **Scikit-learn** - Machine learning library
- **NLTK** - Natural language processing
- **Joblib** - Model serialization
- **Uvicorn** - ASGI server

### Frontend
- **React 18**
- **React Router** - Client-side routing
- **Recharts** - Data visualization
- **React Icons** - Icon library
- **Axios** - HTTP client

### Machine Learning
- **Logistic Regression** - Two-layer classification
- **TF-IDF Vectorization** - Text feature extraction
- **Preprocessing Pipeline** - Text cleaning and normalization

## 📁 Project Structure

```
spam-mail-detection/
├── backend/
│   ├── models/                 # Trained ML models
│   │   ├── layer1_logreg_model.pkl
│   │   ├── layer2_logreg_model.pkl
│   │   ├── vectorizer_layer1.pkl
│   │   └── vectorizer_layer2.pkl
│   ├── main.py                # FastAPI application
│   ├── utils.py               # Text preprocessing utilities
│   ├── requirements.txt       # Python dependencies
│   └── venv/                  # Virtual environment
├── frontend/
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── App.js            # Main App component
│   │   └── App.css           # Styles
│   ├── package.json          # Node.js dependencies
│   └── package-lock.json
├── .gitignore                # Git ignore rules
├── env.example               # Environment variables template
└── README.md                # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spam-mail-detection.git
   cd spam-mail-detection
   ```

2. **Setup Environment Variables**
   ```bash
   cp env.example .env
   # Modify .env with your configuration
   ```

3. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

4. **Model Files**
   
   ✅ **Ready to use**: The trained ML model files are included in the repository (total size: ~0.5MB):
   
   - `layer1_logreg_model.pkl` (~40KB) - Binary classification (Ham vs Others)
   - `layer2_logreg_model.pkl` (~157KB) - Spam type classification  
   - `vectorizer_layer1.pkl` (~184KB) - TF-IDF vectorizer for layer 1
   - `vectorizer_layer2.pkl` (~183KB) - TF-IDF vectorizer for layer 2
   
   No additional downloads required!

5. **Setup Frontend**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

2. **Start the Frontend Development Server**
   ```bash
   cd frontend
   npm start
   ```

3. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://127.0.0.1:8000
   - API Documentation: http://127.0.0.1:8000/docs

## 📖 API Documentation

### Endpoints

- `GET /` - Health check endpoint
- `POST /predict` - Analyze email for spam detection
- `GET /stats` - Get dataset statistics and model metrics

### Request/Response Examples

#### Predict Spam
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"message": "You have won $1000! Click here to claim now!"}'
```

Response:
```json
{
  "label": "Spam",
  "spam_type": "promotional",
  "confidence": "High Risk"
}
```

#### Get Statistics
```bash
curl "http://127.0.0.0:8000/stats"
```

## 🔧 Development

### Backend Development

1. **Virtual Environment Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Running Tests**
   ```bash
   # Add test commands here
   pytest tests/
   ```

### Frontend Development

1. **Development Mode**
   ```bash
   cd frontend
   npm install
   npm start
   ```

2. **Building for Production**
   ```bash
   npm run build
   ```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset sourced from public email corpora
- Scikit-learn team for excellent ML tools
- FastAPI developers for the amazing framework
- React team for the robust frontend library

## 📞 Support

If you have any questions or need help:

- 📧 Email: your.email@example.com
- 💬 Issues: [GitHub Issues](https://github.com/yourusername/spam-mail-detection/issues)
- 📖 Documentation: [Wiki](https://github.com/yourusername/spam-mail-detection/wiki)

## 🗺️ Future Enhancements

- [ ] User authentication and personal history
- [ ] Advanced spam filtering rules
- [ ] Email pattern learning
- [ ] API rate limiting and security
- [ ] Docker containerization
- [ ] Database integration for history storage

---


