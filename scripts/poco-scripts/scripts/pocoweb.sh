#!/bin/bash

# TODO: extract these envs to a .conf or .env file or use system envs
PYENV=$HOME/home/vanessa/.virtualenvs/pocowev-2/bin/activate/
PROJECT_FOLDER=$HOME/Intelie/Projects/pocoweb/


function start_django(){
    local directory="${PROJECT_FOLDER}/django/"
    local port=$1

    echo "Running project on $directory"

    source $PYENV


    python ${directory}manage.py makemigrations
    python ${directory}manage.py migrate
    python ${directory}manage.py runserver $port
}


function start_ui(){
    local directory=${1}/ui/painel

    echo "Running project on $directory"

    yarn --cwd $directory watch
}

function start_js(){
    local directory=${1}/js/explorer/

    echo "Running project on $directory"

    yarn --cwd $directory watch
}


function deploy(){
    echo "Deploying to QA Server"
    local directory=${1}/tools/

    fab qa build deploy
}


function start(){
    echo "Starting $1..."

    local port=$2
    local opt=$1

    # TODO: getopts was not working therefore decided to take the argument manually. Remember to fix this when having time. Maybe on a weekend ;D
    case "${opt}" in
    deploy*)
        deploy $PROJECT_FOLDER
        ;;
    d*) 
        start_django $port $PROJECT_FOLDER
        ;;
    u*) 
        start_ui $PROJECT_FOLDER
        ;;
    j*) 
        start_js $PROJECT_FOLDER
        ;;
    
    esac
}

port=$2
command=$1
start $command $port
