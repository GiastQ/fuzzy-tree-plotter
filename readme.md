# Fuzzy Tree Plotter

**FuzzyTreePlotter** is a Python script that visualizes fuzzy decision trees based on a set of fuzzy logic rules.

## 🚀 Features
- Parses fuzzy logic rules and constructs a tree representation.
- Uses **Graphviz** for visualization.
- Supports multiple fuzzy rule formats.
- Option to aggregate branches with the same outcome.

## 🛠 Requirements
### Python Version:
This project requires **Python 3.11** or later.

### Required Libraries:
Before running the script, install the following dependencies:

```bash
pip install graphviz
---

## 🚀 Usage
Follow these steps to use **FuzzyTreePlotter** in your project.

### 1️⃣ Import the Class:
First, import the `FuzzyTreePlotter` class into your Python script:

```python
from fuzzy_tree_plotter import FuzzyTreePlotter


### 2️⃣ Define Your Fuzzy Rules:
Define a set of fuzzy logic rules that will be used to generate the tree.

```python
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


### 3️⃣ Create an Instance of `FuzzyTreePlotter`:
Now, create an instance of the `FuzzyTreePlotter` class and pass the rules as an argument.

```python
plotter = FuzzyTreePlotter(rules, aggrega=True, text_size=20, line_width=2, edge_text_size=18)


### 4️⃣ Generate and Visualize the Decision Tree:
Call the render() method to generate the decision tree and save it as an image.

```python
plotter.render("fuzzy_tree", format="png", view=True)
