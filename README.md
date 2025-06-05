# 🚀 ML-E2E: End-to-End Machine Learning Pipeline with CI/CD and Deployment

This repository showcases a complete machine learning pipeline, encompassing data ingestion, preprocessing, model training, evaluation, and deployment. The project integrates CI/CD practices using GitHub Actions and containerization with Docker, aiming for seamless deployment on AWS EC2 instances.

---

## 📁 Project Structure

```
ML-E2E/
├── .github/workflows/       # CI/CD workflows
├── Network_Data/            # Raw and processed datasets
├── data_schema/             # Data schema definitions
├── final_model/             # Serialized trained models
├── networksecurity/         # Network security configurations
├── pipeline/                # Data processing and ML pipeline scripts
├── templates/               # HTML templates for FastAPI
├── app.py                   # FastAPI application
├── main.py                  # Entry point for training and evaluation
├── push_data_DB.py          # Script to push data to the database
├── test_db_conn.py          # Database connection testing script
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup script
└── .gitignore               # Git ignore rules
```

---

## 🧰 Technologies Used

- **Programming Language**: Python
- **Frameworks**: FastAPI
- **Machine Learning**: scikit-learn, pandas, numpy
- **Database**: PostgreSQL
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Cloud Deployment**: AWS EC2

---

## 🔄 CI/CD Pipeline

- **GitHub Actions**:
  - Automated testing and linting on push and pull requests.
  - Docker image build and push to Docker Hub.
  - Deployment to AWS EC2 upon successful build.

---

## 📊 Model Evaluation Metrics

- **Accuracy**: Evaluates the overall correctness of the model.
- **Precision**: Measures the proportion of positive identifications that were actually correct.
- **Recall**: Measures the proportion of actual positives that were identified correctly.
- **F1 Score**: Harmonic mean of precision and recall.

*Detailed evaluation reports are available in the `final_model/` directory.*

---

## 📌 Future Enhancements

- Integrate MLflow for experiment tracking.
- Implement model versioning.
- Set up monitoring and logging with Prometheus and Grafana.
- Expand the API with additional endpoints for data analysis.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 👤 Author

**Manik Singh**

- GitHub: [@maniksingh10](https://github.com/maniksingh10)
- LinkedIn: [Manik Singh](https://www.linkedin.com/in/maniksingh10/)

  Thanks to Krish Naik
