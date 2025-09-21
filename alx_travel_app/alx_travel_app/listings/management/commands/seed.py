import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create a default user if not exists
        user, _ = User.objects.get_or_create(username="demo", defaults={"password": "password123"})

        # Sample data
        listings_data = [
            {"title": "Beachfront Villa", "description": "Luxury villa by the sea", "price_per_night": 200.00, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains", "price_per_night": 120.00, "location": "Colorado"},
            {"title": "City Apartment", "description": "Modern apartment downtown", "price_per_night": 150.00, "location": "New York"},
        ]

        for data in listings_data:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
