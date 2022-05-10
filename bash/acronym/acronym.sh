#!/usr/bin/env bash
main() {
    string="${1/[-_\*]/ }"
    string="${string/_/ }"

	IFS=" "
	read -ra words <<<"$string"
	acronym=""

	for word in "${words[@]}"; do

		# case "${word:0:1}" in
		# "-") continue ;;
		# "_") word=${word#__} ;;
		# "*") continue ;;
		# esac

		acronym=${acronym}${word:0:1}
	done

	echo "${acronym^^}"
}

main "$@"
