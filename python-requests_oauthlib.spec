# Conditional build:
%bcond_without  python2         # build python 2 module
%bcond_without  python3         # build python 3 module
#
%define 	module	requests_oauthlib
Summary:	First-class OAuth library support for python-requests
Name:		python-%{module}
Version:	0.5.0
Release:	3
License:	ISC
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/r/requests-oauthlib/requests-oauthlib-%{version}.tar.gz
# Source0-md5:	139a17c495fb593b5842634faf72ebb0
URL:		https://github.com/requests/requests-oauthlib
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.6
Requires:	python-oauthlib >= 0.4.2
Requires:	python-requests >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
First-class OAuth library support for python-requests.

%package -n python3-requests_oauthlib
Summary:	First-class OAuth library support for python-requests
Group:		Development/Languages/Python
Requires:	python3-modules >= 3.2
Requires:	python3-oauthlib >= 0.4.2
Requires:	python3-requests >= 1.0.0

%description -n python3-requests_oauthlib
First-class OAuth library support for python-requests.

%prep
%setup -q -n requests-oauthlib-%{version}

%build
%if %{with python2}
%py_build -b py2
%endif

%if %{with python3}
%py3_build -b py3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build -b py2 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py  \
	build -b py3 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%{__rm} -rf $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py3_sitescriptdir}}/%{module}/{cacert.pem,packages}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-requests_oauthlib
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
