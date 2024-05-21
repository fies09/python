#!/usr/bin/env python
# -*- coding : utf-8 -*-
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for i in range(5):
    print(f"{i} is even: {is_even(i)}")
