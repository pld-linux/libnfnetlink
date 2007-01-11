Summary:	low-level library for netfilter related kernel/userspace communication
Summary(pl):	Niskopoziomowa biblioteka do zwi±zanej z netfiltrem komunikacji miêdzy j±drem a przestrzeni± u¿ytkownika
Name:		libnfnetlink
Version:	0.0.25
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnfnetlink/files/%{name}-%{version}.tar.bz2
# Source0-md5:	fc915a2e66d282e524af6ef939042d7d
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
libnfnetlink to niskopoziomowa biblioteka do zwi±zanej z netfiltrem
komunikacji miêdzy j±drem a przestrzeni± u¿ytkownika. Udostêpnia
ogóln± infrastrukturê komunikatów dla podsystemów netfiltra w j±drze
(takich jak nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) oraz
ich u¿ytkowników i/lub narzêdzi zarz±dzaj±cych w przestrzeni
u¿ytkownika. Ta biblioteka nie jest przeznaczona jako publiczne API
dla twórców aplikacji; jest jedynie u¿ywana przez inne projekty
netfilter.org, takie jak libnetfilter_log, libnetfilter_queue czy
libnetfilter_conntrack.

%package devel
Summary:	Header files for libnfnetlink library
Summary(pl):	Pliki nag³ówkowe biblioteki libnfnetlink
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	linux-libc-headers >= %{_llh_version}

%description devel
Header files for libnfnetlink library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libnfnetlink.

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
