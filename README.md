# Price Prediction API and Web Application

![header app](img src="https://raw.githubusercontent.com/nasesmae/immo_eliza_deployment/main/streamlit/images/header.webp" alt="header app" width="400"/)

## Introduction

This project integrates a machine learning model for predicting property prices, served through a FastAPI application, and facilitated by a user-friendly interface built with Streamlit. It uses an XGBoost model trained on a dataset of property features to estimate prices based on various attributes such as location, type of property, and amenities.

## Repository Structure

- `app.py`: The FastAPI server script to serve the XGBoost model's predictions.
- `prediction.py`: The Streamlit script providing a web interface for interacting with the price prediction model.
- `Dockerfile`: Docker setup for deploying the FastAPI application.
- `XGBoost_artifacts.pkl`: Serialized file containing the trained model and preprocessing tools.
- `requirements.txt`: Python packages required for running the application.

## App
https://immo-eliza-deployment-xzpq.onrender.com/predict
https://price-prediction-property.streamlit.app

## Features

- **Independent Evaluation**: Sellers can evaluate their property price without relying agencies. 
- **Precision and Reliability**: The app provides precise and reliable price estimations.
- **User-Friendly Interface**: The interface is designed to be easy to use.

## Usage
**FastAPI Endpoints**:
- "/": A simple GET request to verify the API is operational.
- "/predict": A POST request endpoint for submitting property features and receiving a price prediction.

**Streamlit Web Interface**:
The web interface allows users to easily input property features and obtain price predictions without directly interacting with the API.

## About
This project was developed by Nasrin Esmaeilian: https://github.com/nasesmae


