#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nosehtmloutput
Version  : 0.0.5
Release  : 11
URL      : https://pypi.python.org/packages/source/n/nosehtmloutput/nosehtmloutput-0.0.5.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nosehtmloutput/nosehtmloutput-0.0.5.tar.gz
Summary  : Nose plugin to produce test results in html.
Group    : Development/Tools
License  : Apache-2.0
Requires: nosehtmloutput-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
A plugin for nosetests that will write out test results to results.html. The
code is adapted from the example html output plugin at
https://github.com/nose-devs/nose/blob/master/examples/html_plugin/htmlplug.py
and the pyunit Html test runner at
http://tungwaiyip.info/software/HTMLTestRunner.html.

%package python
Summary: python components for the nosehtmloutput package.
Group: Default

%description python
python components for the nosehtmloutput package.


%prep
%setup -q -n nosehtmloutput-0.0.5

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
