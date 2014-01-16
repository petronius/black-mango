#!/bin/bash

PYTHON="python"
if hash python2 >/dev/null 2>&1; then
    PYTHON=python2
fi
if hash python2.7 >/dev/null 2>&1; then
    PYTHON=python2.7
fi

PYINSTALLER=$(which pyinstaller)

BRANCH=$(git rev-parse --abbrev-ref HEAD)

export BRANCH
export PYINSTALLER
export PYTHON
