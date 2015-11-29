Summary:	Python binding to unicap video capture library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki przechwytywania obrazu unicap
Name:		python-unicap
Version:	0.3.0
Release:	2
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: http://unicap-imaging.org/download.htm
Source0:	http://unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7afcb0a1d03579baa1107f3e760d67b2
URL:		http://unicap-imaging.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	libucil-devel
BuildRequires:	libunicap-devel
BuildRequires:	libunicapgtk-devel
BuildRequires:	python-devel
BuildRequires:	python-pygobject-devel >= 2.0
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	rpm-pythonprov
Requires:	python-pygobject >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyunicap is a Python extension to access video capture devices
supported by the unicap library from Python programs.

%description -l pl.UTF-8
pyunicap to rozszerzenie Pythona pozwalające na dostęp do urządzeń
przechwytujących obraz obsługiwanych przez bibliotekę unicap z poziomu
programów w Pythonie.

%package -n python-unicapgtk
Summary:	Python binding for unicapgtk video capturing widget
Summary(pl.UTF-8):	Wiązanie Pythona do widgetu przechwytywania obrazu unicapgtk
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.0

%description -n python-unicapgtk
Python binding for unicapgtk video capturing widget.

%description -n python-unicapgtk -l pl.UTF-8
Wiązanie Pythona do widgetu przechwytywania obrazu unicapgtk.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd src
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{py_sitedir}/unicap.so
%{py_sitedir}/Unicap-1.0-py*.egg-info

%files -n python-unicapgtk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/unicapgtk.so
%{py_sitedir}/UnicapGtk-1.0-py*.egg-info
