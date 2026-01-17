#!/bin/bash
# Convenience script to run the 2D game editor

# Navigate to the project directory
cd "$(dirname "$0")"

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the editor
python -m src.main
