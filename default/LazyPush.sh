#!/bin/sh
git add -A
git commit -a -m "just commit"
git push --set-upstream origin $(git branch | awk '{print $2}')
