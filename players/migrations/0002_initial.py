# Generated by Django 3.2.12 on 2022-08-10 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sellhistory',
            name='buying_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchases', to='players.team'),
        ),
        migrations.AddField(
            model_name='sellhistory',
            name='selling_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sales', to='players.team'),
        ),
        migrations.AddField(
            model_name='sellhistory',
            name='transfer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.sell'),
        ),
        migrations.AddField(
            model_name='sell',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.player'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.team'),
        ),
        migrations.AddField(
            model_name='gamehistory',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.player'),
        ),
    ]
