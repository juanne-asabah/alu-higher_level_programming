#!/bin/bash
# Sends a GET request to a URL with the required school header variable
curl -sH "X-School-User-Id: 98" "$1"
