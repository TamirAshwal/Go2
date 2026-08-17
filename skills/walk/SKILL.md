---
name: walk
description: Move the Go2 robot. It can translate (forward, backward, left, right) by a distance in meters, OR rotate in place (turn_left, turn_right) by an angle in degrees. Use this whenever the user asks the robot to walk, move, go, step, turn, rotate, or look around. Do NOT use for sitting (use sit) or stretching (use stretch).
---

# Walk Skill

Moves the Go2 in the requested direction by the requested amount, then stops.

## Parameters
- **magnitude** (number): For moves (forward/backward/left/right) this is DISTANCE IN METERS. For turns (turn_left/turn_right) this is ANGLE IN DEGREES. If unspecified, use 0.9 for moves and 45 for turns.
- **direction** (string): one of `forward`, `backward`, `left`, `right`, `turn_left`, `turn_right`. Default `forward`.

## How to run
`unitree_venv/bin/python ~/.openclaw/workspace/skills/walk/walk.py <magnitude> <direction>`

Examples:
- "walk forward 2 meters"  -> walk.py 2 forward
- "go back half a meter"   -> walk.py 0.5 backward
- "step left"              -> walk.py 0.9 left
- "turn left 90 degrees"   -> walk.py 90 turn_left
- "turn around"            -> walk.py 180 turn_right
- "look around / scan"     -> turn in steps, e.g. walk.py 45 turn_right repeatedly

Do not modify this script. Pass values only as arguments.
