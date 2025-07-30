cmake_minimum_required(VERSION 3.8)
project(warehouse_simulation)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Align to ROS2 Jazzy https://docs.ros.org/en/jazzy/The-ROS2-Project/Contributing/Code-Style-Language-Versions.html#id2
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# generate a compile_commands.json file for tools like clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# === Dependencies ===
find_package(ament_cmake REQUIRED)

# === Install ===
install(DIRECTORY
  launch
  models
  worlds
  maps
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
