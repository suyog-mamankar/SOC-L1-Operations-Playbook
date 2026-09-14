---
title: SOC Analyst L1 - Day 2 Notes (Workflows, Tooling & Tier Hierarchies)
tags: [cybersecurity, soc, blue-team, siem, threat-intel, day2]
course: SOC Analyst L1 From Basic to Advance
instructor: Sumit Jain
created: 2026-09-12
type: lecture-notes
status: complete
---

# 🛡️ SOC Analyst L1 Training — Day 2 Notes

> [!info] Course Tag
> #cybersecurity #soc #blue-team #day2 #siem #threat-intel

---

## 1. 🎬 Introduction & Session Objectives

### 1.1 Program Context
- **Host:** Sumit Jain — **ZeroDayVault** YouTube channel, Day 2 of the 30-day SOC Analyst L1 series
- **Core question addressed:** *"What does a SOC Analyst really do on a daily basis?"*

### 1.2 AI vs. Human Role in SOC L1

```mermaid
flowchart LR
    AI["AI Automation<br/>Handles repetitive triage,<br/>reduces investigation time"]
    HUMAN["Human Analyst<br/>Contextual validation,<br/>complex decision-making,<br/>handles anomalies"]
    RESULT["Effective SOC Operations"]

    AI -->|supports| RESULT
    HUMAN -->|drives| RESULT
    AI -. cannot fully replace .-> HUMAN

    classDef ai fill:#cffafe,stroke:#0891b2,stroke-width:2px,color:#164e63,font-weight:bold
    classDef human fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    classDef result fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold

    class AI ai
    class HUMAN human
    class RESULT result
```

> [!note] Key Takeaway
> AI automation reduces investigation time and workforce burden, but **cannot replace human analysts entirely** — complex decision-making, contextual validation, and unexpected anomalies still require human critical thinking.

---

## 2. 🏢 SOC Organizational Hierarchy & Tier Breakdown

### 2.1 The 4-Tier Hierarchy Architecture

```mermaid
flowchart BT
    T1["TIER 1 — L1 Security Analyst<br/>Real-Time Alert Triage & Log Monitoring"]
    T2["TIER 2 — L2 Security Analyst<br/>Deep Investigation & Incident Response"]
    T3["TIER 3 — L3 Security Analyst<br/>Threat Hunting & Advanced Malware Analysis"]
    T4["TIER 4 — SOC Manager / Lead<br/>Operations Management & Strategy"]

    T1 --> T2 --> T3 --> T4

    classDef tier1 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold
    classDef tier2 fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f,font-weight:bold
    classDef tier3 fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d,font-weight:bold
    classDef tier4 fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold

    class T1 tier1
    class T2 tier2
    class T3 tier3
    class T4 tier4
```

### 2.2 Detailed Role Specifications

#### 🟢 1. L1 Security Analyst (Junior SOC Analyst)
- **Primary role:** First line of defense in the organization
- **Shift pattern:** **24/7/365 rotational shifts** (not standard 9-to-5) — threats occur continuously
- **Core activities:**
  - Operating **SIEM** consoles to monitor real-time security events
  - Initial alert triage — separating **False Positives** from **True Positives**
  - Routine admin checks (user security awareness, firewall rule tweaks, endpoint settings) *under supervision*
  - Opening tickets for verified alerts, escalating true threats to L2/L3
- **Required skillset:**
  - Foundational Networking protocols/architecture
  - CLI & sysadmin basics — Windows & Linux
  - Basic SIEM operations & log parsing
  - Core understanding of Phishing, Malware, DoS, Brute Force attacks

#### 🟡 2. L2 Security Analyst (Incident Responder)
- **Primary role:** Deep technical investigation & active incident response
- **Core activities:**
  - In-depth analysis of breaches escalated by L1
  - Using **Threat Intelligence feeds**, **EDR** platforms, security analytics tools
  - Determining attack vectors, assessing blast radius, isolating systems, executing containment playbooks

#### 🔴 3. L3 Security Analyst (Threat Hunter / Advanced Analyst)
- **Primary role:** Advanced forensics, proactive threat detection, structural defense engineering
- **Core activities:**
  - **Malware Analysis** & binary **Reverse Engineering**
  - Hypothesis-driven **Threat Hunting** across the enterprise — not reliant solely on automated alerts
  - Researching **Zero-Day Threats**, developing security policies & detection rules
- **Required skillset:** Reverse engineering mastery, digital forensic frameworks, advanced scripting, strategic security planning

#### 🟣 4. SOC Lead & SOC Manager
- **Primary role:** Team operations, strategic planning, inter-departmental coordination
- **Core activities:**
  - Overseeing SOC personnel performance & shift operations (not raw alert analysis)
  - Coordinating workflows between Analysts, Incident Responders, Threat Hunters
  - Managing client SLAs, executive reporting, infrastructure planning

#### ⚙️ 5. Additional Specialized Roles
| Role | Focus |
| :--- | :--- |
| **Incident Responders** | Active breach management, system recovery, containment |
| **Threat Hunters** | Advanced VA/PT, proactive threat hunting |
| **Security Engineers** | Building/configuring security controls, SIEM ↔ IT infra integrations |

### 2.3 Comprehensive Tier Comparison Matrix

| Attribute | L1 Security Analyst | L2 Security Analyst | L3 Security Analyst | SOC Manager / Lead |
| :--- | :--- | :--- | :--- | :--- |
| **Operational Scope** | Alert monitoring, triage, false-positive filtering | Deep incident investigation, containment, response | Advanced malware analysis, threat hunting, zero-days | Team management, workflow planning, governance |
| **Shift Structure** | 24/7/365 Rotational Shifts | Standard / On-Call Rotations | Business Hours / On-Call | Business Hours |
| **Primary Tools** | SIEM dashboards, basic ticketing, basic threat intel | EDR tools, forensic analysis suites, threat intel feeds | Reverse engineering tools, memory forensics, custom YARA/Sigma | Management dashboards, SLA trackers, reporting portals |
| **Trigger Mechanism** | Automated SIEM alerts & incoming log streams | Escalated incident tickets from L1 | Unalerted anomalies, threat hunting hypotheses, zero-days | Operational metrics & compliance audits |

### 2.4 Career Progression Path

```mermaid
flowchart LR
    L1["Junior SOC<br/>Analyst (L1)"] --> L2["SOC Analyst (L2)"] --> L3["Senior SOC<br/>Analyst (L3)"] --> MGR["SOC Manager"] --> DIR["SOC Director"]

    classDef l1 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold
    classDef l2 fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f,font-weight:bold
    classDef l3 fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d,font-weight:bold
    classDef mgr fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold
    classDef dir fill:#e2e8f0,stroke:#475569,stroke-width:2px,color:#1e293b,font-weight:bold

    class L1 l1
    class L2 l2
    class L3 l3
    class MGR mgr
    class DIR dir
```

---

## 3. 🔄 SOC Daily Operational Workflows & Lifecycle

### 3.1 Daily Shift Lifecycle Flowchart (L1 Analyst)

```mermaid
flowchart TD
    START(["Shift Start / Login<br/>e.g., 10:00 AM"]) --> DASH["Access & Review<br/>SIEM Dashboard"]
    DASH --> MON["Monitor Triggered<br/>Security Alerts"]
    MON --> TRI["Perform Alert Triage & Log Validation<br/>Analyze IPs, Hashes, URLs, User-Agents & Event Logs"]
    TRI --> DEC{"Real Threat or<br/>False Positive?"}
    DEC -->|False Positive| CLOSE["Document & Close Ticket"]
    DEC -->|Real Threat| TICKET["Ticket Incident<br/>in Jira / ServiceNow"]
    TICKET --> ESC["Escalate to L2 / Superior"]

    classDef startNode fill:#e2e8f0,stroke:#475569,stroke-width:2px,color:#1e293b,font-weight:bold
    classDef process fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef decision fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold
    classDef good fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold
    classDef escalate fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d,font-weight:bold

    class START startNode
    class DASH,MON,TRI process
    class DEC decision
    class CLOSE good
    class TICKET,ESC escalate
```

**Step-by-step logic:**
1. **Shift Login** — analyst logs into workstation, accesses the centralized SIEM dashboard
2. **Alert Monitoring** — alerts triggered by correlation rules are systematically reviewed from the queue
3. **Alert Validation & Triage** — inspect raw logs (IPs, hashes, URLs, user-agents) to verify legitimacy
4. **Ticketing & Documentation** — False Positive → log justification & close; True Positive → open ticket (Jira/ServiceNow)
5. **Escalation** — validated threats documented with preliminary findings, escalated to L2/L3

### 3.2 🚫 Core Rules: What an L1 Analyst Must NEVER Do

```mermaid
flowchart TD
    R1["NEVER Ignore Alerts<br/>Every alert in the queue must be evaluated"]
    R2["NEVER Delete Logs<br/>Log integrity & chain-of-custody must be preserved"]
    R3["NEVER Take Unauthorized Actions<br/>No production firewall/system changes without escalation"]
    R4["NEVER Escalate Without Analysis<br/>Preliminary triage & documentation required first"]
    R5["NEVER Skip Documentation<br/>All findings, shift logs & reports must be recorded"]

    classDef rule fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d,font-weight:bold
    class R1,R2,R3,R4,R5 rule
```

---

## 4. 🧰 SOC Tooling Ecosystem & Tech Stack (Day 2)

| Category                          | Primary Tools                                                                                 | Core Purpose                                                                       |
| :-------------------------------- | :-------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **SIEM**                          | Splunk, Wazuh, ELK Stack (Elasticsearch, Logstash, Kibana), IBM QRadar, LogRhythm, Sumo Logic | Centralized log ingestion, correlation, real-time alerting, visualization          |
| **Ticketing Systems**             | ServiceNow, Jira                                                                              | Incident tracking, triage documentation, SLA management, escalation workflows      |
| **Threat Intelligence Platforms** | VirusTotal (`virustotal.com`), AbuseIPDB (`abuseipdb.com`)                                    | Reputation scoring, multi-vendor signature scanning, IP/domain/hash lookup         |
| **Communication & Collaboration** | Slack, Microsoft Teams, Email                                                                 | Team coordination, incident notifications, shift handovers                         |
| **Infra Lookup & CLI Utilities**  | `netstat` (Windows CLI), WHOIS (`whois.com`, `domaintools.com`, MX Toolbox), AMASS            | Active connection extraction, domain registration lookup, ASN/IP block enumeration |

```mermaid
flowchart LR
    SIEM["SIEM<br/>Splunk / Wazuh / ELK /<br/>QRadar / LogRhythm"]
    TIX["Ticketing<br/>ServiceNow / Jira"]
    TI["Threat Intel<br/>VirusTotal / AbuseIPDB"]
    COMMS["Comms<br/>Slack / Teams / Email"]
    CLI["Infra Lookup<br/>netstat / WHOIS / AMASS"]

    SIEM --> TIX
    SIEM --> TI
    TI --> TIX
    TIX --> COMMS
    CLI --> TI

    classDef siemC fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    classDef tixC fill:#ecfccb,stroke:#65a30d,stroke-width:2px,color:#3f6212,font-weight:bold
    classDef tiC fill:#cffafe,stroke:#0891b2,stroke-width:2px,color:#164e63,font-weight:bold
    classDef commsC fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f,font-weight:bold
    classDef cliC fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold

    class SIEM siemC
    class TIX tixC
    class TI tiC
    class COMMS commsC
    class CLI cliC
```

---

## 5. 🕵️ Practical Threat Intelligence Demos

### 5.1 Command Utility: Extracting Active Connection IPs (`netstat`)

```cmd
netstat 3
```

**Step-by-step:**
1. Open Windows Command Prompt (`cmd.exe`)
2. Run `netstat 3` — refreshes active connection stats every 3 seconds
3. Identify external IPs under the **Foreign Address** column
4. Select active destination IPs (e.g., `185.234.219.246`) for enrichment on VirusTotal/AbuseIPDB
5. **Practical assignment:** run `netstat 3`, pick active connections, do lookups, document findings, post to the Telegram community channel

### 5.2 Demo 1 — Suspicious IP Investigation via VirusTotal

**Scenario:** SIEM flags abnormal auth failures → suspicious source IP `185.234.219.246` (Brute Force Attack trigger)

```mermaid
flowchart TD
    IP["Target IP<br/>185.234.219.246"] --> VT["Search on virustotal.com"]
    VT --> P1["1. Detection Overview<br/>Vendor score (e.g., 2/94 flagged malicious)"]
    VT --> P2["2. Details Tab<br/>Subnet, ASN 21415, RIPE NCC, country, WHOIS"]
    VT --> P3["3. Reputation Section<br/>Community trust score"]
    VT --> P4["4. Relations Tab<br/>Passive DNS, referring files"]
    VT --> P5["5. Community & Timeline<br/>Last analysis date, researcher comments"]

    classDef target fill:#e2e8f0,stroke:#475569,stroke-width:2px,color:#1e293b,font-weight:bold
    classDef vt fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    classDef panel fill:#cffafe,stroke:#0891b2,stroke-width:1px,color:#164e63

    class IP target
    class VT vt
    class P1,P2,P3,P4,P5 panel
```

| UI Tab | Data Points Extracted | Significance |
| :--- | :--- | :--- |
| **Detection Overview** | Vendor score **2/94**; **NTY AVL** flagged malware; AlienVault, Abusix, GreenSnow, MISOFT, Malware Patrol, OpenPhish, Tank, Quick Heal marked clean | Low-to-moderate vendor consensus — requires further investigation |
| **Details Tab** | Subnet range, **ASN 21415**, **RIPE NCC** registry, country, registration data | Organizational ownership & network boundary |
| **Reputation Section** | Community trust score & distribution | Collective crowd-sourced trust metric |
| **Relations Tab** | Passive DNS → `clickandshipwholesale.com` (NS: `ns2`), referring SQL database files | Maps infrastructure dependencies & linked artifacts |
| **Community & Timeline** | Last analysis date, community comments | Crowdsourced context & scan recency |

### 5.3 Demo 2 — IP Investigation via AbuseIPDB

**Steps:** Navigate to `abuseipdb.com` → complete CAPTCHA if prompted → paste IP → **Search/Check** → extract metrics

| Metric | Value |
| :--- | :--- |
| **Target IP** | `185.234.219.246` |
| **Abuse Confidence Score** | 0% (low report volume) |
| **Total Reports** | 1 report from 1 source (~4 years ago) |
| **Network Properties** | ISP, User Type, ASN, Domain Name, Country, City |
| **Report Comment** | *"PHP email form abuse or spam"* |

> [!tip] Root Cause Scenario (Connecting the Dots)
> Combining VirusTotal's referring database files with AbuseIPDB's comment reveals the attack pattern: an **unpatched/vulnerable PHP email form** on a web server was exploited to send bulk spam containing malicious attachments.

**Triage decision:**
- ✅ **Clean** → document metrics, close ticket, baseline monitoring
- 🚨 **Malicious** → document ASN/country/passive DNS/vendor flags, escalate to **L2** for firewall blocking

### 5.4 Demo 3 — Malicious File Investigation via VirusTotal

- **Sample:** EICAR Standard Anti-Virus Test File (`eicar.org`) — a benign string safe for testing AV detection workflows
- **Steps:** Download sample → `virustotal.com` → **File** tab → **Choose File** → upload → inspect report

| UI Tab | Data Points | Significance |
| :--- | :--- | :--- |
| **Detection** | **66/69** vendors flagged malicious; malware family names | High consensus → confirmed True Positive |
| **Details** | MD5 / SHA-1 / SHA-256 hashes; file type (PowerShell/executable); first-seen timestamp; aliases (e.g., `eicr.com`) | Hashes become IOCs for EDR/SIEM blocklists |
| **Relations** | Contacted domains/IPs (C2 endpoints); execution vectors (PDF, ZIP, Android wrapper, shell script) | Network indicators for perimeter blocking |
| **Behavior** | Sandbox execution patterns, dropped system files | Reveals host-level changes for containment |
| **Community** | Researcher notes & campaign context | Crowdsourced analysis |

---

## 6. 🌐 Deep-Dive Concepts: ASN & WHOIS

### 6.1 Autonomous System Number (ASN)

```mermaid
flowchart TD
    ORG["Enterprise / ISP<br/>e.g., Google"] -->|assigned unique ID| ASN["ASN 15169"]
    ASN --> BLOCK["Controls IP Address Block<br/>e.g., 172.217.0.0/16"]

    classDef org fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    classDef asn fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95,font-weight:bold
    classDef block fill:#cffafe,stroke:#0891b2,stroke-width:2px,color:#164e63

    class ORG org
    class ASN asn
    class BLOCK block
```

- **Definition:** A globally unique identifier assigned to a group of IP blocks managed by a single operator/ISP/enterprise
- **SOC utility:**
  1. **Infrastructure Attribution** — identify parent org, ISP, country governing a suspicious IP
  2. **Reputation/Blacklist Checking** — verify if an entire ASN/IP range is flagged malicious
  3. **Attack Surface Mapping** — enumerate all IP ranges owned by a target entity
  4. **Tooling:** **AMASS** (CLI) discovers IP blocks & subdomains tied to an ASN; instructor references his *Art of Recon* series for deeper ASN extraction techniques

### 6.2 WHOIS Domain & IP Lookups
- **Definition:** Query/response protocol for databases storing registration/ownership records for domains & IP blocks
- **Key data fields:** Registrar, registrant contact info (email, phone, address — unless privacy-redacted), creation/updated/expiration dates, name servers, WHOIS server URL, IP geolocation
- **Common tools:** `whois.com`, `domaintools.com` (`whois.domaintools.com`), MX Toolbox, or native Linux CLI:
```bash
whois <domain-or-ip>
```

---

## 7. 🎓 Core L1 Analyst Governance

### 7.1 Essential Skillset Requirements

```mermaid
flowchart TD
    S1["1. Network Fundamentals<br/>IP addressing, protocols, traffic flow"]
    S2["2. OS Proficiency<br/>Windows & Linux CLI/admin"]
    S3["3. Security Tooling<br/>SIEM / EDR / Firewall"]
    S4["4. Analytical & Problem-Solving<br/>Correlating log artifacts, tracing attack paths"]
    S5["5. Technical Communication<br/>Tickets, handover logs, reports"]
    S6["6. Security Frameworks<br/>Compliance & governance policies"]

    classDef skill fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    class S1,S2,S3,S4,S5,S6 skill
```

### 7.2 Core Prohibitions (Consolidated)

| # | Rule | Rationale |
| :--- | :--- | :--- |
| 1 | **Never Ignore Alerts** | Every queued alert must be evaluated — ignoring creates blind spots |
| 2 | **Never Delete Logs** | Log integrity & chain-of-custody required for legal/forensic compliance |
| 3 | **Never Take Unauthorized Direct Actions** | No production firewall/system changes without approval & escalation |
| 4 | **Never Escalate Without Initial Analysis** | Preliminary triage & documentation required before forwarding to L2/L3 |
| 5 | **Never Skip Documentation** | All findings, shift logs & status reports must be recorded |

### 7.3 Career Growth Path Matrix

| Stage | Role | Core Focus & Responsibilities |
| :--- | :--- | :--- |
| **1** | **Junior SOC Analyst (L1)** | Real-time SIEM monitoring, initial log triage, false-positive filtering, admin checks, ticket generation |
| **2** | **SOC Analyst (L2)** | Deep incident investigation, root-cause analysis, containment playbooks, host isolation |
| **3** | **Senior SOC Analyst (L3)** | Proactive threat hunting, zero-day research, malware reverse engineering, custom detection engineering |
| **4** | **SOC Manager** | Managing personnel, shift operations, SLA tracking, cross-department coordination |
| **5** | **SOC Director** | Enterprise security strategy, capital budgets, governance policy, reports to CISO/executive board |

---

## 8. 📈 Real-World Log Volume & SIEM Filtering Mechanics

> [!question] Student Inquiry (Sunil)
> How does a SOC analyst effectively monitor the overwhelming volume of thousands of logs/alerts generated daily?

```mermaid
flowchart LR
    RAW["Thousands of Raw<br/>Logs & Events"] --> SIEM["SIEM Correlation Engine<br/>Normalizes, filters & correlates"]
    SIEM --> NOISE["Suppressed Benign<br/>Background Noise"]
    SIEM --> ALERT["Actionable Alerts Only<br/>threshold exceeded"]
    ALERT --> ANALYST["Analyst Reviews<br/>Prioritized High-Priority Alerts"]

    classDef raw fill:#e2e8f0,stroke:#475569,stroke-width:2px,color:#1e293b
    classDef siemC fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a,font-weight:bold
    classDef noise fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155
    classDef alert fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d,font-weight:bold
    classDef analyst fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold

    class RAW raw
    class SIEM siemC
    class NOISE noise
    class ALERT alert
    class ANALYST analyst
```

- **Alert prioritization:** analysts don't manually read every raw log line — they prioritize high-priority alerts surfaced during triage
- **SIEM correlation engine:** normalizes, filters, and correlates raw event streams using predefined rules rather than flagging every event
- **Noise reduction:** benign background noise is suppressed; actionable alerts trigger only when correlated events exceed threat thresholds

---

## 9. 🔑 Summary Matrix: Core Day 2 Takeaways

| Topic Area | Key Concept / Requirement | Operational Value |
| :--- | :--- | :--- |
| **Entry Core Skills** | Networking, Windows/Linux OS, SIEM platforms, Analytical Triage, Communication, Compliance | Technical baseline for L1 daily duties |
| **Operational Rules** | No alert skipping, no log deletion, no unauthorized actions, no blind escalations | Preserves security baselines, chain-of-custody, SLA efficiency |
| **Career Roadmap** | Junior L1 → L2 Analyst → L3 Senior → SOC Manager → SOC Director | Clear long-term Blue Team career growth path |
| **Log Management** | SIEM correlation rules & threat prioritization | Prevents analyst fatigue from non-malicious noise |

---

## 🔑 Quick Recap

- [ ] SOC hierarchy: **L1 (Triage) → L2 (Investigation) → L3 (Threat Hunting) → SOC Manager → SOC Director**
- [ ] L1 works **24/7/365 rotational shifts**; L2/L3 mostly business hours + on-call
- [ ] Daily L1 workflow: **Login → SIEM Dashboard → Monitor Alerts → Triage → Ticket/Close → Escalate**
- [ ] 5 core prohibitions: never ignore alerts, never delete logs, never take unauthorized action, never escalate without analysis, never skip documentation
- [ ] Threat intel toolkit: **VirusTotal** (IP/URL/file/hash scanning) + **AbuseIPDB** (abuse history) + **WHOIS/ASN/AMASS** (attribution & attack surface mapping)
- [ ] SIEM correlation engines suppress noise so analysts only see actionable, threshold-breaching alerts

---
