#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	General Window Manager interfacing for GNOME utilities
Summary(pl):	Interfejs General Window Manager dla narzêdzi GNOME
Name:		libwnck
Version:	2.14.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libwnck/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	df5c7a764e81a7214d493194ee394918
Patch0:		%{name}-compiz.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.8.18
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General Window Manager interfacing for GNOME utilities. This library
is a part of the GNOME 2 platform.

%description -l pl
Ogólny interfejs zarz±dcy okien dla narzêdzi GNOME. Ta biblioteka jest
czê¶ci± platformy GNOME 2.

%package devel
Summary:	Header files and documentation for libwnck
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla libwnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.8.18
Requires:	gtk-doc-common
Requires:	startup-notification-devel >= 0.8

%description devel
Header, docs and development libraries for libwnck.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libwnck.

%package static
Summary:	Static libwnck libraries
Summary(pl):	Statyczne biblioteki libwnck
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libwnck libraries.

%description static -l pl
Statyczna wersja bibliotek libwnck.

%prep
%setup -q
%patch0 -p0

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
