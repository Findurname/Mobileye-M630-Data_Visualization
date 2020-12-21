## Reference: https://stackoverflow.com/questions/49221565/unable-to-use-cv-bridge-with-ros-kinetic-and-python3



sudo apt-get install python-catkin-tools python3-dev python3-catkin-pkg-modules python3-numpy python3-yaml ros-melodic-cv-bridge
catkin init

catkin config -DPYTHON_EXECUTABLE=/home/jerry/anaconda3/bin/python3 -DPYTHON_INCLUDE_DIR=/home/jerry/anaconda3/include/python3.7m -DPYTHON_LIBRARY=/home/jerry/anaconda3/lib/libpython3.7m.so
# Instruct catkin to install built packages into install place. It is $CATKIN_WORKSPACE/install folder
catkin config --install
# Clone cv_bridge src
git clone https://github.com/ros-perception/vision_opencv.git src/vision_opencv
# Find version of cv_bridge in your repository
apt-cache show ros-melodic-cv-bridge | grep Version

cd src/vision_opencv/
git checkout 1.13.0
cd ../../
# Build
catkin build cv_bridge -DSETUPTOOLS_DEB_LAYOUT=OFF
# Extend environment with new package
source install/setup.zsh --extend