# Interactive Marimo Notebook
# Author email: 23f1002246@ds.study.iitm.ac.in

import marimo as mo

# --- Cell 1: Load or create data ---------------------------------------
# This cell provides the dataset. Downstream cells depend on `x` and `y`.
# Data flow: slider -> transformation -> markdown
x = list(range(1, 101))
y = [v * 2 for v in x]  # simple linear relationship

# --- Cell 2: Interactive widget ----------------------------------------
# Slider controls how many data points we reveal.
limit = mo.ui.slider(1, 100, label="Number of points to display")
limit

# --- Cell 3: Reactive computation --------------------------------------
# This cell uses the slider's value to slice the dataset.
# Data flow: uses `limit.value` and sources from Cell 1 variables.
x_slice = x[: limit.value]
y_slice = y[: limit.value]

# --- Cell 4: Dynamic Markdown ------------------------------------------
# Reactive: any change to `limit` recomputes this markdown.
mo.md(f"### Showing **{limit.value}** data points\n" 
      f"First value: **{x_slice[0]}** → {y_slice[0]}\n" 
      f"Last value: **{x_slice[-1]}** → {y_slice[-1]}")

# --- Note --------------------------------------------------------------
# Raw GitHub URL example (replace USER/REPO/PATH):
# https://raw.githubusercontent.com/USER/REPO/main/notebook.py
