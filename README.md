# My Docker Project

A simple Python web application containerized with Docker and served behind an Nginx reverse proxy.

## Project Structure
- `app.py` - Python web application
- `Dockerfile` - Instructions to build the app image
- `docker-compose.yml` - Runs the app and Nginx together
- `nginx.conf` - Nginx reverse proxy configuration

## How to Run
```bash
docker-compose up
```
Visit http://localhost:80 in your browser.

## Tech Stack
- Docker
- Docker Compose
- Python
- Nginx# mycompose
