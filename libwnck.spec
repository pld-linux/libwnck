Summary:	General Window Manager interfacing for GNOME utilities
Summary(pl):	Interfejs General Window Manager dla narzêdzi GNOME
Name:		libwnck
Version:	2.7.90
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	bd58db8d639586727639e307d68094d9
Patch0:		%{name}-locale-names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.6
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
Requires:	gtk+2-devel >= 2:2.4.4
Requires:	startup-notification-devel >= 0.6

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
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
