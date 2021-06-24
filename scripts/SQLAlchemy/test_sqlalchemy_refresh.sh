# get
curl -X 'GET' \
  'http://127.0.0.1:5000/users/1' 
# put
curl -X 'PUT' \
  'http://127.0.0.1:5000/users/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "owner_id": 1
}' 