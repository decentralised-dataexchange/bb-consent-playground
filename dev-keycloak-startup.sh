#!/bin/bash
set +e

CONTAINER_API="keycloak"
TIMEOUT=120  # Timeout value in seconds
WAIT_INTERVAL=1  # Interval to check

echo "Waiting for Keycloak to start..."
elapsed_time=0

while [ $elapsed_time -lt $TIMEOUT ]; do
    if docker logs "$CONTAINER_API" 2>&1 | grep -q "Listening on: http://0.0.0.0:8080"; then
        echo "Keycloak started!"
        break
    else
        sleep $WAIT_INTERVAL
        elapsed_time=$((elapsed_time + WAIT_INTERVAL))
    fi
done

if [ $elapsed_time -ge $TIMEOUT ]; then
    echo "Timeout: Keycloak did not start within $TIMEOUT seconds."
    exit 1
fi
