# Generated by Django 3.0.4 on 2020-04-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='Model_DeskPhoneHeadset',
            field=models.CharField(choices=[('SENNHEISER', 'SENNHEISER SC 230'), ('SENNHEISER ', 'SENNHEISER SC 260'), ('JABRA', 'Jabra  GN 2000'), ('JABRA', 'JABRA - GN 2000 - BIZ'), ('JABRA', 'JABRA GN 1216'), ('JABRA ', 'JABRA -SC 260'), ('JABRA ', 'JABRA - BIZ620'), ('JABRA', 'JABRA 2300'), ('JABRA', 'JABRA')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='Model_DeskPhoneHeadset',
            field=models.CharField(choices=[('SENNHEISER', 'SENNHEISER SC 230'), ('SENNHEISER ', 'SENNHEISER SC 260'), ('JABRA', 'Jabra  GN 2000'), ('JABRA', 'JABRA - GN 2000 - BIZ'), ('JABRA', 'JABRA GN 1216'), ('JABRA ', 'JABRA -SC 260'), ('JABRA ', 'JABRA - BIZ620'), ('JABRA', 'JABRA 2300'), ('JABRA', 'JABRA')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='Model_DeskPhoneHeadset',
            field=models.CharField(choices=[('SENNHEISER', 'SENNHEISER SC 230'), ('SENNHEISER ', 'SENNHEISER SC 260'), ('JABRA', 'Jabra  GN 2000'), ('JABRA', 'JABRA - GN 2000 - BIZ'), ('JABRA', 'JABRA GN 1216'), ('JABRA ', 'JABRA -SC 260'), ('JABRA ', 'JABRA - BIZ620'), ('JABRA', 'JABRA 2300'), ('JABRA', 'JABRA')], max_length=100, null=True),
        ),
    ]
