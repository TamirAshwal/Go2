---
name: sit
description: Make the robot sit down or lie down. Use when the user asks the robot to sit, sit down, lie down, or rest.
---

# Sit

When the user wants the robot to sit down, run the sit script with this exact command:

```bash
cd "/home/tamir/Desktop/openClaw Go2" && unitree_venv/bin/python ~/.openclaw/workspace/skills/sit/sit.py
```

## Rules
- Only run sit.py via the command above. Do not write your own movement code.
- Do not import or call the Unitree SDK directly.
- Do not create scripts in /tmp or anywhere else.
