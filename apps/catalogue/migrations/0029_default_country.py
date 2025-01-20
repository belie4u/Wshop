from django.db import migrations


def set_default_country_and_currency(apps, schema_editor):
    Country = apps.get_model('address', 'Country')

    Country.objects.get_or_create(
        iso_3166_1_a2='ES',
        iso_3166_1_a3='ESP',
        iso_3166_1_numeric='724',
        printable_name='Spain',
        name='Spain',
        display_order=1,
        is_shipping_country=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0028_new_product_vendor_subscription'),
    ]

    operations = [
        migrations.RunPython(set_default_country_and_currency),
    ]
