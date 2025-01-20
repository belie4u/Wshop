from django.db import migrations

def create_vendor_subscription_product_class(apps, schema_editor):
    ProductClass = apps.get_model('catalogue', 'ProductClass')
    ProductAttribute = apps.get_model('catalogue', 'ProductAttribute')

    vendor_subscription_product_class, _ = ProductClass.objects.get_or_create(
        name='Vendor Subscription',
        defaults={'requires_shipping': False},
    )

    attributes = [
        {'name': 'subscription_type', 'type': 'option'},
        {'name': 'fixed_amount', 'type': 'float'},
        {'name': 'percentage_fee', 'type': 'float'},
    ]

    for attr in attributes:
        ProductAttribute.objects.get_or_create(
            product_class=vendor_subscription_product_class,
            name=attr['name'],
            defaults={
                'type': attr['type'],
                'code': attr['name'].replace(' ', '_').lower(),
            },
        )

    AttributeOptionGroup = apps.get_model('catalogue', 'AttributeOptionGroup')
    AttributeOption = apps.get_model('catalogue', 'AttributeOption')

    subscription_type_group, _ = AttributeOptionGroup.objects.get_or_create(name='Subscription Type Options')

    options = ['monthly', 'trimestral', 'semestral', 'yearly']
    for option in options:
        AttributeOption.objects.get_or_create(
            group=subscription_type_group,
            option=option
        )

    # Link the option group to the subscription_type attribute
    subscription_type_attribute = ProductAttribute.objects.get(
        product_class=vendor_subscription_product_class,
        code='subscription_type'
    )
    subscription_type_attribute.option_group = subscription_type_group
    subscription_type_attribute.save()

class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0027_attributeoption_code_attributeoptiongroup_code_and_more'),
    ]

    operations = [
        migrations.RunPython(create_vendor_subscription_product_class),
    ]
