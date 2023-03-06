from django.db.models import (
    Model,
    DateTimeField,
    CharField,
    ManyToManyField,
    TextField,
)


class Merchant(Model):
    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    name = CharField(max_length=32)
    description = TextField(default="")

    own_wallets = ManyToManyField("Wallet")

    class Meta:
        verbose_name = "Merchant"
        verbose_name_plural = "Merchants"
        db_table = "merchant"

    def __str__(self):
        return (
            f"<{self._meta.verbose_name} {self.name} "
            f"wallets exists: {self.own_wallets.exists()}>"
        )
