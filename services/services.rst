Overview of services
******

Below are tools and resources that are used in the PFS project. 
Many services are hosted at IPMU under `pfs.ipmu.jp (https) <https://pfs.ipmu.jp>`_ 
(mainly for instrument hardware development) or 
`pfspipe.ipmu.jp <pfspipe.ipmu.jp>`_ (for software development), and also PFS 
project is using several external services, like 
`GitHub Subaru-PFS organization <https://github.com/Subaru-PFS>`_. 
You may need account(s) and access to some or all of them depending on your 
roles and contributions to the project, most of services hosted at IPMU are 
under single sign on (SSO) by pfs.ipmu.jp. 
Refer `account policy <account.rst>`_ for details and registration. 

* `SuMIRe/PFS PBworks wiki`_
* `Public Web Site at pfs.ipmu.jp (http)`_
* `PFS project internal website (https pfs.ipmu.jp)`_
* `Online meeting`_
* `Services for software development at pfspipe.ipmu.jp and external`_

SuMIRe/PFS PBworks wiki
------

"SuMIRe/PFS PBworks" is the only official wiki system for PFS. 

======
Login and ToC
======

After logging in at `PBworks <http://sumire.pbworks.com/>`_, 
you will get a project index page named 
"Subaru Measurement of Images and Redshifts (SuMIRe)". 
This page contains links to contents in the wiki, such as 

* PFS Project Office (General links, including link to telecon indexes)
* Documents (Link list to documents)
* Meeting, conference, etc.  (Link list to meetings)
* Mailing lists (List of avail lists)
* PFS working groups (Member list)

======
Page indexes
======

For some continuous meetings, index for each agenda/memo pages are avail.

* `Systems Engineering group telecon <http://sumire.pbworks.com/Systems-engineering-telecons>`_
* `Manager group telecon <http://sumire.pbworks.com/Management-telecons>`_


======
Files
======

Also, you can find all files uploaded into this SuMIRe/PFS PBworks from 
`folder listing <http://sumire.pbworks.com/w/browse/#view=ViewAllFiles>`_.
Some files are categorized into *FOLDERS*, and you can get each list by 
clicking FOLDER name at left side. 

======
Editing manual
======

You can find `manual for editing PBworks <http://usermanual.pbworks.com/>`_. 


Public Web Site at pfs.ipmu.jp (http)
------

Public project information is at http://pfs.ipmu.jp , 
such as list of meetings, list of publications, and instrument parameters. 

PFS project internal website (https pfs.ipmu.jp)
------

Every contents at https://pfs.ipmu.jp/ are project only, and you 
need to log in to view pages. 

If you have any issue on this site, refer 
`lost account or change password section <account.rst#lost-account-or-change-password>`_.

======
Login and user account
======

Use your 'account name' (not email address) and 'password'.
For your first time, please follow notification email to change your password 
from an initial one (randomly created). 

You can edit your account information from `LDAP account manipulator service <https://pfs.ipmu.jp/ldap-manip/>`_, 
such as password, your real name, institution, and photo. 
Also you can view list of all accounts from 

* `List of existing accounts <https://pfs.ipmu.jp/ldap-manip/view_all.cgi>`_
* `photo directory <https://pfs.ipmu.jp/ldap-manip/view_allphoto.cgi>`_

======
ToC
======

When accessing to https://pfs.ipmu.jp/, you will get the newest list of 
contents in this server. 

LDAP account manipulator
  You can view your account setting, list of all avail accounts, and photo 
  directory. 
  Also, you can edit your account setting (real name, password, institution, 
  photo, etc.) from this service.
Content sharing services
  Available services:

  * Document server for PFS
  * Photo archive
  * WebDAV Storage (see `WebDAV Storage`_)

Issue tracker and ticketing system
  Issue tracker system -- Bugzilla : 
  for help refer `Bugzilla help page <http://www.bugzilla.org/docs/tip/en/html/>`_
Temporal sharing services
  Available services:

  * Etherpad list : web-based collaborative real-time editor
  * pastebin
  * EtherCalc : online spreadsheet

pfs.ipmu.jp internal maillist (ML)
  web interface of mailman, and you will get list of avail lists. 
  It depends on settings per each list, you can view registered members, 
  view logs of past emails, and also register (or request to register) on 
  each list. 
Internal wiki (not official)
  for pfs.ipmu.jp server administration and scratch. 
Server status viewer
  for system administration use, you can view system status graph.

------
Photo archive
------

Photo archive for pfs.ipmu.jp, 
contact `system administrator <pfs@pfs.ipmu.jp>`_ to put new 
set of photos, after uploading your phots to WebDAV. 


------
WebDAV Storage
------

You can upload files via clients supporting WebDAV protocol, like cadaver on 
Linux and MacOS. 
You can upload/store/publish any project related files to this space, 
including temporal file exchange. 

Please refer `a page in the internal wiki <https://pfs.ipmu.jp/wiki/System/webdav>`_
for how to connect to WebDAV storage.

======
Landfill services
======

Some landfill instances would avail. 
(Note: landfill will be used for some testing purpose, but not a real 
operated service.) 

Online meeting
------

PFS project uses Zoom system for teleconference. 
For accessing on-line, you will need to `install clients <https://zoom.us/download>`_.

For scheduled list of upcoming teleconferences for PFS technical team, 
the project is providing a list of scheduled teleconferences calendar at 
`google calendar <https://calendar.google.com/calendar/embed?src=su0pbsaull17etlj62tet5anm0%40group.calendar.google.com>`_.


Services for software development at pfspipe.ipmu.jp and external
------

PFS software development group has its dedicated website at 
`pfspipe.ipmu.jp <https://pfspipe.ipmu.jp/>`_, and also uses several external 
services like `GitHub Subaru-PFS organization <https://github.com/Subaru-PFS>`_. 
Followings are a list of commonly used services, refer top page at 
`pfspipe.ipmu.jp <https://pfspipe.ipmu.jp/>`_ and links in the page 
for details and full list of services with descriptions. 
Also for details on accounts, please refer `account policy <account.rst>`_ 
page. 

pfspipe mailman
  Several public mail lists are hosted on `mailman at pfspipe.ipmu.jp 
  <https://pfspipe.ipmu.jp/mailman/listinfo>`_. It is recommended to join 
  `allhands <https://pfspipe.ipmu.jp/mailman/listinfo/allhands>`_ 
  to receive important notices and announcements. 
PFS JIRA
  A project management tool "Atlassian JIRA" is used for software development 
  of the PFS project for the issue ticketing. The contents on the PFS JIRA 
  are open to the public, but login using an account under a Single Sign On 
  integrated with other services at pfs.ipmu.jp or by 
  `registration through JIRA site <https://pfspipe.ipmu.jp/jira/secure/Signup!default.jspa>`_
  is required for making actions. 
GitHub Subaru-PFS organization
  PFS project uses 
  `Subaru-PFS organization at GitHub <https://github.com/Subaru-PFS>`_. 
  In 'Subaru-PFS' organization at GitHub, there is one (mostly private) 
  `team per institute <https://github.com/orgs/Subaru-PFS/teams>`_
  where the members have the admin privilege.
PFS Slack
  PFS project uses `sumire-pfs workspace <https://sumire-pfs.slack.com/>`_ 
  for chat tool.

