from django.core.management.base import BaseCommand

from wallet_app.models.currency import Currency


class Command(BaseCommand):
    help = "Add base currencies to the database"

    def handle(self, *args, **options):

        ccy_list = [
            (True, "GBP", "Pound sterling", "£"),
            (True, "EUR", "Euro", "€"),
            (True, "USD", "United States dollar", "$"),
            (True, "PLN", "Polish złoty", "zł"),
        ]

        for ccy in ccy_list:
            ccy, is_created = Currency.objects.update_or_create(
                iso_code=ccy[1],
                verbose_name=ccy[2],
                sign=ccy[3],
            )
            print(ccy, is_created)
