from oscar.apps.catalogue.categories import create_from_breadcrumbs

categories = ['Travels', 'Subscriptions']

for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)

print('Categories succesfuly added.')
