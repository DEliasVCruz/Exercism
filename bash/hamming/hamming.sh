#!/usr/bin/env bash
main() {
	if [[ "${#@}" -le 1 ]]; then
		echo "Usage: hamming.sh <string1> <string2>"
		exit 2
	fi
	if [[ "${#1}" -ne "${#2}" ]]; then
		echo "strands must be of equal length"
		exit 1
	fi
	differences=0
	for ((i = 0; i < ${#1}; i += 1)); do
		if [[ "${1:i:1}" != "${2:i:1}" ]]; then
			((differences += 1))
		fi
	done
	echo "$differences"
}

main "$@"
