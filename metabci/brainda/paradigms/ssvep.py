# -*- coding: utf-8 -*-
#
# Authors: Arya Banerjee
# Date: 2020/6/01
# License: MIT License
"""
SSVEP Paradigm.

"""
from .base import BaseParadigm


class SSVEP(BaseParadigm):
    def is_valid(self, dataset):
        ret = True
        if dataset.paradigm != "ssvep":
            ret = False
        return ret
