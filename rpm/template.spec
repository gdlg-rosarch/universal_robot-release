Name:           ros-indigo-ur-bringup
Version:        1.1.7
Release:        0%{?dist}
Summary:        ROS ur_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ur_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-ur-description
Requires:       ros-indigo-ur-driver
BuildRequires:  ros-indigo-catkin

%description
The ur_bringup package

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
* Fri Dec 30 2016 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.6-0
- Autogenerated by Bloom

