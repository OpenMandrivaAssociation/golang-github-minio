# https://github.com/minio/minio-go
%global goipath         github.com/minio/minio-go
Version:    6.0.8

%global common_description %{expand:
The Minio Go Client SDK provides simple APIs to access any Amazon S3 compatible
object storage.}

%gometa

Name:       %{goname}
Release:    1%{?dist}
Summary:    Minio Client SDK for Go
License:    ASL 2.0
URL:        %{gourl}
Source0:    %{gosource}

%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/go-ini/ini)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(golang.org/x/crypto/argon2)
BuildRequires: golang(golang.org/x/net/http/httpguts)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
#tests are disabled since they require Internet access

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README_zh_CN.md CONTRIBUTING.md MAINTAINERS.md README.md

%changelog
* Sun Oct 14 2018 Steve Miller (copart) <code@rellims.com> - 6.0.8-1
- Bumped upstream version, bug fix release

* Tue Jul 31 2018 Steve Miller (copart) <code@rellims.com> - 6.0.5-1
- Bumped upstream version, bug fix release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 4 2018 Steve Miller (copart) <code@rellims.com> - 6.0.4-2
- Removed patch as the dependency golang-googlecode-net was updated

* Sun Jun 24 2018 Steve Miller (copart) <code@rellims.com> - 6.0.4-1
- Bumped upstream version, bug fix release

* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 6.0.2-1
- First package for Fedora
