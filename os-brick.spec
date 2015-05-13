# Created by pyp2rpm-1.1.2
%global pypi_name os-brick

Name:           os-brick
Version:        XXX
Release:        XXX{?dist}
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:	python-oslo-sphinx


%description
===============================
brick
===============================
OpenStack Cinder brick library for managing local volume attaches


Features
--------

* Discovery of volumes being attached to a host for many transport
protocols.
* Removal of volumes from a host.

For any other imformation,
refer to the parent project, Cinder:
  https://github.com/openstack/cinder

* License: Apache 2.0

%prep
%setup -q -n %{name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%license LICENSE
%doc html README.rst doc/source/readme.rst
%{python2_sitelib}/os_brick*

%changelog
* Wed May 13 2015 jpena <jpena@redhat.com> - 0.1.0-1
- Initial package.
