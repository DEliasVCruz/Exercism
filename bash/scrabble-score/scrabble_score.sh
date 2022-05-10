#!/usr/bin/env bash
look_up() {
	case "$1" in
	A | E | I | O | U | L | N | R | S | T) echo 1 ;;
	D | G) echo 2 ;;
	B | C | M | P) echo 3 ;;
	F | H | V | W | Y) echo 4 ;;
	K) echo 5 ;;
	J | X) echo 8 ;;
	Q | Z) echo 10 ;;
	esac
}

main() {
	[[ "${#1}" -eq 0 ]] && echo 0 && exit 0
	letters="${1^^}"
	total_points=0
	for ((i = 0; i < ${#letters}; i++)); do
		((total_points += $(look_up "${letters:i:1}")))
	done
	echo "$total_points"
}

main "$@"
