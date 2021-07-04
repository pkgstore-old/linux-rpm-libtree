%global debug_package %{nil}
%global release_prefix          100

Name:                           libtree
Version:                        1.0
Release:                        %{release_prefix}%{?dist}
Summary:                        Implementation of AVL (Adelson-Velskii and Landis) balanced trees
License:                        MIT
URL:                            https://piumarta.com/software/tree/
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source0:                        %{url}/tree-%{version}.tar.gz

%define common_desc tree.h Implementation of AVL (Adelson-Velskii and Landis) \
balanced trees in the spirit of the BSD queue and list implementations.

%description
%{common_desc}

# -------------------------------------------------------------------------------------------------------------------- #
# Package: devel
# -------------------------------------------------------------------------------------------------------------------- #

%package  devel
Summary:                        %{summary}
Provides:                       libtree-static = %{version}-%{release}

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
* Sun Jul 04 2021 Package Store <kitsune.solar@gmail.com> - 1.0-100
- UPD: Move to Package Store.
- UPD: License.

* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 1.0-1
- Let there be package.
