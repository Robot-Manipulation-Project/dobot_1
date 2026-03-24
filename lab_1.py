# Yasiru Fernando : 22345563
# Ladurshi Sivapalan: 22295011

import time

def move(dobot):

    points = [
        (-74.14408874511719, 14.930240631103516, -10.431154251098633, 0.0),
        (-74.11761474609375, 54.147674560546875, -1.848876953125, 0.0),
        (-74.14408874511719, 14.930240631103516, -10.431154251098633, 0.0),
        (-36.6352653503418, 42.7051887512207, 20.168678283691406, 0.0),
        (2.9416294637485407e-05, 0.0, 0.0, 0.0)
]

    #for i in range(len(points)):
    #    x, y, z, r = points[i]
    
    for i, (x, y, z, r) in enumerate(points):

        if dobot.is_goal_valid(x, y, z, r):
            print(f"Moving to point {i+1}: X={x}, Y={y}, Z={z}, R={r}")
            dobot.set_joint_ptp(x, y, z, r)
            
            time.sleep(5) 

            if i == 1:
               dobot.set_suction_cup(True)
               print("Suction cup turned on")
               time.sleep(1)

            if i == len(points) - 2:

                dobot.set_suction_cup(False)
                print("Suction cup turned off")
        else:
            print(f"WARNING: Point {i+1} exceeds safe limits.")

    print("Task finished.")
