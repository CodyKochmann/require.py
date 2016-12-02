# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 19:07:10
# @Last Modified 2016-12-02
# @Last Modified time: 2016-12-02 12:11:43

"""
    This is where hypothesis will be taking its turn
    making sure that require.py behaves the way it
    should with the correct inputs.
"""

from hypothesis import (
    strategies as st,
    settings,
    Verbosity,
    given
)

from require import require

test_samples = 2048

with settings(
        verbosity=Verbosity.normal,
        min_satisfying_examples=test_samples,
        max_examples=test_samples):

    @given(arg_list=st.lists(min_size=1, elements=st.text()))
    def test_str(arg_list):
        try:
            require.str(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.floats()))
    def test_float(arg_list):
        try:
            require.float(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.integers()))
    def test_int(arg_list):
        try:
            require.int(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.lists(
        min_size=1,
        elements=st.floats())))
    def test_list(arg_list):
        try:
            require.list(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.lists(
        min_size=1,
        elements=st.tuples())))
    def test_tuple(arg_list):
        try:
            require.tuple(*arg_list)
        except AssertionError:
            pass

    if __name__ == "__main__":
        tests = [test_str, test_float, test_int, test_list, test_tuple]
        for t in tests:
            print("running ({} times) - {}".format(test_samples, t.__name__))
            t()
            print("success")
        print("done")
