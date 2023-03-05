from django.db.models import (
    Model,
    CharField,
    UUIDField,
    DateTimeField,
    BooleanField,
    ForeignKey,
    UniqueConstraint,
    PROTECT,
    Q,
)

from wallet_app.choices import MerchantsChoices, CurrenciesChoices


class Wallet(Model):

    created_on = DateTimeField(auto_now_add=True)
    modified_on = DateTimeField(auto_now=True)

    ccy = ForeignKey(
        "Currency",
        on_delete=PROTECT,
        choices=CurrenciesChoices.choices,
        related_name="wallets",
    )

    name = CharField(
        max_length=64,
        blank=False,
        default="main",
        help_text="Account name used in user interface",
    )

    user_id = UUIDField(
        help_text="ID from User Service or any other User ID that we need",
        db_index=True,
    )
    merchant_id = CharField(
        max_length=32, choices=MerchantsChoices.choices, db_index=True
    )

    is_active = BooleanField(default=True, help_text="For disable purposes")
    is_deleted = BooleanField(default=False, help_text="For delete purposes")

    class Meta:
        db_table = "wallet"
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
        constraints = [
            UniqueConstraint(
                fields=["user_id", "merchant_id", "user_id", "ccy"],
                condition=Q(is_active=True),
                name="unique_active_wallet_per_user_per_ccy",
                violation_error_message=(
                    "It's not possible to add additional "
                    "Wallet with this Currency to this User"
                ),
            )
        ]

    def __str__(self):
        return f"<{self.Meta.verbose_name} {self.pk=} {self.ccy=} {self.user_id=}>"
