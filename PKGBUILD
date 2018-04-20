# Script generated with Bloom
pkgdesc="ROS - Provides forward and inverse kinematics for Universal Robots designs. See http://hdl.handle.net/1853/50782 for details."
url='http://wiki.ros.org/ur_kinematics'

pkgname='ros-kinetic-ur-kinematics'
pkgver='1.2.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-core'
'ros-kinetic-moveit-kinematics'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-tf-conversions'
)

depends=('boost'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-core'
'ros-kinetic-moveit-kinematics'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-tf-conversions'
)

conflicts=()
replaces=()

_dir=ur_kinematics
source=()
md5sums=()

prepare() {
    cp -R $startdir/ur_kinematics $srcdir/ur_kinematics
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

