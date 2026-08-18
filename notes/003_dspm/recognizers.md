---
title: Presidio Recognizers Reference
parent: DSPM
grand_parent: Notes
nav_order: 2
description: "The full table of Presidio's country-specific PII recognizers — 19 countries/regions, 65 recognizers — used by the DSPM scan engine."
---

# Presidio Country-Specific Recognizers

Source: `presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/`

| Country/Region | Class | Supported Entity | Description |
|---|---|---|---|
| Australia | `AuAbnRecognizer` | `AU_ABN` | Australian Business Number — 11-digit ID issued to entities registered in the Australian Business Register. |
| Australia | `AuAcnRecognizer` | `AU_ACN` | Australian Company Number — 9-digit number with a modulus-10 check digit. |
| Australia | `AuMedicareRecognizer` | `AU_MEDICARE` | Australian Medicare card number, detected via regex, context words, and checksum. |
| Australia | `AuTfnRecognizer` | `AU_TFN` | Australian Tax File Number — unique ID issued by the Australian Taxation Office. |
| Canada | `CaSinRecognizer` | `CA_SIN` | Canadian Social Insurance Number — 9-digit ID validated with a Luhn checksum. |
| Finland | `FiPersonalIdentityCodeRecognizer` | `FI_PERSONAL_IDENTITY_CODE` | Finnish Personal Identity Code (Henkilötunnus), regex + validation based. |
| Germany | `DeBsnrRecognizer` | `DE_BSNR` | Betriebsstättennummer — 9-digit practice/site-of-care number for German statutory healthcare practices. |
| Germany | `DeFuehrerscheinRecognizer` | `DE_FUEHRERSCHEIN` | Führerscheinnummer — German driving license document number. |
| Germany | `DeHandelsregisterRecognizer` | `DE_HANDELSREGISTER` | Handelsregisternummer — German commercial register number for legal entities/sole traders. |
| Germany | `DeHealthInsuranceRecognizer` | `DE_HEALTH_INSURANCE` | KVNR — German statutory health insurance number. |
| Germany | `DeIdCardRecognizer` | `DE_ID_CARD` | Personalausweisnummer — German national ID card document number. |
| Germany | `DeKfzRecognizer` | `DE_KFZ` | KFZ-Kennzeichen — German vehicle registration plate number. |
| Germany | `DeLanrRecognizer` | `DE_LANR` | Lebenslange Arztnummer — 9-digit lifetime physician number for licensed doctors. |
| Germany | `DePassportRecognizer` | `DE_PASSPORT` | Reisepassnummer — German passport document number. |
| Germany | `DePlzRecognizer` | `DE_PLZ` | Postleitzahl — German 5-digit postal code. |
| Germany | `DeSocialSecurityRecognizer` | `DE_SOCIAL_SECURITY` | Rentenversicherungsnummer/RVNR — 12-character German statutory pension insurance number. |
| Germany | `DeTaxIdRecognizer` | `DE_TAX_ID` | Steueridentifikationsnummer — 11-digit lifetime personal tax ID. |
| Germany | `DeTaxNumberRecognizer` | `DE_TAX_NUMBER` | Steuernummer — tax number assigned by the local Finanzamt (can change over time). |
| Germany | `DeVatIdRecognizer` | `DE_VAT_ID` | Umsatzsteuer-Identifikationsnummer (USt-IdNr.) — German VAT ID for registered businesses. |
| India | `InAadhaarRecognizer` | `IN_AADHAAR` | 12-digit UIDAI Aadhaar identification number. |
| India | `InGstinRecognizer` | `IN_GSTIN` | Goods and Services Tax Identification Number — 15-character ID encoding state code and PAN. |
| India | `InPanRecognizer` | `IN_PAN` | Permanent Account Number — 10-digit alphanumeric code with a check digit. |
| India | `InPassportRecognizer` | `IN_PASSPORT` | Indian passport number — 8-character alphanumeric ID. |
| India | `InVehicleRegistrationRecognizer` | `IN_VEHICLE_REGISTRATION` | Indian vehicle registration number issued by the RTO. |
| India | `InVoterRecognizer` | `IN_VOTER` | Voter/Election ID (EPIC) — 10-digit alphanumeric code issued by the Election Commission of India. |
| Italy | `ItDriverLicenseRecognizer` | `IT_DRIVER_LICENSE` | Italian driver's license number. |
| Italy | `ItFiscalCodeRecognizer` | `IT_FISCAL_CODE` | Italian Fiscal Code (Codice Fiscale). |
| Italy | `ItIdentityCardRecognizer` | `IT_IDENTITY_CARD` | Italian identity card number (case-insensitive regex). |
| Italy | `ItPassportRecognizer` | `IT_PASSPORT` | Italian passport number. |
| Italy | `ItVatCodeRecognizer` | `IT_VAT_CODE` | Italian VAT identification number (Partita IVA), regex + checksum. |
| Korea | `KrBrnRecognizer` | `KR_BRN` | Business Registration Number — 10-digit ID for South Korean businesses. |
| Korea | `KrDriverLicenseRecognizer` | `KR_DRIVER_LICENSE` | Korean driver's license number, 12 digits (AA-BB-CCCCCC-DD). |
| Korea | `KrFrnRecognizer` | `KR_FRN` | Foreigner Registration Number — 13-digit ID issued to registered foreigners in Korea. |
| Korea | `KrPassportRecognizer` | `KR_PASSPORT` | Korean passport number. |
| Korea | `KrRrnRecognizer` | `KR_RRN` | Resident Registration Number — 13-digit ID issued to all Korean residents. |
| Nigeria | `NgNinRecognizer` | `NG_NIN` | National Identification Number — 11-digit ID with a Verhoeff checksum digit. |
| Nigeria | `NgVehicleRegistrationRecognizer` | `NG_VEHICLE_REGISTRATION` | Nigerian vehicle registration plate number (current 2011+ format, e.g. ABC-123DE). |
| Philippines | `PhTinRecognizer` | `PH_TIN` | Taxpayer Identification Number — 9 or 12-digit ID with a modulo-11 check digit. |
| Poland | `PlPeselRecognizer` | `PL_PESEL` | PESEL national identification number, regex + checksum validated. |
| Singapore | `SgFinRecognizer` | `SG_NRIC_FIN` | Singapore NRIC/FIN identity number. |
| Singapore | `SgUenRecognizer` | `SG_UEN` | Unique Entity Number — Singapore business/entity registration identifier. |
| South Africa | `ZaIdNumberRecognizer` | `ZA_ID_NUMBER` | South African 13-digit ID number (YYMMDDSSSSCAZ layout) with structural validation. |
| Spain | `EsNieRecognizer` | `ES_NIE` | Número de Identidad de Extranjero — foreigner ID number, regex + checksum. |
| Spain | `EsNifRecognizer` | `ES_NIF` | Número de Identificación Fiscal — Spanish tax ID number, regex + checksum. |
| Spain | `EsPassportRecognizer` | `ES_PASSPORT` | Spanish passport number (3 letters + 6 digits). |
| Sweden | `SeOrganisationsnummerRecognizer` | `SE_ORGANISATIONSNUMMER` | Swedish Organisationsnummer — 10-digit organization number with Luhn checksum. |
| Sweden | `SePersonnummerRecognizer` | `SE_PERSONNUMMER` | Swedish Personal Identity Number, incl. samordningsnummer, with Luhn checksum. |
| Thailand | `ThTninRecognizer` | `TH_TNIN` | Thai National ID Number — 13-digit ID issued to all Thai residents. |
| Turkey | `TrLicensePlateRecognizer` | `TR_LICENSE_PLATE` | Turkish vehicle license plate (plaka), province code + letters + digits. |
| Turkey | `TrNationalIdRecognizer` | `TR_NATIONAL_ID` | TC Kimlik No — 11-digit Turkish National Identification Number with checksum. |
| UK | `UkDrivingLicenceRecognizer` | `UK_DRIVING_LICENCE` | UK driving licence number (16-character alphanumeric, DVLA-issued). |
| UK | `NhsRecognizer` | `UK_NHS` | UK NHS number, regex + checksum validated. |
| UK | `UkNinoRecognizer` | `UK_NINO` | UK National Insurance Number. |
| UK | `UkPassportRecognizer` | `UK_PASSPORT` | UK passport number (2015+ format: 2-letter prefix + 7 digits). |
| UK | `UkPostcodeRecognizer` | `UK_POSTCODE` | UK postcode across all standard formats. |
| UK | `UkVehicleRegistrationRecognizer` | `UK_VEHICLE_REGISTRATION` | UK vehicle registration number (current and legacy formats). |
| US | `AbaRoutingRecognizer` | `ABA_ROUTING_NUMBER` | American Bankers Association routing transit number (RTN) for financial institutions. |
| US | `MedicalLicenseRecognizer` | `MEDICAL_LICENSE` | Common US medical license number, regex + checksum. |
| US | `UsBankRecognizer` | `US_BANK_NUMBER` | US bank account number. |
| US | `UsLicenseRecognizer` | `US_DRIVER_LICENSE` | US driver's license number. |
| US | `UsItinRecognizer` | `US_ITIN` | US Individual Taxpayer Identification Number. |
| US | `UsMbiRecognizer` | `US_MBI` | US Medicare Beneficiary Identifier — 11-character CMS-issued identifier. |
| US | `UsNpiRecognizer` | `US_NPI` | US National Provider Identifier — 10-digit HIPAA-mandated healthcare provider ID with checksum. |
| US | `UsPassportRecognizer` | `US_PASSPORT` | US passport number. |
| US | `UsSsnRecognizer` | `US_SSN` | US Social Security Number. |

**Totals:** 19 countries/regions, 65 recognizers.
