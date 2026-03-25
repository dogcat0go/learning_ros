# fish_bot_ws

本仓库是一个 ROS 2（colcon）工作空间示例。

## 快速开始（编译）

### 依赖

- ROS 2 Humble（Ubuntu 22.04 常用）
- colcon（一般随 ROS 2 安装或可通过 apt 安装）

打开新终端后，先加载 ROS 环境：

```bash
source /opt/ros/humble/setup.bash
```

### 一键编译整个工作空间

在工作空间根目录（包含 `src/` 的这一层）执行：

```bash
cd ~/ros2_projects/fish_bot_ws
colcon build
source install/setup.bash
```

### 只编译指定包（更快）

例如只编译 `fishbot_description`：

```bash
cd ~/ros2_projects/fish_bot_ws
colcon build --packages-select fishbot_description
source install/setup.bash
```

## 运行示例（显示 URDF）

编译并 `source install/setup.bash` 后：

```bash
ros2 launch fishbot_description display_robot.launch.py
```

## 常见问题

### 修改了 URDF / xacro / launch，为啥没生效？

这些文件会随包一起安装到 `install/` 下。修改后重新执行一次：

```bash
colcon build --packages-select fishbot_description
source install/setup.bash
```

