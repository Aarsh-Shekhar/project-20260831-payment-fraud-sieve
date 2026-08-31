# Payment Fraud Sieve

Detects unusual synthetic payment behavior with explainable rules.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m payment_fraud_sieve.cli --input data/sample_payments.json
```

## Test

```bash
python3 -m unittest discover tests
```
