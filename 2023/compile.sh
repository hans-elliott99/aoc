#!/usr/bin/bash

input="$1"
output="${input/.cpp/".o"}"

echo "$output"

g++ -Wall -Werror -g "$input" -o "$output"

