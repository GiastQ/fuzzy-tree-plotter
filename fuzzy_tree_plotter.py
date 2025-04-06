# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 6 2025

@author: Giustino C. Miglionico
"""

from graphviz import Digraph
import os, re

class FuzzyTreePlotter:
    def __init__(self, rules, aggrega=False, text_size=12, line_width=1, edge_text_size=12):
        """
        Class for building and visualizing a fuzzy decision tree from fuzzy rules.
        Accepts either a list of rules or a path to a .txt file (one rule per line).
        """
        self.rules = self._load_rules(rules)
        self.aggrega = aggrega
        self.text_size = text_size
        self.line_width = line_width
        self.edge_text_size = edge_text_size
        self.tree = self._build_tree()
        self.counter = 0
        self.dot = self._build_graphviz_tree()

    def _load_rules(self, source):
        """Loads rules from a list or from a text file."""
        if isinstance(source, list):
            return source

        elif isinstance(source, str) and os.path.isfile(source):
            try:
                with open(source, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f if line.strip()]
            except Exception as e:
                print(f"[WARNING] Failed to open rules file: {source}\n  → {e}")
                return []

            if not lines:
                print(f"[WARNING] Rules file '{source}' is empty or contains only blank lines.")

            return lines

        else:
            raise ValueError("The 'rules' parameter must be a list of strings or a valid path to a .txt file.")


    def _parse_rule(self, rule):
        """Parses a fuzzy rule and returns a tuple (conditions, outcome)."""
        rule = rule.strip()
        rule = re.sub(r"(?i)^if\s+", "", rule)
        parts = re.split(r"(?i)\s+then\s+", rule)

        if len(parts) != 2:
            raise ValueError("Invalid rule format (missing 'then'): " + rule)

        conditions_part, outcome_part = parts
        outcome = outcome_part.strip()
        raw_conditions = re.split(r"(?i)\s+and\s+", conditions_part.strip())
        conditions = []
        for cond in raw_conditions:
            cond_parts = re.split(r"(?i)\s+is\s+", cond.strip())
            if len(cond_parts) != 2:
                raise ValueError("Malformed condition: " + cond)
            attr, value = cond_parts
            conditions.append((attr.strip(), value.strip()))

        return conditions, outcome

    def _insert_into_tree(self, tree, conditions, outcome):
        """Inserts a rule into the tree structure."""
        if not conditions:
            tree['_leaf'] = outcome
            return
        attr, value = conditions[0]
        if attr not in tree:
            tree[attr] = {}
        if value not in tree[attr]:
            tree[attr][value] = {}
        self._insert_into_tree(tree[attr][value], conditions[1:], outcome)

    def _build_tree(self):
        """Builds the tree structure from rules."""
        tree = {}
        for rule in self.rules:
            conditions, outcome = self._parse_rule(rule)
            self._insert_into_tree(tree, conditions, outcome)
        return tree

    def _traverse_tree(self, dot, tree, parent_id=None, edge_label=""):
        """Creates the Graphviz graph based on the tree structure."""
        leaves = []
        if '_leaf' in tree and len(tree) == 1:
            leaf_id = f"leaf_{self.counter}"
            self.counter += 1
            dot.node(leaf_id, tree['_leaf'], shape="box")
            if parent_id:
                dot.edge(parent_id, leaf_id, label=edge_label)
            return [leaf_id]

        for attr, subtrees in tree.items():
            if attr == '_leaf':
                continue
            node_id = f"node_{self.counter}"
            self.counter += 1
            dot.node(node_id, attr)
            if parent_id:
                dot.edge(parent_id, node_id, label=edge_label)

            aggregated_leaves = {}
            for val, subtree in subtrees.items():
                if self.aggrega and '_leaf' in subtree and len(subtree) == 1:
                    outcome = subtree['_leaf']
                    if outcome in aggregated_leaves:
                        dot.edge(node_id, aggregated_leaves[outcome], label=val)
                    else:
                        leaf_id = f"leaf_{self.counter}"
                        self.counter += 1
                        dot.node(leaf_id, outcome, shape="box")
                        dot.edge(node_id, leaf_id, label=val)
                        aggregated_leaves[outcome] = leaf_id
                        leaves.append(leaf_id)
                else:
                    child_leaves = self._traverse_tree(dot, subtree, node_id, val)
                    leaves.extend(child_leaves)
        return leaves

    def _build_graphviz_tree(self):
        """Creates the Graphviz graph for fuzzy tree visualization."""
        dot = Digraph(comment="Fuzzy Decision Tree", graph_attr={'rankdir': 'TB'})
        dot.node_attr.update(fontsize=str(self.text_size))
        dot.edge_attr.update(penwidth=str(self.line_width), fontsize=str(self.edge_text_size))

        self.counter = 0  # Reset counter before traversal
        leaf_ids = self._traverse_tree(dot, self.tree)

        with dot.subgraph() as s:
            s.attr(rank='same')
            for lid in leaf_ids:
                s.node(lid)

        return dot

    def render(self, filename="fuzzy_tree", format="png", view=True):
        """Renders and saves the fuzzy tree to a file."""
        self.dot.render(filename, format=format, view=view)
