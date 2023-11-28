# Technology and Administrative Burden
## DRAFT (last updated November 28, 2023)
Rasmi Elasmar

## Introduction
* Introducing concept of administrative burden, digital public infrastructure, why these are fundamental to how government serves communities and in the general interest.
* Background:
	* Administrative burden
	* Public benefits & services
	* Digital public infrastructure
* Public benefits delivery is a high-leverage, high-impact area for improvement of community living standards. It can also be taken as a key litmus test of government’s ability to create or leverage technology to fulfill its core functions.


When government services break, people turn to technology. Broken websites, inaccessible forms, and complex processes are telltale signs of failure in digital service delivery. In the same breath, technology is framed as an obvious solution to these issues -- a new website, a new database, a new chatbot just might be the tools that save us. Technology has become central to how residents access public services at a time when more of them need help, and fewer of them are receiving it.

But how much can technology actually help? What role does it play in how administrative burdens are constructed and experienced? What would it take for technology to deliver on its many promises, and which ones will it struggle to live up to?

This report explores the relationship between technology and administrative burdens through the lens of public service delivery. In particular, we focus on key public assistance programs related to cash assistance, housing, food, education, and healthcare administered at the federal, state, and local levels. We narrow our focus to these programs because despite their importance and value to society, their underlying technical infrastructures are complex, unreliable, and often fail to center the needs of residents in their design and function. Improvements to these systems present an immense opportunity to relieve burdens and provide better support for the most vulnerable members of society. At the same time, there are important limits to what technology can accomplish in the broader context of a complex and capacity-constrained public assistance system.

Part I of this report gives an overview of common burdens, assessing why they exist, who bears them, and why they are difficult to address. This is largely a review of existing literature, and provides motivation and grounding for the remainder of the report.

Part II of this report proposes a framework for assessing technology's role in shifting burdens. We outline new and existing technical strategies for shifting burdens, with a focus on the capacity and tactics necessary for them to be effective in practice.

Part III concludes this report with an affirmative vision of technology's role in facilitating public benefits access. By pushing technical interventions to their most optimistic conclusions, we can better understand the limits of technology in addressing broader challenges in public benefits access, as well as the risks associated with reliance on specific technologies.

---
## Part I: The way things are
## Overview: Technology and administrative burdens

One in five New York City residents depend on the Supplemental Nutrition Assistance Program (SNAP) to get by. SNAP and other public assistance programs make it possible for families to weather crises, put food on the table, afford their rent, and escape poverty. For many residents, these safety net programs provide health and stability in a city where it is increasingly expensive to live and work. They also support New York City's broader economy -- every dollar in SNAP benefits spent has a multiplicative effect on the local economy, supporting local businesses and their employees.

Despite the benefits these programs have on local communities, many of the city's most vulnerable residents are not being reached. New York City's Department of Social Services (DSS) estimates that only three quarters of eligible New York City residents are enrolled in SNAP, leaving over 600,000 eligible residents unenrolled and approximately $1 billion in unclaimed food benefits. For those who are able to access these services, the process of enrollment and renewal can be challenging, time-consuming, and demeaning. The *administrative burdens* residents face throughout these processes can make the difference in whether or not families can access food, housing, and healthcare.

Administrative burdens are inherent and abundant in government -- records must be kept and organized, information must be communicated and verified, and decisions must be made in accordance with policies and processes. As Herd and Moynihan argue, we as a society decide the magnitude of those burdens and who we obligate to shoulder them. Though burdens are primarily a result of political and administrative choices, technology plays a key role in exacerbating or alleviating burdens and shifting them from one actor to another.

Core to accessing these programs are *learning costs* related to discovering the existence and potential value of these programs, understanding eligibility requirements and policy details, and understanding application requirements and processes. In addition, such programs may impose *compliance costs* associated with organizing and sharing required documents, managing information, and communicating with program staff. Finally, there are *psychological costs* associated with having one's life analyzed, being made to work through an arcane process, and having low agency over one's well-being.

**Note**: This report assumes a good-faith origin of burdens -- we focus solely on burdens that arise from the basic logistics of administering programs meant to reach people in need. It is often the case that burdens are intentionally constructed to exclude individuals. Some of the strategies outlined in this report can just as well be applied (intentionally or unintentionally) to make access to services *more* difficult for people. It is the responsibility of policymakers and administrators to continue to center expansion of access to services in the course of their work.



Service delivery is fundamentally a test of society's ability to take care of its most vulnerable members.

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

### Common burdens and who bears them
The variety of administrative burdens in public benefits access are well-documented. For the purposes of this analysis, we leverage a 2016 report from USDS that maps user journeys in applying to key federally-administered benefits. Additionally, a 2018 report from GSA's Customer Experience Center of Excellence provides a similar mapping for USDA Direct Farm Loans. Consolidating these and other analyses reveals a pattern of burdens distributed across government staff, third-party organizations, and residents seeking assistance.

[TODO]: Interactive journey map screenshot.

[TODO] Table 1.1 from *Administrative Burden*?

First and foremost, individuals must understand which programs are available to them. Second, key public assistance programs in the US are means-tested, so individuals must understand and prove whether or not they are eligible for a given service. And finally, the individual must navigate and complete the application process to receive a final determination.

At each step, individuals may encounter changing technical systems, processes, and requirements. While there are often organizations and professionals available to support individuals through these processes, there is still a significant degree of knowledge and labor necessary to facilitate access to these services.
### Causes and distribution of burdens
In researching benefits access, a common refrain from individuals is "Why can't I just..." or "Why can't it just..." -- there is an overt difficulty involved with accomplishing things that seem like they should otherwise be simple. The experience feels unnecessarily hard, as if this can't possibly be the best way.

Why do these burdens exist in the first place, and why are they distributed the way they are?

The primary origin of these burdens is reliance on the practice of means-testing as the core mechanism for deciding who gets to access public assistance. This is at face value understandable -- these programs are funded by the public, and there are complicated and varied sentiments about who is deserving of what type of support. Means-testing is a way of turning these sentiments of "deservedness" into a set of requirements and processes that can be broadly administered by agency staff. The immediate consequence is an apparatus must be built to carry out this administration, and individuals must go to great lengths to prove that they meet the necessary criteria.

A related factor is that the onus is placed on individuals to seek out assistance. The reasoning behind this is similarly political, and its implications similarly far-reaching.

Finally, programs in the US are administered at the federal, state, and local levels. This is a natural consequence of federalism, but it has directly led to a fragmented system of administration, with differing requirements, funding mechanisms, processes, and underlying technical infrastructures. Individuals often have to start anew when seeking out additional assistance from a different agency or program, learning and navigating a new set of requirements, processes, and systems (despite them all coming from "the government"). Similarly, agencies must implement their own programs' processes and systems themselves (despite serving the same residents in operationally related ways). By default, these programs will be designed and implemented in isolation of one another if no care is taken to act otherwise.

* Means-testing
	* Reason: Not everyone is seen as "worthy" of support given limited resources.
	* Intention: Ensure societal resources are being allocated to those who need them most, and no one else.
	* Mechanism: Requires proof of income, resources, status, etc.
	* Burden: documentation must be produced and managed
* Programs are administered by separate jurisdictions and/or organizations
	* Reason: "The Government" is not a single entity, federalism in the US.
	* Intention: Agencies specialize in their purpose
	* Mechanism: Agencies are funded accordingly, administered at appropriate jurisdiction, staffed individually. Policies etc. are set from the perspective of each initiative/program/agency, not necessarily across programs and not from the resident's perspective.
	* Burden: Different eligibility requirements, processes, application requirements. New learning and compliance costs associated *with each program*.
* Onus is on individuals
	* Political/moral choice intended to create good incentives for individuals and society.

These factors come together to place burdens squarely on residents. At each step, the onus is on individuals to seek, understand, prepare for, and apply for the assistance they need. What if burdens were distributed differently?

Burden:
* Connect eligible residents to programs
	* Resident learns what programs are available / what they are eligible for
	* vs. Administrator identifies who is eligible and enrolls them / reaches out.
* Verify eligibility and make determinations
	* Resident gathers information, submits
	* vs. Administrator gathers necessary info
* Connect residents to all relevant programs based on their needs
	* Resident must learn of *each program*
	* vs. Administrator learns about resident and connects to programs.

## Why addressing burdens is hard
There is a growing understanding that burdens restrict access and create worse outcomes for individuals and communities. Yet, these issues persist despite broad recognition and a desire to address them. How are burdens created in practice, and what does it take to change them?
### Policy, service design, and service delivery
There are three key stages that decide how residents experience programs. First, public assistance programs are created via *policies* at the federal, state, and local level. Second, the implementation mechanisms of the program are *designed* by the agency or jurisdiction responsible for administering it, taking into account policy requirements as well as administrative goals. Finally, the program itself is *delivered* by the agency, manifesting the actual day-to-day experience residents have with the program.

In this sense, the decisions made at each stage provide constraints on the decisions that come after -- policy dictates legal requirements, which constrains the design of services, which constrains the delivery of services. If policies outline the requirements of a program, service design represents a plan for how the program *should* be delivered, and service delivery is the realized outcome of how the program is *actually* delivered.

* Policy: Dictates the goals of the program, along with requirements.
* Service design: A plan for how the program *should* be delivered.
* Service delivery: The practical implementation of how the program is administered and delivered.

These constraints have direct consequences for the burdens residents face: Policy spells out the requirements, which inherently create or remove burdens. By defining processes and other implementation details, service design plans for who shoulders the burdens. And by turning the plan into action that people experience day-to-day, service delivery decides who shoulders the burdens in practice.
### Challenges in civic service design
Service designers are tasked with translating policy requirements and resident needs into a plan for delivery.

These plans are directly constrained by policy requirements and organizational capacity. Policy requirements may decide who is eligible for services, goals for delivery, and what organizational resources are available to the agency delivering those services. If an agency must reach a certain percent of the eligible population, or deliver services within a certain time frame, or make services available through specific channels, they must design their service with these requirements in mind. Similarly, if residents are primarily reachable in certain locations or through specific channels, the service must be designed and resourced accordingly.

Agency capacity places a key constraint on service design. Agencies need adequate resources -- whether staff, technology, or other expertise -- to meet these needs. Without the necessary capacity to deliver services, sacrifices in the design and delivery of the service are inevitable. Technical capacity is inextricably linked with service design, as it can limit or enable the specific delivery mechanisms that are planned for in the design stage. Knowing what technology is and isn't capable of, and what the agency is capable of, allows service designers to plan for the reality of delivery. For example, an agency without text or e-mail notification capabilities will need to plan and staff for other methods of outreach and notification, such as phone calls. Similarly, an agency without an approach to digital document management will need to plan and direct resources to more manual approaches. These capabilities will directly affect what the agency is or isn't able to achieve in their delivery of programs. Having an accurate understanding of an agency's own technical capacity allows it to design and deliver services to the best of its abilities.

The design and implementation of these services directly shapes their associated burdens and who bears them by default. These burdens are well-known to residents, program staff, and policymakers, yet they persist despite broad motivation to address them. Service design and implementation is complex and multifaceted, and there are many challenges associated with seemingly obvious solutions.

See above points on root causes, often stemming from policy.

Design can be bad on purpose as well, as administrative burdens are constructed.

Strong technical capacity can affect design (an agency can know what is or isn't possible, and plan to leverage technology to meet specific requirements/address burdens).

### Challenges in service delivery
The delivery of the service is where all the previous constraints reveal themselves in practice as administrative burdens.

An agency may struggle to deliver services because its process is too complex, because the process must comply with complex policies. Or it may have long processing times because it is under-resourced and unable to design for a more robust process, which requires up-front investment. Or it may not have anticipated the ways in which the process would be hindered by its supporting technical implementation.

We place service delivery challenges into three categories: Organizational, Operational, and Technical.  By categorizing these challenges and their origins, we can consider which practical approaches may or may not be effective in addressing them.

Why hasn't this been done? What are the technical, operational, organizational, and other challenges associated with creating such infrastructure?

#### Operational challenges
* Challenges related to how programs are designed, implemented, and administered (and the role technology plays in each phase). Determined primarily by policy and administrative decision-making in the broader context of each organization/program.
* e.g. process changes, policy requirements, legal requirements, etc.
	* "Because that's the process" "Because that's the policy"
* These can be remedied by strong executive/administrative decision-making and/or policy changes (it is generally a deliberate choice that can be readily modified).

#### Organizational challenges
* Challenges within and across programs related to enacting technical/operational change. Determined primarily by political priorities and concerns, conflicting requirements/needs/incentives, resource constraints, capacity, ability.
* e.g. political will to change, resources necessary to change, technical skill and capacity, procurement challenges
* These may require long-term changes, additional resources, restructuring of incentives, political or organizational will, and capacity development.

#### Technical challenges
* Challenges directly related to technical feasibility or implementation. 
* e.g. specific tool interoperability, data management, existence/availability of technology, usability/accessibility of technology, and complexity of technology.
* These problems can be remedied in part by the development of better technologies.

#### Security & privacy needs
* Essential facets of managing resident data that may be at odds with other goals (e.g. cross-agency data sharing)
* Data sharing, ownership, consent, management, auditing, protection from unwanted access/abuse.

### Summary of key challenges in service design & delivery
* Sources of burden for residents: Learning costs, psychological costs, compliance costs, e.g.:
	* People may not know what they are eligible for.
	* Documents and requirements vary by program.
	* Even if you are enrolled, you need to renew.
* Programs are administered at different levels of government (e.g. city vs. county vs. state vs. federal), and even by different organizations within the same jurisdiction. As a result, it is challenging to coordinate processes, program requirements, and information sharing across jurisdictions (or even different programs/organizations within the same jurisdiction).
	* The program requirements, processes, tools, technologies, etc. all may differ by program or organization.
	* Informational definitions may be different even for similar-seeming questions (e.g. income) across programs.
	* Enrollment in one benefit may affect or be contingent on enrollment for others.
## Part II: Strategies for improvement

The delivery of public assistance programs relies on much more than just good technology. Well-implemented technology is not enough to make a program succeed, but poorly-implemented technology is enough to make it fail. Given the complexities of service administration and delivery, where can technology be most useful? What is necessary to make it so? Where is it not an appropriate solution? How can agencies think about how to best leverage technology in the delivery of their programs?

To answer these questions, we assess new and existing technical strategies in terms of how they **shift** burdens. This approach centers the existing costs of burdens and helps clarify the potential benefits of implementing specific strategies, as well as the opportunity costs of leaving the burdens unaddressed. This framework allows decisionmakers to understand which factors are in their control, which approaches may be most effective in reducing burdens for residents, and what is necessary to successfully make those changes.

We argue that technology can help fundamentally reduce or eliminate certain burdens for residents seeking public assistance by managing labor-intensive tasks such as information-gathering, information-sharing, communication, and process management. Conceptually, because the burdens of accessing and administering these programs are often rooted in information management, technology is well-suited to facilitate or automate these toilsome tasks. In addition, digitizing aspects of these burdens makes it easier to shift their associated costs away from residents and to governments or third parties.

Because government agencies are central to the administration of these programs, they serve as a key leverage point where implementing technical interventions within agencies can scale the reach and effectiveness of reducing burdens across all actors in the system. Despite the systemic scale of these benefits, the necessary interventions can often be implemented with relatively low fixed costs to governments, making them highly cost-effective investments compared to the status quo of imposing these burdens on residents or third parties.

## A framework for shifting burdens
A burden is **shifted** when it becomes the responsibility of a different actor or organization involved in the end-to-end journey of accessing a program. At each stage, burdens can be shifted upstream (away from residents) to either the administering agency, a third-party organization, or across all stages, technology. This section details methods of shifting burdens away from residents, though burdens can also be shifted towards residents.

Burdens can also be created and removed, as they are primarily the result of policy and administrative decisions. While policy affects the total degree of burdens, service design/delivery (and technology) can decide where those burdens are shifted and who bears them. But the impact of technology is fundamentally limited by policy -- it can only mask the complexity of the underlying program. In this sense, technology does not increase or decrease the inherent burden of policy, but it can increase or decrease the realized burden of service design (in service delivery).

---
Service design is the primary lever for shifting burdens, but technology can make shifts easier and also adjust the magnitude of burdens faced by people. It is a secondary lever operating within the realm of service design (as part of service delivery).

Increase vs. decrease burdens
Towards residents vs. away from residents

Extended analogy: policy decides the total weight carried. Service design plans for who carries what weight. Service delivery decides in practice who carries what weight. Technology can help residents/staff/others carry that weight (alleviating burdens), or it can make it harder for them (magnifying/exacerbating burdens).

---
How can these burdens be shifted away from residents? By understanding the key needs individuals have at different stages of service delivery, we can identify the work involved and understand whether or not that work can be shifted upstream.

We list the actions each actor currently takes throughout the end-to-end process of accessing or administering a program (detailed in Part I). Tasks that are common among actors are especially well-suited to be shifted away from residents, either upstream or to technology.

We also note the nature of each task -- essential tasks are inherent to the challenge of providing assistance to the right individuals, regardless of the specific operational or administrative details. Imposed tasks are not directly related to providing or receiving  assistance, but are made necessary due to e.g. policy or other administrative choices. Finally, tertiary tasks are natural consequences of essential and imposed tasks -- for example, removing an imposed application process removes a tertiary task of uploading documents.

All types of tasks may be made easier through technical strategies. Imposed and tertiary tasks are especially conducive to being removed or shifted (whether through policy, design, or delivery).

Essential tasks -> understanding relevance of resources, distributing resources
Imposed tasks -> navigating processes, applying, attending interviews, etc.
Tertiary tasks -> Gather information, upload documents, fill out forms, etc.

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

See also O\*NET work activities:
* [43-4061.00](https://www.onetonline.org/link/details/43-4061.00)  Eligibility Interviewers, Government Programs
* [21-1093.00](https://www.onetonline.org/link/details/21-1093.00)  Social and Human Service Assistants
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

## Existing approaches and ideas
In recent years, significant progress has been made in developing and implementing strategies to reduce burdens for applicants. Key tools and strategies are summarized here.

For each approach, outline:
* Approach name
	* A brief definition
		* Examples in theory or practice
	* What issues it solves (in terms of administrative burden)
		* Which specific actions are shifted to/from which actors.
	* What issues it does not solve
	* What is required to implement this approach

Other factors to explore:
* Expected outcomes on burdens etc. when implementing approach (e.g. increase, deacrease, eliminate, approximate magnitude).
* How to measure such outcomes (do datasets or proxies exist?)
* Timeline of implementation/effect
* Role relative to broader process/system
* Type of reform (e.g. reformist vs. non-reformist)
	* Is it reflecting good/simple policy, or obscuring bad/complex policy?

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

## Part III: An affirmative vision of technology in public benefits access
## Opportunities for resident-centered services

While these strategies are each useful individually, together they form a powerful set of tools for minimizing burdens. At their core, they address burdens all across the applicant and staff journeys in service delivery. The remainder of this report details a vision for reducing burdens by pushing these strategies to their limits. Independent of existing tools, processes, and infrastructure, what would a service delivery experience look like when designed primarily around the needs of residents?

* What changes can be made to more holistically provide benefits and services to residents, to design the experience primarily from the perspective of the resident rather than individual programs and departments?

### Proactive service delivery
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


### Strategies for information management
Information management is central to the task of administering public services. Residents bear the learning costs associated with knowing about a program's existence, assessing its potential utility, and understanding its requirements and associated processes. Residents also bear the compliance costs of filling out applications and putting together the necessary documentation in order to prove they meet the program's criteria and renew their enrollment regularly.

Social workers and CBOs are instrumental to supporting residents in navigating these processes. While their work is enabling in many ways, this type of support simply shifts burdens from one person to another and does not address the underlying causes of burdens or minimize the overall degree of burdens within the system. With the right process and technical interventions, a reduction of burdens would leave both residents and social workers with more time to engage in more differential pursuits.

In order to lessen burdens related to information management, we identify specific activities that each actor must engage in throughout the process, and outline technical interventions that lessen or remove the need for those activities.

#### A public assistant
Consider for example an applicant with a very helpful public assistant. The assistant knows all of the eligibility rules and application requirements for each program, and can tell the applicant which programs they qualify for given minimal information. The assistant can also fill and submit the completed applications for these programs on behalf of the applicant when given the minimum set of documents required, which the assistant knows to ask for. Such assistants exist as staff in Community Benefit Organizations (CBOs), which do an excellent job of abstracting away the burdens of this process; however, the role of the assistant in this scenario can also be fulfilled by a well-implemented set of technologies.

If eligibility rules and application requirements were encoded programmatically, an applicant could submit the required raw documentation to a software tool that then analyzes the document, extracts the relevant information, and maps/transforms it to the eligibility rules or application requirements as necessary. From this, an assessment of eligibility (and the confidence of that assessment) could be made for the applicant, who can then be prompted to submit any additional required documents or information.

Additionally, if this information were stored for re-use, the software could screen the applicant for eligibility for other programs and indicate which additional information may be necessary to determine eligiblity or apply to those programs. This would also enable proactive outreach for new or changing programs, and proactive renewal that requires minimal submission of additional information.

The primary benefit in this scenario is that the applicant does not need to sift through documents to map information from the document to information in eligibility rules or application. This assumes no change in process or policy for any given program, just a mediating set of tools between applicants and programs that understand the strict details of each program's requirements much in the way that CBO staff do. In a scenario where policy changes were made, the eligibility rules would be simple enough for someone to understand and determine for themselves without needing to reference any additional documentation, even if a full application does require that documentation. Similarly, if program requirements were consoldiated across programs through policy changes or benefits linkage, determining eligibility or submitting applications to multiple programs would require little to no additional effort.

Note that these proposed technologies are not capable of or intended to replace the role of program or support staff in government or CBOs. Instead, the technology would enable these staff to spend more time focusing on the more differentiated work of providing care and support to individuals, rather than the toil of navigating and complying with administrative processes. Tasks like digitizing paper information, mapping data across fields, and running an applicant's information through a set of rules are all well-suited to software-based workflows. Staff can then spend more time providing more holistic support for individuals and handling exceptional cases that are failed by these tools.

#### The challenge and importance of semantic data modeling
In order for these tasks to be facilitated by software, the information requirements for different programs must be clarified in a way that enables semantic reasoning and consistency across programs. While a universal schema or ontology for benefits data may seem unwieldy, enabling some degree of semantic interoperability across programs would enable information re-use, rules-as-code, structured information extraction, and other key information management strategies for different programs. Importantly, for such a model to exist independent of any one program enables any number of systems or actors to interoperate at various steps or in different capacities throughout the process.

In the Public Assistant example above, information extraction would be possible on-device (e.g. a "digital wallet") or even through a centralized service (e.g. a "digital locker") such that information could come from any number of sources and be used for any program, regardless of the data source or program. For example, data could be extracted from uploaded documents, official APIs (such as from banks, other government agencies such as Departments of Labor or Taxation, or other programs), or even social workers or virtual agents making phone calls, writing e-mails, or browsing the web on behalf of a resident. Regardless of the source of the information, it would be organized into the resident's datastore and would be available for use as-needed and at their sole request. This model shifts the burden of information retrieval from the resident to automated tooling, and centralizes the necessary data under their ownership rather than across disparate agencies. In this sense, information gathering is a "pull" process for the resident, whereby much of the pulling of data from disparate sources can be automated, and application becomes a "push" process, whereby a resident simply needs to consent to specific data being shared with an agency once needed for validation and verification purposes. Because the data models and eligibility rules live on-device (or in some other service distinct from any one agency), an application's completeness and potential eligibility can be determined before any data is even submitted to the agency for processing. Additionally, if certain subsets of the information were cryptographically signed and could be verified to have come from a specific source, on-device rules could provide zero-knowledge proof of compliance with certain eligibility criteria without needing to submit specific information to the administering agency at all. Alternatively, the agency could "pull" the necessary information from the original sources, or even verify high-level compliance with specific criteria without needing or accessing the underlying information itself (e.g. verifying that income falls within a certain range, or that someone was recently unemployed, or that someone requires certain health assistance).

#### System components

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

#### Models for managing shared data
Current models of information management place much of the burden of gathering and organizing information on applicants. This information is collected from various sources either physically (e.g. a paystub, a photo ID) or digitally (e.g. a PDF of a recent utility bill), then processed either physically through paper or digitally through scans and the manual entry of information into digital application forms.

Importantly, much of this information already exists across the many digital systems that we interact with day to day. The burden placed on an individual is in finding this information, accessing it, mapping it to the necessary information requirements for a given program, digitizing it or printing it, and submitting it as part of an application. If these tasks could be managed by technology, these burdens can be shifted away from applicants to either the technology itself or program staff who are assisted by this technology.

Given the sensitive nature of much of this information, it is essential to ensure strong access controls and clear indicators of how data may be accessed and used for a given task. We propose the following models for managing shared data.

##### Distributed: Shared organization-to-organization as needed
In a distributed model, sharing is done ad-hoc between organizations when opportunities to do so arise. For example, two agencies with similar enrollment criteria may choose to share lists of enrollees to identify individuals who are known to be eligible for a service but are not yet enrolled and can be targeted for outreach. Similarly, if a housing program accepts enrollment in a food program as proof that an individual meets the necessary criteria for enrollment, those two programs may directly share enrollment information to negate the need for other more burdensome forms of proof. Programs may also interface with third-party organizations such as banks, utility companies, or employers to verify other relevant information.

In this model, there is no complete or unified view of a person's information in any one place -- information is pulled from different sources as needed for specific purposes. Importantly, this type of data sharing does not need to involve the applicant in the storage or transmission of data, aside from gathering appropriate consent (see section below). Such approaches require each agency to implement specific data sharing agreements and direct integrations with each data provider and consumer.

See "[Data Sharing to Build Effective and Efficient Benefits Systems](https://bdtrust.org/data-sharing-to-build-effective-and-efficient-benefits-systems_january-2023.pdf)".

Because data definitions vary broadly across agencies and systems, this requires each agency to (1) maintain their own clear definitions for information, and (2) map it to other agency/system definitions *individually for each piece of shared information*. While the explicitness and intentionality of this approach can be effective, it requires significantly more effort, as it essentially distributes semantic knowledge of information across all different instantiations of it. This is analogous to "assumed on read" and "enforced on write" models of data management.

##### Data hub: Centrally hosted, centrally managed
A Data Hub extends the distributed model by consolidating records in one place. In this model, a central information store acts as a broker that provides a unified view into a person's information. Many agencies may integrate with the Hub, both contributing information to it and pulling information from it depending on the specific needs and policies of a given program. Similarly, a Data Hub can pull information from various third-party sources and consolidate them in a single data store for programs to access as needed. In this model, it is still necessary for the Hub to integrate with each data consumer or provider, but in this case, the information itself is more readily normalized and consumed by agencies due to the centralized nature of the Hub. Because applicants do not have direct control over their information in the Data Hub, data governance is dictated through privacy policies and agreements with individual agencies and providers.

##### Digital locker: Centrally hosted, personally managed
A digital locker is an information store that is managed centrally, enabling individual agencies to integrate directly with it as needed, with information being shared in a context-dependent way at the discretion of each individual applicant. Examples include [My File NYC](https://www.nyc.gov/site/opportunity/portfolio/my-file-nyc.page), the State of Vermont's [Document Uploader](https://info.healthconnect.vermont.gov/how-apply/document-uploader) tool, and [Kiip](https://www.kiipco.com/). Each of these tools enables applicants to upload documents, allowing program staff across different agencies and processes to access them. As opposed to the Data Hub model, a digital locker gives individuals direct control over how their data is accessed. Importantly, the data is still stored centrally to enable simple integration and access across programs, but no information can leave the system without the direct consent of the applicant.

##### Digital wallet: Personally hosted, personally managed
A digital wallet is similar to a digital locker, except the information store is managed by each individual rather than a central organization. In this model, the information only ever leaves the individual's control once it is submitted to a given agency for processing. Past approaches to digital wallets have come with usability challenges; however, recent developments in consumer-facing authentication standards (e.g. webauthn and Passkeys) may make such approaches more user-friendly.

##### Organizing information from many sources
The combination of a private, personally-managed data store and a standardized ontology of program-related information can shift the framing of how information is gathered and organized throughout the application process. Rather than view information as a set of documents that must be gathered, it can be seen as information about a person's life that exists across a disparate set of sources, which can be passively consolidated and organized under their control. That is, each person is obligated to have access to all digital information about themselves, regardless of the source. The ontology can be thought of as a universal "file" of details about the person that they manage, and this file can passively pull information from a variety of sources or push information to other individuals or organizations as desired.

###### Beyond files: the opportunity and importance of normalized data
* Extract normalized data
* Verify completeness
* Automate completion via info-gathering
* Automate verification via rules-as-code
##### Affirmative consent in data sharing

* See Nissenbaum

##### Privacy-preserving verification

* Centrally managed by a single agency, accessible by many as needed
	* e.g. shared "folder" of files that can be used across programs.
		* [Nava PBC with State of Vermont](https://www.navapbc.com/case-studies/integrating-eligibility-enrollment-software)
		* [My File NYC](https://www.nyc.gov/site/opportunity/portfolio/my-file-nyc.page)
		* [Kiip](https://www.kiipco.com/)
* Distributed across agencies, conforming to a standard, unified as-needed
	* Mechanisms for affirmative consent from resident to share specific data for a given use.
	* Mechanisms for government oversight to ensure no misuse.
* Individuals as data-holders (or unifiers/conduits, pulling and sharing data as needed)
	* Zero-knowledge verification
* Unified data schema
	* Enables rules-as-code, proactive outreach, unified applications, information re-use.
	* Tools that can map information from specific documents (e.g. tax returns) to standard schema for each program.
		* Requires a map from application information requirement, to information field, to the source of information (e.g. a common document or the applicant.)
* Different strategies can be used together
* Enabled by having a standard schema/taxonomy
* Information addition patterns
* Information access patterns

### Transparency & oversight
* How can data use and sharing be managed transparently?
* How can inequities, bias, and discrimination in both policy and implementation be more proactively identified and addressed?

#### Failure modes

### Long-term development
#### Building blocks of digital public infrastructure

#### Incentive alignment
* How can the needs of residents be centered in how agencies operate and are evaluated?
	* E.g. CfA Safety Net Scorecard
	* Comparison to current measures in Mayor's Management Report

## Beyond administrative burden
Even if we leverage technical tools to make the improvements described above, the biggest determinant of social outcomes is policy and implementation.

### Limitations of technology
#### Normative assumptions in public benefits access
Though technology can alleviate burdens residents face in accessing services, it should not excuse the existence of such burdens to begin with.

As an extreme example, consider a set of increasingly complex and detailed eligibility requirements that must be met for a given program. Suppose that there is correspondingly capable technology, which can readily track all aspects of a person's life to assess whether or not they meet the necessary requirements. Though this technology addresses key learning and compliance costs associated with the process of benefits access, there are significant psychological and compliance costs associated with having the details of one's life be continuously monitored and potentially visible to others. The imposition of technology as the only mechanism through which a service's process can be readily navigated is itself a barrier, and is not a substitute for simply not creating the burdens to begin with.
#### Tradeoffs in eligibility and accessibility
Such complex requirements may be motivated by a desire to ensure that only "worthy" individuals receive public assistance, but come at the cost of reduced accessibility for every person eligible for assistance.

Consider two axes: One which dictates the specific eligibility criteria of a given program, and another which reflects the actual accessibility of that program. The first axis is a theoretical threshold, where the letter of the policy is applied such that every person intended to be eligible for benefits receives them. The second axis is a practical reflection of reality -- given the design and implementation of the policy, how many people are actually able to access the program?

Importantly, these axes are coupled. Imposing additional eligibility criteria on a given program decreases its accessibility (by design).

In one corner, there are those who are both eligible and readily able to access the program. In the opposite corner, there are those who are ineligible and unable to access the program. In the upper right, there are those who are ineligible for the program but are still able to access it -- commonly considered fraud. And finally, in the lower left, there are those who are eligible but unable to access the program.

In theory, adding additional eligibility criteria is a useful tool if one's primary motivating policy goal is to help those who "deserve" help without mistakenly allowing others to access the program. However, this comes at the cost of increasing burdens (and therefore reducing accessibility) for *everyone*, including those who are eligible.

Much attention is given to reducing potential fraud in the upper-right box (i.e. the False Positive rate), ...
TODO: Finish this section.

See:
* [Leverage Points: Places to Intervene in a System](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/)
* Reformist reforms vs. non-reformist reforms
* Roles for Computing in Social Change
* CARIN deservingness principles scale
* "Prediction value" of data (Parsons & Viljoen)
## Conclusion
### Towards a universal safety net
*  Burden is on government to identify and reach potentially eligible residents. Likely eligibility determined via rules-as-code, leading to proactive outreach and enrollment.
* Universal benefits linkage: Any one condition triggers eligibility for all other programs if desired (or, no means-testing, e.g. universal school food programs, universal healthcare).
* Application and approval completed via zero-knowledge proof(?).
* Enrollment and renewal happen as desired by resident, burden is on government to disprove need (possibly retroactively, with no consequences for resident).

---
# Appendix

## Audit of NYC benefits and services
This report focuses on service delivery in New York City, though the lessons can be applied broadly to government-administered programs. New York City administers or facilitates access to a mix of federal, state, and locally-funded or managed programs. These differences in administering agencies and jurisdictions across programs provide a valuable case study in the real-world complexities of managing information, processes, and service delivery across disjoint technical, legal, and operational domains.

New York City also provides an interesting case study because it has made significant technical investments in expanding access to public assistance programs.
TODO: Add details on past and ongoing NYC efforts.

* A birds-eye view of e.g. HRA, housing, other core benefits and services systems. What is the life cycle of resident's data across programs? What are the processes and technologies involved at each step?
	* See: Local Law 60 Report, Local Law 75 Report
		* Should have been updated yearly since, but no clear updates online.

### Assessment of existing services
In order to identify areas for opportunity across the delivery of these services, we map their current state in detail.

#### Key service details
For each service, understand:
* Administering jurisdiction. (federal, state, county, city)
* Administering agency. (NY Office of Temporary and Disability Assistance, NYC Department of Social Services, etc.)
* Key resident-facing entrypoints. (AccessNYC, NY MyBenefits, in-person offices, community-based organizations, etc.)
* High-level journey/process.

#### Additional service details
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

#### Information taxonomy
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

### Assessment of burdens
This analysis of NYC services adds to an existing body of work that assesses administrative burdens through journey and systems mapping. Based on an archetypal journey through the process, we can identify key burdens and their underlying causes.
