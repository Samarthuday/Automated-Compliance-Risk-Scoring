# 🚀 Real-Time Compliance Risk Monitoring System

A comprehensive real-time financial transaction monitoring system with AI-powered risk assessment and live dashboard visualization.

## 📁 **Project Structure**

```
Automated-Compliance-Risk-Scoring/
├── src/
│   ├── api/
│   │   └── simple_api_server.py      # Main API server (Flask)
│   ├── dashboard/
│   │   ├── real_time_dashboard.html  # Live monitoring dashboard
│   │   └── serve_dashboard.py        # Dashboard HTTP server
│   ├── utils/
│   │   ├── simple_ingestion.py       # Transaction generator
│   │   ├── start_system.py           # System startup script
│   │   ├── test_ingestion.py         # Testing utility
│   │   └── check_status.py           # Status checker
│   ├── models/
│   │   ├── best_model.pkl            # Trained XGBoost model
│   │   └── model_metadata.pkl        # Model metadata
│   ├── notebooks/
│   │   ├── system.ipynb              # System analysis notebook
│   │   └── Model.ipynb               # Model training notebook
│   └── __init__.py
├── requirements.txt                   # Python dependencies
├── SAML-D.csv                        # Sample transaction data (950MB)
├── .firebaserc                       # Firebase configuration
└── venv/                             # Virtual environment
```

## 🎯 **System Components**

### **1. API Server (`src/simple_api_server.py`)**
- **Flask-based REST API** for transaction processing
- **ML model integration** with XGBoost risk assessment
- **Real-time monitoring** with statistics and alerts
- **Health checks** and system status endpoints
- **Feature engineering** with 18 engineered features
- **Risk level classification** (MINIMAL, LOW, MEDIUM, HIGH)

### **2. Transaction Generator (`simple_ingestion.py`)**
- **Synthetic transaction generation** for testing
- **Realistic transaction patterns** with varying risk levels
- **Continuous data flow** to simulate live environment
- **Configurable generation rates** (2-5 second intervals)
- **Multiple transaction types**: transfer, payment, investment, loan, refund
- **Multi-currency support**: USD, EUR, GBP, JPY, CAD

### **3. Live Dashboard (`real_time_dashboard.html`)**
- **Real-time visualization** of transaction data
- **Interactive charts** using Chart.js
- **Risk distribution** with color-coded indicators
- **Alert management** with filtering options
- **Responsive design** for all devices
- **Modern dark theme** with particle.js animations
- **Live counters** and trend analysis

### **4. Dashboard Server (`serve_dashboard.py`)**
- **Local HTTP server** to serve the dashboard on port 8080
- **CORS handling** for API communication
- **Automatic browser opening**
- **Simple file serving** with proper headers

## 🚀 **Quick Start**

### **Option 1: Automated Startup (Recommended)**
```bash
# Start the entire system with one command
python start_system.py
```

This will:
- ✅ Start the API server on port 5000
- ✅ Start the transaction generator
- ✅ Start the dashboard server on port 8080
- ✅ Open the dashboard in your browser

### **Option 2: Manual Startup**
```bash
# 1. Start the API server
python src/api/simple_api_server.py

# 2. In a new terminal, start the transaction generator
python src/utils/simple_ingestion.py

# 3. In a new terminal, start the dashboard server
python src/dashboard/serve_dashboard.py
```

## 🌐 **Access Points**

- **Dashboard**: http://localhost:8080/real_time_dashboard.html
- **API Server**: http://localhost:5000
- **Health Check**: http://localhost:5000/api/health
- **API Documentation**: Available at runtime

## 📊 **Dashboard Features**

### **Real-Time Monitoring**
- **Live transaction count** with processing rates
- **Risk distribution** (High, Medium, Low, Minimal)
- **System uptime** and health indicators
- **Alert generation** statistics
- **Processing rate** calculations

### **Interactive Elements**
- **Risk Grid** with animated counters
- **Transaction trend chart** with real-time updates
- **Alert filtering** with dropdown controls
- **Manual refresh** button
- **Responsive design** for mobile/desktop

### **Visual Design**
- **Modern dark theme** with gradient backgrounds
- **Particle.js animations** for visual appeal
- **Smooth transitions** and hover effects
- **Professional color scheme** with risk-based coding
- **Glassmorphism effects** with backdrop blur

## 🔌 **API Endpoints**

### **Health & Status**
- `GET /api/health` - System health check
- `GET /api/model/info` - ML model information

### **Transaction Processing**
- `POST /api/process_transaction` - Process individual transactions
- `POST /api/process_bulk` - Process multiple transactions

### **Monitoring & Analytics**
- `GET /api/monitoring/stats` - Real-time statistics
- `GET /api/monitoring/alerts` - Recent alerts
- `GET /api/monitoring/high-risk` - High-risk transactions

## 🤖 **ML Model Details**

### **Model Information**
- **Algorithm**: XGBoost with optimized parameters
- **Threshold**: Configurable risk threshold
- **Features**: 18 engineered features
- **Performance**: Optimized for real-time processing

### **Feature Engineering**
- **Cyclic encoding** for time-based features
- **Hashing** for categorical variables
- **Log transformations** for numerical features
- **Risk-based feature selection**
- **Custom FeatureSelector class** for model compatibility

## 🛠️ **Development & Testing**

### **Testing Utilities**
```bash
# Test the ingestion system
python src/utils/test_ingestion.py

# Check system status
python src/utils/check_status.py
```

### **Manual Testing**
```bash
# Test API health
curl http://localhost:5000/api/health

# Test transaction processing
curl -X POST http://localhost:5000/api/process_transaction \
  -H "Content-Type: application/json" \
  -d '{"transaction_id": "test_001", "amount": 50000, "sender_id": "user1", "receiver_id": "user2", "transaction_type": "transfer", "payment_currency": "USD", "sender_bank_location": "US", "timestamp": "2025-01-13T16:00:00Z"}'
```

## 📈 **System Performance**

### **Real-Time Capabilities**
- **Sub-second response times** for transaction processing
- **Live data updates** every 2-5 seconds
- **Concurrent processing** of multiple transactions
- **Memory-efficient** operations with in-memory storage

### **Scalability Features**
- **Modular architecture** for easy scaling
- **Stateless API design** for load balancing
- **Efficient data structures** for high throughput
- **Configurable processing rates**

## 🔧 **Configuration**

### **Environment Variables**
- `LOG_LEVEL` - Logging level (default: INFO)
- `API_PORT` - API server port (default: 5000)
- `DASHBOARD_PORT` - Dashboard server port (default: 8080)

### **Customization Options**
- **Transaction generation rates** in `src/utils/simple_ingestion.py`
- **Dashboard refresh intervals** in `src/dashboard/real_time_dashboard.html`
- **API timeout settings** in `src/api/simple_api_server.py`
- **Visual themes** in dashboard CSS

## 🚨 **Troubleshooting**

### **Common Issues**

1. **Port Already in Use**
   ```bash
   # Check what's using the port
   netstat -ano | findstr :5000
   # Kill the process or change the port
   ```

2. **Model Loading Errors**
   ```bash
   # Ensure model files exist
   ls -la *.pkl
   # Check file permissions
   ```

3. **Dashboard Not Loading**
   ```bash
   # Check if dashboard server is running
   curl http://localhost:8080
   # Verify CORS settings
   ```

### **Debug Mode**
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python start_system.py
```

## 📚 **Documentation**

- **System Architecture**: See `src/notebooks/system.ipynb`
- **Model Training**: See `src/notebooks/Model.ipynb`
- **API Documentation**: Available at runtime
- **Code Comments**: Comprehensive inline documentation

## 🤝 **Contributing**

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

---

