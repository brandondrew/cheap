#completion for cheap
complete -c cheap -s h -l help -f -x --description "Display help and exit"
complete -c cheap -l edit -f -x --description "Edit <cheatsheet>"
complete -c cheap -s e -f -x --description "Edit <cheatsheet>"
complete -c cheap -s l -l list -f -x --description "List all available cheatsheets"
complete -c cheap -s d -l cheap-directories -f -x --description "List all current cheap dirs"
complete -c cheap --authoritative -f
for cheatsheet in (cheap -l | cut -d' ' -f1)
    complete -c cheap -a "$cheatsheet"
    complete -c cheap -o e -a "$cheatsheet"
    complete -c cheap -o '-edit' -a "$cheatsheet"
end
