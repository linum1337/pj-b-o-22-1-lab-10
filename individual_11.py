#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "h", "k"}
    b = {"c", "d", "h", "p", "r"}
    c = {"h", "i", "s"}
    d = {"c", "g", "j", "v", "w"}
    x = (a.union(b)).intersection(b)
    print(f"x = {x}")
    ab = a.union(b)
    cd = a.intersection(b)
    y = ab.difference(cd)
    print(f"y = {y}")