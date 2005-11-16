Summary:	libnfnetlink - low-level library for netfilter related kernel/userspace communication
Name:		libnfnetlink
Version:	0.0.13
Release:	1@%{_kernel_ver_str}
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnfnetlink/%{name}-%{version}.tar.bz2
# Source0-md5:	cc9e6d5f42f5a64dc29da724c9c88908
URL:		http://www.netfilter.org/projects/libnfnetlink/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers >= 2.6.14.0
Requires:	kernel = 3:%{_kernel_ver}
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

%package devel
Summary:	Header files for libnfnetlink library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnfnetlink library.

%package static
Summary:	Static libnfnetlink library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnfnetlink library.

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
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
