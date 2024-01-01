#!/usr/bin/env bash

set -euo pipefail

declare -i exit_code=0

for cur_file in "$@"
do
    printf "Checking \"%s\"\n" "${cur_file}"
    printf "Checking with pylint:\n"
    if ! poetry run pylint "${cur_file}" ; then
        exit_code=1
    fi

    printf "Checking with flake8:\n"
    if ! poetry run flake8 "${cur_file}" --count --max-line-length=88 --show-source --ignore=E203,W503 ; then
        exit_code=1
    fi

    printf "Checking with mypy:\n"
    if ! poetry run mypy "${cur_file}"; then
        exit_code=1
    fi
done

if [[ ${exit_code} -eq 0 ]] ; then
   printf "\nNo errors found!\n"
fi

exit "${exit_code}"
