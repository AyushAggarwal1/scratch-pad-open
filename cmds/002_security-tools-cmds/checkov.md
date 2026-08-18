---
title: Checkov
parent: Security Tools Cmds
grand_parent: Cmds
nav_order: 2
description: "CLI commands to run Checkov IaC scanning over a directory, all frameworks or default, with JSON output."
---

# Checkov

checkov -d '/home/ayush/Desktop/work/cspm-backend/' --framework all -o json > '/home/ayush/Desktop/work/cspm-backend/dist/scratchpad/checkov.json'

 checkov -d '/home/ayush/Desktop/work/cspm-backend/' -o json > '/home/ayush/Desktop/work/cspm-backend/dist/scratchpad/checkov.json'