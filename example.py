# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 5 2025

@author: Giustino C. Miglionico
"""

from fuzzy_tree_plotter import FuzzyTreePlotter

# Definiamo le regole fuzzy
rules = [
    "if F2 is L and F8 is L and F7 is L then 3",
    "if F2 is L and F8 is L and F7 is M then 3",
    "if F2 is L and F8 is L and F7 is H then 1",
    "if F2 is L and F8 is M and F7 is L then 2",
    "if F2 is L and F8 is M and F7 is M then 1",
    "if F2 is L and F8 is M and F7 is H then 3",
    "if F2 is M and F8 is L and F7 is L then 2",
    "if F2 is M and F8 is L and F7 is M then 3",
    "if F2 is M and F8 is L and F7 is H then 1",
    "if F2 is M and F8 is M and F7 is L then 3",
    "if F2 is M and F8 is M and F7 is M then 1",
    "if F2 is M and F8 is M and F7 is H then 2",
    "if F2 is H and F8 is L and F7 is L then 3",
    "if F2 is H and F8 is L and F7 is M then 2",
    "if F2 is H and F8 is L and F7 is H then 1",
    "if F2 is H and F8 is M and F7 is L then 1",
    "if F2 is H and F8 is M and F7 is M then 2",
    "if F2 is H and F8 is M and F7 is H then 3",
    "if F2 is H and F8 is H and F7 is L then 2",
    "if F2 is H and F8 is H and F7 is M then 3",
    "if F2 is H and F8 is H and F7 is H then 1",
]


plotter = FuzzyTreePlotter(rules, aggrega=True, text_size=20, line_width=2, edge_text_size=18)

plotter.render("fuzzy_tree_example", format="png", view=True)
