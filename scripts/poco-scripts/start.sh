#!/bin/bash

# TODO: Reorganize the scripts not by project but functionality

PORTS_FILE=scripts/ports.conf

# TODO: Extract this to a file for containing implementation for different terminals
function tmux_terminal(){
    local orientation=$1 # either h or v
    local exe=$2


    # gnome-terminal --tab-with-profile=pocoweb --title "$title"  -- /bin/bash -c "$exe"
    tmux split-window -${orientation} "$exe"
}


function new_terminal(){
    local terminal=$1
    local exe=$2
    local orientation=$3


    gnome-terminal --tab-with-profile=pocoweb --title "$title"  -- /bin/bash -c "$exe"
    # tmux_terminal $orientation "$exe"
}


function get_port() {
    local project=$1
    
    # Search the project name on thgrep -i pocoweb projects.conf | grep -o "\/[a-zA-Z]*" | tr -d '\n'e .env file ignoring case
    # Then extract the port numbers from what have been found
    # Then remove de new line from the previous output

    echo $(grep -i $project $PORTS_FILE | grep -o [0-9] | tr -d '\n')
}

function get_project_folder(){
    local project=$1

    echo $(grep -i $project $PROJECT_FOLDER_FILE | grep -o "\/[a-zA-Z]*" | tr -d '\n')
}


# TODO: Put the code below inside a function, maybe?
# if [ "$1" = "tmux" ]; then # TODO: Treat the tmux session option as another option on getopts
#     tmux new -d -s $2 ". start.sh $2" 
# else
for project in "$@" # TODO: Try using getops and GETARG again,
do
    port=$(get_port $project)

    echo $port
    case $project in
        pocoweb)
            echo "Starting pocoweb..." && \
            new_terminal "Poço" ". scripts/pocoweb.sh django $port" v && \
            new_terminal "Poço - ui/painel" ". scripts/pocoweb.sh ui" h && \
            new_terminal "Poço - js/explorer" ". scripts/pocoweb.sh js" v
            ;;
        # handover) 
        #     echo "Start handover" && \
        #     new_terminal 
        #     tmux new -d -s $project ". start.sh $2"
        #     ;;
        # *) 
        #     tmux new -d -s $project ". start.sh $2"
        #     ;;

    esac
done
# fi
