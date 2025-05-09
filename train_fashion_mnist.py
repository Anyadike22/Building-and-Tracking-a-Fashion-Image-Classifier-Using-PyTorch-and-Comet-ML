# -*- coding: utf-8 -*-
"""train_fashion_mnist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gq8CJPsZamcthSlDlxJCt4kEWYjIiYQ0
"""

pip install comet_ml

from comet_ml import Experiment
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

#  Comet ML setup
experiment = Experiment(
    api_key="fL21dFQkgKqCFEaarp7WdUpY0",  # Replace with your Comet API key
    project_name="fashion-mnist-demo",
    workspace="emexy"
)

# Hyperparameters
hyper_params = {
    "learning_rate": 0.001,
    "batch_size": 64,
    "epochs": 5
}
experiment.log_parameters(hyper_params)

# Data loading & transformation
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_data = datasets.FashionMNIST(root='data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=hyper_params["batch_size"], shuffle=True)

#Model definition
class FashionClassifier(nn.Module):
    def __init__(self):
        super(FashionClassifier, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Training loop
def train(model, loader, criterion, optimizer, epochs):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        avg_loss = total_loss / len(loader)
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {avg_loss:.4f}")
        experiment.log_metric("loss", avg_loss, step=epoch+1)

# 🚀 Run training
model = FashionClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=hyper_params["learning_rate"])
train(model, train_loader, criterion, optimizer, hyper_params["epochs"])

# 💾 Save & log model
torch.save(model.state_dict(), "fashion_model.pt")
experiment.log_model("FashionClassifier", "fashion_model.pt")