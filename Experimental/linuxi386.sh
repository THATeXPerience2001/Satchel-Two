#!/usr/bin/env bash
# ==============================================================================
# Script Name: linuxi386.sh
# Target OS: Linux (32-bit / i686)
# Description: Installs dependencies, compiles Python 3.13.5 from source, 
#              and builds the target Python library stack from source.
# ==============================================================================

# Exit immediately if any command fails
set -e

PYTHON_VERSION="3.13.5"
INSTALL_DIR="$HOME/python313"
VENV_NAME="venv"

echo "=== Satchel:Two Linux i386 installer == "

echo "=== [1/5] Updating system packages and installing build dependencies == "
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    checkinstall \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    liblzma-dev \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    pkg-config \
    git \
    wget

echo "=== [2/5] Downloading and compiling Python ${PYTHON_VERSION} from source == "
cd /tmp
if [ ! -f "Python-${PYTHON_VERSION}.tgz" ]; then
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
fi

tar -xzvf Python-${PYTHON_VERSION}.tgz
cd Python-${PYTHON_VERSION}

# Configure with optimizations enabled for i686
./configure \
    --prefix="${INSTALL_DIR}" \
    --enable-optimizations \
    --with-ensurepip=install

# Compile using all available CPU cores
make -j$(nproc)

# Install locally to avoid breaking system python (/usr/bin/python)
make altinstall

echo "=== [3/5] Creating Virtual Environment == "
cd ~
"${INSTALL_DIR}/bin/python3.13" -m venv "${VENV_NAME}"

# Activate virtual environment
source "${VENV_NAME}/bin/activate"

echo "=== [4/5] Upgrading core packaging tools == "
pip install --upgrade pip setuptools wheel

echo "=== [5/5] Installing and building target libraries from source == "
# Force source builds for packages with heavy C extensions on 32-bit
pip install --no-binary=:all: numpy
pip install --no-binary=pandas pandas
pip install --no-binary=pillow pillow
pip install --no-binary=pyyaml pyyaml

# Install pure-python libraries and Tcl/Tk-dependent tools
pip install requests iCalendar custom2kinter tkinterweb

echo "=============================================================================="
echo "Source Build Complete!"
echo "To activate your environment later, run:"
echo "    source ~/${VENV_NAME}/bin/activate"
echo "To run your Python 3.13.5 environment:"
echo "    python --version"
echo "=============================================================================="