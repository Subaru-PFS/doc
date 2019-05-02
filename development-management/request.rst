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

- Long name of the new project 
- Key (e.g. INFRA) of the new project
- Username of the project lead
- Description
- Initial components

Procedure to add new JIRA project (to assignee)
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
Once operation procedure finished, this ticket will be marked 'IN REVIEW' with 
a requestee as a reviewer by sysadmin, 
a requestee SHALL check new repository is working (like succeeded to push 
something, and to access repository admin panel) and mark as 'DONE', 
but a requestee does not need to check PR for public web site (etc.).

- Name of the new repository (need to follow `naming convention of PFS GitHub <https://pfspipe.ipmu.jp/repos.html>`_)
- Short description of the new repository (one line, to be used as a description at `github <https://github.com/Subaru-PFS>`_ and `web page <https://pfspipe.ipmu.jp/repos.html>`_)
- Responsible institution of the repository (coordination, development)
- Corresponding JIRA project and component 
  (request new if need; default to add a component with a name of repository 
  in the target area, like INSTRM for ics\_)
- License (OSS license is required; default to GPLv2)

Procedure to add new GitHub repository (to assignee)
======

Following verification of supplied information per project requirements, such 
as naming conventions, following procedures shall be performed by sysadmin. 

1. Add new GitHub repository with specified repository name and description
2. From Settings panel, do following configurations.

   1. Disable issues from 'Options' tab (if requested repositories are public)
   2. In 'Collaboration & teams' tab, add team(s) of responsible institution 
      with setting them as 'Admin'. 
      Write permission is default for all members in the organization and 
      nothing to do for them. 

3. Add a line of new repository to 
   `repos.html <https://pfspipe.ipmu.jp/repos.html>`_ and 
   `about.html <https://pfspipe.ipmu.jp/about.html>`_, 
   with a PR branch named as the repository creation ticket and sysadmin as 
   reviewer (not a requestee). Just merge if updated website is fine. 
4. Create new JIRA project or component, if requested.
5. Check JIRA integration to load repository updates (branch, PR etc.).
6. Add target repository by `command <https://api.slack.com/slash-commands>`_ 
   '/github subscribe Subaru-PFS/<repo_name>' 
   at #github channel of PFS slack.

After all procedures performed, sysadmin SHALL set the JIRA ticket as 
'IN REVIEW' with setting requestee as a reviewer. 
Also, sysadmin SHALL work on 'pfs_www_pipe' PR independently. 

