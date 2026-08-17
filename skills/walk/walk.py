import sys
import time
import math
sys.path.insert(0, "/home/tamir/Desktop/openClaw Go2/unitree_sdk2_python")
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient

# argv[1] = magnitude: meters for moves, DEGREES for turns (default 0.9)
# argv[2] = direction: forward|backward|left|right|turn_left|turn_right (default forward)
magnitude = float(sys.argv[1]) if len(sys.argv) > 1 else 0.9
direction = sys.argv[2] if len(sys.argv) > 2 else "forward"

VELOCITY = 0.3      # m/s for translation
YAW_RATE = 1.0      # rad/s for turning

translate = {
    "forward":  (VELOCITY, 0, 0),
    "backward": (-VELOCITY, 0, 0),
    "left":     (0, VELOCITY, 0),
    "right":    (0, -VELOCITY, 0),
}
turn = {
    "turn_left":  (0, 0, YAW_RATE),
    "turn_right": (0, 0, -YAW_RATE),
}

if direction in turn:
    vx, vy, vyaw = turn[direction]
    duration = math.radians(abs(magnitude)) / YAW_RATE   # magnitude = degrees
    unit = "deg"
else:
    vx, vy, vyaw = translate.get(direction, translate["forward"])
    duration = abs(magnitude) / VELOCITY                 # magnitude = meters
    unit = "m"

ChannelFactoryInitialize(0, "enp0s31f6")
sport_client = SportClient()
sport_client.SetTimeout(10.0)
sport_client.Init()

# Resend Move continuously so the robot keeps moving for the full duration
start = time.time()
while time.time() - start < duration:
    sport_client.Move(vx, vy, vyaw)
    time.sleep(0.1)   # refresh at ~10 Hz
sport_client.StopMove()
print(f"Walked {direction} {magnitude}{unit} ({duration:.1f}s)")
