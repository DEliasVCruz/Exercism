#!/usr/bin/env bash

main() {
	[[ "$1" = "total" ]] && echo 18446744073709551615 && exit 0
	[[ "$1" -le 0 || "$1" -gt 64 ]] && echo "Error: invalid input" && exit 1
	if [[ "$1" -eq 1 ]]; then
		echo 1
	elif [[ "$1" -eq 64 ]]; then
		echo 9223372036854775808
	else
		number="$1"
		((number -= 1))
		result=$(main "$number")
		result=$((result * 2))
	fi
	echo "$result"
}

main "$@"
