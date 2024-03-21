#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/29 22:05
# @Author     : fany
# @Project    : PyCharm
# @File       : auto_createquirements.py
# @description:
import os
import subprocess

# Step 1: Generate the current dependencies into temp_requirements.txt
subprocess.run(["pip", "freeze", ">", "temp_requirements.txt"], shell=True)

# Step 2: Get the dependency tree using pipdeptree
subprocess.run(["pipdeptree", "--warn", "silence", "--freeze", ">", "dependencies.txt"], shell=True)

# Step 3: Compare and update requirements.txt
with open("dependencies.txt", "r") as deps_file, open("temp_requirements.txt", "r") as temp_file:
    deps_set = set(line.strip().split("==")[0] for line in deps_file)
    temp_deps = temp_file.readlines()

# Remove duplicates and sort the dependencies
unique_deps = sorted(set(temp_deps) - deps_set)

# Write the unique dependencies to requirements.txt
with open("requirements.txt", "w") as reqs_file:
    reqs_file.writelines(unique_deps)

# Step 4: Clean up temporary files
os.remove("temp_requirements.txt")
os.remove("dependencies.txt")
