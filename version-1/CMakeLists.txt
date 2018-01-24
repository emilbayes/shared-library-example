cmake_minimum_required(VERSION 3.9)

project(share-native)

add_library(share SHARED libshare.c)
set_target_properties(share PROPERTIES
  VERSION 1.0.0
  SOVERSION 1
  PUBLIC_HEADER libshare.h
)

file(GLOB SOURCE_FILES binding.cpp)

add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})

# Gives our library file a .node extension without any "lib" prefix
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "" SUFFIX ".node")

# Essential include files to build a node addon,
# You should add this line in every CMake.js based project
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_JS_INC})

# Essential library files to link to a node addon
# You should add this line in every CMake.js based project
target_link_libraries(${PROJECT_NAME} ${CMAKE_JS_LIB})
target_link_libraries(${PROJECT_NAME} share)
