# Digital Public Infrastructure and Administrative Burden
Rasmi Elasmar

## Introduction
* Introducing concept of administrative burden, digital public infrastructure, why these are fundamental to how government serves communities and in the general interest.
* Background:
	* Administrative burden
	* Public benefits & services
	* Digital public infrastructure
* Public benefits delivery is a high-leverage, high-impact area for improvement of community living standards. It can also be taken as a key litmus test of government’s ability to create or leverage technology to fulfill its core functions.

## Technology and administrative burdens
* Burdens as a tradeoff of time, labor, money, etc. shouldered either by government or by residents (or third parties). 
	* But not a zero-sum tradeoff -- better policy and implementation (including through technical improvements) can lessen burdens for residents and governments.
		* Admittedly, shifting burdens can be worse than zero-sum, e.g. having government staff manually re-submit an online application into another system -- but these costs can be explicitly accounted for on principle to reduce burdens on residents.
* Technology as a tool to reduce burdens through:
	* sharing information
	* facilitating discovery and delivery
	* organizing documents/recordkeeping
	* managing processes
	* reducing toil
* These programs are costly to administer and accesss for governments and residents. Technical improvements readily justify themselves if they sufficiently reduce burdens or expand access.
* Centralizing administration and operations gives greater leverage for technical improvements.

## Audit of NYC benefits and services
* A birds-eye view of e.g. HRA, housing, other core benefits and services systems. What is the life cycle of resident's data across programs? What are the processes and technologies involved at each step?
	* See: Local Law 60 Report, Local Law 75 Report
		* Should have been updated yearly since, but no clear updates online.

### Assessment
For each service, understand:
* Administering jurisdiction.
* Administering agency.
* Key resident-facing entrypoints.
* High-level journey/process.
* Underlying data systems
	* In-house vs. 3rd party
		* If 3P, what software?
		* If in-house, who develops/maintains?
	* API, data export, interoperability, etc. functionality of data systems.
	* Existing or planned integrations with other data systems.
* Program data
	* What is required for eligibility determination?
	* What is required to apply?
	* Attempt at a detailed schema/definitions.
	* Proposed simplified schema/definitions.
* Legal framework(s) for privacy/data sharing.


## Challenges
Why hasn't this been done? What are the technical, operational, organizational, and other challenges associated with creating such infrastructure?

By categorizing these challenges, we can consider which approaches may or may not be effective in addressing them.

### Operational challenges
* Challenges related to how programs are designed, implemented, and administered (and the role technology plays in each phase). Determined primarily by policy and administrative decisionmaking in the broader context of each organization/program.
* e.g. process changes, policy requirements, legal requirements, etc. 
* These can be remedied by strong executive/administrative decisionmaking and/or policy changes (it is generally a deliberate choice that can be readily modified).

### Organizational challenges
* Challenges within and across programs related to enacting technical/operational change. Determined primarily by political priorities and concerns, conflicting requirements/needs/incentives, resource constraints, capacity, ability.
* e.g. political will to change, resources necessary to change, technical skill and capacity, procurement challenges
* These may require long-term changes, additional resources, restructuring of incentives, political or organizational will, and capacity development.

### Technical challenges
* Challenges directly related to technical feasibility or implementation. 
* e.g. specific tool interoperability, data management, existence/availability of technology, usability/accessibility of technology, and complexity of technology.
* These problems can be remedied in part by the development of better technologies.

### Security & privacy needs
* Essential facets of managing resident data that may be at odds with other goals (e.g. cross-agency data sharing)
* Data sharing, ownership, consent, management, auditing, protection from unwanted access/abuse.

### Key challenges
* Sources of burden for residents: Learning costs, psychological costs, compliance costs, e.g.:
	* People may not know what they are eligible for.
	* Documents and requirements vary by program.
	* Even if you are enrolled, you need to renew.
* Programs are administered at different levels of government (e.g. city vs. county vs. state vs. federal), and even by different organizations within the same jurisdiction. As a result, it is challenging to coordinate processes, program requirements, and information sharing across jurisdictions (or even different programs/organizations within the same jurisdiction).
	* The program requirements, processes, tools, technologies, etc. all may differ by program or organization.
	* Informational definitions may be different even for similar-seeming questions (e.g. income) across programs.
	* Enrollment in one benefit may affect or be contingent on enrollment for others.

### Existing approaches and ideas
For each approach, outline:
* Approach name
	* A brief definition
		* Examples in theory or practice
	* What issues it solves (in terms of administrative burden)
	* What issues it does not solve
	* What is required to implement this approach

Other factors to explore:
* Expected outcomes on burdens etc. when implementing approach (e.g. increase, deacrease, eliminate, approximate magnitude).
* How to measure such outcomes (do datasets or proxies exist?)
* Timeline of implementation/effect
* Role relative to broader process/system
* Type of reform (e.g. reformist vs. non-reformist)
	* Is it reflecting good/simple policy, or obscuring bad/complex policy?


* Benefits linkage
	* Fully or partially enrolling someone based on their enrollment in (or eligibility for) other programs.
		* Examples: SNAP/Medicaid
	* Solves:
		* Learning costs of discovering other programs and understanding requirements.
		* Compliance costs of applying to another program.
	* Does not solve:
		* Compliance cost of original program.
		* Marginal learning/compliance cost of linkage.
		* Learning and compliance costs associated with potential negative interactions across programs.
	* Requires:
		* Political / process change to require benefits linkage.
		* Technical capacity to share status/eligibility information across programs.
* Proactive outreach
	* Using data from one or more programs to target individuals with information about other programs or renewal.
		* Examples: Benefits Data Trust, GetCalFresh
	* Solves:
		* Learning costs of discovering programs, understanding eligibility.
	* Does not solve:
		* Compliance costs of completing applications.
	* Requires:
		* Data sharing across programs
		* Standardized defintions of application data (but not requirements) across programs.
		* SMS / email / data analysis infrastructure
* Integrated benefits
	* Combining multiple benefits applications into a single unified application.
		* Examples: CfA MNBenefits.mn.gov, Civilla Re:Form
	* Solves:
		* Lessens learning costs, compliance costs through consolidation.
		* Learning costs associated with discovery and eligibility determination across programs.
	* Does not solve:
		* Complexity and associated learning and compliance costs of unified application.
	* Requires:
		* Technical and operational capacity to standardize forms
* Information re-use
	* Re-using information from one program in applications for another.
		* Examples: [Nava PBC with State of Vermont](https://www.navapbc.com/case-studies/integrating-eligibility-enrollment-software),  [My File NYC](https://www.nyc.gov/site/opportunity/portfolio/my-file-nyc.page), CiviForm.us (disclaimer: I worked on this)
	* Solves:
		* Compliance costs of re-entering information
		* Legal/process requirements around data sharing (depending on architecture of data sharing)
	* Does not solve:
		* Differing definitions for similar requirements across programs.
		* Compliance cost of any one program.
		* Learning and compliance costs associated with potential negative interactions across programs.
		* Government administrative/process burden for any one program.
	* Requires:
		* Unified definitions for requirements across programs.
		* Technical capacity to share information.
		* Legal/policy frameworks to share information (depending on implementation)
* Rules as code
	* Defining and determining eligibility and approval of benefits via programmatic rules that can be processed automatically.
		* Examples: AccessNYC, 18F Eligibility APIs
	* Solves:
		* Compliance costs of eligibility determination, approval, renewal.
		* Possible learning costs of discovery and elgibility determination (by enabling proactive outreach).
	* Does not solve:
		* Political challenge of unifying requirements and definitions across programs.
		* Compliance costs / complexity of a given program.
		* Complexities of individual cases (still need appeals, human processes, etc.)
	* Requires:
		* 

## Opportunities
### Resident-centered services
* What changes can be made to more holistically provide benefits and services to residents, to design the experience primarily from the perspective of the resident rather than individual programs and departments?

#### Proactive service delivery
* What changes could be implemented to shift as much of the burden of delivery onto government as possible? How can these changes be implemented?
	* Rules-as-code for automatic enrollment and renewal
	* Data standardization and sharing across agencies rather than requiring individuals to submit information.
	* Proactive outreach via text and other channels
	* Proactive cross-enrollment
	* Partial eligibility determination to inform applicants of potential eligibility (and what other conditions / information may be necessary).
	* Assess elibility for other programs when applying to any one program. Collecting data for these additional programs if eligibility is determined.
	* Automatically extracting information from submitted documents, leave burden of verification on programs.
		* Applicants can't be held responsible for errors made by such tools.
	* Pre-assessing likely procedural denials
	* Holistic intake and assessment of needs rather than program-by-program.

#### Models for shared data
* Centrally managed by a single agency, accessible by many as needed
	* e.g. shared "folder" of files that can be used across programs.
		* [Nava PBC with State of Vermont](https://www.navapbc.com/case-studies/integrating-eligibility-enrollment-software)
		* [My File NYC](https://www.nyc.gov/site/opportunity/portfolio/my-file-nyc.page)
* Distributed across agencies, conforming to a standard, unified as-needed
	* Mechanisms for affirmative consent from resident to share specific data for a given use.
	* Mechanisms for government oversight to ensure no misuse.
* Individuals as data-holders (or unifiers/conduits, pulling and sharing data as needed)
	* Zero-knowledge verification
* Unified data schema
	* Enables rules-as-code, proactive outreach, unified applications, information re-use.
	* Tools that can map information from specific documents (e.g. tax returns) to standard schema for each program.

### Strategies for shifting burdens
Summary/taxonomy of ways that burdens can be shifted, especially things that can be readily implemented.

Actors & actions:
* Resident
	* Identify available resources
	* Understand eligibility
	* Understand application requirements
	* Submit application(s)
	* Receive benefits
	* Understand renewal process
	* Submit renewal information
* CBO
	* Determine relevant resources
	* Determine possible eligiblity for various resources
	* Support completion of application(s)
	* Support renewal
* Program staff
	* Determine relevant resources
	* Determine possible eligiblity for various resources
	* Receive applications
	* Process applications
	* Follow up for additional information
	* Conduct interview
	* Make final determinations
	* Approve/Deny and notify
	* Disburse benefits
* Program administrator
	* Enforce eligibility requirements
* Policymaker
	* Decide eligibility requirements
	* Decide legal/privacy requirements
	* Decide operational requirements
	* Decide desired outcomes / evaluation criteria
	* Decide resources/funding/investments
* Technical system
	* Present information
	* Store documents
	* Store resident information
	* Notify
	* Automate process
	* Rules-based eligibility determination
	* Simulate outcomes of policy change

Intervention:
* Simplify process
* Automate process
* Introduce process
* Remove process
* Shift process

Outcome:
* Increase/Decrease access
* Increase/Decrease labor
* Increase/Decrease time
* Increase/Decrease costs

#### Technical levers
##### Automate processes
##### Share application information
##### Enable eligibility determination

#### Scenarios
1. No policy/operation change, build tech to minimize burdens at each step.
2. No policy change, enable operation + technical change.
3. Policy + operation + technical change.

### Long-term development
#### Building blocks of digital public infrastructure

#### Incentive alignment
* How can the needs of residents be centered in how agencies operate and are evaluated?
	* E.g. CfA Safety Net Scorecard
	* Comparison to current measures in Mayor's Management Report

### Transparency & oversight
* How can data use and sharing be managed transparently?
* How can inequities, bias, and discrimination in both policy and implementation be more proactively identified and addressed?

## Beyond administrative burden
Even if we leverage technical tools to make the improvements described above, the biggest determinant of social outcomes is policy and implementation.

### Towards a universal safety net
*  Burden is on government to identify and reach potentially eligible residents. Likely eligibility determined via rules-as-code, leading to proactive outreach and enrollment.
* Universal benefits linkage: Any one condition triggers eligibility for all other programs if desired (or, no means-testing, e.g. universal school food programs, universal healthcare).
* Application and approval completed via zero-knowledge proof(?).
* Enrollment and renewal happen as desired by resident, burden is on government to disprove need (possibly retroactively, with no consequences for resident).

### Limitations of technology
See:
* [Leverage Points: Places to Intervene in a System](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/)
* Reformist reforms vs. non-reformist reforms
* Roles for Computing in Social Change
