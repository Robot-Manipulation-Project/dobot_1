import time

def execute_movements(robot):
    target_points = [
        (-74.14408874511719, 14.930240631103516, -10.431154251098633, 0.0),
        (-74.11761474609375, 54.147674560546875, -1.848876953125, 0.0),
        (-74.14408874511719, 14.930240631103516, -10.431154251098633, 0.0),
        (-36.6352653503418, 42.7051887512207, 20.168678283691406, 0.0),
        (2.9416294637485407e-05, 0.0, 0.0, 0.0)


]

    for i, (j1, j2, j3, j4) in enumerate(target_points):

        if robot.is_goal_valid(j1, j2, j3, j4):
            print(f"Moving to point {i+1}: J1={j1}, J2={j2}, J3={j3}, J4={j4}")
            robot.set_joint_ptp(j1, j2, j3, j4)
            
            time.sleep(5) 

            if i == 1:
               robot.set_suction_cup(True)
               time.sleep(1)

            if i == len(target_points) - 2:

                robot.set_suction_cup(False)
                print("Suction cup turned off at the last point.")
        else:
            print(f"WARNING: Point {i+1} exceeds safe limits. Skipping.")

    print("Task 1 finished.")
