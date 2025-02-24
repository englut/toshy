#!/usr/bin/env bash


# Run the Toshy machine context module to get the hashed machine ID, for
# use in the config file with 'if' conditions or keymap conditionals.

# Check if the script is being run as root
if [[ $EUID -eq 0 ]]; then
    echo "This script must not be run as root"
    exit 1
fi

# Check if $USER and $HOME environment variables are not empty
if [[ -z $USER ]] || [[ -z $HOME ]]; then
    echo "\$USER and/or \$HOME environment variables are not set. We need them."
    exit 1
fi


# shellcheck disable=SC1091
source "$HOME/.config/toshy/.venv/bin/activate"

python3 "$HOME/.config/toshy/lib/machine_context.py"
