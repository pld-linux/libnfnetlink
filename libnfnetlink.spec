Summary:	low-level library for netfilter related kernel/userspace communication
Summary(pl):	Niskopoziomowa biblioteka do związanej z netfiltrem komunikacji między jądrem a przestrzenią użytkownika
Name:		libnfnetlink
Version:	0.0.16
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnfnetlink/%{name}-%{version}.tar.bz2
# Source0-md5:	5c9b7fc55c5cc7869ecf2ae5ac8afff3
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

%description -l pl
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
Summary(pl):	Pliki nagłówkowe biblioteki libnfnetlink
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	linux-libc-headers >= %{_llh_version}

%description devel
Header files for libnfnetlink library.

%description devel -l pl
Pliki nagłówkowe biblioteki libnfnetlink.

%package static
Summary:	Static libnfnetlink library
Summary(pl):	Statyczna biblioteka libnfnetlink
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnfnetlink library.

%description static -l pl
Statyczna biblioteka libnfnetlink.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
