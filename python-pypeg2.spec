%global srcname pyPEG2

Name:		python-pypeg2
Version:	2.15.2
Release:	4
Summary:	A PEG Parser-Interpreter in Python

License:	GPLv2
URL:		http://fdik.org/pyPEG
Source0:	https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:	python3-devel
#BuildRequires:	python-pytest
Requires: python-lxml

%description
pyPEG is a plain and simple intrinsic parser interpreter framework for Python
version 3.x. It is based on Parsing Expression Grammar, PEG.
With pyPEG you can parse many formal languages in a very easy way.


%prep
%setup -q -n %{srcname}-%{version}


%build
python setup.py build

%install
python setup.py install --root=%{buildroot}


%check
#PYTHONPATH=. py.test-%{py3_ver} pypeg2/test


%files
%doc LICENSE.txt README.txt CHANGES.txt PKG-INFO docs
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitelib}/pypeg2

