#!/bin/bash

# Define the project directory and virtual environment directory
PROJECT_DIR="/Users/megablast/Desktop/Code/Project-Peregrine"
VENV_DIR="$PROJECT_DIR/venv"

# Change to the project directory
cd $PROJECT_DIR || { echo "Failed to change directory to $PROJECT_DIR"; exit 1; }

# Check if virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    # Create a virtual environment
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required Python modules
echo "Installing required modules..."
pip install numpy tqdm pandas

echo "Setup complete. Virtual environment is ready and modules are installed."

# Keep the terminal open in the virtual environment
exec bash
