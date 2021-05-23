%global debug_package %{nil}

Name:           yarn
Version:        1.22.10
Release:        1%{?dist}
Summary:        Fast, reliable, and secure dependency management
License:        BSD-2-Clause
URL:            https://github.com/yarnpkg/%{name}
BuildArch:      noarch

Source0:        https://github.com/yarnpkg/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz

Requires:       nodejs

%description
Fast: Yarn caches every package it has downloaded, so it never needs to download
the same package again. It also does almost everything concurrently to maximize
resource utilization. This means even faster installs.

Reliable: Using a detailed but concise lockfile format and a deterministic
algorithm for install operations, Yarn is able to guarantee that any
installation that works on one system will work exactly the same on another
system.

Secure: Yarn uses checksums to verify the integrity of every installed package
before its code is executed.

%prep
%autosetup -n %{name}-v%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a bin lib *.js *.json %{buildroot}%{_libdir}/%{name}

mkdir -p %{buildroot}%{_bindir}/
ln -sf ../%{_lib}/%{name}/bin/%{name} %{buildroot}%{_bindir}/
ln -sf ../%{_lib}/%{name}/bin/%{name}pkg %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}pkg
%{_libdir}/%{name}/bin/%{name}
%{_libdir}/%{name}/bin/%{name}.cmd
%{_libdir}/%{name}/bin/%{name}.js
%{_libdir}/%{name}/bin/%{name}pkg
%{_libdir}/%{name}/bin/%{name}pkg.cmd
%{_libdir}/%{name}/lib/cli.js
%{_libdir}/%{name}/lib/v8-compile-cache.js
%{_libdir}/%{name}/package.json
%{_libdir}/%{name}/preinstall.js

%changelog
* Sun May 23 2021 Simone Caronni <negativo17@gmail.com> - 1.22.10-1
- First build from prebuilt binaries.
