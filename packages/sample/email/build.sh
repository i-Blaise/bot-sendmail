#!/bin/bash
set -e

echo "Creating virtualenv..."
virtualenv --no-download virtualenv

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt --target virtualenv/lib/python3.11/site-packages
