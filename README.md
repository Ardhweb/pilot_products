# pilot_products
#RunnerUp


**Render Free Tier Deployment **
Stat Command:  gunicorn pilot_products.wsgi:application

use this command *$ gunicorn pilot_products.wsgi:application *
for deploying put this into Render Project Settings below pre-Command

**Unix Sub-system**
Here’s the table in a copyable format:  

| **Dependency (Debian)**          | **Description**                                          | **Installation Command (Debian)**                        | **Python Package** (if applicable) | **Installation Command (Python)** |
|----------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------|----------------------------------|
| **Python Virtual Environment**  | Used to create isolated Python environments             | `sudo apt install -y python3-venv`                        | -                                | -                                |
| **Build Essentials**            | Required for compiling various Python packages          | `sudo apt install -y build-essential`                     | -                                | -                                |
| **pkg-config**                  | Helps find library locations during compilation         | `sudo apt install -y pkg-config`                          | -                                | -                                |
| **MySQL Development Headers**   | Required for MySQL database support (`mysqlclient`)     | `sudo apt install -y default-libmysqlclient-dev`          | `mysqlclient`                   | `pip install mysqlclient`        |
| **PostgreSQL Development Headers** | Required for PostgreSQL support (`psycopg2`)       | `sudo apt install -y libpq-dev`                          | `psycopg2`                      | `pip install psycopg2`           |
| **PostgreSQL Database Server**  | PostgreSQL database server                              | `sudo apt install -y postgresql postgresql-contrib`      | `psycopg2`                      | `pip install psycopg2`           |
| **Libffi**                      | Required for cryptographic and PDF-related libraries   | `sudo apt install -y libffi-dev`                         | `weasyprint`                    | `pip install weasyprint`         |
| **Libjpeg**                     | JPEG image support (used by WeasyPrint)                | `sudo apt install -y libjpeg-dev`                        | `weasyprint`                    | `pip install weasyprint`         |
| **Libpng**                      | PNG image support (used by WeasyPrint)                 | `sudo apt install -y libpng-dev`                         | `weasyprint`                    | `pip install weasyprint`         |
| **Cairo Graphics Library**      | Rendering library required for WeasyPrint              | `sudo apt install -y libcairo2 libcairo2-dev`            | `weasyprint`                    | `pip install weasyprint`         |
| **Pango Text Rendering**        | Text rendering support for WeasyPrint                  | `sudo apt install -y pango1.0-tools libpango1.0-dev`     | `weasyprint`                    | `pip install weasyprint`         |
| **GDK Pixbuf**                  | Image rendering for WeasyPrint                         | `sudo apt install -y libgdk-pixbuf2.0-dev`               | `weasyprint`                    | `pip install weasyprint`         |
| **HarfBuzz**                    | Text shaping library for WeasyPrint                    | `sudo apt install -y libharfbuzz-dev`                    | `weasyprint`                    | `pip install weasyprint`         |
| **FriBidi**                     | Bidirectional text support for WeasyPrint              | `sudo apt install -y libfribidi-dev`                     | `weasyprint`                    | `pip install weasyprint`         |
| **Gunicorn**                    | WSGI HTTP server for running Django in production     | -                                                        | `gunicorn`                      | `pip install gunicorn`           |