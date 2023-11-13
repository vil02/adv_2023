#!/usr/bin/env bash

set -euo pipefail

declare -i exit_code=0

for cur_script in "$@"
do
    printf "Checking \"%s\"\n" "${cur_script}"
    if ! shellcheck "${cur_script}" --enable=all; then
      exit_code=1
    fi
    if ! grep -q "set -euo pipefail" "${cur_script}"; then
      printf "add \"set -euo pipefail\"\n"
      exit_code=1
    fi
done

if [[ ${exit_code} -eq 0 ]] ; then
   printf "\nNo errors found!\n"
fi
exit "${exit_code}"
