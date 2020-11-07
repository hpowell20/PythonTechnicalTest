from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lei', models.CharField(max_length=100, unique=True)),
                ('legal_name', models.TextField(blank=True, default=None, null=True)),
                ('isin', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=50)),
                ('maturity', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bond',
                'ordering': ('created_date',),
            },
        ),
    ]
