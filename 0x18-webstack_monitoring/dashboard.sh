#!/usr/bin/bash

DASHBOARD_NAME="server01"
YOUR_API_KEY="caa9afa389d3d9e2db186086e09ec690"

# Make API request to retrieve the dashboard ID
DASHBOARD_ID=$(curl -s -G "https://api.datadoghq.com/api/v1/dashboard" \
    -H "Content-Type: application/json" \
    -H "DD-API-KEY: $YOUR_API_KEY" \
    -d "title=$DASHBOARD_NAME" \
    | jq -r '.dashboards[0].id')

# Print the dashboard ID
echo "Dashboard ID: $DASHBOARD_ID"

