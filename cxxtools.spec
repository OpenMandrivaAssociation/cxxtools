
%define name	cxxtools
%define version	1.4.8
%define rel	2

# NOTE: when updating, make sure tntnet and vdr-plugin-live still build. -Anssi

%define major	6
%define libname	%mklibname cxxtools %major
%define devname	%mklibname cxxtools -d

Summary:	Toolbox with reusable c++ components
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://www.tntnet.org/
Source:		http://www.tntnet.org/download/%name-%version.tar.gz
# from upstream, fixes build:
Patch0:		cxxtools-605-use-right-eof-value.patch
BuildRoot:	%{_tmppath}/%{name}-root

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
%apply_patches

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/cxxtools-config

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%{_libdir}/*.so.%{major}*

%files -n %devname
%doc README AUTHORS
%{_bindir}/cxxtools-config
%{multiarch_bindir}/cxxtools-config
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}
