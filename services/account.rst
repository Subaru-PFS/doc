Account policy and procedures
*****************************

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
  `Lost account or password`_. 
* The contents in the services for PFS software development are 
  open to the public (except some in the private repositories), 
  so they are readable without any account. 
* Some services are configured as 2FA 
  (`two factor authentication <https://en.wikipedia.org/wiki/Multi-factor_authentication>`_) 
  as mandatory, you will be required to configure using some 2FA application. 
  Refer `2FA (two factor authentication) configuration`_ section for links to 
  help pages. 

Technical team member
---------------------

If you are committing to works for the instrument development as a member 
in the technical team of the PFS project, you need to get an account to use 
`services of pfs.ipmu.jp <https://pfs.ipmu.jp/internal>`_ at least. 
Optionally you need access to 
software development tools (like `PFS JIRA <https://pfspipe.ipmu.jp/jira/>`_ 
or `Subaru-PFS GitHub <https://github.com/Subaru-PFS>`_) if you work 
on software development. Ask the local site manager at your institute 
to send the following information to pfsprojectoffice at ipmu.jp.

* Your contact email address
* Preferred account name
* If you will work on software development (in any area of PFS software development) 

  * Request of access to `PFS JIRA <https://pfspipe.ipmu.jp/jira/>`_ and `PFS Slack <https://sumire-pfs.slack.com/>`_
  * Your GitHub account

Once your request is granted, the account information for pfs.ipmu.jp 
is emailed, so you must change your password from the initial one delivered 
by the email within 7 days. 
If you need to reset your password, contact pfs at pfs.ipmu.jp.

Science team member
-------------------

If you are not working for the instrument development, you are categorized as 
a science team member here, and usually you do not need any other account. 
But depending on your roles and contributions to the studies of PFS science 
cases and survey planning, you may need an account to use services at 
`pfs.ipmu.jp <https://pfs.ipmu.jp/internal>`_. 
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
-------------------------------------------

* If you already have a pfs.ipmu.jp account but cannot login to PFS JIRA, you should send an email to jira at pfs.ipmu.jp, instead of registration at signup page. 
* You will receive email from GitHub but not from the PFS project for further registration procedures to GitHub organization. Registration process will not finish unless you follow these procedures. This registration to GitHub organization does not mean to subscribe activities of repositories, you need to subscribe repositories in interest by yourself if you want. 
* PFS GitHub is open to the public, so you can read the contents and add comments except for those in the private repositories, but you cannot push to git repositories unless you follow the above procedure.
* PFS JIRA is open to the public, so you can read the contents, but you cannot make any commitments therein unless you follow the above procedure.
* In the PFS GitHub organization, there is one team per institute where the members are given admin privilege. So instead of sending email to github at pfs.ipmu.jp, you can also ask the members in your institute to add yourself with privilege given to repositories related to your institute. 

Helps
-----

Lost account or password
========================

If you have lost your account information or forgot your password, follow these procedures.

*Single sign on (SSO) account at pfs.ipmu.jp and pfspipe.ipmu.jp*
  Contact the administrators (pfs at pfs.ipmu.jp).

*PFS JIRA*
  If you have an account under SSO at pfs.ipmu.jp, contact the administrators (pfs at pfs.ipmu.jp). 
  Otherwise, access `JIRA registration page <https://pfspipe.ipmu.jp/jira/secure/ForgotLoginDetails.jspa>`_
  and follow the instruction there. 

*SuMIRe/PFS PBworks wiki*
  If you have forgot password, access `password reset page on PBworks <https://my.pbworks.com/?p=forgot>`_ and follow an instruction there. If you are not sure what email address is used, contact to the Project Office (pfsprojectoffice at ipmu.jp).

*PFS Slack*
  Put your email address to the 
  `password reset page on Slack <https://sumire-pfs.slack.com/forgot>`_, 
  or contact the administrator (pfs at pfs.ipmu.jp) for help. 

*Github*
  Visit `password reset page on Github <https://github.com/password_reset>`_ and follow instruction there.
  If you are removed from Subaru-PFS organization by this process, contact to the administrators (pfs at pfs.ipmu.jp).

Change account information
==========================

If you would like to change account information follow these procedures.

*Single sign on (SSO) account at pfs.ipmu.jp and pfspipe.ipmu.jp*
  If you have an access, you can change account information `on this page <https://pfs.ipmu.jp/internal/ldap-manip/>`_ , except for e-mail address.
  To change the e-mail address, contact the administrators (pfs at pfs.ipmu.jp).

*PFS JIRA*
  If you have an account under SSO at pfs.ipmu.jp, you cannot change the profile on JIRA, so contact the administrators (pfs at pfs.ipmu.jp). 
  Otherwise, visit `PFS JIRA Profile page <https://pfspipe.ipmu.jp/jira/secure/ViewProfile.jspa>`_ to change your information.

*SuMIRe/PFS PBworks wiki*
  Visit PBowrks pages to change `your profile <https://my.pbworks.com/?p=profile>`_ or `email address <https://my.pbworks.com/?p=email>`_ .
  **Note: keep your email address updated!!**

*PFS Slack*
  You can change your account information on `Slack account settig page <https://sumire-pfs.slack.com/account/settings>`_

*PFS mailing list*
  If you would like to change e-mail address, visit mailman's page whose link you should have received in "welcome" mail, or contact the Project Office (pfsprojectoffice at ipmu.jp) for help.

*Github*
  Change information on your account page.

2FA (two factor authentication) configuration
=============================================

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


