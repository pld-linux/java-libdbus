Summary:	Java 1.5 bindings for D-BUS library
Summary(pl.UTF-8):   Dowiązania Javy 1.5 dla biblioteki D-BUS
Name:		java-libdbus
Version:	1.13
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Development/Languages/Java
Source0:	http://dbus.freedesktop.org/releases/dbus-java/libdbus-java-%{version}.tar.gz
# Source0-md5:	3edbd6b16aef2d4b7b18ba101344e3e9
Patch0:		%{name}-make.patch
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	dbus-devel >= 0.90
BuildRequires:	docbook-to-man
BuildRequires:	jdk >= 1.5
BuildRequires:	tex4ht
Requires:	dbus-libs >= 0.90
Requires:	jre >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java 1.5 bindings for D-BUS library.

%description -l pl.UTF-8
Dowiązania Javy 1.5 dla biblioteki D-BUS.

%prep
%setup -q -n libdbus-java-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags}"

%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	BINPREFIX=$RPM_BUILD_ROOT%{_bindir} \
	DOCPREFIX=`pwd`/docs \
	JARPREFIX=$RPM_BUILD_ROOT%{_javadir} \
	LIBPREFIX=$RPM_BUILD_ROOT%{_libdir} \
	MANPREFIX=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README changelog
# javadoc
%doc doc/api
%attr(755,root,root) %{_bindir}/DBusViewer
%attr(755,root,root) %{_bindir}/CreateInterface
%attr(755,root,root) %{_bindir}/ListDBus
%attr(755,root,root) %{_libdir}/libdbus-java.so
%{_javadir}/dbus*.jar
%{_mandir}/man1/DBusViewer.1*
%{_mandir}/man1/CreateInterface.1*
%{_mandir}/man1/ListDBus.1*
