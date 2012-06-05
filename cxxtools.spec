
%define name	cxxtools
%define version	2.1.1
%define rel	1

# NOTE: when updating, make sure tntnet and vdr-plugin-live still build. -Anssi

%define major	8
%define libname	%mklibname cxxtools %major
%define devname	%mklibname cxxtools -d

Summary:	Toolbox with reusable c++ components
Name:		%name
Version:	%version
Release:	%rel
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://www.tntnet.org/
Source0:	http://www.tntnet.org/download/%name-%version.tar.gz

%description
Toolbox with reusable c++ components.

%package -n %libname
Summary:	Shared library of cxxtools
Group:		System/Libraries

%description -n %libname
Toolbox with reusable c++ components.

%package -n %devname
Summary:	Headers and static library for cxxtools development
Group:		Development/C++
Requires:	%libname = %version
Provides:	cxxtools-devel = %version-%release

%description -n %devname
Toolbox with reusable c++ components.

%prep
%setup -q
# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build
./configure     --disable-static \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--disable-dependency-tracking \
		--disable-demos \
		--disable-unittest
make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/cxxtools-config

%files -n %libname
%{_libdir}/*.so.%{major}*

%files -n %devname
%doc README AUTHORS
%{_bindir}/cxxtools-config
%{multiarch_bindir}/cxxtools-config
%{_libdir}/*.so
%{_includedir}/%{name}
