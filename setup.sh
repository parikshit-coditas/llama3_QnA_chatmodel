#!/bin/bash

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "Virtual environment created successfully!"

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated successfully!"

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip3 install -r requirement.txt
echo "Dependencies installed successfully!"

echo "Setup complete!"
