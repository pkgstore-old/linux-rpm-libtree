# linux-rpm-libtree

Implementation of AVL (Adelson-Velskii and Landis) balanced trees in the spirit of the BSD queue and list implementations.

## Install

### Fedora COPR

```
$ dnf copr enable pkgstore/lib
$ dnf install -y libtree
```

### Open Build Service (OBS)

```
# Work in Progress
```

## Update

```
$ dnf upgrade -y libtree
```

## Remove

```
$ dnf erase -y libtree
$ dnf copr remove pkgstore/lib
```

## How to Build

1. Get source from [src.fedoraproject.org](https://src.fedoraproject.org/rpms/libtree).
2. Write last commit SHA from [src.fedoraproject.org](https://src.fedoraproject.org/rpms/libtree) to [CHANGELOG](CHANGELOG).
3. Modify & update source (and `*.spec`).
4. Build SRPM & RPM.
