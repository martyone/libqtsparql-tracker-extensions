Name: libqtsparql-tracker-extensions
Version: 0.0.11
Release: 1
Summary: Tracker-specific add-on for QtSparql
Group:   System/Libraries
License: LGPLv2
URL:     http://gitorious.org/+maemo-af-developers/maemo-af/libqtsparql-tracker
Source0: %{name}-%{version}.tar.gz
Patch0: fix-tests.patch
Patch1: increase-timeouts.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: libqtsparql-devel
BuildRequires: libtool
BuildRequires: pkgconfig(QtCore)
BuildRequires: fdupes  

%description
Tracker-specific add-on for QtSparql.

%package devel
Summary:  Qt Sparql development files
Group:    Development/Libraries
Requires:  %{name} >= %{version}

%description devel
Tracker-specific add-on for QtSparql.
documentation

%package tests
Summary:  QtSparql testsuite 
Group:    System/X11
Requires:  %{name} >= %{version}
Requires: libqtsparql-tracker-extensions >= 0.0.1

%description tests
Tests for libqtsparql-tracker-extensions.

%package live-tests
Summary:  QtSparql testsuite 
Group:    System/X11
Requires:  %{name} >= %{version}
Requires: libqtsparql-tracker-extensions >= 0.0.1

%description live-tests
Live tests for libqtsparql-tracker-extensions.

%package doc  
Summary:    API reference for libqtsparql-tracker-extensions
Group:      Documentation  
Requires:   %{name} = %{version}-%{release}  
  
%description doc  
Description: %{summary}  

%prep
%setup -q -n %{name}-%{version}/libqtsparql-tracker

%patch0 -p1
%patch1 -p1

%build
./autogen.sh
./configure -prefix /usr
make 
make doc

%install
%make_install
sed -i 's,-L/home/abuild/[^ ]*,,' %{buildroot}/%{_libdir}/pkgconfig/*.pc
mv %{buildroot}/%{_datadir}/doc/ %{buildroot}/%{_datadir}/libqtsparql-tracker-live-doc
%fdupes  %{buildroot}/%{_datadir}  

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel 
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libqtsparqltrackerextensions.so.*
%{_libdir}/libqtsparqltrackerlive.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_libdir}/libqtsparqltrackerextensions.so
%{_libdir}/libqtsparqltrackerlive.so
%{_includedir}/QtSparqlTrackerExtensions/*
%{_includedir}/QtSparqlTrackerLive/*
%{_datadir}/qt4/mkspecs/features/*

%files tests
%defattr(-,root,root,-)
%{_libdir}/libqtsparql-tracker-extensions-tests/*
%{_datadir}/libqtsparql-tracker-extensions-tests/*

%files live-tests
%defattr(-,root,root,-)
%{_libdir}/libqtsparql-tracker-live-tests/*
%{_datadir}/libqtsparql-tracker-live-tests/*

%files doc 
%defattr(-,root,root,-)
%{_datadir}/libqtsparql-tracker-live-doc/*
