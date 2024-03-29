# Generated by Django 5.0.2 on 2024-02-29 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='partit',
            unique_together={('local', 'visitant', 'lliga')},
        ),
        migrations.AddField(
            model_name='partit',
            name='detalls',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partit',
            name='inici',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps', models.TimeField()),
                ('tipus', models.CharField(choices=[('GOL', 'Gol'), ('AUTOGOL', 'Autogol'), ('FALTA', 'Falta'), ('PENALTY', 'Penalty'), ('MANS', 'Mans'), ('CESSIO', 'Cessio'), ('FORA_DE_JOC', 'Fora De Joc'), ('ASSISTENCIA', 'Assistencia'), ('TARGETA_GROGA', 'Targeta Groga'), ('TARGETA_VERMELLA', 'Targeta Vermella')], max_length=30)),
                ('detalls', models.TextField(blank=True, null=True)),
                ('equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ligas.equip')),
                ('jugador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_fets', to='ligas.jugador')),
                ('jugador2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_rebuts', to='ligas.jugador')),
                ('partit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligas.partit')),
            ],
        ),
        migrations.RemoveField(
            model_name='partit',
            name='data',
        ),
        migrations.RemoveField(
            model_name='partit',
            name='resultat_local',
        ),
        migrations.RemoveField(
            model_name='partit',
            name='resultat_visitant',
        ),
    ]
