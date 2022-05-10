#!/usr/bin/env bash
main() {
	if [[ "$1" =~ [A-Z]+ ]] && [[ ! "$1" =~ [\?]$ ]] && [[ ! "$1" =~ [a-z]+ ]]; then
		echo "Whoa, chill out!"
	elif [[ "$1" =~ [A-Z]+ ]] && [[ "$1" =~ [\?]$ ]] && [[ ! "$1" =~ [a-z]+ ]]; then
		echo "Calm down, I know what I'm doing!"
	elif [[ "${1// /}" =~ [\?]$ ]]; then
		echo "Sure."
	elif [[ "${1// /}" = "" ]]; then
		echo "Fine. Be that way!"
	else
		echo "Whatever."
	fi
}


main "$@"
