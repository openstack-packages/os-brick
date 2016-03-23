%if 0%{?fedora}
# There are some missing deps
%global with_python3 0
%endif

%global pypi_name os-brick

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
OpenStack Cinder brick library for managing local volume attaches

%package -n python2-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python2-%{pypi_name}}
Provides:       os-brick = %{version}-%{release}

Requires:       python-babel >= 1.3
Requires:       python-eventlet >= 0.17.4
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-concurrency >= 2.3.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-log >= 1.8.0
Requires:       python-oslo-service >= 0.7.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-requests >= 2.5.2
Requires:       python-retrying
Requires:       python-six >= 1.9.0

BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.6.0
BuildRequires:  python-reno
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-concurrency  >= 2.3.0
BuildRequires:  python-oslo-i18n >= 1.5.0
BuildRequires:  python-oslo-log >= 1.8.0
BuildRequires:  python-oslo-service >= 0.7.0
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildRequires:  python-requests >= 2.5.2
BuildRequires:  python-six >= 1.9.0
BuildRequires:  python-setuptools

%description -n python2-%{pypi_name}
OpenStack Cinder brick library for managing local volume attaches

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-babel >= 1.3
Requires:       python3-eventlet >= 0.17.4
Requires:       python3-oslo-serialization >= 1.4.0
Requires:       python3-oslo-concurrency >= 2.3.0
Requires:       python3-oslo-i18n >= 1.5.0
Requires:       python3-oslo-log >= 1.8.0
Requires:       python3-oslo-service >= 0.7.0
Requires:       python3-oslo-utils >= 2.0.0
Requires:       python3-requests >= 2.5.2
Requires:       python3-retrying
Requires:       python3-six >= 1.9.0

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.6.0
BuildRequires:  python3-reno
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-concurrency  >= 2.3.0
BuildRequires:  python3-oslo-i18n >= 1.5.0
BuildRequires:  python3-oslo-log >= 1.8.0
BuildRequires:  python3-oslo-service >= 0.7.0
BuildRequires:  python3-oslo-sphinx >= 2.5.0
BuildRequires:  python3-requests >= 2.5.2
BuildRequires:  python3-six >= 1.9.0
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
OpenStack Cinder brick library for managing local volume attaches

%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%py3_install
%endif

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap

%files -n python2-%{pypi_name}
%license LICENSE
%doc html README.rst
%{python2_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc html README.rst
%{python3_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%endif

%changelog
* Wed Mar 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 1.1.0-
- Update to 1.1.0

