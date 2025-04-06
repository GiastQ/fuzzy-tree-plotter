# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 6 2025

@author: Giustino C. Miglionico
"""

from fuzzy_tree_plotter import FuzzyTreePlotter

# ================================================================
# CASE 1: Load rules directly from a Python list
# ================================================================

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

# Create and render fuzzy decision tree from the list
plotter = FuzzyTreePlotter(
    rules,
    aggrega=True,
    text_size=20,
    line_width=2,
    edge_text_size=18
)
plotter.render("fuzzy_tree_from_list", format="png", view=True)

# ================================================================
# CASE 2: Load rules from a .txt file
# Each line in the file must be a valid fuzzy rule
# ================================================================

rules_file_path = "rules.txt"  # Relative path (must exist in the same directory)

# Create and render fuzzy decision tree from the file
plotter = FuzzyTreePlotter(
    rules_file_path,
    aggrega=True,
    text_size=20,
    line_width=2,
    edge_text_size=18
)
plotter.render("fuzzy_tree_from_file", format="png", view=True)
