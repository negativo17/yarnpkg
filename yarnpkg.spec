%global debug_package %{nil}

Name:           yarnpkg
Version:        1.22.19
Release:        1%{?dist}
Summary:        Fast, reliable, and secure dependency management
License:        BSD-2-Clause
URL:            https://github.com/%{name}/yarn
BuildArch:      noarch

Source0:        https://github.com/%{name}/yarn/releases/download/v%{version}/yarn-v%{version}.tar.gz

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
%autosetup -n yarn-v%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a bin lib *.js *.json %{buildroot}%{_libdir}/%{name}

mkdir -p %{buildroot}%{_bindir}/
ln -sf ../%{_lib}/%{name}/bin/yarn %{buildroot}%{_bindir}/
ln -sf ../%{_lib}/%{name}/bin/%{name} %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/yarn
%{_bindir}/%{name}
%{_libdir}/%{name}/bin/yarn
%{_libdir}/%{name}/bin/yarn.cmd
%{_libdir}/%{name}/bin/yarn.js
%{_libdir}/%{name}/bin/%{name}
%{_libdir}/%{name}/bin/%{name}.cmd
%{_libdir}/%{name}/lib/cli.js
%{_libdir}/%{name}/lib/v8-compile-cache.js
%{_libdir}/%{name}/package.json
%{_libdir}/%{name}/preinstall.js

%changelog
* Thu Jun 02 2022 Simone Caronni <negativo17@gmail.com> - 1.22.19-1
- Update to 1.22.19.

* Sun May 01 2022 Simone Caronni <negativo17@gmail.com> - 1.22.18-1
- Update to 1.22.18.

* Thu Jan 13 2022 Simone Caronni <negativo17@gmail.com> - 1.22.17-1
- Update to 1.22.17.

* Mon May 24 2021 Simone Caronni <negativo17@gmail.com> - 1.22.10-2
- Rename to yarnpkg.

* Sun May 23 2021 Simone Caronni <negativo17@gmail.com> - 1.22.10-1
- First build from prebuilt binaries.
