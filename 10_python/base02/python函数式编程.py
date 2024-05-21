#!/usr/bin/env python
# -*- coding : utf-8 -*-
def multiply_by_two(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled_numbers = list(map(multiply_by_two, numbers))
print(doubled_numbers)
