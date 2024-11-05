#!/bin/env python3

import os
import shutil

try:
    shutil.rmtree("pages")
except:
    pass
os.mkdir("pages")

with open("links.csv", "r") as f:
    for l in f.readlines():
        [name, link] = l.rstrip().split(",", 1)

        with open(f"pages/{name}.html", "w") as p:
            p.write(f"\
<!DOCTYPE HTML><html>\
<head>\
<meta charset=\"utf-8\">\
</head>\
<body>\
<script>window.location.href=\"{link}\"</script>\
<a href=\"{link}\">Click here to continue</a>\
</body>\
</html>")
