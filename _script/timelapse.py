import time
import os

snap_dir = os.environ['HOME'] + "/ascii_snap"
snapshots = sorted(os.listdir( snap_dir ))
for snap in snapshots:
    os.system("clear")
    with open( snap_dir + f"/{snap}") as f:
        print(f.read())
    time.sleep(0.07)  # スピード調整