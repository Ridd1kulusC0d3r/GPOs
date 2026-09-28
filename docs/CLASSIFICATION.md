# Classification model

This repository ranks controls by **threat relevance and deployment value**, not by compliance checkbox count.

## Priority bands

| Priority | CTI score | Meaning |
|---|---:|---|
| **P0** | 95-100 | Highest-value controls against common credential theft, lateral movement, malware execution and ransomware paths. |
| **P1** | 89-94.99 | Core hardening and detection controls that materially improve resistance and visibility. |
| **P2** | 83-88.99 | Strong controls that are more role-, workflow- or environment-dependent. |
| **P3** | <83 | Useful controls that usually require more compatibility analysis or provide narrower defensive value. |

## Defensive function

- **Prevent**: reduces the chance an adversary can execute, persist, steal credentials or exploit a service.
- **Detect**: increases telemetry for hunting, detection engineering and incident response.
- **Contain**: limits blast radius, lateral movement or remote access.
- **Recover**: protects recovery material or improves restoration after compromise.

## CTI score

`cti_score` is an **ordinal curation score**, not a breach probability.

It considers:

1. threat prevalence;
2. blast-radius reduction;
3. detection value;
4. deployment friction.

The score answers: **what should I evaluate first if the goal is reducing real attack paths?**

## ATT&CK mapping

Mappings are tactical, not claims that one GPO “solves” an ATT&CK technique.

Main themes represented:

- `TA0001` Initial Access
- `TA0002` Execution
- `TA0003` Persistence
- `TA0004` Privilege Escalation
- `TA0005` Defense Evasion / Stealth
- `TA0006` Credential Access
- `TA0007` Discovery
- `TA0008` Lateral Movement
- `TA0009` Collection
- `TA0010` Exfiltration
- `TA0011` Command and Control
- `TA0040` Impact
- `TA0112` Defense Impairment

## Rollout labels

| Label | Meaning |
|---|---|
| `Enforce` | Usually suitable for direct enforcement after normal testing. |
| `Audit` | Telemetry-only or observation-oriented control. |
| `Audit -> Enforce` | Measure dependencies first, then block or deny. |
| `Pilot -> Enforce` | Requires limited rollout before wider deployment. |
| `Pilot` | Environment-specific; evaluate on representative systems. |
| `Evaluate` | No universal recommendation without architecture context. |
| `Exception-only` | Keep exceptions minimal, documented and time-bounded. |

## Limitation

Policy availability, exact UI wording and supported values vary by Windows release, role and ADMX version. The catalog is a **curated defensive index**. Microsoft baseline packages and product documentation remain authoritative for exact implementation semantics.
