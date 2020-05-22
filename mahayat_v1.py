import torch
import torchvision.datasets as datasets
#%%
#class TwoCropsTransform:
#    """Take two random crops of one image as the query and key."""
#
#    def __init__(self, base_transform):
#        self.base_transform = base_transform
#
#    def __call__(self, x):
#        q = self.base_transform(x)
#        k = self.base_transform(x)
#        return [q, k]
#%% Dataset 
traindir = '/global/cscratch1/sd/wbhimji/imagenet/raw_data/'

## https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder
#train_dataset = datasets.ImageFolder(traindir)

## https://pytorch.org/docs/stable/torchvision/datasets.html#imagenet
train_dataset = datasets.ImageNet(traindir, split='train')

print('shape of sample#1: {}'.format(train_dataset[1][0].shape))
print('shape of target#1: {}'.format(train_dataset[1][1].shape))
#%%

