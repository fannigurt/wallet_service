from django.db.models import Model, DateTimeField, DecimalField, ForeignKey, DO_NOTHING


class Rate(Model):
    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    date = DateTimeField(auto_now_add=True)

    from_ccy = ForeignKey(
        "Currency", on_delete=DO_NOTHING, null=False, related_name="rates_from"
    )
    to_ccy = ForeignKey(
        "Currency", on_delete=DO_NOTHING, null=False, related_name="rates_to"
    )

    rate_value = DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        db_table = "rate"
        verbose_name = "Rate"
        verbose_name_plural = "Rates"

    def __str__(self):
        return f"<{self._meta.verbose_name}: 1.00 {self.from_ccy} > {self.rate_value} {self.to_ccy}>"
