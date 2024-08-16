## Project Overview
This project is a web application built using Django that features a multilingual (Turkish and English) translation system integrated with Django Rest Framework (DRF). The project provides an API capable of handling searches with Turkish character compatibility in the database. Users can create content in both Turkish and English and perform searches that account for Turkish characters.

## Technologies Used
- **Django**: Used as the web framework.
- **Django Rest Framework (DRF)**: Used for building APIs.
- **django-parler**: Used for multilingual content management.
- **PostgreSQL**: Used as the database.
- **psycopg2-binary**: Used to connect Django with PostgreSQL.
- **Elasticsearch**: Used to provide advanced search capabilities.
- **Docker Compose**: Used to start Elasticsearch.

## Requirements
- **Python**
- **Django**
- **PostgreSQL**
- **Docker & Docker Compose**

## Install Required Packages
```bash
pip install -r requirements.txt
Database Configuration
Update the database settings in the settings.py file according to your PostgreSQL setup.

Elasticsearch
Start Elasticsearch using Docker Compose:


docker-compose up -d
You can check if Elasticsearch is running by visiting the following URL: http://localhost:9200

Integrate Elasticsearch with Django
Install the necessary packages:

pip install django-elasticsearch-dsl django-elasticsearch-dsl-drf
Build Elasticsearch Indexes

python manage.py search_index --rebuild
Start the Server

python manage.py runserver
Usage (Main)
Multilingual Content Management: Users can create content in both Turkish and English using django-parler.
Turkish Character Compatible Search: Searches can be performed with Turkish character compatibility by using the "unaccent" extension in PostgreSQL and custom search functions.
