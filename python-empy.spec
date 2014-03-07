%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global tarname empy

Name:           python-empy
Version:        3.3.2
Release:        1%{?dist}
Summary:        A powerful and robust template system for Python

Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.alcyone.com/software/empy/
Source:         http://www.alcyone.com/software/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools, python-devel

%description
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

%prep
%setup -q -n %{tarname}-%{version}

#fix shebang on rpmlint
sed -i -e '1d' em.py

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README version.txt
%{python_sitelib}/*


%changelog
* Fri Mar 07 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Fri Jan 24 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-1
- Update to 3.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Mar 03 2010 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-5
- Fix compilation error

* Mon Mar 01 2010 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-4
- Fix license

* Sat Feb 27 2010 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-3
- Remove python-devel in BuildRequires
- Fix shebang on rpmlint

* Tue Feb 23 2010 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-2
- Add build information

* Mon Jan 11 2010 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-1
- Initial RPM release
