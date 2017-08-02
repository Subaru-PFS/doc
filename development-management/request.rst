******
Flows on requests for system configuration with procedures and checklists
******

This document lists flows for the entire process on requests for system 
configuration used for the PFS software development works, contains flows of 
both filing new or modification requests and working on adding or modifying 
configurations of services, not to miss important information required for 
requests or not to forget items to be configured. 
It is highly encouraged to check this document before filing new ticket in the 
`INFRA project <https://pfspipe.ipmu.jp/jira/projects/INFRA/>`_ 
of the PFS JIRA for requests or working on these tickets for both users and 
site administrators. 

Most of procedures start from filing a new ticket by a requestee, sysadmin 
works on configurations, and review (check by requestee whether the new 
configuration is working or not) by requestee to close the ticket. Requestee 
shall not forget to mark review completed and close the ticket as the final 
procedure. 

ToC
***

Following list contains items to be written.

- `Add new JIRA project`_
- Add new JIRA component
- `Add new GitHub repository`_
- Accept transfer of GitHub repository from user

For new user request, refer user account manual of the PFS web based services. 

Add new JIRA project
******

To request
======

File a new JIRA ticket to the INFRA project with following information.

- Long name of a new project, key (e.g. INFRA) of a new project, username of project lead, and description
- Initial components

Procedure to add new JIRA project
======

1. On list of projects page, add new and select "Basic software development"
2. Set name, key, lead, and description of the project as specified in a request
3. Go to the project page, set issue types to "Default issue type scheme", and delete one created by JIRA
4. Set issue type screen to "Default issue type screen scheme", and delete ones created by JIRA (screen scheme, issue type screen scheme)
5. Set workflow to "2-D pipeline workflow scheme", and delete one created by JIRA (from inactive section in workflow list)
6. Add components if provided
7. Add JIRA project to `About <https://pfspipe.ipmu.jp/about.html>`_ page.

Add new GitHub repository
******

To request
======

File a new JIRA ticket to the INFRA project with following information.
Once operation procedure finished, this ticket will be set 'IN REVIEW' with 
a requestee as reviewer, a requestee SHALL check new repository and mark as 
'DONE'. 

- Name of new repository (need to follow `naming convention of PFS GitHub <https://pfspipe.ipmu.jp/repos.html>`_)
- Short description of new repository
- Responsible institution of the repository (coordination, development)
- Corresponding JIRA project and component (request new if need)
- License (OSS license is required)

Procedure to add new GitHub repository
======

Following verification of supplied information per project requirements, such 
as naming conventions, following procedures shall be performed by sysadmin. 

1. Add new GitHub repository with specified repository name and description
2. From Settings panel, do following configurations.

  1. Disable issues
  2. Mark a team in the organization as admin for operation. Write permission is default for all members in the organization
  3. Check slack integration (post activities) is configured

3. Add a line of new repository to `repos.html <https://pfspipe.ipmu.jp/repos.html>`_ and `about.html <https://pfspipe.ipmu.jp/about.html>`_.
4. Create new JIRA project or component, if required.
5. Check JIRA integration to load repository updates (branch, PR etc.).
6. Modify github-slack integration to add repository to channel via `slack app management page <https://sumire-pfs.slack.com/apps/manage>`_.

After all procedures performed, sysadmin is required to set the JIRA ticket as 
IN REVIEW with setting requestee as a reviewer. 

Once requestee success to push a file to the repository, requestee shall mark 
the JIRA ticket as DONE. 

