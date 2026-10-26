# Research note: Indian home-loan approval workflow

**Purpose.** This short note provides domain context for the LoanPilot proof of concept. It describes a typical workflow, not a binding process for every lender. Actual checklists, approval authority and turnaround time vary by bank, borrower, property and completeness of the file.

## Typical stages, roles and checks

1. **Application and acknowledgement — sales/branch or digital channel.** Capture borrower/co-borrower details, requested amount, tenure, property/purpose and consent. Confirm the application is complete and communicate any missing information. RBI fair-practice guidance expects comprehensive application forms, transparent disclosure of charges and a reasonable process for informing applicants about missing documents and decisions [1].
2. **Identity, KYC and income documents — operations/KYC team.** Typical documents include identity/address proof, photograph, salary slips or business income evidence, tax documents where applicable, and bank statements. The exact list depends on applicant type and lender. RBI's housing-loan FAQ lists identity/residence proof, salary slips, Form 16 for relevant applicants, bank statements/balance sheets and legal property documents as examples [2].
3. **Credit and repayment capacity — credit analyst/underwriter.** Review credit-bureau information, existing obligations, income stability and disposable/surplus income. Calculate repayment affordability/FOIR using the lender's own approved method. RBI guidance describes repayment capacity in terms of disposable income, expenses, liabilities and income stability [2].
4. **Property and collateral due diligence — legal and technical/valuation teams.** Review title/ownership chain, encumbrances, approvals and property valuation. Verify the lender's acceptable security and calculate loan-to-value (LTV). RBI's housing-finance directions specify LTV bands for individual housing loans and state that stamp duty/registration costs generally should not inflate property value for LTV calculation [3]. Confirm the currently applicable directions and lender type before applying exact thresholds.
5. **Credit decision and sanction — authorised credit officer/committee.** Combine the verified borrower and property evidence with the bank's current policy and delegated authority. Resolve exceptions or inconsistencies, document reasons, and communicate approved terms and conditions. RBI fair-practice guidance calls for proper appraisal, written terms and transparent disclosure of fees/charges [1].
6. **Agreement, conditions precedent and disbursement — operations/legal.** Complete acceptance, agreements, mortgage/security formalities and pre-disbursement conditions. Disbursement may be staged for under-construction properties and is subject to the sanction terms and required checks.
7. **Post-disbursement monitoring — servicing/collections.** Track repayment, account servicing, insurance/security documentation where applicable, and delinquencies.

## Roles and common pain points

Roles commonly involved are applicant/co-applicant, relationship manager/branch or digital intake, KYC/document operations, credit analyst/underwriter, bureau service, legal/title reviewer, technical valuer, sanctioning authority and loan operations. Typical process risks inferred from the workflow include repeated document requests, inconsistent field formats across systems, manual comparison of income against bank credits, waiting for property/legal checks, unclear exception ownership, policy-version confusion and weak traceability between a decision and its evidence. These are process-design observations, not measured findings from a named bank.

## Turnaround time

There is no single defensible turnaround time for every Indian home loan in the sources reviewed here. It varies with completeness of documents, property/legal complexity, lender operations and whether the property is ready or under construction. This demo therefore does **not** claim a specific bank TAT or percentage reduction. A real implementation should baseline application-to-sanction and sanction-to-disbursement times from the bank's own process data.

## How LoanPilot maps to the workflow

The prototype joins synthetic borrower, account, repayment, bureau, CERSAI and application records in BigQuery. The browser applies transparent demonstration rules and shows the policy label/reason behind each check. Missing or unusual data and document/property flags should be treated as referrals. The final lending decision remains with a human officer. It does not use real customer records or connect to live bureau/government systems.

## Sources

1. Reserve Bank of India, *Guidelines on Fair Practices Code for Lenders* / RBI master-circular material on loan applications, appraisal, terms and disclosures. https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/36102.pdf
2. Reserve Bank of India, *Housing Loans — FAQs* (historical general guidance on repayment capacity and common documents; verify current requirements with the lender). https://rbi.org.in/CommonPerson/english/scripts/FAQs.aspx?Id=701
3. Reserve Bank of India, *Commercial Banks – Credit Facilities Directions, 2025*, housing-finance/LTV section (current applicable provisions should be checked for the relevant lender and loan). https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13156
4. State Bank of India, *Home Loan on YONO* (example of a lender's digital application journey; not a universal bank process). https://sbi.bank.in/web/yono/home-loan

**Research limitation:** No banking professional interview was conducted for this draft. Do not imply otherwise. If you speak with a banking professional, add their role, date and non-confidential observations with permission.
