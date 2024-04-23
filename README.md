# Linear Regression Web Service

## Overview
This project implements a linear regression model in a web application to predict outcomes based on input data. The application is written in Python and uses Flask as the web framework. A Jupyter notebook (`Linear Regression ML Implementation.ipynb`) is included to illustrate the model's development and testing process.


## Structure
- `app.py`: The Flask application entry point.
- `requirements.txt`: The required Python libraries for running the application.
- `Linear Regression ML Implementation.ipynb`: Jupyter notebook with the model training and testing process.
- `regmodel.pkl` & `scaling.pkl`: Serialized versions of the trained regression model and scaling object.
- `static/`: Folder containing static files like CSS and JavaScript for the web interface.
- `templates/`: HTML templates for the web interface.
- `Dockerfile`: Definitions for building a Docker container for the application.

## Getting Started
To get this web service running on your machine, follow these steps:

### Prerequisites
- Python 3.6+
- pip (Python package installer)

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/HassaneSkikri/CaliforniaHousePricingEndToEndProject.git
   cd CaliforniaHousePricingEndToEndProject
