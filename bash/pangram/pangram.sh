#!/usr/bin/env bash
main() {
	# Process the string
	letters=${1// /}
	letters=${letters//[0-9_.\"]/}
	letters=${letters,,}

	# Turn it into an array
	letters_array=()
	for ((i = 0; i < ${#letters}; i++)); do
		letters_array+=("${letters:i:1}")
	done

	# Sort the string
	sorted="$(echo "${letters_array[*]}" | tr " " "\n" | sort -u | tr "\n" " ")"
	sorted="${sorted// /}"

	# Compere
	alpahbet="abcdefghijklmnopqrstuvwxyz"
	[[ "${sorted}" = "$alpahbet" ]] && echo "true" || echo "false"
}

main "$@"
