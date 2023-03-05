from decimal import Decimal as D

from django.db.models import Model, DateTimeField, DecimalField, ForeignKey, PROTECT

from wallet_app.constants import MAX_DIGITS, DECIMAL_PLACES


class Transaction(Model):
    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    amount = DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, default=D(0.00)
    )
    ccy = ForeignKey("Currency", on_delete=PROTECT, related_name="transactions")

    from_wallet = ForeignKey(
        "Wallet", on_delete=PROTECT, related_name="transactions_from"
    )
    to_wallet = ForeignKey("Wallet", on_delete=PROTECT, related_name="transactions_to")

    class Meta:
        db_table = "transaction"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"<{self.Meta.verbose_name} >"
