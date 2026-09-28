# GPO Threat-Informed Security Catalog

> **200 Windows security GPO/ADMX controls classified through a threat-intelligence lens.**  
> Built for labs, purple teams, detection engineering, Active Directory hardening and security-baseline review.

[![Catalog](https://img.shields.io/badge/catalog-200%20controls-blue)](catalog/top-200-gpos.csv)
[![Focus](https://img.shields.io/badge/focus-threat--informed%20hardening-purple)](docs/CLASSIFICATION.md)
[![CI](https://img.shields.io/badge/CI-catalog%20validation-success)](.github/workflows/catalog-ci.yml)

## Why this repository exists

The original repository started as a small lab collection of PowerShell snippets. This version turns it into a structured, versionable security catalog rather than a pile of registry edits with optimistic comments.

The project does **not** claim that one universal GPO baseline fits every organization. Microsoft recommends using security baselines as a starting point, then testing and adapting them to the environment.

Each control adds a threat-intelligence layer:

- **CTI score (0-100)** for implementation sequencing.
- **Priority:** `P0`, `P1`, `P2`, `P3`.
- **Defensive function:** `Prevent`, `Detect`, `Contain`, `Recover`.
- **MITRE ATT&CK tactical mapping**.
- **Threat scenario** such as credential theft, lateral movement, ransomware, C2 or anti-forensics.
- **Rollout mode:** `Enforce`, `Audit -> Enforce`, `Pilot`, `Evaluate` or `Exception-only`.
- **Source ID** linked to Microsoft documentation and current baseline material.

## Repository map

```text
.
├── catalog/
│   └── top-200-gpos.csv
├── docs/
│   ├── CLASSIFICATION.md
│   ├── DEPLOYMENT.md
│   └── SOURCES.md
├── scripts/
│   ├── query_catalog.py
│   └── validate_catalog.py
├── legacy/
└── .github/workflows/
    └── catalog-ci.yml
```

## Query examples

```bash
python scripts/validate_catalog.py
python scripts/query_catalog.py --priority P0
python scripts/query_catalog.py --tactic "Credential Access"
python scripts/query_catalog.py --search NTLM
python scripts/query_catalog.py --rollout "Audit -> Enforce"
```

## Recommended operating model

1. **Baseline first:** compare the environment against the current Microsoft Security Compliance Toolkit.
2. **Threat relevance second:** prioritize controls tied to observed adversaries, attack paths and crown jewels.
3. **Audit before block** for compatibility-sensitive controls such as NTLM restrictions, ASR, AppLocker/App Control, device restrictions and some RDP/printing settings.
4. **Pilot by OU or security group** before broad deployment.
5. **Collect telemetry before and after enforcement** so the control can be measured.
6. **Document exceptions** with owner, justification, compensating control and expiry date.

See [Deployment Playbook](docs/DEPLOYMENT.md).

## Scope

Primary target:

- Windows 11 enterprise endpoints
- Windows Server 2025 member servers
- Windows Server 2025 domain controllers
- Active Directory environments using Group Policy and current ADMX templates

Some controls are version-, role-, licensing- or feature-dependent. Always verify the exact policy name, ADMX availability and supported value for the Windows build you deploy.

## Sources

The catalog is anchored in Microsoft Security Baselines / Security Compliance Toolkit and Microsoft product documentation, with MITRE ATT&CK used for threat mapping.

See [Sources](docs/SOURCES.md).

## Safety / deployment warning

This repository is intended for **lab validation and controlled enterprise hardening**. Do not import all 200 controls blindly into production. Authentication, application control, device control, firewall, print and remote-access policies can break legitimate workloads when deployed without dependency analysis.

## Legacy

The original scripts are preserved under `legacy/` for historical context. They are not the authoritative implementation layer for this catalog.
