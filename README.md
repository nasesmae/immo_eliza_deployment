# Price Prediction API and Web Application

![header app](https://github.com/brain8d/immo-eliza-deployment/assets/153182255/7d75faab-5f00-4186-a7f8-4a909134fe76)

## Introduction

This project integrates a machine learning model for predicting property prices, served through a FastAPI application, and facilitated by a user-friendly interface built with Streamlit. It uses an XGBoost model trained on a dataset of property features to estimate prices based on various attributes such as location, type of property, and amenities.

## Repository Structure

- `app.py`: The FastAPI server script to serve the XGBoost model's predictions.
- `prediction.py`: The Streamlit script providing a web interface for interacting with the price prediction model.
- `Dockerfile`: Docker setup for deploying the FastAPI application.
- `XGBoost_artifacts.pkl`: Serialized file containing the trained model and preprocessing tools.
- `requirements.txt`: Python packages required for running the application.



# Property Price Estimation App

## Overview

Property prices serve as a significant economic indicator, influencing various stakeholders such as governments, real estate agents, investors, developers, as well as private buyers and sellers. Our project aims to aid sellers in determining fair property selling prices independently, precisely, and instantly through a user-friendly interface.

## App

Find our app here: https://immo-mermade.streamlit.app/

## Features

- **Independent Evaluation**: Sellers can evaluate their property price without relying on intermediaries.
- **Precision and Reliability**: The app provides precise and reliable price estimations.
- **Instant Evaluation**: Sellers receive property price estimations instantly.
- **User-Friendly Interface**: The interface is designed to be intuitive and easy to use.

## Objective

Our objective is to provide a reliable price estimation based on the most impactful property features of the real estate market. These features are identified through robust data collection and analysis, and the estimations are generated using a machine learning model (XGBoost).

## Future Development

In the future, we plan to integrate statistical information on the real estate market to enhance the usefulness of the app for a wider audience.

## Follow Us

Stay informed about our project's updates and developments by following us on [GitHub](https://github.com/brain8d/immo-eliza-deployment).

## About

This project was developed by

