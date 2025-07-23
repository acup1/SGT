#!/bin/sh
read message
git commit -a -m "$message"
git push
