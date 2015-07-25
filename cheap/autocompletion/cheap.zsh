#compdef cheap

declare -a cheats
cheats=$(cheap -l | cut -d' ' -f1)
_arguments "1:cheats:(${cheats})" && return 0
