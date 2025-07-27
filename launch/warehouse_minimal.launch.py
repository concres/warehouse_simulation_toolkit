from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    AppendEnvironmentVariable,
)

from launch.launch_description_sources import PythonLaunchDescriptionSource
from os import path as os_path


def generate_launch_description():
    # gazebo paths
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")
    gz_launch_path = os_path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")

    # warehouse simulation paths
    pkg_warehouse = get_package_share_directory("warehouse_simulation")
    warehouse_world_path = os_path.join(pkg_warehouse, "worlds", "warehouse.sdf")
    warehouse_resources_paths = [
        os_path.join(pkg_warehouse, "models"),
        os_path.join(pkg_warehouse, "models", "workcell", "materials", "textures"),
        os_path.join(pkg_warehouse, "models", "workcell_bin", "materials", "textures"),
    ]

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gz_launch_path),
        launch_arguments={
            "gz_args": warehouse_world_path,
            "on_exit_shutdown": "True",
        }.items(),
    )

    return LaunchDescription(
        [
            AppendEnvironmentVariable(
                name="GZ_SIM_RESOURCE_PATH",
                value=":".join(warehouse_resources_paths),
            ),
            gazebo_launch,
        ]
    )
