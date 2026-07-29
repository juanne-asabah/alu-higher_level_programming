#!/bin/bash
# Sends a GET request to a URL with a custom header variable and value
curl -sLH "X-HolbertonSchool-User-Id: 98" "$1"
