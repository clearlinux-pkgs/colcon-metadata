#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-metadata
Version  : 0.2.5
Release  : 16
URL      : https://files.pythonhosted.org/packages/9e/f9/a8cad1da3626ef7e94779fa395ca274fb265f59ae3151a62dae324f54076/colcon-metadata-0.2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/f9/a8cad1da3626ef7e94779fa395ca274fb265f59ae3151a62dae324f54076/colcon-metadata-0.2.5.tar.gz
Summary  : Extension for colcon to read package metadata from files.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-metadata-python = %{version}-%{release}
Requires: colcon-metadata-python3 = %{version}-%{release}
Requires: PyYAML
Requires: colcon-core
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
===============

%package python
Summary: python components for the colcon-metadata package.
Group: Default
Requires: colcon-metadata-python3 = %{version}-%{release}

%description python
python components for the colcon-metadata package.


%package python3
Summary: python3 components for the colcon-metadata package.
Group: Default
Requires: python3-core
Provides: pypi(colcon_metadata)
Requires: pypi(colcon_core)
Requires: pypi(pyyaml)

%description python3
python3 components for the colcon-metadata package.


%prep
%setup -q -n colcon-metadata-0.2.5
cd %{_builddir}/colcon-metadata-0.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597076927
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
