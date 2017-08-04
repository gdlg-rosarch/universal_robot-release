Name:           ros-indigo-universal-robot
Version:        1.1.10
Release:        0%{?dist}
Summary:        ROS universal_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/universal_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-ur-bringup
Requires:       ros-indigo-ur-description
Requires:       ros-indigo-ur-driver
Requires:       ros-indigo-ur-gazebo
Requires:       ros-indigo-ur-kinematics
Requires:       ros-indigo-ur-msgs
Requires:       ros-indigo-ur10-moveit-config
Requires:       ros-indigo-ur3-moveit-config
Requires:       ros-indigo-ur5-moveit-config
BuildRequires:  ros-indigo-catkin

%description
Drivers, description, and utilities for Universal Robot Arms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 04 2017 Felix Messmer <fxm@ipa.fhg.de> - 1.1.10-0
- Autogenerated by Bloom

* Mon Jan 02 2017 Felix Messmer <fxm@ipa.fhg.de> - 1.1.9-0
- Autogenerated by Bloom

* Fri Dec 30 2016 Felix Messmer <fxm@ipa.fhg.de> - 1.1.8-0
- Autogenerated by Bloom

* Fri Dec 30 2016 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.6-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.5-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.0.3-0
- Autogenerated by Bloom

