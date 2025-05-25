from pathlib import Path
import csv, os
from django.core.management.base import BaseCommand
from core.models import BusinessProfile, Location

class Command(BaseCommand):
    help = "Import locations from data/Table_Rock_Go_Locations.csv"

    def handle(self, *args, **options):
        # Base path is the project root (table-rock-go/)
        base_dir = Path(__file__).resolve().parents[4]
        csv_path = base_dir / 'data' / 'Table_Rock_Go_Locations.csv'

        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV not found at {csv_path}"))
            return

        count = 0
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                business = None
                if row['Type'].strip().lower() == 'restaurant':
                    business, _ = BusinessProfile.objects.get_or_create(
                        name=row['Name'].strip(),
                        defaults={'description': row.get('Notes', '').strip()}
                    )
                loc, created = Location.objects.get_or_create(
                    name=row['Name'].strip(),
                    defaults={
                        'type': row['Type'].strip().lower(),
                        'address': row.get('Address', '').strip(),
                        'phone': row.get('Phone', '').strip(),
                        'dock_access': row.get('Dock Access', '').strip().lower() == 'yes',
                        'courtesy_dock': row.get('Courtesy Dock', '').strip().lower() == 'yes',
                        'lanes': int(row['Lanes']) if row.get('Lanes', '').isdigit() else None,
                        'description': row.get('Notes', '').strip(),
                        'business': business,
                    }
                )
                count += 1
                status = "✅ Created" if created else "⚠️ Exists"
                self.stdout.write(f"{status}: {loc.name}")
        self.stdout.write(self.style.SUCCESS(f"Imported {count} locations."))
