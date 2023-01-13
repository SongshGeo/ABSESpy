#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/


from abses import MainModel
from abses.variable import Variable


def create_variable(*args):
    for i, v in enumerate(args):
        var = Variable(
            name=f"v{i+1}", long_name=f"variable {i+1}", initial_value=v
        )
        yield var


def test_variable_data():
    var1, var2, var3 = create_variable(0.1, 2, "defect")

    assert var1.dtype == float
    assert var2.dtype == int
    assert var3.dtype == str
    assert var1.__repr__() == "<Var[v1]: 0.1>"
    # --------------------------------
    # testing var ±*/ other -> var.data ±*/ other
    assert var1 + 0.9 == 1.0 == 0.9 + var1
    assert var1 - 0.1 == 0.0 == -(0.1 - var1)
    assert var2 - 1 == 1 == -(1 - var2)
    assert var2 + 2 == 4 == 2 + var2
    assert var3 + "!" == "defect!"
    assert var2**3 == 8
    assert var2 // 3 == 0
    assert var2 % 1 == 0
    assert -var1 == -0.1
    assert +var2 == 2
    assert var1 < 1
    assert 3 > var2
    # --------------------------------
    # assert var calculate with var
    assert var1 != var2
    assert var3 * var2 == "defectdefect"
    assert var2 > var1
    assert var1 <= var2


def test_variable_dtype():
    var1, var2 = create_variable(None, None)
    assert var1.dtype is None
    var1.data = 1
    assert var1.dtype == int
    try:
        var1.data = 0.1
    except TypeError as e:
        assert "mismatches" in str(e)
    var1.creator
