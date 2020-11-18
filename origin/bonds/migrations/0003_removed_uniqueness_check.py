from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0002_updated_data_type_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bond',
            name='lei',
            field=models.CharField(max_length=20),
        ),
    ]
