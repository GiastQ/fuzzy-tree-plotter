# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 5 2025

@author: Giustino C. Miglionico
"""

from graphviz import Digraph

class FuzzyTreePlotter:
    def __init__(self, rules, aggrega=False, text_size=12, line_width=1, edge_text_size=12):
        """Classe per costruire e visualizzare un albero fuzzy a partire da regole fuzzy."""
        self.rules = rules
        self.aggrega = aggrega
        self.text_size = text_size
        self.line_width = line_width
        self.edge_text_size = edge_text_size
        self.tree = self._build_tree()
        self.counter = 0  # Inizializza il contatore
        self.dot = self._build_graphviz_tree()

    def _parse_rule(self, rule):
        """Parsa una regola fuzzy e restituisce una tupla (conditions, outcome)."""
        rule = rule.strip()
        if rule.lower().startswith("if "):
            rule = rule[3:]
        if " then " not in rule:
            raise ValueError("Formato regola non valido (manca 'then'): " + rule)
        conditions_part, outcome_part = rule.split(" then ", 1)
        outcome = outcome_part.strip()
        conditions = [tuple(c.strip().split(" is ")) for c in conditions_part.split(" and ")]
        return conditions, outcome

    def _insert_into_tree(self, tree, conditions, outcome):
        """Inserisce una regola nella struttura ad albero."""
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
        """Costruisce la struttura ad albero a partire dalle regole."""
        tree = {}
        for rule in self.rules:
            conditions, outcome = self._parse_rule(rule)
            self._insert_into_tree(tree, conditions, outcome)
        return tree

    def _traverse_tree(self, dot, tree, parent_id=None, edge_label=""):
        """Crea il grafo Graphviz in base alla struttura ad albero."""
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
        """Crea il grafo Graphviz per la visualizzazione dell'albero fuzzy."""
        dot = Digraph(comment="Fuzzy Decision Tree", graph_attr={'rankdir': 'TB'})
        dot.node_attr.update(fontsize=str(self.text_size))
        dot.edge_attr.update(penwidth=str(self.line_width), fontsize=str(self.edge_text_size))

        self.counter = 0  # Inizializza il contatore prima della traversata
        leaf_ids = self._traverse_tree(dot, self.tree)

        with dot.subgraph() as s:
            s.attr(rank='same')
            for lid in leaf_ids:
                s.node(lid)

        return dot

    def render(self, filename="fuzzy_tree", format="png", view=True):
        """Renderizza e salva l'albero fuzzy in un file."""
        self.dot.render(filename, format=format, view=view)
