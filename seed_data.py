"""
Script para poblar la base de datos con datos iniciales.
Ejecutar con: python manage.py shell < seed_data.py
  o: python seed_data.py (desde la carpeta del proyecto)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportsvision.settings')
django.setup()

from apps.exercises.models import Equipo, GrupoMuscular, Ejercicio

print("Creando equipos...")
equipos_data = [
    ('banco',          '🏋️'),
    ('peso_corporal',  '🤸'),
    ('disco',          '⚫'),
    ('mancuernas',     '💪'),
    ('barra',          '🏋️'),
    ('barra_dominadas','🔱'),
    ('kettlebell',     '🔔'),
    ('banda',          '🟠'),
]
equipos = {}
for nombre, icono in equipos_data:
    e, _ = Equipo.objects.get_or_create(nombre=nombre, defaults={'icono': icono})
    equipos[nombre] = e
    print(f"  ✓ {e}")

print("\nCreando grupos musculares...")
grupos_data = [
    ('Pecho', 'pecho'),
    ('Espalda', 'espalda'),
    ('Hombros', 'hombros'),
    ('Bíceps', 'biceps'),
    ('Tríceps', 'triceps'),
    ('Piernas', 'piernas'),
    ('Glúteos', 'gluteos'),
    ('Abdomen', 'abdomen'),
    ('Pantorrillas', 'pantorrillas'),
    ('Antebrazos', 'antebrazos'),
]
grupos = {}
for nombre, slug in grupos_data:
    g, _ = GrupoMuscular.objects.get_or_create(slug=slug, defaults={'nombre': nombre})
    grupos[slug] = g
    print(f"  ✓ {g}")

print("\nCreando ejercicios...")
ejercicios_data = [
    # (nombre, grupo_slug, [equipos], nivel, descripcion)
    ('Press de Banca con Barra', 'pecho', ['banco', 'barra'], 'intermedio',
     'Acostado en el banco, baja la barra al pecho y empuja hacia arriba.'),
    ('Flexiones (Push-ups)', 'pecho', ['peso_corporal'], 'principiante',
     'En posición de plancha, baja el pecho al suelo y empuja.'),
    ('Press con Mancuernas', 'pecho', ['banco', 'mancuernas'], 'principiante',
     'Acostado en el banco con mancuernas, baja controlado y empuja.'),
    ('Aperturas con Mancuernas', 'pecho', ['banco', 'mancuernas'], 'intermedio',
     'Acostado, abre los brazos en arco hasta estirar el pecho.'),

    ('Dominadas', 'espalda', ['barra_dominadas'], 'intermedio',
     'Cuelga de la barra y jala el cuerpo hacia arriba.'),
    ('Remo con Barra', 'espalda', ['barra'], 'intermedio',
     'Inclinado, jala la barra hacia el abdomen.'),
    ('Remo con Mancuerna', 'espalda', ['mancuernas', 'banco'], 'principiante',
     'Apoyado en el banco, jala la mancuerna hacia la cadera.'),
    ('Pull-down con Banda', 'espalda', ['banda'], 'principiante',
     'Jala la banda de arriba hacia abajo, imitando las dominadas.'),

    ('Press Militar con Barra', 'hombros', ['barra'], 'intermedio',
     'De pie, empuja la barra desde los hombros hacia arriba.'),
    ('Elevaciones Laterales', 'hombros', ['mancuernas'], 'principiante',
     'Eleva las mancuernas hacia los lados hasta la altura de los hombros.'),
    ('Press Arnold', 'hombros', ['mancuernas'], 'intermedio',
     'Gira las muñecas mientras empujas las mancuernas hacia arriba.'),

    ('Curl de Bíceps con Barra', 'biceps', ['barra'], 'principiante',
     'Parado, flexiona los codos levantando la barra.'),
    ('Curl con Mancuernas', 'biceps', ['mancuernas'], 'principiante',
     'Alternado o simultáneo, flexiona los codos con mancuernas.'),
    ('Curl con Banda', 'biceps', ['banda'], 'principiante',
     'Pisa la banda y realiza curl de bíceps.'),

    ('Extensión de Tríceps', 'triceps', ['banda', 'mancuernas'], 'principiante',
     'Extiende el codo con resistencia de banda o mancuerna.'),
    ('Fondos en Paralelas', 'triceps', ['peso_corporal'], 'intermedio',
     'Baja y sube el cuerpo en paralelas apoyando en los brazos.'),
    ('Press Francés', 'triceps', ['barra', 'mancuernas'], 'intermedio',
     'Acostado, flexiona los codos detrás de la cabeza y extiende.'),

    ('Sentadilla con Barra', 'piernas', ['barra'], 'intermedio',
     'Con barra en los hombros, baja como si fueras a sentarte.'),
    ('Sentadilla con Peso Corporal', 'piernas', ['peso_corporal'], 'principiante',
     'Baja hasta que los muslos queden paralelos al suelo.'),
    ('Prensa con Disco', 'piernas', ['disco'], 'intermedio',
     'Usa un disco como peso adicional para variaciones de sentadilla.'),
    ('Zancadas', 'piernas', ['mancuernas', 'peso_corporal'], 'principiante',
     'Da un paso adelante y baja la rodilla trasera al suelo.'),
    ('Sentadilla con Kettlebell', 'piernas', ['kettlebell'], 'principiante',
     'Sostén el kettlebell frente al pecho y realiza sentadilla goblet.'),

    ('Hip Thrust con Barra', 'gluteos', ['barra', 'banco'], 'intermedio',
     'Apoya la espalda en el banco y eleva las caderas con barra.'),
    ('Patada de Glúteo con Banda', 'gluteos', ['banda'], 'principiante',
     'Con banda en los tobillos, realiza patadas traseras.'),
    ('Peso Muerto Rumano', 'gluteos', ['barra', 'mancuernas'], 'intermedio',
     'Con piernas casi extendidas, baja el peso manteniendo la espalda recta.'),

    ('Plancha Abdominal', 'abdomen', ['peso_corporal'], 'principiante',
     'Mantén la posición de plancha con el cuerpo recto.'),
    ('Crunchs', 'abdomen', ['peso_corporal'], 'principiante',
     'Acostado, contrae el abdomen levantando los hombros.'),
    ('Rueda Abdominal', 'abdomen', ['peso_corporal'], 'avanzado',
     'Desde rodillas, rueda hacia adelante extendiendo el cuerpo.'),

    ('Elevaciones de Pantorrilla con Mancuernas', 'pantorrillas', ['mancuernas'], 'principiante',
     'De pie con mancuernas, elévate en puntas de pie.'),
    ('Elevaciones de Pantorrilla', 'pantorrillas', ['peso_corporal', 'barra'], 'principiante',
     'Elévate en puntas de pie con o sin peso adicional.'),
]

for nombre, grupo_slug, equipo_nombres, nivel, descripcion in ejercicios_data:
    ej, created = Ejercicio.objects.get_or_create(
        nombre=nombre,
        defaults={
            'grupo_muscular': grupos[grupo_slug],
            'nivel': nivel,
            'descripcion': descripcion,
        }
    )
    ej.equipos.set([equipos[e] for e in equipo_nombres if e in equipos])
    status = "creado" if created else "ya existía"
    print(f"  {'✓' if created else '·'} {nombre} ({status})")

print(f"\n✅ Listo!")
print(f"   Equipos: {Equipo.objects.count()}")
print(f"   Grupos musculares: {GrupoMuscular.objects.count()}")
print(f"   Ejercicios: {Ejercicio.objects.count()}")
print("\nPróximos pasos:")
print("  python manage.py createsuperuser")
print("  python manage.py runserver")
