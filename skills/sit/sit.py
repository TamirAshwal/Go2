import sys
import time
sys.path.insert(0, "/home/tamir/Desktop/openClaw Go2/unitree_sdk2_python")

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient

ChannelFactoryInitialize(0, "enp0s31f6")

sport_client = SportClient()
sport_client.SetTimeout(10.0)
sport_client.Init()

# Sit down
ret = sport_client.StandDown()
print(f"StandDown ret: {ret}")
