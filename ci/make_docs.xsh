#!/usr/bin/env xonsh

$RAISE_SUBPROC_ERROR = True
trace on

jupyter kernelspec list --json

cd doc
python convert_nb.py
mkdocs build

../ci/upload_docs_github.sh
