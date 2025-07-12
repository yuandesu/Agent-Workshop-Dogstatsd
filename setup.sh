#!/bin/bash
docker build -t weather-sim:1.0 .
docker compose up -d
