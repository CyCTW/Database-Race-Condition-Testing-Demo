#!/bin/bash
echo "Execute first PUT Request..."
curl -X 'PUT' \
  'http://127.0.0.1:5000/items/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "owner_id": 2
}' &
echo "Execute Second PUT Request..."
curl -X 'PUT' \
  'http://127.0.0.1:5000/items/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "owner_id": 1
}' &
wait