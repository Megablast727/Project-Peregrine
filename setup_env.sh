#!/bin/bash

# Set up a virtual environment and install modules

# Define the virtual environment directory
VENV_DIR="venv"

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

# Deactivate the virtual environment

