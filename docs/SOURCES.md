# Sources

The catalog uses short `source_id` values so every row stays machine-friendly. These links are starting points for validation; exact policy availability depends on OS build, role and ADMX version.

| Source ID | Primary reference | Purpose |
|---|---|---|
| `MS-SCT` | https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines | Security baseline model and Security Compliance Toolkit. |
| `MS-SERVER2602` | https://techcommunity.microsoft.com/blog/microsoft-security-baselines/security-baseline-for-windows-server-2025-version-2602/4496468 | Windows Server 2025 v2602 changes including NTLM auditing, MotW and printer hardening. |
| `MS-LAPS` | https://learn.microsoft.com/windows-server/identity/laps/laps-management-policy-settings | Windows LAPS Group Policy settings. |
| `MS-CRED` | https://learn.microsoft.com/windows/security/identity-protection/credential-guard/configure | Credential Guard. |
| `MS-SMB` | https://learn.microsoft.com/windows-server/storage/file-server/smb-signing-overview | SMB signing. |
| `MS-FW` | https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/ | Windows Defender Firewall. |
| `MS-DEFENDER` | https://learn.microsoft.com/windows/client-management/mdm/policy-csp-defender | Microsoft Defender policy mappings. |
| `MS-ASR` | https://learn.microsoft.com/defender-endpoint/attack-surface-reduction-rules-reference | Attack Surface Reduction rules. |
| `MS-APPCONTROL` | https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/ | App Control for Business and AppLocker. |
| `MS-POWERSHELL` | https://learn.microsoft.com/windows/client-management/mdm/policy-csp-windowspowershell | Windows PowerShell logging policy mapping. |
| `MS-RDP` | https://learn.microsoft.com/windows-server/remote/remote-desktop-services/ | Remote Desktop Services. |
| `MS-BITLOCKER` | https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/ | BitLocker. |
| `MS-AUDIT` | https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration | Advanced Audit Policy. |
| `MS-PRINT` | https://techcommunity.microsoft.com/blog/microsoft-security-baselines/security-baseline-for-windows-server-2025-version-2602/4496468 | Current printer-security baseline changes. |

## MITRE ATT&CK

Enterprise tactics: https://attack.mitre.org/tactics/enterprise/

ATT&CK mappings in this repository are defensive mappings created for this project. They do not imply validation or endorsement by MITRE.

## Current baseline packages

Microsoft Security Compliance Toolkit:

https://www.microsoft.com/download/details.aspx?id=55319

At the September 2026 repository refresh, the Download Center lists Windows 11 v25H2 and Windows Server 2025 Security Baseline v2602. Re-check the Download Center before production use because baseline packages change.
