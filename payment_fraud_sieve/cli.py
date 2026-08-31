from __future__ import annotations

import argparse
import json

from .io import load_records
from .scoring import rank_records, summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Detects unusual synthetic payment behavior with explainable rules.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    records = load_records(args.input)
    payload = summarize(records)
    payload["top_records"] = [
        {"id": record.id, "fraud_score": score}
        for record, score in rank_records(records)[: args.limit]
    ]
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
