Account policy and procedures
******

This page presents PFS account policy and procedures on registration, update, 
and contacts on trouble. 

**PBworks wiki**: 
First of all, if you are a member of the institutes in the PFS collaboration, 
you need an account for access to SuMIRe/PFS PBworks wiki page. 
You can go to `Request access <http://sumire.pbworks.com/w/request-access>`_
page and request an account. 

**Other services for PFS Project**: 
After you have access to this SuMIRe/PFS PBworks wiki, your needs of other 
accounts and services depend on your role in the PFS project as explained 
in `Technical team member`_ and `Science team member`_. 
Follow the instructions and request appropriate account(s). 

Notes and tips:

* If you already have some of the accounts and plan to request others, 
  please read `Notes and tips for the registration process`_.
* If you lost your account information, refer 
  `Lost account or change password`_. 
* The contents in the services for PFS software development are 
  open to the public (except some in the private repositories), 
  so they are readable without any account. 
* Some services are configured as 2FA 
  (`two factor authentication <https://en.wikipedia.org/wiki/Multi-factor_authentication>`_) 
  as mandatory, you will be required to configure using some 2FA application. 
  Refer `2FA (two factor authentication) configuration`_ section for links to 
  help pages. 

Technical team member
------

If you are committing to works for the instrument development as a member 
in the technical team of the PFS project, you need to get an account to use 
`services of pfs.ipmu.jp (https) <https://pfs.ipmu.jp>`_ at least. 
Optionally you need access to 
software development tools (like `PFS JIRA <https://pfspipe.ipmu.jp/jira/>`_ 
or `Subaru-PFS GitHub <https://github.com/Subaru-PFS>`_) if you work 
on software development. Ask the local site manager at your institute 
to send the following information to pfsprojectoffice at ipmu.jp.

* Your contact email address
* Preferred account name
* Photo for photo directory at pfs.ipmu.jp (JPEG, less than 50kB; width 250-300 pixels, height 250-350 pixels)
* If you will work on software development (in any area of PFS software development) 

  * Request of access to `PFS JIRA <https://pfspipe.ipmu.jp/jira/>`_ and `PFS Slack <https://sumire-pfs.slack.com/>`_
  * Your GitHub account

Once your request is granted, the account information for pfs.ipmu.jp (https) 
is emailed, so you must change your password from the initial one delivered 
by the email within 7 days. 
If you need to reset your password, contact pfs at pfs.ipmu.jp.

Science team member
------

If you are not working for the instrument development, you are categorized as 
a science team member here, and usually you do not need any other account. 
But depending on your roles and contributions to the studies of PFS science 
cases and survey planning, you may need an account to use services at 
`pfs.ipmu.jp (https) <https://pfs.ipmu.jp/>`_. 
In this case, please go back and read `Technical team member`_. 
In particular, if you plan to contribute to software development, 
you should follow the procedure as follows:

* Contact the local site manager at your institute in the PFS technical team and formalize your commitment(s) to the software development.
* `Register to PFS JIRA <https://pfspipe.ipmu.jp/jira/secure/Signup!default.jspa>`_, if you need to participate in discussions by filing tickets, sending comments, and so on.
* Send your GitHub account name by email to github at pfs.ipmu.jp, if you need to push to git repositories for software coding works, code reviews, and documentations. 

  * For institutes actively working on software development, one (mostly 
    private) `team per group <https://github.com/orgs/Subaru-PFS/teams>`_ 
    (by instrument, data reduction, survey) is defined with admin privilege 
    of repositories owned by each team, so you can ask your site local 
    members to make your account in the group. 
  * Otherwise, you can request to be a member of teams (if you have any one 
    working for) or `outside collaborators to repositories 
    <https://help.github.com/articles/adding-outside-collaborators-to-repositories-in-your-organization/>`_ 
    by email to github at pfs.ipmu.jp. 

* You can create a `PFS Slack <https://sumire-pfs.slack.com/>`_ account 
  `by yourself <https://sumire-pfs.slack.com/signup/>`_ (for some email 
  addresses), or send a request of invitation to pfs at pfs.ipmu.jp. 

Notes and tips for the registration process
------

* If you already have a pfs.ipmu.jp (https) account but cannot login to PFS JIRA, you should send an email to jira at pfs.ipmu.jp, instead of registration at signup page. 
* You will receive email from GitHub but not from the PFS project for further registration procedures to GitHub organization. Registration process will not finish unless you follow these procedures. This registration to GitHub organization does not mean to subscribe activities of repositories, you need to subscribe repositories in interest by yourself if you want. 
* PFS GitHub is open to the public, so you can read the contents and add comments except for those in the private repositories, but you cannot push to git repositories unless you follow the above procedure.
* PFS JIRA is open to the public, so you can read the contents, but you cannot make any commitments therein unless you follow the above procedure.
* In the PFS GitHub organization, there is one team per institute where the members are given admin privilege. So instead of sending email to github at pfs.ipmu.jp, you can also ask the members in your institute to add yourself with privilege given to repositories related to your institute. 

Helps
-----

======
Lost account or change password
======

If you lost your account information or forgot your password, ask to reset 
by following procedures. 

SuMIRe/PFS PBworks wiki
  Access `password reset <https://my.pbworks.com/?p=forgot>`_ and follow an instruction shown.
pfs.ipmu.jp and pfspipe.ipmu.jp
  Send email to pfs at pfs.ipmu.jp from email address you registered.
PFS JIRA
  If you have an account under single sign on at pfs.ipmu.jp (https), 
  send email to pfs at pfs.ipmu.jp. Otherwise access 
  `JIRA registration page <https://pfspipe.ipmu.jp/jira/secure/ForgotLoginDetails.jspa>`_
  and follow an instruction shown. 
PFS Slack
  Put your email address to the 
  `slack password reset page <https://sumire-pfs.slack.com/forgot>`_, 
  or contact pfs at pfs.ipmu.jp for help. 

If you can access to services, and just want to change, process from following 
links. 

* `SuMIRe/PFS PBworks wiki <https://my.pbworks.com/?p=email>`_
* `Single sign on for pfs/pfspipe.ipmu.jp <https://pfs.ipmu.jp/ldap-manip/>`_ 
* Visit `PFS JIRA Profile page 
  <https://pfspipe.ipmu.jp/jira/secure/ViewProfile.jspa>`_ 
  and find 'change password' link. 
  If you cannot find, you are under a single sign on. 
* `Sumire-PFS slack account settings <https://sumire-pfs.slack.com/account/settings#password>`_

======
2FA (two factor authentication) configuration
======

To configure 2FA on services, or if you have issues on 
`2FA <https://en.wikipedia.org/wiki/Multi-factor_authentication>`_), 
refer official helps: 

* `GitHub help <https://help.github.com/articles/configuring-two-factor-authentication/>`_

  * To login on git operation (git command or integrated/plugin for code 
    editors), you need to use 
    `GitHub personal access token <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`_ 
    or 
    `ssh public key authentication <https://help.github.com/articles/connecting-to-github-with-ssh/>`_. 

* `Slack help <https://get.slack.help/hc/en-us/articles/204509068-Set-up-two-factor-authentication>`_
* `JIRA secure login user's guide <https://syracom-bee.atlassian.net/wiki/spaces/SL/pages/15007764/User+s+Guide>`_


