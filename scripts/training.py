# AUTOGENERATED! DO NOT EDIT! File to edit: ../fastai.ipynb.

# %% auto 0
__all__ = ['seed', 'IMG_PATH', 'TRAIN_PATH', 'TEST_PATH', 'item_tfms', 'dls', 'learn34', 'fname']

# %% ../fastai.ipynb 1
import glob

import pandas as pd
import numpy as np
from fastai.vision.all import *

seed = 42

np.random.seed(seed)

# %% ../fastai.ipynb 2
IMG_PATH = "imgs"
TRAIN_PATH = f"{IMG_PATH}/train"
TEST_PATH = f"{IMG_PATH}/test"


# %% ../fastai.ipynb 3
item_tfms = aug_transforms(do_flip=False)

dls = ImageDataLoaders.from_folder("imgs/train", valid_pct=0.2, batch_tfms=item_tfms, seed=seed)

# %% ../fastai.ipynb 7
learn34 = vision_learner(dls, resnet34, metrics=error_rate)
learn34.fine_tune(1)

# %% ../fastai.ipynb 9
fname = fname="../../models/fastai-resnet34.pkl"
learn34.export(fname=fname)
