# Django Postgres IOT: An IOT project example using Django Rest Framework, Firebase Authentication and Postgres

This project aims to create a web server that responds in less than 100 ms to all data requests 
from a large timeseries database (1B), for that it uses some optimizations and architectural decisions


## Usage

*In Fedora use podman command instead docker*

1. Use postgres docker container

```bash
docker run --name postgres-iot-1 -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

2. Use memcached docker container

```bash
docker run --name memcached-iot-1 -p 11211:11211 -d memcached memcached -m 64
```

3. Set Firebase Authentication

You need create a Firebase Project and download de credentials

4. Create a virtual env

```bash
python -m venv .env
```

5. In Fedora install some dependencies (without that you can not install psycopg2 Python package)

```bash
dnf install python3-devel libpq-devel
```

6. Install Python dependencies

```bash
pip install -r requirements.txt
```

7. Run migrations


```bash
python manage.py makemigrations
python manage.py migrate
```

8. Use populate_database.py to create a huge database 

```bash
./populate_database.py
```


## License

The MIT License (MIT)

Copyright (c) 2020 Robinson D. S. Santos <robinsondssantos at gmail dot com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
