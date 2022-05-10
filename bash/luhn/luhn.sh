#!/usr/bin/env bash
sum=0

double_and_sum_every_second_digit() {
	for ((i = 2; i <= ${#numbers}; i += 2)); do
		index=$((-i))
		number="${numbers:index:1}"
		[[ ! "$number" =~ [0-9] ]] && echo "false" && exit 0
		number=$((number * 2))
		[[ "$number" -gt 9 ]] && number=$((number - 9))
		((sum += number))
	done
}

sum_non_double_digits() {
	for ((i = 1; i <= ${#numbers}; i += 2)); do
		index=$((-i))
		number="${numbers:index:1}"
		[[ ! "$number" =~ [0-9] ]] && echo "false" && exit 0
		((sum += number))
	done
}

main() {
	numbers=${1// /}
	[[ "${#numbers}" -le 1 ]] && echo "false" && exit 0
	double_and_sum_every_second_digit "$numbers"
	sum_non_double_digits "$numbers"
	[[ "$sum"%10 -eq 0 ]] && echo "true" || echo "false"
}

main "$@"
