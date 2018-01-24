cmake_minimum_required(VERSION 3.9)

project(dependent)

if (APPLE)
  SET(LINK_FLAGS "-L${CMAKE_SOURCE_DIR}/../version-2/build/Release -lazy-lshare")
elseif(UNIX)
  SET(LINK_FLAGS "-L${CMAKE_SOURCE_DIR}/../version-2/build/Release -z lazy -lshare")
endif()

file(GLOB SOURCE_FILES binding.cpp libshare.h)

add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})

# Gives our library file a .node extension without any "lib" prefix
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "" SUFFIX ".node" LINK_FLAGS ${LINK_FLAGS})

# Essential include files to build a node addon,
# You should add this line in every CMake.js based project
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_JS_INC})

# Essential library files to link to a node addon
# You should add this line in every CMake.js based project
target_link_libraries(${PROJECT_NAME} ${CMAKE_JS_LIB})
