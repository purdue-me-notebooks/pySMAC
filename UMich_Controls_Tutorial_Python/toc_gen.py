#!/usr/bin/env python3

import glob
import urllib
import os
from IPython.display import display_markdown
notebooks = glob.glob("*.ipynb")
notebooks.sort()
cfg = {
    "gh_user": "purdue-me-notebooks",
    "gh_proj": "pySMAC",
    "gh_branch": "master",
    "base": "UMich_Controls_Tutorial_Python",
}
url_fmt = "https://mybinder.org/v2/gh/{gh_user}/{gh_proj}/{gh_branch}?="
table = list()
table.append(["", "", "Notebook", "Jupyter Lab", ""])
table.append(["", "---", "---", "---", ""])
for notebook in notebooks:
    url = url_fmt.format(**cfg)+urllib.parse.urlencode({"filepath": os.path.join(cfg["base"], notebook)})
    table.append([
        "",
        f"[{os.path.splitext(notebook)[0]}](os.path.splitext(notebook))",
        f"[![Binder](https://mybinder.org/badge_logo.svg)]({url})",
        f"[![Binder](https://mybinder.org/badge_logo.svg)]({url}&urlpath=lab)",
    ""])

header = """# UMich Controls Tutorials in Python

[Control Tutorials for MATLAB & Simulink](http://ctms.engin.umich.edu/CTMS/index.php?aux=Home), re-created with Python where available.

## Notebook Table of Contents

Follow the links on the left to launch the notebooks on Binder in either a Jupyter Notebook or Jupyter Lab interface

"""

md_rows = ["|".join(row) for row in table] 
md = "\n".join(md_rows)
with open("TableOfContents.md", "wt") as fid:
    fid.write(header)
    fid.write(md)
