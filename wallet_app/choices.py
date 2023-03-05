from django.db.models import TextChoices


class MerchantsChoices(TextChoices):
    capital_com_fca = "capital_com_fca", "Capital.com FCA Licence"


class CurrenciesChoices(TextChoices):
    GBP = "GBP", "Great Britain Pound"
