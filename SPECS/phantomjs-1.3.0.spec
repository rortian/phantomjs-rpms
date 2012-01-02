Summary: PhantomJS is a headless WebKit with JavaScript API
Name: phantomjs
Version: 1.3.0
Release: 9%{?dist}
License: BSD
Group: unknown
URL: http://code.google.com/p/phantomjs/
Source0: %{name}-%{version}-source.tar.gz
Source1: xvfb-run.sh
BuildRequires: qt-devel
BuildRequires: qt-webkit-devel
BuildRequires: sqlite-devel
Requires: qt
Requires: qt-webkit
Requires: xorg-x11-xauth
Requires: xorg-x11-server-Xvfb
Requires: xorg-x11-server-Xorg
Requires: xorg-x11-fonts-100dpi
Requires: xorg-x11-fonts-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-14-100dpi
Requires: xorg-x11-fonts-ISO8859-14-75dpi
Requires: xorg-x11-fonts-ISO8859-15-100dpi
Requires: xorg-x11-fonts-ISO8859-15-75dpi
Requires: xorg-x11-fonts-ISO8859-2-100dpi
Requires: xorg-x11-fonts-ISO8859-2-75dpi
Requires: xorg-x11-fonts-ISO8859-9-100dpi
Requires: xorg-x11-fonts-ISO8859-9-75dpi
Requires: xorg-x11-fonts-Type1
Requires: xorg-x11-fonts-base
Requires: xorg-x11-fonts-cyrillic
Requires: xorg-x11-fonts-ethiopic
Requires: xorg-x11-fonts-misc
%if 0%{?el5}
Requires: xorg-x11-fonts-syriac
Requires: xorg-x11-fonts-truetype
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q

%build
qmake-qt4
make

%install
rm -rf "$RPM_BUILD_ROOT"

mkdir -p "$RPM_BUILD_ROOT/usr/bin"
cp bin/* "$RPM_BUILD_ROOT/usr/bin"
%if 0%{?el5}
cp %SOURCE1 "$RPM_BUILD_ROOT/usr/bin/xvfb-run"
%endif
find "$RPM_BUILD_ROOT/usr/bin" -type f -exec chmod 755 '{}' ';'

mkdir -p "$RPM_BUILD_ROOT/usr/share/doc/%{name}"
cp -r examples "$RPM_BUILD_ROOT/usr/share/doc/%{name}/"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/bin/phantomjs
/usr/share/doc/%{name}/examples
%if 0%{?el5}
/usr/bin/xvfb-run
%endif

%changelog
* Tue Sep 27 2011 Jens Braeuer <jens@numberfour.eu> - 1.3.0-6
- Package 1.3.0/Water Lily for SL6.1. Tested on el5 and el6 only.

* Thu Sep 22 2011 Jens Braeuer <jens@numberfour.eu> - 
- Initial build.

