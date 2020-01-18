%global commit      cbab0ea488669fee8727d5165e534a010b5e1c2c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dockerfiledir %{_datadir}/rhscl-dockerfiles

Name:           rhscl-dockerfiles
Version:        1.2
Release:        4%{?dist}
Summary:        Example dockerfiles to assist standing up containers quickly
License:        GPLv2
URL:            https://github.com/sclorg/rhscl-dockerfiles
Source0:        https://github.com/sclorg/rhscl-dockerfiles/archive/%{commit}/rhscl-dockerfiles-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
This package provides a set of example Dockerfiles that can be used
with Red Hat Software Collections.  Use these examples to stand up
test environments using the Docker container engine.

%prep
%setup -n rhscl-dockerfiles-%{commit}

%build

%install
install -d %{buildroot}%{dockerfiledir}

collections="httpd24 mariadb55 mongodb24 mysql55 nginx16 nodejs010 \
             perl516 php54 php55 postgresql92 python27 python33 ror40 ruby193 \
             ruby200"
install -d -p -m 755 %{buildroot}%{dockerfiledir}/rhel{6,7}
for d in $collections; do
   install -d -p -m 755 %{buildroot}%{dockerfiledir}/rhel{6,7}/$d
   install -p -m 644 rhel6.$d/* %{buildroot}%{dockerfiledir}/rhel6/$d
   install -p -m 644 rhel7.$d/* %{buildroot}%{dockerfiledir}/rhel7/$d
done

%files 
%defattr(-,root,root,-)
%{dockerfiledir}

%changelog
* Fri Oct 31 2014 Joe Orton <jorton@redhat.com> - 1.2-4
- drop Requires for docker

* Fri Oct 31 2014 Joe Orton <jorton@redhat.com> - 1.2-3
- update READMEs

* Thu Oct 30 2014 Joe Orton <jorton@redhat.com> - 1.2-2
- package for both RHEL 6, 7

* Wed Oct 22 2014 Joe Orton <jorton@redhat.com> - 1.2-1
- initial package (#1158483)
