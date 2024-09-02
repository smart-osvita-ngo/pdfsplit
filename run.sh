
# A script to automate env installation for the end user to run the script without hassle 
# Script copied from https://github.com/DhruvMakwana/python-virtual-environment-management/blob/main/pvenv.sh

ENV_NAME=".venv"

check_virtualenv() {
    if ! command -v virtualenv &> /dev/null; then
        echo "virtualenv is not installed. Installing..."
        python3 -m pip install --user virtualenv
        echo "virtualenv installation complete."
    fi
}

create_venv() {
    # Check if virtualenv is installed, if not, install it
    check_virtualenv
    
    local env_name=$ENV_NAME

    if [ -d "$env_name" ]; then
        echo "Virtual environment '$env_name' already exists. Aborting."
        return 1
    fi

    python3 -m venv "$env_name"
    source "./$env_name/bin/activate"
    pip install -U pip
}

activate_venv() {
    local env_name=$ENV_NAME

    if [ ! -d "$env_name" ]; then
        echo "Virtual environment '$env_name' not found. Use '$0 create [env_name]' to create one."
        return 1
    fi

    source "./$env_name/bin/activate"
}

install_deps() {
    local env_name=$ENV_NAME

    if [ ! -d "$env_name" ]; then
        echo "Virtual environment '$env_name' not found. Use '$0 create [env_name]' to create one."
        return 1
    fi

    source "./$env_name/bin/activate"

    if [ -f "requirements.txt" ]; then
        pip install -r ./requirements.txt
    fi

    if [ -f "setup.py" ]; then
        pip install -e .
    fi
}

export_deps() {
    local env_name=$ENV_NAME

    if [ ! -d "$env_name" ]; then
        echo "Virtual environment '$env_name' not found. Use '$0 create [env_name]' to create one."
        return 1
    fi

    source "./$env_name/bin/activate"
    pip freeze > requirements.txt
    echo "Dependencies exported to requirements.txt"
}

remove_venv() {
    local env_name=$ENV_NAME

    if [ ! -d "$env_name" ]; then
        echo "Virtual environment '$env_name' not found."
        return 1
    fi

    deactivate
    rm -rf "$env_name"
}

# ========

if [[ activate_venv() != 0 ]]; then
    echo "Встановлюємо все..."
    create_venv
    install_deps
    activate_venv
fi

echo "Запускаємо скрипт..."
source "./$ENV_NAME/bin/activate"
python pdfsplit.py
