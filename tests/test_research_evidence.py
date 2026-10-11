import unittest
from scripts.verify_research_evidence import check_case_studies, validate_packet

PACKET = """# Research Evidence Packet

Task ID: RESEARCH-ZTG-001
Status: IN_PROGRESS
Accountable owner: Research maintainer
Risk tier: R1

## Claim and risk
Add claim provenance and limitation checks to public case studies.

## Scope and acceptance criteria
Case-study changes need source-controlled packets and must retain explicit evidence and claim-boundary sections.

## Verification plan and results
CI checks required headings in case studies and packet structure on the exact candidate revision.

## Validation plan and results
Human review must still verify that material claims are traceable to source and that interpretations are clearly labelled.

## Sources, security and privacy
Use public or authorized source materials only; omit private client information and credentials.

## Limitations and open items
The checker validates structure and presence of sections, not source truth or causal inference.

## Recovery and rollback
Revert the gate if valid research is rejected or evidence requirements are not correctly applied.

## Evidence and tested revision
Read the final candidate SHA and CI output after completion. No research claim is accepted by this gate alone.
"""

class ResearchEvidenceTests(unittest.TestCase):
 def test_current_case_studies_have_evidence_boundaries(self):
  self.assertEqual(check_case_studies(),[])
 def test_packet_passes_as_in_progress(self):
  self.assertEqual(validate_packet(PACKET),[])
 def test_missing_sources_section_fails(self):
  text=PACKET.replace("## Sources, security and privacy\nUse public or authorized source materials only; omit private client information and credentials.\n","")
  self.assertTrue(any("missing section" in e for e in validate_packet(text)))
 def test_accepted_without_independent_readback_fails(self):
  text=PACKET.replace("Status: IN_PROGRESS","Status: ACCEPTED")
  self.assertTrue(any("Independent read-back: PASS" in e for e in validate_packet(text)))
if __name__=="__main__": unittest.main()
