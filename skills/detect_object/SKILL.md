---
name: detect_object
description: Look through the robot's camera and report whether a specific object is visible, where it is (left/center/right), and roughly how close it is (near/medium/far). Use whenever the user wants the robot to find, look for, locate, see, or check for an object (for example a chair, a person, a bottle, a couch). The object to look for is passed as an argument.
---

# Detect Object

When the user wants the robot to look for an object, run the detection script with the object name as an argument. Use this exact command, replacing OBJECT with the lowercase object name:

```bash
cd "/home/tamir/Desktop/openClaw Go2" && unitree_venv/bin/python ~/.openclaw/workspace/skills/detect_object/detect_object.py OBJECT
```

Example for a chair:

```bash
cd "/home/tamir/Desktop/openClaw Go2" && unitree_venv/bin/python ~/.openclaw/workspace/skills/detect_object/detect_object.py chair
```

## Supported objects

The detector can ONLY recognize these objects (the YOLO/COCO classes). Pass exactly one of these names, in lowercase:

person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic light, fire hydrant, stop sign, parking meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard, sports ball, kite, baseball bat, baseball glove, skateboard, surfboard, tennis racket, bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake, chair, couch, potted plant, bed, dining table, toilet, tv, laptop, mouse, remote, keyboard, cell phone, microwave, oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy bear, hair drier, toothbrush

If the user asks for something that is NOT in this list (for example "keys", "wallet", "my phone charger"), DO NOT run the script with a made-up class and DO NOT edit the script. Instead, tell the user that object is not supported and, if helpful, suggest the closest supported one (for example "cell phone" instead of "phone").

## Reading the result

The script prints one line. Examples:

- `RESULT: object_found=yes object=chair confidence=0.92 position=center closeness=near`
- `RESULT: object_found=no reason=not_in_view requested=chair`
- `RESULT: object_found=no reason=unsupported_object requested=keys`

Interpretation:
- `object_found=yes` means the requested object is currently visible.
- `position` is where it is in the camera frame: `left`, `center`, or `right`.
- `closeness` is a rough distance: `near`, `medium`, or `far`.
- `object_found=no` means it was not seen this time; `reason` says why.

Use this result to decide what to do next. For example, if the user said "if you see a chair, stretch" and the result is `object_found=yes`, then run the stretch skill next.

## Rules
- Only run detect_object.py via the command above. Do not write your own detection or camera code.
- Do not import or call the Unitree SDK, OpenCV, or YOLO directly.
- Do not create scripts in /tmp or anywhere else.
- Do not edit this script or its SKILL.md to handle an unsupported object. Report instead.
- This skill only looks; it does not move the robot.
