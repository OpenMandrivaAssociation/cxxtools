
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
URL:		https://www.tntnet.org/
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


%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1.1-1
+ Revision: 802668
- version update 2.1.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.8-3mdv2011.0
+ Revision: 610186
- rebuild

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 1.4.8-2mdv2010.1
+ Revision: 501446
- fix build (use-right-eof-value.patch from upstream)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Sep 06 2008 Emmanuel Andry <eandry@mandriva.org> 1.4.8-1mdv2009.0
+ Revision: 281915
- New version
- New major 6

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 24 2008 Anssi Hannula <anssi@mandriva.org> 1.4.7-2mdv2009.0
+ Revision: 197071
- new version
- new major

* Sat Jan 19 2008 Anssi Hannula <anssi@mandriva.org> 1.4.6-1mdv2008.1
+ Revision: 155075
- initial Mandriva release

