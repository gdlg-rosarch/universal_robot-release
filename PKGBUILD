# Script generated with Bloom
pkgdesc="ROS - Driver for the UR5/10 arm based on the Polyscope control scheme."
url='http://ros.org/wiki/ur_driver'

pkgname='ros-kinetic-ur-driver'
pkgver='1.2.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
)

depends=('python2-lxml'
'ros-kinetic-actionlib'
'ros-kinetic-control-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-ur-msgs'
)

conflicts=()
replaces=()

_dir=ur_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/ur_driver $srcdir/ur_driver
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

