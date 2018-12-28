#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-metadata
Version  : 0.2.1
Release  : 4
URL      : https://files.pythonhosted.org/packages/14/30/25c40b5c20650d95cf343fff27155fdeb1356bfdc4638c81fe29af432ec4/colcon-metadata-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/30/25c40b5c20650d95cf343fff27155fdeb1356bfdc4638c81fe29af432ec4/colcon-metadata-0.2.1.tar.gz
Summary  : Extension for colcon to read package metadata from files.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-metadata-python3
Requires: colcon-metadata-python
Requires: PyYAML
Requires: colcon-core
BuildRequires : buildreq-distutils3

%description
===============

%package python
Summary: python components for the colcon-metadata package.
Group: Default
Requires: colcon-metadata-python3

%description python
python components for the colcon-metadata package.


%package python3
Summary: python3 components for the colcon-metadata package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-metadata package.


%prep
%setup -q -n colcon-metadata-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536215967
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
