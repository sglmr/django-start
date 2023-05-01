# django-start
A starter project template project for Django. Why would I use this over something else?
1. You don't want to use bootstrap.
2. You don't want to rely on crispy forms to style forms because you're not using bootstrap.
3. You want to use "email" and don't want to use "username" on your custom users.
4. You want easier out-of-the-box access to all of the available django-allauth templates within your project.
5. You don't want to use docker.
6. You believe starting development with Postgres might be premature optimization for your fledgling application (or at least that you won't need a server with more resources than Simon Willison's laptop in 2022)[https://simonwillison.net/2022/Oct/23/datasette-gunicorn/#benchmarking-sqlite])

Comes pre-configured with:
- Django==4.2
- environs[django] for handling environment variables
- django-allauth for authentication
- django-authtools for custom users
- whitenoise[brotli] for static files
- pytest + a whole bunch of plugins for testing
- black & ruff



# Get Started

```bash
# 1. Create a virtual environment

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Check for outdated dependencies (and update if needed)
python -m pip list --outdated
python -m pip install -r requirements.txt --upgrade
```