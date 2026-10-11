# Evidence Packet — Research Repository Quality Gate

Task ID: RESEARCH-ZTG-001
Status: IN_PROGRESS
Accountable owner: Research maintainer
Risk tier: R1

## Claim and risk
Enforce source/claim-boundary structure in public case studies and require evidence packets for material research changes. Risk includes publishing polished analysis whose claims are not traceable to evidence.

## Scope and acceptance criteria
In scope: research-agent policy, case-study structural checks, evidence validator/tests and CI workflow. Out of scope: automatic factual certification, external source availability verification and client/business outcome certification. CI must reject missing Evidence map or “What it does not prove” sections in case studies and missing evidence packets for material content edits.

## Verification plan and results
The PR workflow runs Python unit tests, case-study structure checks and packet validation on the candidate revision. Exact SHA and CI results must be read back once the run completes. No PASS is asserted in advance.

## Validation plan and results
A human reviewer must trace material statements to cited/source materials, distinguish interpretation from facts and challenge assumptions. This control does not validate whether a recommendation caused a business result.

## Sources, security and privacy
Only public or authorized historical sources should be used. Do not publish private client details, contracts, credentials or identifying information. Preserve source versions/dates and the limits of source provenance.

## Limitations and open items
The checker verifies section presence and packet structure only. It does not automatically fetch the original historical source archive or prove factual accuracy. Source provenance and claims still need reviewer validation.

## Recovery and rollback
Revert the workflow/script if it produces false positives or misses missing evidence sections. Preserve the last known-good public research content.

## Evidence and tested revision
Record the exact candidate SHA and CI run after completion. Keep status IN_PROGRESS until source/claim review and human acceptance are complete.
