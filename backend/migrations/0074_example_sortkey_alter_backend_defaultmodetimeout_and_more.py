# Generated by Django 5.0.3 on 2024-10-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0073_backend_mapviewbaseurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='sortKey',
            field=models.CharField(blank=True, default='', help_text='Sort key, according to which examples are ordered lexicographically for a backend', max_length=100, verbose_name='Sort key'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='defaultModeTimeout',
            field=models.FloatField(default=0, help_text='Default timeout in seconds for autocompletion queries', verbose_name='Autocomplete timeout'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='dynamicSuggestions',
            field=models.IntegerField(choices=[(3, '4. Mixed mode'), (2, '3. SPARQL & context sensitive entities'), (1, '2. SPARQL & context insensitive entities'), (0, '1. SPARQL syntax & keywords only')], default=2, help_text='Default for how to compute autocompletion queries if any', verbose_name='Default autocompletion mode'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='isDefault',
            field=models.BooleanField(default=0, help_text='Check if this should be the default backend for the QLever UI', verbose_name='Use as default'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='isNoSlugMode',
            field=models.BooleanField(default=0, help_text='Check if this default backend should also be available without a slug in the QLever UI', verbose_name='Enable no-slug mode'),
        ),
        migrations.AlterField(
            model_name='backend',
            name='mixedModeTimeout',
            field=models.FloatField(default=1, help_text='Timeout in seconds for the sensitive autocompletion query in mixed mode', verbose_name='Mixed mode timeout'),
        ),
    ]