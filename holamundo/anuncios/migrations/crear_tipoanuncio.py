from django.db import migrations


def create_default_tipo_anuncio(apps, schema_editor):
    TipoAnuncio = apps.get_model('anuncios', 'TipoAnuncio')
    TipoAnuncio.objects.create(id=1, glosa_tipo='General', estado='A')


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_tipo_anuncio),
    ]
