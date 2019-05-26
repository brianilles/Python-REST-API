## To Get started

### Follow these steps

Assumes proper Python workspace

1. In base directory, you can run: `python server.py`

2. Open Postman (or similar) to **_http://localhost:5000 [endpoint]_**

| Endpoint                | Description            |
| ----------------------- | ---------------------- |
| GET `/test`             | Returns current time   |
| GET `/todos`            | Returns todos          |
| GET `/todo?id=<id>`     | Returns a todo by ID   |
| POST `/todos`           | Returns created todo   |
| PUT `/todos`            | Returns updated todo   |
| DELETE `/todos?id=<id>` | Returns 204 No content |
