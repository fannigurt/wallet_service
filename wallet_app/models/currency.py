from django.db.models import Model, CharField, DateTimeField, BooleanField


class Currency(Model):
    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    verbose_name = CharField(max_length=128)
    iso_code = CharField(max_length=3)
    sign = CharField(max_length=3)

    is_active = BooleanField(default=True)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        db_table = "currency"

    def __str__(self):
        return f"{self.iso_code}"
