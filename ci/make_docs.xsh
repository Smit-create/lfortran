#!/usr/bin/env xonsh

$RAISE_SUBPROC_ERROR = True
trace on

import os
os.environ['CXXFLAGS'] = "-Werror"

echo "CONDA_PREFIX=$CONDA_PREFIX"
./build0.sh
cmake -DCMAKE_BUILD_TYPE=Debug -DWITH_LLVM=yes -DWITH_XEUS=yes -DCMAKE_PREFIX_PATH=$CONDA_PREFIX -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX .
make -j
make install

jupyter kernelspec list --json

cd doc
python convert_nb.py
mkdocs build

../ci/upload_docs_github.sh
