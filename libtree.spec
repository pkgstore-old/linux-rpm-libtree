%global debug_package %{nil}
%global release_prefix          1000

Name:                           libtree
Version:                        1.0
Release:                        %{release_prefix}%{?dist}
Summary:                        Implementation of AVL (Adelson-Velskii and Landis) balanced trees
License:                        MIT
URL:                            https://piumarta.com/software/tree/

Source0:                        tree-%{version}.tar.xz

%define common_desc tree.h Implementation of AVL (Adelson-Velskii and Landis) \
balanced trees in the spirit of the BSD queue and list implementations.

%description
%{common_desc}

# -------------------------------------------------------------------------------------------------------------------- #
# Package: devel
# -------------------------------------------------------------------------------------------------------------------- #

%package  devel
Summary:                        %{summary}
Provides:                       %{name}-static = %{version}-%{release}

%description devel
%{common_desc}

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%autosetup -n tree-%{version}


%build


%install
%{__mkdir_p} %{buildroot}%{_includedir}
%{__install} -p -m 644 tree.h %{buildroot}%{_includedir}


%files devel
%{_includedir}/tree.h


%changelog
* Thu Mar 31 2022 Package Store <pkgstore@mail.ru> - 1.0-1000
- UPD: Rebuild by Package Store.
- UPD: File "libtree.spec".

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 1.0-1
- Let there be package.
