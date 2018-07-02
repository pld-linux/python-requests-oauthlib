# Conditional build:
%bcond_without  python2         # build python 2 module
%bcond_without  python3         # build python 3 module

%define		module		requests_oauthlib
%define		egg_name	requests_oauthlib
%define		pypi_name	requests-oauthlib
Summary:	First-class OAuth library support for python-requests
Name:		python-%{pypi_name}
Version:	0.8.0
Release:	3
License:	ISC
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	4358a879a4377393bcfd37d0f9ae6d4d
URL:		https://github.com/requests/requests-oauthlib
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules >= 1:2.6
Requires:	python-oauthlib >= 0.4.2
Requires:	python-requests >= 1.0.0
Obsoletes:	python-requests_oauthlib < 0.6.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
First-class OAuth library support for python-requests.

%package -n python3-%{pypi_name}
Summary:	First-class OAuth library support for python-requests
Group:		Development/Languages/Python
Requires:	python3-modules >= 3.2
Requires:	python3-oauthlib >= 0.4.2
Requires:	python3-requests >= 1.0.0
Obsoletes:	python3-requests_oauthlib < 0.6.1-3

%description -n python3-%{pypi_name}
First-class OAuth library support for python-requests.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
