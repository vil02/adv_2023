#!/usr/bin/env bash

set -euo pipefail

find . -name "*.sh" -exec ./check_shell_script.sh {} +
