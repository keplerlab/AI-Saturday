from pathlib import Path

from fastai.imports import *

from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *

import config

C = config.Config()

PATH = C.PATH
sz = C.sz
model = C.model

arch = resnet50

class FastaiImageClassifier(object):
    def __init__(self):
        self.data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz))
        self.learn = ConvLearner.pretrained(arch, self.data, precompute=True)
        self.learn.load(model)

    def predict(self, img_path):
        trn_tfms, val_tfms = tfms_from_model(arch, sz)
        img = val_tfms(open_image(img_path))
        preds = self.learn.predict_array(img[None])
        pred_class = self.data.classes[np.argmax(preds)]
        print("Predicted class: ", pred_class)

        return { "predict": pred_class }
