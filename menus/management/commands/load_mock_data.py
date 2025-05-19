from django.core.management.base import BaseCommand
from menus.models import Menu, MenuItem
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Loads mock data + creates superuser"

    def handle(self, *args, **options):
        # Create superuser
        User.objects.create_superuser(
            username="admin",
            password="admin123",
            email="admin@example.com"
        )

        # Create mock menu
        main_menu = Menu.objects.create(name="Main Navigation")
        second_menu = Menu.objects.create(name="Second Navigation")

        # Create menu items
        MenuItem.objects.bulk_create([
            MenuItem(menu=main_menu, name="Home"),
            MenuItem(menu=second_menu, name="Products"),
            MenuItem(menu=main_menu, name="Premium", parent_id=2),  # Child of Products
            MenuItem(menu=main_menu, name="Contact"),
        ])

        self.stdout.write(self.style.SUCCESS("Mock data loaded!"))