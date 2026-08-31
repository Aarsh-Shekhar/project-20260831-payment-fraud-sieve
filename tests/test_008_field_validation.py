import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="payment-008", exposure=46193, signal=0.628, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
