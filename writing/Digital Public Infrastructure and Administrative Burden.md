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
Administrative burdens are inherent and abundant in government -- records must be kept and organized, information must be communicated and verified, and decisions must be made in accordance with policies and processes. As Herd and Moynihan argue, we as a society decide the magnitude of those burdens and who we obligate to shoulder them. Though burdens are primarily a result of political and administrative choices, technology plays a key role in exacerbating or alleviating burdens and shifting them from one actor to another.

This report explores the relationship between technology and administrative burdens through the lens of public service delivery. In particular, we focus on key public assistance programs related to cash assistance, housing, food, education, and healthcare administered at the federal, state, and local levels. We narrow our focus to these programs because despite their importance and value to society, their underlying technical infrastructures are complex, unreliable, and do not center the needs of residents in their design and function. Improvements to these systems present an immense opportunity to relieve burdens and provide better support for the most vulnerable members of society.

Core to accessing these programs are *learning costs* related to discovering the existence and potential value of these programs, understanding eligibility requirements and policy details, and understanding application requirements and processes. In addition, such programs may impose *compliance costs* associated with organizing and sharing required documents, managing information, and communicating with program staff.

We argue that technology can help fundamentally reduce or eliminate burdens for residents seeking public assistance by managing labor-intensive tasks such as information-gathering, information-sharing, communication, and process management. Conceptually, because the burdens of accessing and administering these programs are often rooted in information management, technology is well-suited to facilitate or automate these toilsome tasks. In addition, digitizing aspects of these burdens makes it easier to shift their associated costs away from residents and to governments or third parties. Becuase government agencies are central to the administration of these programs, they serve as a key leverage point where implementing technical interventions within agencies can scale the reach and effectiveness of reducing burdens across all actors in the system. Despite the systemic scale of these benefits, the necessary interventions can often be implemented with relatively low fixed costs to governments, making them highly cost-effective investments compared to the status quo of imposing these burdens on residents or third parties.

* Burdens as a tradeoff of time, labor, money, etc. shouldered either by government or by residents (or third parties). 
	* But not a zero-sum tradeoff -- better policy and implementation (including through technical improvements) can lessen burdens for residents and governments.
		* Admittedly, shifting burdens can be worse than zero-sum, e.g. having government staff manually re-submit an online application into another system -- but these costs can be explicitly accounted for on principle to reduce burdens on residents.
* Technology as a tool to reduce burdens through:
	* sharing information
	* facilitating discovery and delivery
	* organizing documents/recordkeeping
	* managing processes
	* reducing toil
* These programs are costly to administer and access for governments and residents. Technical improvements readily justify themselves if they sufficiently reduce burdens or expand access.
* Centralizing administration and operations gives greater leverage for technical improvements.

## Audit of NYC benefits and services
This report focuses on service delivery in New York City, though the lessons can be applied broadly to government-administered programs. New York City administers or facilitates access to a mix of federal, state, and locally-funded or managed programs. These differences in administering agencies and jurisdictions across programs provide a valuable case study in the real-world complexities of managing information, processes, and service delivery across disjoint technical, legal, and operational domains.

New York City also provides an interesting case study because it has made significant technical investments in expanding access to public assistance programs.
TODO: Add details on past and ongoing NYC efforts.

* A birds-eye view of e.g. HRA, housing, other core benefits and services systems. What is the life cycle of resident's data across programs? What are the processes and technologies involved at each step?
	* See: Local Law 60 Report, Local Law 75 Report
		* Should have been updated yearly since, but no clear updates online.

### Assessment
For each service, understand:
* Administering jurisdiction. (federal, state, county, city)
* Administering agency. (NY Office of Temporary and Disability Assistance, NYC Department of Social Services, etc.)
* Key resident-facing entrypoints. (AccessNYC, NY MyBenefits, in-person offices, community-based organizations, etc.)
* High-level journey/process.
* Underlying data systems
	* In-house vs. 3rd party
		* If 3P, what software?
		* If in-house, who develops/maintains?
	* API, data export, interoperability, etc. functionality of data systems.
	* Existing or planned integrations with other data systems.
* Program information requirements
	* What is required for eligibility determination?
	* What is required to apply?
	* Attempt at a detailed schema/definitions.
	* Proposed simplified schema/definitions.
* Legal framework(s) for privacy/data sharing, data governance.
	* Existing and proposed data sharing agreements.

### Information taxonomy
A detailed information taxonomy can be developed from the above questions and encoded programmatically. In theory, a complete taxonomy would include:
* Which information is required for eligibility determination.
* Which information is required for a complete application.
* The semantic meanings or precise definitons of each piece of information, which would allow that information to be mapped to or from other fields. 
* The original sources of each piece of information, whether from commonly availabe documents or from an applicant's inherent knowledge.
* Any secondary sources of information, such as other data systems where this information may be stored.
* The shareability of the information across programs based on the legal and technical constraints of its primary or secondary sources.

Layers:
* Semantic -- literal meanings/definitions of pieces of information. Can be mapped on a program-by-program level and across programs. Relationships between pieces of information can be mapped (e.g. birthdate -> age)
* Dataset -- literal data sources/tables/fields and their associated metadata. Relationships between data sources/tables can be mapped directly to represent complete schemas and possible combinations of information that can transform/map to semantic definitions.
* Legal/organizational -- Metadata about which datasets/fields exist under which programs/jurisdictions/data-sharing agreements, which can be used to assess the feasibility of sharing data across programs/applications. Stick to dataset-level permissions for now rather than field-level.

Questions we can answer with this model:
* Which data systems need to be integrated to enable <proactive outreach,pre-approval,benefits linkage> for each program?
* Where are two-way integrations possible? Where are one-way integrations necessary?
* What information can be transformed/mapped across programs at which stages of the application process?
* Which data integrations are a technical challenge, which are organizational/legal? What are the opportunities and limitations of technical interventions?
* To what extent can proactive outreach/pre-approval/benefits linkage be automated for each program? What informational or administrative requirements will still require manual effort on behalf of applicants or program staff?
* Which documents or other sources of information are the minimum necessary for eligibility/application for each program?
* What additional technologies might be useful for different programs (e.g. information extraction from documents)
* To what extent can rules-as-code be useful for eligibility determination / application approval for each program?
* With additional baseline data, what outcomes can we expect in implementing certain integrations/interventions for each program?
* What metrics can be computed given these integrations?

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

Format as a table?:
| Approach | Description | Examples | Addresses | Does not address | Requires | Outcomes |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| **Benefits linkage** | Fully or partially enrolling someone based on their enrollment in (or eligibility for) other programs. | SNAP/Medicaid cross-enrollment | <ul><li>Learning costs of discovering other programs and understanding requirements.</li><li>Compliance costs of applying to another program.</li></ul> | <ul><li>Compliance cost of original program.</li><li>Marginal learning/compliance cost of linkage.</li><li>Learning and compliance costs associated with potential negative interactions across programs.</li></ul> | <ul><li>Political / process change to require benefits linkage.</li><li>Technical capacity to share status/eligibility information across programs.</li></ul>| <ul><li>Increased enrollement for those eligible but not enrolled.</li><li>Faster processing times.</li><li>Decreased staff labor.</li></ul> |

* **Benefits linkage**
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
	* Outcomes:
		* Increased enrollement for those eligible but not enrolled.
		* Decreased processing times.
		* Decreased staff labor.

* **Proactive outreach**
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
	* Outcomes:
		* Increased enrollment for those eligible but not enrolled.

* **Integrated benefits**
	* Combining multiple benefits applications into a single unified application.
		* Examples: CfA MNBenefits.mn.gov, Civilla Re:Form
	* Solves:
		* Lessens learning costs, compliance costs through consolidation.
		* Learning costs associated with discovery and eligibility determination across programs.
	* Does not solve:
		* Complexity and associated learning and compliance costs of unified application.
	* Requires:
		* Technical and operational capacity to standardize forms
	* Outcomes:
		* Increase in application completion.
		* Increase in enrollment.
		* Decreased application time.
		* Decreased processing time.
		* Decreased staff labor (?)

* **Information re-use**
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
			* Or, a way to map information from one program to another.
		* Technical capacity to share information.
		* Legal/policy frameworks to share information (depending on implementation)
	* Outcomes:
		* Decreased application time.
		* Increased enrollment rate.

* **Rules as code**
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
		* Policy changes to fund and require such functionality.
		* Technical and operational capacity to represent law programmatically.
	* Outcomes:
		* Increased enrollment due to proactive outreach.
		* Increased enrollment due to eligibility screening.
		* Decreased staff labor due to assisted determination.


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
		* Requires a map from application information requirement, to information field, to the source of information (e.g. a common document or the applicant.)

### Strategies for shifting burdens
Summary/taxonomy of ways that burdens can be shifted, especially things that can be readily implemented.

Actors & actions:
* Resident
	* Identify available resources
	* Understand eligibility
	* Understand application requirements
	* Gather information
	* Submit application(s)
	* Receive benefits
	* Understand renewal process
	* Submit renewal information
* CBO
	* Determine relevant resources
	* Determine possible eligiblity for various resources
	* Support gathering of information
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
	* Decide processes within limits of requirements.
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
	* Transform or re-map resident information
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
	* Covering up / abstracting away an inherently broken and messy set of tools and processes with technology.
2. No policy change, enable operational + technical change.
	* Can minimize process burdens, facilitate with technology.
3. Policy + operation + technical change.
	* Can simplify + unify program requirements, minimize process burdens, facilitate with technology.

### Strategies for information management
Information management is central to the task of administering public services. Residents bear the learning costs associated with knowing about a program's existence, assessing its potential utility, and understanding its requirements and associated processes. Residents also bear the compliance costs of filling out applications and putting together the necessary documentation in order to prove they meet the program's criteria and renew their enrollment regularly.

Social workers and CBOs are instrumental to supporting residents in navigating these processes. While their work is enabling in many ways, this type of support simply shifts burdens from one person to another and does not address the underlying causes of burdens or minimize the overall degree of burdens within the system. With the right process and technical interventions, a reduction of burdens would leave both residents and social workers with more time to engage in more differential pursuits.

In order to lessen burdens related to information management, we identify specific activities that each actor must engage in throughout the process, and outline technical interventions that lessen or remove the need for those activities.

##### A public assistant
Consider for example an applicant with a very helpful public assistant. The assistant knows all of the eligibility rules and application requirements for each program, and can tell the applicant which programs they qualify for given minimal information. The assistant can also fill and submit the completed applications for these programs on behalf of the applicant when given the minimum set of documents required, which the assistant knows to ask for. Such assistants exist as staff in Community Benefit Organizations (CBOs), which do an excellent job of abstracting away the burdens of this process; however, the role of the assistant in this scenario can also be fulfilled by a well-implemented set of technologies.

If eligibility rules and application requirements were encoded programmatically, an applicant could submit the required raw documentation to a software tool that then analyzes the document, extracts the relevant information, and maps/transforms it to the eligibility rules or application requirements as necessary. From this, an assessment of eligibility (and the confidence of that assessment) could be made for the applicant, who can then be prompted to submit any additional required documents or information.

Additionally, if this information were stored for re-use, the software could screen the applicant for eligibility for other programs and indicate which additional information may be necessary to determine eligiblity or apply to those programs. This would also enable proactive outreach for new or changing programs, and proactive renewal that requires minimal submission of additional information.

The primary benefit in this scenario is that the applicant does not need to sift through documents to map information from the document to information in eligibility rules or application. This assumes no change in process or policy for any given program, just a mediating set of tools between applicants and programs that understand the strict details of each program's requirements much in the way that CBO staff do. In a scenario where policy changes were made, the eligibility rules would be simple enough for someone to understand and determine for themselves without needing to reference any additional documentation, even if a full application does require that documentation. Similarly, if program requirements were consoldiated across programs through policy changes or benefits linkage, determining eligibility or submitting applications to multiple programs would require little to no additional effort.

Note that these proposed technologies are not capable of or intended to replace the role of program or support staff in government or CBOs. Instead, the technology would enable these staff to spend more time focusing on the more differentiated work of providing care and support to individuals, rather than the toil of navigating and complying with administrative processes. Tasks like digitizing paper information, mapping data across fields, and running an applicant's information through a set of rules are all well-suited to software-based workflows. Staff can then spend more time providing more holistic support for individuals and handling exceptional cases that are failed by these tools.

##### The challenge and importance of semantic data modeling
In order for these tasks to be facilitated by software, the information requirements for different programs must be clarified in a way that enables semantic reasoning and consistency across programs. While a universal schema or ontology for benefits data may seem unwieldy, enabling some degree of semantic interoperability across programs would enable information re-use, rules-as-code, structured information extraction, and other key information management strategies for different programs. Importantly, for such a model to exist independent of any one program enables any number of systems or actors to interoperate at various steps or in different capacities throughout the process.

In the Public Assistant example above, information extraction would be possible on-device (e.g. a "digital wallet") or even through a centralized service (e.g. a "digital locker") such that information could come from any number of sources and be used for any program, regardless of the data source or program. For example, data could be extracted from uploaded documents, official APIs (such as from banks, other government agencies such as Departments of Labor or Taxation, or other programs), or even social workers or virtual agents making phone calls, writing e-mails, or browsing the web on behalf of a resident. Regardless of the source of the information, it would be organized into the resident's datastore and would be available for use as-needed and at their sole request. This model shifts the burden of information retrieval from the resident to automated tooling, and centralizes the necessary data under their ownership rather than across disparate agencies. In this sense, information gathering is a "pull" process for the resident, whereby much of the pulling of data from disparate sources can be automated, and application becomes a "push" process, whereby a resident simply needs to consent to specific data being shared with an agency once needed for validation and verification purposes. Because the data models and eligibility rules live on-device (or in some other service distinct from any one agency), an application's completeness and potential eligibility can be determined before any data is even submitted to the agency for processing. Additionally, if certain subsets of the information were cryptographically signed and could be verified to have come from a specific source, on-device rules could provide zero-knowledge proof of compliance with certain eligibility criteria without needing to submit specific information to the administering agency at all. Alternatively, the agency could "pull" the necessary information from the original sources, or even verify high-level compliance with specific criteria without needing or accessing the underlying information itself (e.g. verifying that income falls within a certain range, or that someone was recently unemployed, or that someone requires certain health assistance).

### System components

* **Service Guide**
	* Can guide individuals through discovery and application process given relevant context about their lives.
	* Implementation details:
		* Can function passively "in the background" to provide support proactively as circumstances change (e.g. job change, family change, health change, finance change).
		* Can also engage directly via natural language or other interfaces.
		* Interfaces with Information Manager to gather information as necessary throughout the process.
		* Interfaces with Rules Engine to ensure validity of eligibility screening and other rule or policy-based information.
		* Relies on LLM + contextual information provided (e.g. administration guides, website data).
* **Information Manager**
	* Can gather and organize information from various sources (e.g. documents, bank accounts, phone calls, third-party platforms/APIs) to map to standardized information taxonomy.
	* Implementation details:
		* Can be stored on-device or in a managed service (end-to-end encrypted).
		* Integrates with e.g. passkeys for authentication.
* **Rules engine**
	* Provides assessment of e.g. eligibility, application completeness, other qualifying/disqualifying conditions.
	* Implementation details:
		*  Interfaces with Service Guide to provide information grounded in formal/rules-based reasoning.
		* Interfaces with Information Manager to understand which information is necessary based on programs surfaced via Service Guide.
		* Publicly auditable, gives clear indications of what criteria are or aren't met and why.

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
