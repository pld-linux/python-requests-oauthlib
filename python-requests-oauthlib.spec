#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module		requests_oauthlib
%define		egg_name	requests_oauthlib
%define		pypi_name	requests-oauthlib
Summary:	OAuthlib authentication support for Requests
Summary(pl.UTF-8):	Obsługa uwierzytelniania przez OAuthlib dla Requests
Name:		python-%{pypi_name}
Version:	1.3.0
Release:	6
License:	ISC
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/requests-oauthlib/
Source0:	https://files.pythonhosted.org/packages/source/r/requests-oauthlib/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	1ebcd55f1b1b9281940b4bc33010e2ba
URL:		https://github.com/requests/requests-oauthlib
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography
BuildRequires:	python-mock
BuildRequires:	python-oauthlib >= 3.0.0
BuildRequires:	python-pyjwt >= 1.0.0
BuildRequires:	python-requests >= 2.0.0
BuildRequires:	python-requests-mock
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography
BuildRequires:	python3-oauthlib >= 3.0.0
BuildRequires:	python3-pyjwt >= 1.0.0
BuildRequires:	python3-requests >= 2.0.0
BuildRequires:	python3-requests-mock
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
Obsoletes:	python-requests_oauthlib < 0.6.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides first-class OAuth library support for Requests.

%description -l pl.UTF-8
Ten pakiet zapewnia obsługę biblioteki OAuth dla Requests.

%package -n python3-%{pypi_name}
Summary:	OAuthlib authentication support for Requests
Summary(pl.UTF-8):	Obsługa uwierzytelniania przez OAuthlib dla Requests
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.4
Obsoletes:	python3-requests_oauthlib < 0.6.1-3

%description -n python3-%{pypi_name}
This project provides first-class OAuth library support for Requests.

%description -n python3-%{pypi_name} -l pl.UTF-8
Ten pakiet zapewnia obsługę biblioteki OAuth dla Requests.

%package apidocs
Summary:	API documentation for requests-oauthlib module
Summary(pl.UTF-8):	Dokumentacja API biblioteki requests-oauthlib
Group:		Documentation

%description apidocs
API documentation for requests-oauthlib module.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki requests-oauthlib.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

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
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,examples,*.html,*.js}
%endif
