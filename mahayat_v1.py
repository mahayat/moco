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
#%%    
traindir = '/global/cscratch1/sd/wbhimji/imagenet/train/'
train_dataset = datasets.ImageFolder(traindir)
print(train_dataset[1][0].shape)
#%%

