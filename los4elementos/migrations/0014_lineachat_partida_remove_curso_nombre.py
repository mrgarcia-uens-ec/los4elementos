# Generated by Django 5.0.4 on 2024-09-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("los4elementos", "0013_estudiante_foto"),
    ]

    operations = [
        migrations.CreateModel(
            name="LineaChat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_hora", models.DateTimeField(null=True)),
                ("nombre_jugador", models.CharField(max_length=100, null=True)),
                ("texto", models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Partida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cod_partida", models.CharField(max_length=100, null=True)),
                ("nombre", models.CharField(max_length=100, null=True)),
                ("fecha_creacion", models.DateTimeField(null=True)),
                ("fecha_inicio", models.DateTimeField(null=True)),
                ("nombre_jugador_1", models.CharField(max_length=100, null=True)),
                ("nombre_jugador_2", models.CharField(max_length=100, null=True)),
                ("nombre_jugador_3", models.CharField(max_length=100, null=True)),
                ("nombre_anfitrion", models.CharField(max_length=100, null=True)),
                ("hora_fin_jugador1", models.DateTimeField(null=True)),
                ("hora_fin_jugador2", models.DateTimeField(null=True)),
                ("hora_fin_jugador3", models.DateTimeField(null=True)),
                ("hora_fin_anfitrion", models.DateTimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="curso",
            name="nombre",
        ),
    ]
