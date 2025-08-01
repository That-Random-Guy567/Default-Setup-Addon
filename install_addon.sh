#!/bin/bash
# filepath: /Users/TRBG/Blender/Add-ons/Default_Setup_Addon/install_addon.sh

# Configuration
BLENDER_VERSION="4.5"
ADDON_NAME="Default_Setup_Addon"
BLENDER_APP="/Applications/Blender 4.5 LTS.app"
BLENDER_EXEC="$BLENDER_APP/Contents/MacOS/blender"
BLENDER_PATH="$HOME/Library/Application Support/Blender/${BLENDER_VERSION}"
EXTENSION_PATH="${BLENDER_PATH}/extensions/user_default/${ADDON_NAME}"
ZIP_PATH="./${ADDON_NAME}.zip"

# Verify Blender exists
if [ ! -f "$BLENDER_EXEC" ]; then
    echo "Error: Blender not found at $BLENDER_EXEC"
    exit 1
fi

echo "=== Addon Installation Script ==="
echo "Blender Version: $BLENDER_VERSION"
echo "Addon Name: $ADDON_NAME"
echo "Blender Path: $BLENDER_EXEC"
echo "Target Path: $EXTENSION_PATH"

# Safety check before deleting old installation
if [ -d "$EXTENSION_PATH" ]; then
    read -p "Delete existing addon at $EXTENSION_PATH? (y/n): " confirm
    if [[ $confirm =~ ^[Yy]$ ]]; then
        rm -rf "$EXTENSION_PATH"
        echo "Addon removed successfully!"
    else
        echo "Skipping deletion. Exiting."
        exit 0
    fi
else
    echo -e "\nNo existing installation found."
fi

# Create temp directory for proper structure
TEMP_DIR="./temp_build"
echo -e "\nPreparing files..."

if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi
mkdir -p "$TEMP_DIR"

cp *.py "$TEMP_DIR/"
cp -r Operators "$TEMP_DIR/"
cp -r Panels "$TEMP_DIR/"
[ -f "blender_manifest.toml" ] && cp blender_manifest.toml "$TEMP_DIR/"

echo -e "\nCreating zip file..."
if [ -f "$ZIP_PATH" ]; then
    rm "$ZIP_PATH"
fi

if cd "$TEMP_DIR" && zip -r "../$ADDON_NAME.zip" *; then
    cd ..
    echo "Zip file created at: $(pwd)/${ADDON_NAME}.zip"
else
    cd ..
    echo "Error creating zip file"
    rm -rf "$TEMP_DIR"
    exit 1
fi

rm -rf "$TEMP_DIR"

echo -e "\nInstalling addon..."
mkdir -p "$EXTENSION_PATH"
unzip -q "$ZIP_PATH" -d "$EXTENSION_PATH"

if [ $? -eq 0 ]; then
    echo "Addon installed successfully!"
else
    echo "Error installing addon"
    exit 1
fi

echo -e "\n=== Installation Complete ==="

read -p $'\nDo you want to launch Blender? (y/n): ' launch
if [[ $launch =~ ^[Yy]$ ]]; then
    echo "Launching Blender..."
    "$BLENDER_EXEC"
else
    echo "Blender launch skipped."
fi