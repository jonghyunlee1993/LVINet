#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = "yolox_m_LVI"

        # Define yourself dataset path
        self.data_dir = "datasets/LVI_coco"
        self.train_ann = "train_labels.json"
        self.val_ann = "valid_labels.json"
        self.test_ann = "test_labels.json"

        self.num_classes = 1

        self.max_epoch = 100
        self.data_num_workers = 12
        self.eval_interval = 1
