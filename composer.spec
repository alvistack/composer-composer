%global debug_package %{nil}

Name: composer
Epoch: 100
Version: 2.4.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Dependency Manager for PHP
License: MIT
URL: https://github.com/composer/composer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
Requires: php-cli >= 7.2.5

%description
Composer helps you declare, manage and install dependencies of PHP
projects, ensuring you have the right stack everywhere.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_sysconfdir}/profile.d
install -Dpm755 -d %{buildroot}%{_datadir}/php/vendor
install -Dpm755 -t %{buildroot}%{_sysconfdir}/profile.d etc/profile.d/composer.sh
cp -rfT vendor %{buildroot}%{_datadir}/php/vendor
pushd %{buildroot}%{_bindir} && \
    ln -fs %{_datadir}/php/vendor/composer/bin/composer composer && \
    popd
chmod a+x %{buildroot}%{_datadir}/php/vendor/composer/bin/composer
fdupes -qnrps %{buildroot}%{_datadir}/php/vendor

%check

%files
%license LICENSE
%dir %{_datadir}/php
%dir %{_datadir}/php/vendor
%{_bindir}/*
%{_datadir}/php/vendor/*
%{_sysconfdir}/profile.d/*

%changelog
