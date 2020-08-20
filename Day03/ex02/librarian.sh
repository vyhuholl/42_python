VENV_PATH="/Users/olgapichuzhkina/Documents/42python/Day03/ex02/sghezn"

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "librarian.sh: no virtual environment found"
elif [ $VIRTUAL_ENV != $VENV_PATH ]; then
    echo "librarian.sh: wrong virtual environment"
else
    pip install -r requirements.txt
    pip freeze
    pip freeze > output.txt
fi
