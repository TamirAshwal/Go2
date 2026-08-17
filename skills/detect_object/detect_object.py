import sys
sys.path.insert(0, "/home/tamir/Desktop/openClaw Go2/unitree_sdk2_python")

import cv2
import numpy as np
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.video.video_client import VideoClient
from ultralytics import YOLO

# --- Read the object to look for from the command-line argument ---
if len(sys.argv) < 2 or not sys.argv[1].strip():
    print("RESULT: object_found=no reason=no_object_specified")
    sys.exit(0)

target = sys.argv[1].strip().lower()

# --- Load model first so we can validate the requested object ---
model = YOLO("yolov8n.pt")
valid_names = {name.lower(): cid for cid, name in model.names.items()}

if target not in valid_names:
    # Unsupported object: report clearly, do NOT guess or modify anything.
    print(f"RESULT: object_found=no reason=unsupported_object requested={target}")
    sys.exit(0)

# --- Connect to robot camera over DDS (same interface as movement skills) ---
ChannelFactoryInitialize(0, "enp0s31f6")

cam = VideoClient()
cam.SetTimeout(3.0)
cam.Init()

code, data = cam.GetImageSample()
if code != 0 or not data:
    print("RESULT: object_found=no reason=no_camera_frame")
    sys.exit(0)

img = cv2.imdecode(np.frombuffer(bytes(data), dtype=np.uint8), cv2.IMREAD_COLOR)
if img is None or img.size == 0:
    print("RESULT: object_found=no reason=bad_frame")
    sys.exit(0)

frame_h, frame_w = img.shape[:2]

# --- Run YOLO detection (imgsz=640 confirmed to detect objects reliably) ---
res = model.predict(img, imgsz=640, conf=0.4, verbose=False)[0]

# --- Collect all detections matching the requested object ---
matches = []  # (confidence, x1, y1, x2, y2)
if res.boxes is not None and len(res.boxes) > 0:
    boxes = res.boxes.xyxy.cpu().numpy()
    clss = res.boxes.cls.cpu().numpy().astype(int)
    confs = res.boxes.conf.cpu().numpy()
    for (x1, y1, x2, y2), cid, conf in zip(boxes, clss, confs):
        if model.names[int(cid)].lower() == target:
            matches.append((float(conf), float(x1), float(y1), float(x2), float(y2)))

if not matches:
    print(f"RESULT: object_found=no reason=not_in_view requested={target}")
    sys.exit(0)

# --- Pick the most confident match ---
matches.sort(key=lambda m: m[0], reverse=True)
conf, x1, y1, x2, y2 = matches[0]

# --- Horizontal position: left / center / right ---
box_center_x = 0.5 * (x1 + x2)
norm_x = box_center_x / frame_w
if norm_x < 0.4:
    position = "left"
elif norm_x > 0.6:
    position = "right"
else:
    position = "center"

# --- Closeness proxy: box height relative to frame ---
size_frac = (y2 - y1) / frame_h
if size_frac > 0.6:
    closeness = "near"
elif size_frac > 0.3:
    closeness = "medium"
else:
    closeness = "far"

print(f"RESULT: object_found=yes object={target} confidence={conf:.2f} position={position} closeness={closeness}")
