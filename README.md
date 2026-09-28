# GPO Threat-Informed Defense

> **200 Windows security controls connected to threat intelligence, ATT&CK, D3FEND, telemetry, role profiles and validation.**

V1 created the ranked Top 200. **V2 turns it into a defensive knowledge base.**

## Core model

```text
Threat / Actor → ATT&CK → GPO / ADMX → D3FEND → Windows telemetry → validation
```

Every control now has its own `controls/GPO-xxx.yml` with ATT&CK v19.2 techniques, D3FEND 1.6.0 mappings, telemetry, role applicability and risk components.

## Capabilities

- 200 individual YAML controls
- 8 deployment profiles: workstation, member server, DC, PAW, developer workstation, jump server, RDS, high security
- 6 threat packs: ransomware, credential theft, lateral movement, initial access, living off the land, AD takeover
- actor overlays for Scattered Spider, TeamPCP, ShinyHunters and Storm-0501
- environment-adjusted risk engine
- baseline comparator for CSV/JSON/XML/HTML/text exports\n- heuristic GPO-report drift check
- Attack Path to Policy
- graph + STIX 2.1 custom-object export\n- Neo4j node/relationship export
- Sigma starter rules
- 10 defensive labs
- GitHub Pages explorer

## CLI

```bash
python scripts/gpoctl.py search NTLM
python scripts/gpoctl.py search --technique T1003 --priority P0
python scripts/gpoctl.py pack ransomware
python scripts/gpoctl.py profile domain-controller
python scripts/gpoctl.py path credential-theft
python scripts/gpoctl.py score GPO-001 --asset-criticality 100 --detection-gap 70
python scripts/gpoctl.py drift --input gpo-report.xml\npython scripts/baseline_compare.py --observed assessment.csv\npython scripts/export_neo4j.py --output exports/neo4j
```

## Repository

```text
controls/        GPO-001.yml ... GPO-200.yml
data/            machine-readable indexes
profiles/        role baselines
threat-packs/    threat-oriented control views
actors/          ATT&CK actor overlays
detections/      Sigma starters
labs/            validation labs
scripts/         CLI, validation, graph/STIX export
site/            GitHub Pages explorer
docs/            architecture and operating model
```

## Framework versions

- MITRE ATT&CK **19.2**
- MITRE D3FEND **1.6.0**
- Sigma Specification **2.1.0**

ATT&CK v19 replaced the old Enterprise `TA0005 Defense Evasion` label with **TA0005 Stealth** and introduced **TA0112 Defense Impairment**. The catalog has been normalized accordingly.

## Deployment rule

Do not deploy all controls blindly. Authentication, application control, NTLM, RDP, printing, device control and firewall changes need dependency analysis and staged rollout. Microsoft documentation remains authoritative for exact policy semantics.

See [Architecture](docs/ARCHITECTURE.md), [Threat Packs](docs/THREAT_PACKS.md), [Risk Engine](docs/RISK_ENGINE.md), [Telemetry](docs/TELEMETRY.md) and [Sources](docs/SOURCES.md).
