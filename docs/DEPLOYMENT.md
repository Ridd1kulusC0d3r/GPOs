# Deployment playbook

Use this catalog as a **decision layer over Microsoft baselines**, not as one giant GPO to import.

## Phase 0 - Inventory

Before changing policy:

- identify Windows versions, server roles and domain functional level;
- export existing GPOs and inheritance;
- inventory authentication dependencies, especially NTLM;
- inventory RDP, WinRM, WMI and PsExec administration workflows;
- inventory application-control and software-distribution dependencies;
- identify privileged workstations, domain controllers and crown-jewel servers;
- confirm centralized event-collection capacity.

## Phase 1 - Compare against the official baseline

Use Microsoft's Security Compliance Toolkit / Policy Analyzer to compare current GPOs with the supported Microsoft baseline.

Classify every delta as:

- already compliant;
- more restrictive;
- less restrictive;
- intentionally exempted;
- unknown / needs owner.

## Phase 2 - Deploy P0 in waves

Suggested order:

1. Credential Guard / LSA protections.
2. Windows LAPS.
3. NTLM visibility and migration preparation.
4. SMB signing and legacy protocol reduction.
5. Microsoft Defender / ASR.
6. Windows Defender Firewall.
7. PowerShell and process telemetry.

Do **not** begin with domain-wide blocking of NTLM or application control without dependency evidence.

## Phase 3 - Audit first

Start in audit or observation mode for:

- NTLM restrictions;
- ASR rules that can affect line-of-business applications;
- AppLocker / App Control for Business;
- removable-media and device-installation restrictions;
- RDP redirection restrictions;
- print hardening in legacy estates.

A useful success criterion: you can name the legitimate dependencies that would break before enforcement.

## Phase 4 - Pilot

Create dedicated test OUs or security groups for representative:

- workstations;
- privileged workstations;
- member servers;
- domain controllers;
- special workloads.

Track authentication failures, application blocks, event volume, help-desk tickets, performance and rollback steps.

## Phase 5 - Enforce and measure

Useful metrics include:

- Credential Guard coverage;
- LAPS coverage and password freshness;
- NTLM events over time;
- unsigned SMB sessions;
- ASR block/audit events;
- PowerShell script-block logging coverage;
- event-forwarding latency;
- firewall dropped-connection telemetry.

## Exception model

Every exception should include:

- control ID;
- asset / OU / application;
- business owner;
- technical owner;
- reason;
- compensating control;
- approval;
- expiry date;
- revalidation date.

An exception with no expiry date is not an exception. It is a permanent policy change wearing a fake moustache.

## Rollback

Before enforcing compatibility-sensitive policy:

1. export the target GPO;
2. document the prior value;
3. identify the rollback owner;
4. define the rollback trigger;
5. verify Group Policy refresh and replication timing;
6. retain out-of-band administrative access for high-value infrastructure.
