#!/bin/sh

set -e

pip install -r /app/requirements/local.txt

cd /app

export FLASK_APP=books.app
export FLASK_ENV=development

exec flask run -h 0.0.0.0 -p 8001
