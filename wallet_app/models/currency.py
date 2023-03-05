from django.db.models import Model, CharField, DateTimeField, BooleanField


class Currency(Model):
    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    is_active = BooleanField(default=True)

    iso_code = CharField(max_length=3)
    verbose_name = CharField(max_length=128)
    sign = CharField(max_length=1)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        db_table = "currency"

    def __str__(self):
        return f"{self.iso_code}"
