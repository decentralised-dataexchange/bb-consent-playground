#!/bin/bash
set +e

API_URL="http://api:80/onboard/individual/login/"

# Function to check if the API is up and running
check_api() {
  curl -sS -X POST "$API_URL" -H "accept: application/json" -H "content-type: application/json" -d '{"username":"admin@skatteverket.se","password":"qwerty123"}'
}

# Wait for the API to be ready
until check_api; do
  echo "Waiting for the API to be ready..."
  sleep 1
done

python main.py
