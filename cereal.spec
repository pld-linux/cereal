%bcond_without	tests
Summary:	A header-only C++11 serialization library
Name:		cereal
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries
URL:		http://uscilab.github.io/cereal/
Source0:	https://github.com/USCiLab/cereal/archive/v%{version}.tar.gz
# Source0-md5:	4342e811f245403646c4175258f413f1
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel

%define		_enable_debug_packages	0

%description
cereal is a header-only C++11 serialization library. cereal takes
arbitrary data types and reversibly turns them into different
representations, such as compact binary encodings, XML, or JSON.
cereal was designed to be fast, light-weight, and easy to extend - it
has no external dependencies and can be easily bundled with other code
or used standalone.

%package devel
Summary:	Development headers and libraries for %{name}
Group:		Development/Libraries
BuildArch:	noarch

%description devel
cereal is a header-only C++11 serialization library. cereal takes
arbitrary data types and reversibly turns them into different
representations, such as compact binary encodings, XML, or JSON.
cereal was designed to be fast, light-weight, and easy to extend - it
has no external dependencies and can be easily bundled with other code
or used standalone.

This package contains development headers and libraries for the cereal
library.

%prep
%setup -q

%build
install -d build
cd build
%{cmake} \
	-DSKIP_PORTABILITY_TEST=ON \
	-DWITH_WERROR=OFF \
	..
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README.md
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}
