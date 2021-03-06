# Generated by Django 3.2.12 on 2022-02-11 17:37

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_understanding_b4_group', to='otree.session')),
            ],
            options={
                'db_table': 'circle_understanding_b4_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='circle_understanding_b4_subsession', to='otree.session')),
            ],
            options={
                'db_table': 'circle_understanding_b4_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('comprehension_wrong_attempts', otree.db.models.PositiveIntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='circle_understanding_b4.group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_understanding_b4_player', to='otree.participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_understanding_b4_player', to='otree.session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle_understanding_b4.subsession')),
            ],
            options={
                'db_table': 'circle_understanding_b4_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle_understanding_b4.subsession'),
        ),
    ]
