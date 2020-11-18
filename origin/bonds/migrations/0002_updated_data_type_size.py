from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bond',
            name='currency',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='bond',
            name='isin',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bond',
            name='lei',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
