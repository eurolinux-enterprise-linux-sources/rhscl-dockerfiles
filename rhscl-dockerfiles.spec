%global commit      6309cbdb06e61981c0320a371ad3bfa67aadfe29
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dockerfiledir %{_datadir}/rhscl-dockerfiles

Name:           rhscl-dockerfiles
Version:        2.0
Release:        3%{?dist}
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
             perl516 php54 php55 postgresql92 python27 python33 ror40 \
             ruby193 ruby200 rh-mariadb100 \
             rh-mongodb26 rh-mysql56 rh-passenger40 rh-perl520 \
             rh-php56 rh-python34 rh-ror41 rh-ruby22 rh-postgresql94"
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
* Tue Mar 31 2015 Joe Orton <jorton@redhat.com> - 2.0-3
- fix enable.sh in passenger40 (#1206567)

* Fri Mar 27 2015 Joe Orton <jorton@redhat.com> - 2.0-2
- remove rh-java-common, fix rh-passenger40 (#1206567)
- also restore newlines at EOF in templated files

* Sun Jan 25 2015 Joe Orton <jorton@redhat.com> - 2.0-1
- add new collections (#1180341)

* Fri Oct 31 2014 Joe Orton <jorton@redhat.com> - 1.2-4
- drop Requires for docker

* Fri Oct 31 2014 Joe Orton <jorton@redhat.com> - 1.2-3
- update READMEs

* Thu Oct 30 2014 Joe Orton <jorton@redhat.com> - 1.2-2
- package for both RHEL 6, 7

* Wed Oct 22 2014 Joe Orton <jorton@redhat.com> - 1.2-1
- initial package (#1158483)
