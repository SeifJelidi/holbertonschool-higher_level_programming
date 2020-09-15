#!/bin/bash
# Test code
curl -sI "$1" | grep -i "content-length:" | tr -d " \t" | cut -d ':' -f 2
