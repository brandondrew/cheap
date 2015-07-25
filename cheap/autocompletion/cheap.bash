function _cheap_autocomplete {
    sheets=$(cheap -l | cut -d' ' -f1)
    COMPREPLY=()
    if [ $COMP_CWORD = 1 ]; then
	COMPREPLY=(`compgen -W "$sheets" -- $2`)
    fi
}

complete -F _cheap_autocomplete cheap
