# Creature Archive

A REST API for cataloging creatures from horror, fantasy, and science fiction. Built with Django and Django REST Framework.

🔗 **Live API:** https://drf-creature-archive-production.up.railway.app/api/

## Features

- JWT Authentication
- Full CRUD for creatures and tags
- Filter by danger level, sapience, and tags
- Search by name, description, and lore
- Object-level permissions (only owners can edit their creatures)
- Pagination
- PostgreSQL database
- Dockerized

## Running Locally

### With Docker (recommended)

1. Clone the repository
   ```bash
   git clone https://github.com/kivancsy/DRF-Creature-Archive.git
   cd DRF-Creature-Archive
   ```

2. Set up environment variables
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your values.

3. Start with Docker Compose
   ```bash
   docker-compose up --build
   ```

### Without Docker

1. Clone the repository
   ```bash
   git clone https://github.com/kivancsy/DRF-Creature-Archive.git
   cd DRF-Creature-Archive
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your values.

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Start the server
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/login/ | Get JWT tokens |
| POST | /api/auth/refresh/ | Refresh access token |
| GET | /api/creatures/ | List all creatures |
| POST | /api/creatures/ | Create a creature |
| GET | /api/creatures/{id}/ | Get a creature |
| PUT | /api/creatures/{id}/ | Update a creature |
| DELETE | /api/creatures/{id}/ | Delete a creature |
| GET | /api/tags/ | List all tags |
| POST | /api/tags/ | Create a tag |

## Filtering & Search

```
GET /api/creatures/?danger_level=5
GET /api/creatures/?is_sapient=true
GET /api/creatures/?search=eldritch
GET /api/creatures/?mine=true
```