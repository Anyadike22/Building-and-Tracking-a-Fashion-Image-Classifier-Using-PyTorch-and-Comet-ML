# Building-and-Tracking-a-Fashion-Image-Classifier-Using-PyTorch-and-Comet-ML


# 🧠 FashionMNIST Classifier with PyTorch and Comet ML

This project builds and trains a deep learning model to classify clothing items using the FashionMNIST dataset. It integrates [Comet ML](https://www.comet.com/) to track experiments, log metrics, save models, and version your training code — enabling full reproducibility and insight into model performance.


## 🖼️ Dataset

- **FashionMNIST**: A dataset of 28x28 grayscale images of 10 different clothing categories.
- Automatically downloaded via `torchvision.datasets.FashionMNIST`.



## 🚀 Features

- Built with **PyTorch** for model training.
- Uses **Comet ML** to:
  - Log hyperparameters
  - Track training loss
  - Save trained model
  - Log source code


## 🔧 Requirements

Install the required dependencies using pip:


pip install -r requirements.txt


# How to Run
Set up your Comet ML account:

Create a Comet account

Get your API key from your Comet dashboard

You can either:

Set environment variables:

export COMET_API_KEY="your-api-key"
export COMET_PROJECT_NAME="fashion-mnist-demo"
export COMET_WORKSPACE="your-workspace-name"

Or hardcode them in the script (not recommended for shared code).

#Run the training script

python train_fashion_mnist.py

#📊 #Logged Metrics on Comet
After training, you can view your experiment dashboard on comet.com with:

Training loss per epoch

Logged hyperparameters

Model file (.pt)

Source code version
