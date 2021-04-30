set fish_greeting "Hello $USER"
colorscript random

set -gx PATH ~/anaconda3/bin $PATH
# Conda startup script
source ~/anaconda3/etc/fish/conf.d/conda.fish

# Path to system Python3
set fish_user_paths $fish_user_paths /Library/Frameworks/Python.framework/Versions/3.6/bin/

# For Conda < 4.4.0 prepend Conda path to fish path (should be removable in Conda 4.4.0+)
set fish_user_paths $fish_user_paths ~/miniconda3/bin/

if status --is-interactive
    abbr --add --global ls exa -la
    abbr --add --global conda conda activate
    abbr --add --global gco git checkout
    # etcetera
end
