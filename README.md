# Flipr-Externship

This is a simple REST API built using Flask for a basic notes app. The API provides CRUD operations for managing notes.

## Getting Started


### Prerequisites

- Docker
- Docker Compose

### Running the API

First, clone the repository to your local machine using:

    git clone https://github.com/KrishnaRishi2208/Flipr-Externship.git
    cd flask-notes-app

Then, Run the appplication using:

    docker-compose up

Now, the Flask application is up and running on your local system.

The API should now be running at `http://localhost:5000`.

## API Endpoints

### `GET /notes`

Fetches all notes.

**Response:**

- Status: `200 OK`
- Content-Type: `application/json`
- Payload: Array of note objects

```json
[
  {
    "id": 1,
    "content": "This is a note."
  },
  {
    "id": 2,
    "content": "This is another note."
  }
]
```

### `GET /notes/id`

Fetches note using id.

**Response:**

- Status: `200 OK`
- Content-Type: `application/json`
- Payload: note object

```json
[
  {
    "id": 2,
    "content": "This is another note."
  }
]
```

### `POST /notes`

Fetches note using id.

**Request:**

- Content-Type: `application/json`

```json
[
  {
    "content": "This is a new note."
  }
]
```

**Response:**

- Status: `200 OK`
- Content-Type: `application/json`
- Payload: note object

```json
[
  {
    "id": 1,
    "content": "This is a note."
  },
  {
    "id": 2,
    "content": "This is another note."
  }
]
```

### `PUT /notes/id`

Update a note using id.

**Request:**

- Content-Type: `application/json`

```json
[
  {
    "content": "This is a new note."
  }
]
```

**Response:**

- Status: `200 OK`
- Content-Type: `application/json`
- Payload: note object

```json
[
  {
    "id": 2,
    "content": "This is a new note."
  }
]
```

### `DELETE /notes/id`

DELETE a note using id.


**Response:**

- Status: `200 OK`
- Content-Type: `application/json`
- Payload: note object

```json
[
  {
    "message": "Note deleted"
  }
]
```
- Status: `404 NOT FOUND`
- Content-Type: `application/html`
- Payload: note object

```html
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try
	again.</p>
```
