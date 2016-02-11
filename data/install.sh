#!/bin/bash
#
# Installs gRPC in a Homebrew or Linuxbrew installation.
#
# Prerequisites: Homebrew(Mac) / Linuxbrew(Linux) is installed.
#  - to install homebrew: see http://brew.sh
#  - to install linuxbrew: https://github.com/Homebrew/linuxbrew#installation
#
# Usage:
#
# Install grpc core:
#   curl -fsSL https://goo.gl/getgrpc | bash -
#
# Install grpc protoc plugins only:
#   curl -fsSL https://goo.gl/getgrpc | bash -s plugins
#
# Install grpc python:
#   curl -fsSL https://goo.gl/getgrpc | bash -s python
#
# Install grpc php:
#   curl -fsSL https://goo.gl/getgrpc | bash -s php

set -e

GRPC_VERSION='0.11.0'

__grpc_check_for_brew() {
    which 'brew' >> /dev/null || {
        if [ "$(uname)" == "Darwin" ]; then
            echo "Cannot find the brew command" \
            " - please ensure you have installed Homebrew (http://brew.sh)." \
            " If you're running this with sudo, try sudo env \"PATH=\$PATH\" instead." 1>&2
        elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
            echo "Cannot find the brew command" \
            " - please ensure you have installed Linuxbrew (https://github.com/Homebrew/linuxbrew#installation)." \
            " If you're running this with sudo, try sudo env \"PATH=\$PATH\" instead." 1>&2
        else
            echo "Your system is neither a Mac nor Linux, so gRPC is not currently supported" 1>&2
        fi
        return 1;
    }
}

__grpc_brew_install() {
    local pkg=${!#}
    if brew list -1 | grep -q "^${pkg}\$"; then
        echo "$pkg is already installed" 1>&2
        return;
    else
        brew install $@
    fi
}

__grpc_brew_root() {
    __grpc_check_for_brew || return 1;
    brew --prefix
}

__grpc_install_with_brew() {
    # Needed for unzip, m4 (via google-protobuf), and zlib
    brew tap | grep -q 'homebrew/dupes' || brew tap homebrew/dupes

    # Explicitly install OpenSSL.
    if [ "$(uname)" != "Darwin" ]; then
        # there may be unresolved dependency issues installing openssl using linuxbrew on macs.
        __grpc_brew_install pkg-config
    fi

    __grpc_brew_install zlib
    __grpc_brew_install openssl


    # On linux, explicitly install  unzip if it's not present, it's a protobuf dependency
    # TODO: add this to the official homebrew formula
    if [ "$(uname)" != "Darwin" ]; then
        which 'unzip' >> /dev/null || {
            __grpc_brew_install unzip
        }
    fi

    # Current gRPC version is already installed
    [[ $(brew list --versions | grep grpc) =~ $GRPC_VERSION ]] && return 0

    # Otherwise install the tap and install grpc
    brew tap | grep -q 'grpc/grpc' || brew tap grpc/grpc

    # Explicitly install google-protobuf
    __grpc_brew_install --without-python google-protobuf

    # Install gRPC
    __grpc_brew_install "$@" grpc
}

__grpc_install_python_pkg() {
    which 'pip' >> /dev/null || {
        echo "Could not detect pip; is it (and python) installed properly? Please check $PATH and maybe install and try again" 1>&2
        return 1;
    }
    # support custom install locations, that's the default for linuxbrew and may
    # be used in homebrew install as well
    local brew_root=$(__grpc_brew_root) || return 1
    CFLAGS=-I${brew_root}/include LDFLAGS=-L${brew_root}/lib python -m pip install grpcio --pre
}

__grpc_install_php_pkg() {
    which 'pecl' >> /dev/null || {
        echo "Could not detect pecl; please make sure pear and pecl are installed" 1>&2
        return 1;
    }
    # support custom install locations, that's the default for linuxbrew and may
    # be used in homebrew install as well
    local brew_root=$(__grpc_brew_root) || return 1

    # download the gRPC PHP extension
    pecl download grpc-beta

    # before stable, the extension will have a name of grpc-0.x.x
    find . -name grpc-*.tgz -exec tar -zxvf {} \;
    dir=$(find . -type d -name 'grpc-*')
    cd $dir

    # there seems to be no clean way to install the PHP extension without root access
    # build and leave the extension in the current directory
    phpize && ./configure --enable-grpc=${brew_root}/opt/grpc && make
    cp ./modules/grpc.so ../

    # clean up
    cd ..
    rm -rf $dir && rm grpc-*.tgz && rm package.xml
    echo "Run this to install the PHP extension:"
    echo "  sudo mv grpc.so $(php-config --extension-dir)"
    echo "Add this line to php.ini:"
    echo "  extension=grpc.so"
}

__grpc_install_pkgs() {
    local known_pkgs="python php"
    for pkg in $@; do
        if [[ "$known_pkgs" =~ "$pkg" ]]; then
            echo "installing grpc $pkg";
            local cmd="__grpc_install_${pkg}_pkg";
            $cmd;
        else
            echo "did not install package for ${pkg}; it was not known" 1>&2
        fi
    done
}

main() {
    __grpc_check_for_brew;

    local install_with_brew_args=""
    local install_pkgs_args=""
    for arg in "$@"; do
      if [ "$arg" == "plugins" ]
      then
        install_with_brew_args+="--without-libgrpc "
      else
        install_pkgs_args+="$arg "
      fi
    done

    __grpc_install_with_brew "$install_with_brew_args";
    __grpc_install_pkgs "$install_pkgs_args";
}

main "$@"
