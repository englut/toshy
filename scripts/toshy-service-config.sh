#!/usr/bin/env bash


# Start the actual run of the keymapper with Toshy config, making 
# sure to stop existing processes.

# Make sure keymapper binary can be found in user-home-local "bin" location
export PATH=$HOME/.local/bin:$PATH

if command -v keyszer >/dev/null 2>&1; then
    : # no-op operator
else
    echo -e "The \"keyszer\" command was not found in: \n$PATH."
    echo "Toshy config cannot be loaded until \"keyszer\" is installed."
    exit 1
fi


# shut down any existing keyszer (or xkeysnail) process
/usr/bin/pkill -f "bin/keyszer"
/usr/bin/pkill -f "bin/xkeysnail"

$(which keyszer) -w -c "$HOME/.config/toshy/toshy_config.py"
