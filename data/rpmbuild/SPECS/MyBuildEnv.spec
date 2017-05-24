%define version 1.0
%define name MyBuildEnv
%define sources ../SOURCES



Summary: This package contains my rpm build env
Name: %{name} 
Version: %{version}
Release: 20170109
License: BOUDI Ludovic
Source: %{sources}/%{name}_resource-%{version}.tgz
ExclusiveArch: noarch
%description
This package only deploy my personal rpm build environnement
%prep
%setup -qc

%install
%mkdir_in_build_root /data/rpmbuild 
%mkdir_in_build_root /data/rpmbuild/resources
%mkdir_in_build_root /data/rpmbuild/macro
%mkdir_in_build_root /data/rpmbuild/BUILD
%mkdir_in_build_root /data/rpmbuild/BUILDROOT
%mkdir_in_build_root /data/rpmbuild/SPECS
%mkdir_in_build_root /data/rpmbuild/SOURCES
%mkdir_in_build_root /data/rpmbuild/RPMS
%mkdir_in_build_root /data/rpmbuild/SRPMS
%copy_to_build_root rpmmacros /data/rpmbuild/macro
%copy_to_build_root build.sh /data/rpmbuild
%copy_to_build_root generate_source.sh /data/rpmbuild/resources
%copy_to_build_root MyBuildEnv.spec /data/rpmbuild/SPECS

%files
%attr(777, root, root) /data/rpmbuild
%attr(777, root, root) /data/rpmbuild/resources
%attr(777, root, root) /data/rpmbuild/macro
%attr(777, root, root) /data/rpmbuild/BUILD
%attr(777, root, root) /data/rpmbuild/BUILDROOT
%attr(777, root, root) /data/rpmbuild/SPECS
%attr(777, root, root) /data/rpmbuild/SOURCES
%attr(777, root, root) /data/rpmbuild/RPMS
%attr(777, root, root) /data/rpmbuild/SRPMS
%attr(777, root, root) /data/rpmbuild/SPECS/MyBuildEnv.spec
%attr(777, root, root) /data/rpmbuild/macro/rpmmacros
%attr(777, root, root) /data/rpmbuild/build.sh
%attr(777, root, root) /data/rpmbuild/resources/generate_source.sh

%clean
[ "$RPM_BUILD_ROOT" != "/"] && rm -rf "$RPM_BUILD_ROOT"



