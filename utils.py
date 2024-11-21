#!/usr/bin/env python
# @Time : 2022/6/3 11:29
# @Author : Rongrui Zhan
# @desc : 本代码未经授权禁止商用
from __future__ import annotations

from enum import Enum


class ModelName(str, Enum):
    inception = "inception"
    lstm = "lstm"
