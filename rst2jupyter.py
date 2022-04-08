# Imports
import nbformat as nbf
import re
import inspect

# Initialize blank notebook
nb = nbf.v4.new_notebook()

# Define regex pattern for detecting python code from RST file
pattern = r"(\.\. code-block:: python\s+$)((\n +.*|\s)+)"

# RST file path
rst_path = "sample.rst"

# Read RST file
rst_file = open(rst_path)

# Read content in str format
rst_data_in_str = rst_file.read()

# Find the python code blocks which matches our regex
matches = re.finditer(pattern, rst_data_in_str, re.M)

# Code cells list initialization
cells = []

# Iterate through the matches and add the code blocks to the notebook as cells
for m, match in enumerate(matches):
    for g, group_text in enumerate(match.groups()):
        if g == 1:
            # Cleanup is being done here because without cleanup the indent of RST code-block directive flows through
            group_text = inspect.cleandoc(group_text)
            cells.append(nbf.v4.new_code_cell(group_text))

# Add the code cells list to the notebook instance we created earlier
nb['cells'] = cells

# Write the ipynb notebook
nbf.write(nb, rst_path.replace('.rst', '.ipynb'))

# Close the file
rst_file.close()
