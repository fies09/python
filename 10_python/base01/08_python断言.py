#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:53
# @Author     : fany
# @Project    : PyCharm
# @File       : 08_python断言.py
# @description:
import unittest


class Demo(unittest.TestCase):

    def raise_value_error(self):
        raise ValueError

    def test_assert(self):
        a, b = 1, 2
        c = None
        d = True
        e = False
        f = [1, 3, 4]
        g = h = 5

        # >>比较断言
        # 断言相等
        assert a + b == 3
        self.assertEqual(a+b, 3)
        # 断言不等
        assert a + b != 4
        self.assertNotEqual(a+b, 4)

        # >>空值断言
        # 断言非空
        assert a is not None
        self.assertIsNotNone(a)
        # 断言为空
        assert c is None
        self.assertIsNone(c)

        # >>布尔值断言
        # 断言为True
        assert d is True
        self.assertTrue(d)
        # 断言为False
        assert e is False
        self.assertFalse(e)

        # >>包含断言
        # 断言包含在内
        assert a in f
        self.assertIn(a, f)
        # 断言不包含在内
        assert b not in f
        self.assertNotIn(b, f)

        # >>对象断言
        # 断言是同一个对象
        assert g is h
        self.assertIs(g, h)
        # 断言不是同一个对象
        assert a is not h
        self.assertIsNot(a, h)

        # >>断言预期异常
        with self.assertRaises(ValueError):
            self.raise_value_error()


if __name__ == '__main__':
    unittest.main()