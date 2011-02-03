#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	General Window Manager interfacing for GNOME utilities
Summary(pl.UTF-8):	Interfejs General Window Manager dla narzędzi GNOME
Name:		libwnck
Version:	2.91.6
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libwnck/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	f50e90f795626fee7fb07f00e9b76795
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gobject-introspection-devel >= 0.6.14
BuildRequires:	gtk+3-devel >= 2.91.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libX11-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General Window Manager interfacing for GNOME utilities. This library
is a part of the GNOME 2 platform.

%description -l pl.UTF-8
Ogólny interfejs zarządcy okien dla narzędzi GNOME. Ta biblioteka jest
częścią platformy GNOME 2.

%package devel
Summary:	Header files and documentation for libwnck
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla libwnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 2.91.5
Requires:	startup-notification-devel >= 0.8
Requires:	xorg-lib-libXres-devel

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

%description apidocs
libwnck API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libwnck.

%prep
%setup -q

%{__sed} -i -e 's/^en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwnck-3.la

%find_lang %{name}-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/wnck-urgency-monitor
%attr(755,root,root) %{_bindir}/wnckprop
%attr(755,root,root) %{_libdir}/libwnck-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwnck-3.so.0
%{_libdir}/girepository-1.0/Wnck-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwnck-3.so
%{_includedir}/libwnck-3.0
%{_pkgconfigdir}/libwnck-3.0.pc
%{_datadir}/gir-1.0/Wnck-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libwnck-3.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libwnck-3.0
%endif
