#!/bin/bash

echo ">>> Creating virtual environment..."
python3 -m venv venv

echo ">>> Activating virtual environment..."
source venv/bin/activate

echo ">>> Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Adding startapp / stopapp aliases..."

if ! grep -q "alias startapp=" ~/.zshrc; then
    echo 'alias startapp="(cd $(pwd) && source venv/bin/activate && uvicorn main:app --reload)"' >> ~/.zshrc
    echo 'alias stopapp="pkill -f '\''uvicorn main:app'\''"' >> ~/.zshrc
    echo ">>> Aliases added to ~/.zshrc"
else
    echo ">>> Aliases already exist"
fi

echo ">>> Reloading shell config..."
source ~/.zshrc

echo ">>> Setup complete! You can now run:"
echo "startapp"
echo "stopapp"
