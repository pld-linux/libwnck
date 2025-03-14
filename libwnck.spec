#
# Conditional build:
%bcond_without	apidocs		# gtk-doc API documentation
%bcond_without	static_libs	# static library

Summary:	General Window Manager interfacing for GNOME utilities
Summary(pl.UTF-8):	Interfejs General Window Manager dla narzędzi GNOME
Name:		libwnck
Version:	43.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libwnck/43/%{name}-%{version}.tar.xz
# Source0-md5:	b8c29ef589d3427c8a699c1542a2d25e
URL:		https://gitlab.gnome.org/GNOME/libwnck
# cairo-xlib-xrender
BuildRequires:	cairo-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 0.6.14
BuildRequires:	gtk+3-devel >= 3.22.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXres-devel >= 1.2
BuildRequires:	xz
Requires:	glib2 >= 1:2.44
Requires:	gtk+3 >= 3.22.0
Requires:	startup-notification >= 0.8
Requires:	xorg-lib-libXres >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General Window Manager interfacing for GNOME utilities. This library
is a part of the GNOME 2 platform.

%description -l pl.UTF-8
Ogólny interfejs zarządcy okien dla narzędzi GNOME. Ta biblioteka jest
częścią platformy GNOME 2.

%package tools
Summary:	Small tools to manage windows
Summary(pl.UTF-8):	Małe narzędzia do zarządzania oknami
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description tools
Small tools to manage windows.

%description tools -l pl.UTF-8
Małe narzędzia do zarządzania oknami.

%package devel
Summary:	Header files and documentation for libwnck
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla libwnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel
Requires:	glib2-devel >= 1:2.44
Requires:	gtk+3-devel >= 3.22.0
Requires:	startup-notification-devel >= 0.8
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXres-devel >= 1.2

%description devel
Header, docs and development libraries for libwnck.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libwnck.

%package static
Summary:	Static libwnck libraries
Summary(pl.UTF-8):	Statyczne biblioteki libwnck
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libwnck libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libwnck.

%package apidocs
Summary:	libwnck API documentation
Summary(pl.UTF-8):	Dokumentacja API libwnck
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libwnck API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libwnck.

%prep
%setup -q

%if %{with static_libs}
%{__sed} -i -e '/^libwnck_lib/ s/shared_library/library/' libwnck/meson.build
%endif

%build
%meson \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dstartup_notification=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README rationales.txt
%attr(755,root,root) %{_libdir}/libwnck-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwnck-3.so.0
%{_libdir}/girepository-1.0/Wnck-3.0.typelib

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wnck-urgency-monitor
%attr(755,root,root) %{_bindir}/wnckprop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwnck-3.so
%{_includedir}/libwnck-3.0
%{_pkgconfigdir}/libwnck-3.0.pc
%{_datadir}/gir-1.0/Wnck-3.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwnck-3.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libwnck-3.0
%endif
