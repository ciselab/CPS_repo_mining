if [ -d "env" ]; then
    rm -rf env
fi

python3 -m venv env
. env/bin/activate
python3 -m pip install --upgrade pip virtualenv
python3 -m pip install -r requirements.txt
pip install --editable .
