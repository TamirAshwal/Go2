---
name: stretch
description: Make the robot do a stretch routine. Use when the user asks the robot to stretch, do a stretch, or warm up.
---

# Stretch

When the user wants the robot to stretch, run the stretch script with this exact command:

```bash
cd "/home/tamir/Desktop/openClaw Go2" && unitree_venv/bin/python ~/.openclaw/workspace/skills/stretch/stretch.py
```

## Rules
- Only run stretch.py via the command above. Do not write your own movement code.
- Do not import or call the Unitree SDK directly.
- Do not create scripts in /tmp or anywhere else.
