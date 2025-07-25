# -*- coding: utf-8 -*-
#
# Authors: Arya Banerjee
# Date: 2020/6/01
# License: MIT License
"""
P300 Paradigm.
"""
from .base import BaseTimeEncodingParadigm


class P300(BaseTimeEncodingParadigm):
    def is_valid(self, dataset):
        ret = True
        if dataset.paradigm != "p300":
            ret = False
        return ret
