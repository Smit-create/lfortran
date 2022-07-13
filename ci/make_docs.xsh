#!/usr/bin/env xonsh

$RAISE_SUBPROC_ERROR = True
trace on

import os
os.environ['CXXFLAGS'] = "-Werror"

tar xzf dist/lfortran-*.tar.gz
cd lfortran-*
cmake -DCMAKE_BUILD_TYPE=Debug -DWITH_LLVM=yes -DWITH_XEUS=yes .
make
make install

ctest --output-on-failure

cd ..

jupyter kernelspec list --json
rm -r lfortran-*

cd doc
python convert_nb.py
mkdocs build

../ci/upload_docs_github.sh
