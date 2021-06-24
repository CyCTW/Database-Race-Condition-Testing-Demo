curl -X 'POST' \
  'http://127.0.0.1:5000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user1@example.com",
  "password": "1234"
}' 

curl -X 'POST' \
  'http://127.0.0.1:5000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user2@example.com",
  "password": "1234"
}' 

curl -X 'POST' \
  'http://127.0.0.1:5000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Item1",
  "description": "string",
  "owner_id": 1
}' 