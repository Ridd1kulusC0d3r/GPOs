# Baseline comparison

`scripts/baseline_compare.py` compares the Top 200 with exported evidence.

Supported inputs:

- CSV assessment exports;
- JSON;
- XML, including XML-like Policy Analyzer / GPO exports;
- HTML reports;
- gpresult / plain-text output.

For exact comparison, use CSV columns `id,current_state`. For XML/HTML/text the tool performs a policy-name presence check and reports `observed` / `not_observed`; that is deliberately not presented as proof of the configured value.

Examples:

```bash
python scripts/baseline_compare.py --observed gpresult.html
python scripts/baseline_compare.py --observed assessment.csv --format csv --output results.csv
```

For Microsoft Security Compliance Toolkit or CIS material distributed as spreadsheets, export the relevant policy table to CSV before comparison. The repository avoids pretending that arbitrary Excel workbooks share one stable schema.
