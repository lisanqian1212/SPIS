# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:58:40 2021

@author: hudew
"""

import os, sys
# sys.path.insert(0,'E:\\tools\\')
import util
import numpy as np
import torch
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset
import cv2

#%%
class trainDataset(Dataset):
    
    # data_dir = "data/ciliarymuscle/trainB/"
    
    def __init__(self):
        super().__init__()
        self.vol_dir = []
        self.data = []
        self.data_dir = "/data3/risa/lisanqian/lisanqian/dataprocessing/fundus/trainB/"

        for folder in os.listdir(self.data_dir):
            img = cv2.imread(self.data_dir+folder, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, [512, 512])
            im = np.zeros([512, 512], dtype=np.float32)
            im[:, :] = util.ImageRescale(img, [-1, 1])
            self.data.append(im)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx]
        x = torch.tensor(x).type(torch.FloatTensor)
        x = x[None, :, :]
        return x


def load_train_data(*, batch_size):
    dataset = trainDataset()
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return loader



class testDataset(Dataset):
    
    def __init__(self):
        super().__init__()
        self.data = []
        self.name = []
        # data_dir = "dataset/ASOCT/"
        data_dir ="dataset/CM/"
        # data_dir="/data3/risa/lisanqian/lisanqian/dataprocessing/fundus/test512S001/"
        # data_dir="/data3/risa/lisanqian/lisanqian/OCT_DDPM-main/src/dataset/fundus/retinalS004/testA/"
        for folder in os.listdir(data_dir):
            img = cv2.imread( data_dir+folder, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,[512,512])
            # img = cv2.resize(img,[450,450])
            # img = cv2.resize(img,[1000,1000])
            im = np.zeros([512, 512], dtype=np.float32)
            # im = np.zeros([450, 450], dtype=np.float32)
            # im = np.zeros([1000, 1000], dtype=np.float32)
            im[:, :] = util.ImageRescale(img, [-1, 1])
            self.data.append(im)
            self.name.append(folder)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx]
        x = torch.tensor(x).type(torch.FloatTensor)
        x = x[None, :, :]
        return x, self.name[idx]


def load_test_data( *,batch_size, shuffle=False):
    dataset = testDataset()
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return loader


#%%
# data_dir = "E:\\HumanData\\ONH_SNR_101_1\\"
# #
# vol = util.nii_loader(data_dir+"SF_ONH_SNR_101_1.nii.gz")     
