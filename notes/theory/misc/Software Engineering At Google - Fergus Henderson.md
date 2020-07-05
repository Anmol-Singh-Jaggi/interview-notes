***Software Engineering At Google***  
*Fergus Henderson*  
[PDF link](https://arxiv.org/ftp/arxiv/papers/1702/1702.01715.pdf)

----------

**Repository structure**
 - 1 giant repo except chrome and android!!
 - 86 TB !! -> How do they manage?
 - Every subtree in the repo has `owners` who review all the commits.

**Build system**
 - `Blaze`
 - Declarative build steps -> Many languages supported.
 - Distributed -> Each build step explicitly mentions the dependencies needed. Kind of distributed topo sort.
 - Caches results.
 - Stays in memory; so knows which files have changed; incremental building; faster.


**Commits**
 - Precommit checks.
 - Code review by atleast one owner.
 - Auto intelligent suggestions for code review based on ownership, authorship, history and workload.
 - One commit small -> <300 lines.
 - Unit testing -> Code review highlights if source has no unit test.
 - Integration and regression testing.
 - Code coverage -> Displayed along source code.
 - Load/Performance testing.

**Bugs**
 - `Buganizer`
 - Bug labels for triage, fix target release.
 - Bugs hierarchial.
 - Issue ID along with commit.

**Coding**
 - 5 languages encouraged -> C++ Python Java Javascript Go.
 - Style guides.
 - Classes on teaching how to write readable code for each language.
 - Non-trivial code change requires code review by someone who has taken this class.
 - Protocol buffer for serializing data.
 - Commonality of processes(source control, build, test, review, bugs) regardless of language.

**Release**
 - Frequent releases (Daily/weekly/fortnightly).
 - Automated release.
 - Fork off feature branch from the last success-build master commit.
 - Just make the changes -> Test -> Fix -> Test -> Integrate into master.
 - Testing is one-click.
 - Launch of any user-visible change is accompanies by a security/reliability/business/legal/privacy/ requirements check.
 - After any production outage, a **Post-mortem** process is started -> Summary, impact, timeline, root causes, solutions, problems etc.
 - No blame game in post-mortem; just focus on the incident technicalities.
 - Frequent code rewrites -> A project completely rewritten once every few years. Helps in reducing complexity and using modern languages/libraries/paradigms.
 - 20% of the time allowed to do your own side projects.
 - Specific team-wide goals.
 - No formal process to choose which projects to work on. Completely dependent on the manager.


**Roles**
 - Engg. Manager manage 10-15 people; Different from a tech lead.
 - Software Engineer (SWE) do not need to manage people even at the highest levels.
 - Management track is completely different from the engineering track.
 - Research Scientists are like SWE but with exceptional research skills. They work in the same team working on the same product as SWE.
 - Site Reliability Engineer is for managing the infra mostly.
 - Product Managers dont write code; responsible for evangelizing features, coordinating with other teams, bug-tracking, scheduling etc.
 - Program Manager similar to Product Manager but manages projects/processes/operations(eg data collection) instead of products.

**Amenities**
 - Free food/massages/games/gyms on-campus.
 - Open-plan seating -> Managers and subordinate sit nearby.
 - First-class video conferencing tech.


**Misc**
 - Training: Short courses in individual tech on joining.
 - Each Noogler is appointed a mentor and 'buddy' on joining.

**Collaboration**
 - Transfer between projects allowed after 12 months.
 - SWE encouraged to work as SRE for 6 months.
 - 'Peer bonus': One can nominate co-worker for extra 100$ twice per year for extraordinary performance.
 - 'Kudos': Non-financial formal appreciation for co-worker unlimited times per year.
 - Termination for poor performance very rare.
 - Anonymous feedback taken about managers from their subordinates twice per year.