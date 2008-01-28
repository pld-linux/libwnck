#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	General Window Manager interfacing for GNOME utilities
Summary(pl.UTF-8):	Interfejs General Window Manager dla narzędzi GNOME
Name:		libwnck
Version:	2.21.90
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libwnck/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	a5397d164522fdf1f8dd26b1252db8f0
Patch0:		%{name}-compiz.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.3
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXres-devel
Requires:	gtk+2 >= 2:2.12.5
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
Requires:	gtk+2-devel >= 2:2.12.5
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
# needs update!
#%patch0 -p0

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/wnckprop
%attr(755,root,root) %{_libdir}/libwnck-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwnck-1.so.22

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwnck-1.so
%{_libdir}/libwnck-1.la
%{_includedir}/libwnck-1.0
%{_pkgconfigdir}/libwnck-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwnck-1.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libwnck
%endif
