# WALLET SERVICE
### EMI API infrastructure component

Service allow to manage wallets, transactions, currencies and balances for given user and his merchant.

### Installation

Poetry install
```shell
poetry install
```

Apply migrations:
```shell
./manage.py migrate
```

Init currencies:
```shell
./manage.py init_currencies
```
