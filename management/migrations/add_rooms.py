import random

from django.db import migrations

NUM_ROOMS = 5
MAX_CAPACITY = 20
DEPARTMENTS = [
    'Radiology',
    'Psychiatry',
    'Surgery',
    'Paediatrics',
    'Oncology',
    'Nursing',
]

def form_rooms(Room):
    for department in DEPARTMENTS:
        for _ in range(NUM_ROOMS):
            Room.objects.create(
                department=department,
                capacity=MAX_CAPACITY,
                imageNum=random.randint(1, 5)
            )

def add_rooms(apps, schema_editor):
    Room = apps.get_model('management', 'Room')
    db_alias = schema_editor.connection.alias

    rooms_to_add = form_rooms(Room)

    
    Room.objects.using(db_alias).bulk_create(rooms_to_add)

class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('management', '0001_room_capacity'),
    ]

    operations = [
        migrations.RunPython(add_rooms)
    ]