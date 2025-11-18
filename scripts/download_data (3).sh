#!/bin/bash
set -e

echo "Creating data directories..."
mkdir -p data/aerosonicdb data/esc50

echo "Downloading AeroSonicDB from Kaggle..."
kaggle datasets download -d gray8ed/audio-dataset-of-low-flying-aircraft-aerosonicdb -p data/aerosonicdb
unzip -oq data/aerosonicdb/audio-dataset-of-low-flying-aircraft-aerosonicdb.zip -d data/aerosonicdb
rm data/aerosonicdb/audio-dataset-of-low-flying-aircraft-aerosonicdb.zip

echo "Downloading ESC-50 dataset..."
wget -q https://github.com/karolpiczak/ESC-50/archive/refs/heads/master.zip -O data/esc50.zip
unzip -oq data/esc50.zip -d data/esc50
rm data/esc50.zip

echo "Done."
