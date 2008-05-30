Summary:	low-level library for netfilter related kernel/userspace communication
Summary(pl.UTF-8):	Niskopoziomowa biblioteka do związanej z netfiltrem komunikacji między jądrem a przestrzenią użytkownika
Name:		libnfnetlink
Version:	0.0.33
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnfnetlink/files/%{name}-%{version}.tar.bz2
# Source0-md5:	b97bc6747cb4e65b9989daa136f339cb
URL:		http://www.netfilter.org/projects/libnfnetlink/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%define		_llh_version	7:2.6.12.0-9
BuildRequires:	linux-libc-headers >= %{_llh_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication. It provides a generic messaging
infrastructure for in-kernel netfilter subsystems (such as
nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) and their
respective users and/or management tools in userspace. This library is
not meant as a public API for application developers. It is only used
by other netfilter.org projects, such as libnetfilter_log,
libnetfilter_queue or libnetfilter_conntrack.

%description -l pl.UTF-8
libnfnetlink to niskopoziomowa biblioteka do związanej z netfiltrem
komunikacji między jądrem a przestrzenią użytkownika. Udostępnia
ogólną infrastrukturę komunikatów dla podsystemów netfiltra w jądrze
(takich jak nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) oraz
ich użytkowników i/lub narzędzi zarządzających w przestrzeni
użytkownika. Ta biblioteka nie jest przeznaczona jako publiczne API
dla twórców aplikacji; jest jedynie używana przez inne projekty
netfilter.org, takie jak libnetfilter_log, libnetfilter_queue czy
libnetfilter_conntrack.

%package devel
Summary:	Header files for libnfnetlink library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnfnetlink
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	linux-libc-headers >= %{_llh_version}

%description devel
Header files for libnfnetlink library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnfnetlink.

%package static
Summary:	Static libnfnetlink library
Summary(pl.UTF-8):	Statyczna biblioteka libnfnetlink
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnfnetlink library.

%description static -l pl.UTF-8
Statyczna biblioteka libnfnetlink.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libnfnetlink.so.*.*.*
%ghost %{_libdir}/libnfnetlink.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnfnetlink.so
%{_libdir}/libnfnetlink.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnfnetlink.a
