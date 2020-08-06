#!/bin/bash

PYENV=/home/isabelle/.pyenv/versions/handover/bin/activate
PROJECT_FOLDER=/home/isabelle/intelie/handover

function configure(){
    source $PYENV
    nvm use 8.11.3
}


function start_django(){
    local directory="${2}/django/"
    local port=$1

    echo "Running project on $directory"

    python ${directory}manage.py makemigrations
    python ${directory}manage.py migrate
    python ${directory}manage.py runserver $port
}


function start_ui(){
    local directory=${1}/ui

    echo "Running project on $directory"

    yarn --cwd $directory start
}


function start(){
    echo "Starting $1..."
    configure

    local port=$2
    local opt=$1
    local directory=$PROJECT_FOLDER

    echo $directory
    # TODO: getopts was not working therefore decided on taking the argument
    case "${opt}" in
    d*) 
        start_django $port ${directory}
        ;;
    u*) 
        start_ui ${directory}
        ;;
    esac
}

port=$2
command=$1
start $command $port