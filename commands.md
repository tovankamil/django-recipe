# 1. Cleanup total (hapus semua cache)
docker-compose down -v
docker system prune -af --volumes

# 2. Build dengan no-cache (pastikan fresh install)
docker-compose build --no-cache

# 3. Jalankan semua services
docker-compose up

# Atau background mode
docker-compose up -d

# 4. Cek logs
docker-compose logs -f web

# 5. Verifikasi Django terinstall
docker-compose exec web pip list | grep -i django
# Output: Django 4.2.16

# 6. Jalankan migrasi manual
docker-compose exec web python manage.py migrate

# 7. Buat superuser
docker-compose exec web python manage.py createsuperuser

# 8. Test Celery
docker-compose exec celery celery -A myproject inspect active

# 9. Stop semua
docker-compose down

# 10. Stop dan hapus volumes (data bersih)
docker-compose down -v


### Debug

# Cek apakah requirements.txt ter-copy
docker run --rm -it $(docker-compose images -q web) cat /app/requirements.txt

# Cek pip list di container
docker run --rm -it $(docker-compose images -q web) pip list

# Build dengan verbose
docker-compose build --no-cache --progress=plain 2>&1 | tee build.log


# Restart container agar perubahan diterapkan
docker-compose restart web

# Atau rebuild jika perlu
docker-compose up -d --build web


### VERIFIKASI TIMEZONE

# Cek di Django shell
docker-compose exec web python manage.py shell

# Di shell, jalankan:
>>> from django.utils import timezone
>>> timezone.now()
# Output: datetime dengan tzinfo=Asia/Jakarta

>>> from django.conf import settings
>>> settings.TIME_ZONE
# Output: 'Asia/Jakarta'

>>> exit()



docker-compose down
docker-compose build --no-cache web # hanya restart service web lihat pada docker-compose.yml
docker-compose up -d


#### Test celery
docker-compose exec celery celery -A config inspect active


# Cek schedule yang aktif
docker-compose exec celery-beat celery -A config beat -l info --dry-run

# List all scheduled tasks
docker-compose exec web python manage.py shell
>>> from django_celery_beat.models import PeriodicTask
>>> PeriodicTask.objects.all()

# Trigger task manual (untuk test)
docker-compose exec celery celery -A config call apps.orders.tasks.send_order_reminder

# Monitor worker
docker-compose exec celery celery -A config inspect stats
docker-compose exec celery celery -A config inspect active
docker-compose exec celery celery -A config inspect scheduled  # Lihat task yang dijadwalkan

# Celery Beat Inspection & Monitoring Guide

Dokumentasi ini berisi kumpulan command untuk **inspect, monitoring, dan troubleshooting Celery Beat** pada environment **Docker + Django + Redis + Celery**.

---

# 1. Basic Beat Status

Digunakan untuk melihat status scheduler dan task yang berjalan di worker.

```bash
# Cek beat scheduler info (dry run)
docker-compose exec celery-beat celery -A config beat -l info --dry-run

# Cek scheduled tasks dari worker
docker-compose exec celery celery -A config inspect scheduled

# Cek active tasks
docker-compose exec celery celery -A config inspect active

# Cek reserved tasks (waiting to be executed)
docker-compose exec celery celery -A config inspect reserved
```

---

# 2. Database Scheduler (django-celery-beat)

Jika menggunakan **django-celery-beat**, semua schedule disimpan di database.

Masuk ke Django shell:

```bash
docker-compose exec web python manage.py shell
```

### List semua periodic tasks

```python
from django_celery_beat.models import PeriodicTask

PeriodicTask.objects.all().values('name', 'task', 'enabled')

# Example output
<QuerySet [
    {'name': 'cleanup-every-hour', 'task': 'app.tasks.cleanup', 'enabled': True}
]>
```

### List interval schedules

```python
from django_celery_beat.models import IntervalSchedule

IntervalSchedule.objects.all()

# Example
<QuerySet [
    <IntervalSchedule: every 1 hours>,
    <IntervalSchedule: every 10 seconds>
]>
```

### List crontab schedules

```python
from django_celery_beat.models import CrontabSchedule

CrontabSchedule.objects.all()

# Example
<QuerySet [
    <CrontabSchedule: 0 8 * * * (m/h/d/dM/MY)>
]>
```

Keluar dari shell:

```python
exit()
```

---

# 3. Beat Monitoring Commands

Command untuk monitoring **process dan log Celery Beat**.

```bash
# Cek beat container status
docker-compose ps celery-beat

# Lihat logs beat real-time
docker-compose logs -f celery-beat

# Cek beat PID dan uptime
docker-compose exec celery-beat ps aux | grep beat

# Cek beat heartbeat di Redis
docker-compose exec redis redis-cli keys "*beat*"
```

---

# 4. Task Inspection

Digunakan untuk inspect worker dan task yang tersedia.

```bash
# List semua registered tasks
docker-compose exec celery celery -A config inspect registered

# Cek worker statistics
docker-compose exec celery celery -A config inspect stats

# Ping semua workers
docker-compose exec celery celery -A control ping

# Revoke scheduled task berdasarkan ID
docker-compose exec celery celery -A config control revoke <task_id>
```

---

# 5. Beat Configuration Check

Digunakan untuk memastikan **scheduler dan konfigurasi Celery Beat sudah benar**.

### Cek beat schedule dari Celery config

```bash
docker-compose exec celery-beat python -c "
from config.celery import app
print('Beat Schedule:', app.conf.beat_schedule)
print('Scheduler:', app.conf.beat_scheduler)
"
```

### Cek Django settings Celery Beat

```bash
docker-compose exec celery-beat python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.conf import settings
print('CELERY_BEAT_SCHEDULER:', settings.CELERY_BEAT_SCHEDULER)
"
```

---

# 6. Debug Beat Issues

Digunakan saat Celery Beat **tidak menjalankan scheduled tasks**.

```bash
# Jalankan beat dengan verbose debug
docker-compose exec celery-beat celery -A config beat -l debug

# Jalankan beat tanpa detach
docker-compose run --rm celery-beat celery -A config beat -l info

# Force reload beat schedule
docker-compose restart celery-beat

# Cek apakah beat benar-benar mengirim task ke Redis
docker-compose exec redis redis-cli llen celery
```

---

# Summary Table

| Command                      | Purpose                               |
| ---------------------------- | ------------------------------------- |
| `inspect scheduled`          | Melihat task yang dijadwalkan         |
| `inspect active`             | Melihat task yang sedang berjalan     |
| `inspect registered`         | Melihat semua task yang tersedia      |
| `beat --dry-run`             | Test scheduler tanpa menjalankan task |
| `PeriodicTask.objects.all()` | Melihat schedule dari database        |

---

# Troubleshoot Beat Not Working

Langkah cepat untuk debugging jika Celery Beat tidak berjalan.

```bash
# 1. Pastikan container beat berjalan
docker-compose ps | grep beat

# 2. Cek logs error
docker-compose logs celery-beat | tail -50

# 3. Verifikasi beat schedule loaded
docker-compose exec celery-beat celery -A config beat -l info --dry-run

# 4. Restart beat
docker-compose restart celery-beat

# 5. Monitor message broker
docker-compose exec redis redis-cli monitor
```

Jika beat berjalan dengan benar, maka **akan terlihat message masuk ke Redis broker**.

---

# Best Practice

1. Gunakan **django-celery-beat** untuk schedule dinamis.
2. Pastikan hanya **1 instance celery-beat** berjalan.
3. Gunakan **Redis atau RabbitMQ sebagai broker yang stabil**.
4. Monitor worker dengan:

```bash
celery -A config events
```

atau gunakan tools monitoring seperti:

* Flower
* Prometheus
* Grafana

---

# Reference Architecture

```
           +-------------+
           | Celery Beat |
           +-------------+
                  |
                  | send task
                  v
            +-----------+
            |   Redis   |
            +-----------+
                  |
                  | consume
                  v
            +------------+
            | Celery     |
            | Workers    |
            +------------+
                  |
                  v
              Django App
```

---
