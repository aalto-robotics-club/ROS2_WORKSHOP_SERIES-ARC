# ROS 2 Workshop Series - ARC

This README explains how to run the ROS 2 Humble TurtleBot3 VNC Docker image using Docker Compose, open the desktop GUI, launch Gazebo, and drive the robot using keyboard teleoperation.

---

## Quick Start

```bash
docker compose up
```

This command will pull the image (if needed) and start the container with all necessary configurations pre-set.

To stop and remove the container:

```bash
docker compose down
```

---

## Open the GUI

After the container starts, open the noVNC interface in your browser:

```text
http://localhost:6080
```

If you are using a VNC client, connect to:

```text
localhost:5900
```

---

## Launch Gazebo

In the noVNC browser window, open a terminal and launch the TurtleBot3 Gazebo world:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

The `TURTLEBOT3_MODEL` environment variable is pre-configured in the Docker Compose setup, so no export is needed.

---

## Drive the Robot

In the noVNC browser window, open a second terminal and run keyboard teleoperation:

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

Use the keyboard instructions shown in the terminal to drive the robot.

---

## Python Files

The workshop includes standalone Python files that can be run directly with `python3` (not requiring ROS 2). These files are located in:

```
ros2_ws/src/arc_workshop/arc_workshop/
```

Available Python files:

- **cmd_vel_reader.py** - Reads command velocity messages
- **scan_direction_reader.py** - Reads and processes scan direction data
- **stop_on_obstacle.py** - Implements obstacle detection and stopping logic

To run any of these files from the project root:

```bash
python3 ros2_ws/src/arc_workshop/arc_workshop/cmd_vel_reader.py
```

Or navigate to the directory first:

```bash
cd ros2_ws/src/arc_workshop/arc_workshop/
python3 cmd_vel_reader.py
```

---

## Notes

- Keep the Gazebo launch terminal running while driving the robot.
- Use `Ctrl + C` to stop Gazebo or teleoperation.
- Run `docker compose down` to stop and remove the container when finished.
