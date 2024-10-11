# Scones Unlimited Image Classification Project

## Project Overview

This project implements an image classification system for Scones Unlimited, a scone-delivery-focused logistics company. The system is designed to automatically detect the type of vehicle (bicycle or motorcycle) used by delivery drivers, optimizing routing and operations.

## Table of Contents

1. [Project Components](#project-components)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
4. [Model Training and Deployment](#model-training-and-deployment)
5. [Lambda Functions](#lambda-functions)
6. [Step Functions Workflow](#step-functions-workflow)
7. [Monitoring and Evaluation](#monitoring-and-evaluation)

## Project Components

- SageMaker Notebook: For data preparation, model training, and deployment
- S3 Bucket: For storing training data and model artifacts
- Lambda Functions: For image processing and inference
- Step Functions: For orchestrating the serverless workflow
- CloudWatch: For monitoring and logging

## Setup and Installation

1. Clone this repository
2. Set up an AWS account and configure AWS CLI
3. Create an S3 bucket for storing project data
4. Set up a SageMaker Notebook instance
5. Install required Python libraries: pip install sagemaker boto3 numpy pandas matplotlib seaborn

## Usage

1. Upload the CIFAR-100 dataset to your S3 bucket
2. Run the Jupyter notebook to prepare data, train and deploy the model
3. Create and deploy Lambda functions
4. Set up the Step Functions workflow
5. Test the workflow with sample images

## Model Training and Deployment

The image classification model is trained using SageMaker's built-in Image Classification algorithm. The notebook `image_classification.ipynb` contains the code for:

- Data preparation
- Model training
- Model deployment
- Endpoint creation

## Lambda Functions

Three Lambda functions are used in this project:

1. `serializeImageData`: Serializes image data from S3
2. `classifyImage`: Performs inference using the deployed model
3. `filterInferences`: Filters low-confidence predictions

The code for these functions can be found in the `lambda.py` file.

## Step Functions Workflow

The Step Functions workflow orchestrates the image classification process:

1. Serialize image data
2. Classify image
3. Filter inferences

The workflow definition is provided in the `workflowjson.json` file.

## Monitoring and Evaluation

The project includes scripts for visualizing model performance:

- Confidence score distribution
- Inference results over time
- Performance by hour of day

## License

This project is licensed under the MIT License - see the LICENSE file for details.
