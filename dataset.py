import os
from torchvision import transforms
import torch
from torch.utils.data import Dataset
import cv2

class MnistDataset(Dataset):
    def __init__(self, img_dir: str):
        self.img_path = [os.path.join(img_dir, name) for name in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, name))]
        self.y = [0 if 'anom' in name else 1 for name in self.img_path]
        self.transform = transforms.Compose([
             transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.img_path)

    def __getitem__(self, idx):
        image = cv2.imread(self.img_path[idx], 0)
        image = cv2.resize(image, (28, 28))
        if self.transform:
            image = self.transform(image)
        return image, self.y[idx]