#!/bin/sh

set -e

echo "⏳ Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "✅ Database is ready!"

echo "🔄 Applying migrations..."
python manage.py migrate --noinput

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear 2>/dev/null || true

echo "🚀 Starting application..."
exec "$@"