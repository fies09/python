#!/bin/bash
git stash
git pull
git stash pop
git add .
git commit -m ""
git push
