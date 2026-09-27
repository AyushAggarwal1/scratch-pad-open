---
title: Finding Catalog References
parent: DSPM
grand_parent: Notes
nav_order: 3
description: "Research sources behind the DSPM finding catalog: recognizers, finding conventions, and enrichment references."
---

# References — DSPM Finding Catalog

Sources behind `fixtures/findings.json`: vendor naming conventions, compliance
framework mappings, the Presidio detector import, and per-finding enrichment data.

## 1. Vendor finding name/description conventions (Orca, Wiz, Cyera)

Basis for `finding_name` / `description` / `remediation_advice` style (Cyera style chosen).

- [Orca Cloud Risk Encyclopedia — Sensitive Data in File](https://orca.security/resources/cloud-risk-encyclopedia/sensitive-data-in-file/)
- [Orca alert — Database with Potentially Personal Identifying Information found – Credit Card Numbers](https://orca.security/resources/blog/database-with-potentially-personal-identifying-information-found-credit-card-numbers/)
- [Orca alert — Potentially Personal Identifying Information found – Email Addresses](https://orca.security/resources/blog/data-at-risk-personal-identifying-information-email-address-found/)
- [Cyera integration for Elastic — issue/classification field reference](https://www.elastic.co/docs/reference/integrations/cyera)
- [Cyera sample payloads in elastic/integrations — issue name "Credit card number in plain text", PCI DSS description, `remediation_advice`](https://github.com/elastic/integrations/tree/main/packages/cyera)
- [Sekoia — Wiz Issues integration, example payloads](https://docs.sekoia.com/integration/categories/network_security/wiz_issues/)

## 2. Compliance framework sources (`compliance_frameworks` / `sensitivity`)

- [HIPAA Safe Harbor 18 identifiers, 45 CFR 164.514(b)(2) — explained](https://www.johndcook.com/blog/hipaa-identifiers-explained/)
- [Network for Public Health Law — HIPAA Safe Harbor De-Identification reference (PDF)](https://www.networkforphl.org/wp-content/uploads/2020/01/De-Identification_HIPAASafeHarbor-10-1-19.pdf)
- [CPRA full text — Cal. Civ. Code 1798.140(ae) sensitive personal information, 1798.140(v) personal information](https://www.caprivacy.org/cpra-text/)
- [India SPDI Rules 2011, Rule 3 — sensitive personal data list](https://indiankanoon.org/doc/101774797/)
- [India SPDI Rules 2011 — official text (WIPO mirror, PDF)](https://www.wipo.int/edocs/lexdocs/laws/en/in/in098en.pdf)
- [CMS — Understanding the Medicare Beneficiary Identifier (MBI) format (PDF)](https://www.cms.gov/medicare/new-medicare-card/understanding-the-mbi-with-format.pdf)

## 3. Presidio detector import (`src/engine/presidio_patterns.py`)

- [data-privacy-stack/presidio fork](https://github.com/data-privacy-stack/presidio) — source of the 71 imported regex detectors (commit `760d6c8`, presidio_analyzer v2.2.364)

## 4. Per-finding enrichment references (`cwe` / `mitre_attack` / `validation` / `sample_value`)

All URLs cited in `findings.json` `references` fields, with the findings that cite them.

### MITRE CWE / ATT&CK

| Reference | Cited by |
|---|---|
| [CWE-256](https://cwe.mitre.org/data/definitions/256.html) | `Password Pattern` |
| [CWE-312](https://cwe.mitre.org/data/definitions/312.html) | `API Key`, `AWS Access Key`, `AWS Secret Access Key`, `Bearer Token`, +8 more |
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | `AU_ACN`, `Address`, `Bank Account`, `CA_POSTAL_CODE`, +53 more |
| [T1552.004 (MITRE ATT&CK)](https://attack.mitre.org/techniques/T1552/004/) | `Private Key Header` |

### Standards (IETF RFCs, NIST)

| Reference | Cited by |
|---|---|
| [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) | `Secret.PasswordHash` |
| [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122) | `UUID` |
| [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322) | `Email` |
| [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750) | `Bearer Token` |
| [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519) | `JWT Token` |

### Official / vendor documentation

| Reference | Cited by |
|---|---|
| [AWS IAM — Managing access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) | `AWS Access Key`, `AWS Secret Access Key` |
| [CMS — Understanding the MBI format (PDF)](https://www.cms.gov/medicare/new-medicare-card/understanding-the-mbi-with-format.pdf) | `US_MBI` |
| [Google libphonenumber](https://github.com/google/libphonenumber) | `Phone Number` |

### Identifier format specifications

| Reference | Cited by |
|---|---|
| [ABA routing transit number](https://en.wikipedia.org/wiki/ABA_routing_transit_number) | `ABA_ROUTING_NUMBER` |
| [Aadhaar](https://en.wikipedia.org/wiki/Aadhaar) | `IN Aadhaar` |
| [Australian Business Number](https://en.wikipedia.org/wiki/Australian_Business_Number) | `AU_ABN` |
| [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin#Addresses_and_transactions) | `CRYPTO` |
| [Driving licence in the United Kingdom](https://en.wikipedia.org/wiki/Driving_licence_in_the_United_Kingdom) | `UK_DRIVING_LICENCE` |
| [Goods and Services Tax (India)](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)) | `IN GST` |
| [ISO 9362](https://en.wikipedia.org/wiki/ISO_9362) | `SWIFT/BIC` |
| [Individual Taxpayer Identification Number](https://en.wikipedia.org/wiki/Individual_Taxpayer_Identification_Number) | `US_ITIN` |
| [International Bank Account Number](https://en.wikipedia.org/wiki/International_Bank_Account_Number) | `IBAN` |
| [Italian fiscal code](https://en.wikipedia.org/wiki/Italian_fiscal_code) | `IT_FISCAL_CODE` |
| [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) | `CA SIN`, `Credit Card` |
| [MAC address](https://en.wikipedia.org/wiki/MAC_address) | `MAC_ADDRESS` |
| [Medicare card (Australia)](https://en.wikipedia.org/wiki/Medicare_card_(Australia)) | `AU_MEDICARE` |
| [NHS number](https://en.wikipedia.org/wiki/NHS_number) | `UK_NHS` |
| [National Insurance number](https://en.wikipedia.org/wiki/National_Insurance_number) | `GB NINO` |
| [National Provider Identifier](https://en.wikipedia.org/wiki/National_Provider_Identifier) | `US_NPI` |
| [National Registration Identity Card](https://en.wikipedia.org/wiki/National_Registration_Identity_Card) | `SG_NRIC_FIN` |
| [National identification number](https://en.wikipedia.org/wiki/National_identification_number#Finland) | `FI_PERSONAL_IDENTITY_CODE` |
| [National identification number](https://en.wikipedia.org/wiki/National_identification_number#Thailand) | `TH_TNIN` |
| [National identity document (Spain)](https://en.wikipedia.org/wiki/National_identity_document_(Spain)) | `ES_NIF` |
| [PESEL](https://en.wikipedia.org/wiki/PESEL) | `PL_PESEL` |
| [Payment card number](https://en.wikipedia.org/wiki/Payment_card_number) | `Credit Card` |
| [Permanent account number](https://en.wikipedia.org/wiki/Permanent_account_number) | `IN PAN` |
| [Personal identity number (Sweden)](https://en.wikipedia.org/wiki/Personal_identity_number_(Sweden)) | `SE_PERSONNUMMER` |
| [Reserved IP addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses) | `PII.IPAddress` |
| [Resident registration number](https://en.wikipedia.org/wiki/Resident_registration_number) | `KR_RRN` |
| [Social Security number](https://en.wikipedia.org/wiki/Social_Security_number) | `US SSN` |
| [Social insurance number](https://en.wikipedia.org/wiki/Social_insurance_number) | `CA SIN` |
| [South African identity card](https://en.wikipedia.org/wiki/South_African_identity_card) | `ZA_ID_NUMBER` |
| [Tax file number](https://en.wikipedia.org/wiki/Tax_file_number) | `AU_TFN` |
| [Taxpayer Identification Number](https://en.wikipedia.org/wiki/Taxpayer_Identification_Number) | `DE_TAX_ID` |
| [Turkish Identification Number](https://en.wikipedia.org/wiki/Turkish_Identification_Number) | `TR_NATIONAL_ID` |
| [Verhoeff algorithm](https://en.wikipedia.org/wiki/Verhoeff_algorithm) | `IN Aadhaar` |
