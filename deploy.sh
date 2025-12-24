#!/usr/bin/env bash

git fetch origin
git checkout master
git pull origin master

sudo docker compose -f docker-compose.yml build
sudo docker compose -f docker-compose.yml down
sudo docker compose -f docker-compose.yml up -d