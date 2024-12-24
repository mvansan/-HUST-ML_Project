import torch
from torch import nn
import torch.nn.functional as F

import pickle as pkl


x_dims = 256
num_classes = 5

with open("ckpt/vectorizer.skl", "rb") as file:
    vectorizer = pkl.load(file)

with open("ckpt/pca.skl", "rb") as file:
    pca = pkl.load(file)

linear = nn.Linear(x_dims, num_classes)
linear.load_state_dict(torch.load("ckpt/linear.pt", weights_only=True))


def predict(texts):
    x = vectorizer.transform(texts)
    x = pca.transform(x)
    x = torch.tensor(x, dtype=torch.float32)
    p = F.softmax(linear(x), -1).argmax(-1).numpy()
    return p


while True:
    s = input("Input: I love this")
    print("Stars:", predict([s.lower()]).item() + 1)