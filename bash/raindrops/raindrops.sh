#!/usr/bin/env bash
main() {
    drop=""
    (( (("$1" % 3)) == 0 )) && drop=${drop}Pling
    (( (("$1" % 5)) == 0 )) && drop=${drop}Plang
    (( (("$1" % 7)) == 0 )) && drop=${drop}Plong
    [[ "$drop" = "" ]] && drop=$1
    echo "$drop"
}

main "$@"
