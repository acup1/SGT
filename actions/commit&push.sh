#!/bin/sh
git add -A
read message
git commit -a -m "$message"
git push
