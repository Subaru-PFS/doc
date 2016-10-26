******
Ticket organization on integrated JIRA for all software development
******

Overview
******

Current organization and conditions
======

Although code development work itself is somehow independent among packages in 
PFS project, such as ICS for instrument control, DRP for pipeline, etc., all of 
these software packages are working on the same hardware which introduces many 
relationships in various level coordination among packages like from 
definitions and coordination on sequence of PFS survey operation in quite 
high level, down to database for storing and recording instrument and/or 
survey operation, or instrument configurations' management and its handling 
with unified routine for loading. On this point of view, smoothly integrated 
ticketing system over the entire PFS software development from instrument 
control to survey operation is important both for software development and 
for operation with configuration management to keep things updated. 

We have one active JIRA instance at pfspipe.ipmu.jp with OSS license, and 
currently used mostly for ticket handling of pipeline (2D DRP) and introducing 
to survey software (SPT+ETS). JIRA is just used for ticketing for development 
management, and we use public GitHub repositories in 'Subaru-PFS' organization 
for code repository and review process (well known as pull request procedure). 
pfspipe.ipmu.jp is operated under single sign on (SSO) infrastructure built for 
pfs.ipmu.jp which hosts web based services mainly used for hardware development, 
such as the document server, mail list hosting, and shell access to testing 
environment (SSO but requires key authentication).

Within control software for instrument and hardware, we have two components 
which need to be care about information control: H4RG, and MLP1 interface. 
These two software modules are quite small and well isolated from other part 
of instrument control software modules, and also their external interfaces 
are possible to be kept simple, such that detector readout control software 
for H4RG accepts required exposure time to output FITS images using optimized 
electronics control configuration without customization, and MLP1 interface 
requires outputs from AG cameras, which are error values from spot measurement 
and raw image file, without any interaction back from MLP1 interface to other 
instrument control part including AG camera control software. Although some of 
coordination on interactions and/or interfaces among software components would 
be affected by detailed design of two modules, but items/areas to be affected 
(directly) is quite small fraction compared to the entire PFS instrument 
control software, and also we assume that we can define clear boundary and 
its interface to these two modules without touching to any confidential items. 

Plan for ticketing and repository
======

PFS team will plan to:

- Have only **one** public JIRA instance at IPMU (pfspipe.ipmu.jp) to cover 
  all coordination, management and ticketing of PFS software development 
  activities, for all packages including instrument control (ICS), pipeline 
  (DRP), observation and survey operation (SPT+ETS).
- Make all repositories except for ones relates to H4RG and MLP1 interface to 
  be public at GitHub repositories, and do pull requests (PR) and code reviews 
  at GitHub with integrated to JIRA ticketing identified with branch name. 
  Repositories are categorized with preface word in its name, such as ics_ for 
  instrument control, drp_ for pipeline, ets_ for fiber allocation, spt_ for 
  survey operation, and pfs_ for package independent general modules such as 
  project wide miscellaneous items, or project web site.

Also for management point of view, PFS team asks Subaru to:

- Pay close attention to what issues are discussed on JIRA. If any concern is 
  found in such a way that the contents in tickets and/or subsequent 
  discussions may expose some proprietary information, we should share the 
  situations and discuss what to do.

Detailed ticketing organizations plan
******

Overview of ticket management in JIRA
======

Within one JIRA instance (or so called *site*), tickets are organized into 

- Project, which identifies tickets as XXXX-(id) where XXXX is short name for 
  each project. Moving ticket between project could change its identifier to 
  different from original - XXXX-(id) to YYYY-(id'). Within one JIRA instance, 
  we can easily and directly link to another issue with ticket ID with project 
  name - XXXX-(id).
- Component, which is subcategories within each project and every ticket can 
  be categorized in one component to identify in which module ticket is related. 
- Each ticket can have label, epic, and sprint (one per each) to specify 
  relations to development management aspect view managed within one project. 
  Epic is used as some sort of meta ticket to organize well isolated group of 
  tickets, sprint is used for time domain management of development activity 
  to be done in a certain period (duration). 

Considering our project organization that each software package, such as ICS or 
DRP, is mostly developed by an independent group, we may be possible to have one 
project per each software package, not to be bothered by non-direct-ly related 
modules. 
We already have several projects for 2D DRP, which were made in quite early 
phase of introducing JIRA to PFS software development. We may merge them into 
one large project with components, but these are kept for now. 

Datamodel (DAMD)
======

Datamodel provides a standardized representation of all data produced by PFS. 
This contains definitions of:

- Data file formats including FITS format
- File name conventions such as instrument on-site generated files with path, 
  archived observation data files, and pre-/post- processed data files. 


2D DRP (multiple projects) - 2D Data reduction pipeline
======

For 2D DRP, we created projects without well understanding on how to use these 
classifications, and we went to small management that we defined projects per 
small categories and made several projects even within 2D pipeline project, 
such as PIPE2D for core 2D pipeline, SIM2D for simulated instrument to be used 
for (2D) pipeline development. We are better to have larger classification than 
we currently have for 2D development, when we expand our usage of JIRA instance. 

PIPE2D
  The 2D data reduction pipeline. The 2D pipeline receives raw images 
  read out from the detector and produces produces one-dimensional, 
  sky-subtracted, flux- and wavelength-calibrated spectra ready for 
  scientific analyses. 
SIM2D
  The 2D image simulator. This simulates raw images as might be produced 
  by the spectrograph detectors based on ray-tracing of the optical 
  model and incorportation of detector characteristics. 

1D DRP - 1D Data reduction pipeline
======

SPT (TBD) - Survey planning and tracking
======

We have just started coordination and development on survey operation including 
its planning and tracking, from database design for survey operation (although 
we already released ETC - exposure time calculator as one package within SPT, 
which was developed over existing software release), and most of other parts 
are under investigation. 

ICS (INSTRM) - instrument control
======

ICS, which stand of instrument control software, is the most well developed 
package within PFS for now, and have number of GitHub repositories in both 
public and private. Existing private repositories in ICS are ics_doc for 
documentation on instrument control strategy and sequence, ics_mac_mlp1 for 
MLP1 interface, ics_config for configuration repository, and ics_mcsActor 
for metrology camera (which has already decided to turn into public). Also 
we tentatively set GitHub issue for ticketing per each repository. 

As above, we plan to make all repositories except for ics_mac_mlp1, and have 
one project in JIRA for ticketing. Within the project for ICS, we may have 
several components to specify which module to be related on (e.g. SpS, xCU, 
or PFI). Also we will track our instrument (or so called actor in tron's 
definition) configuration, planning, and strategy of sequencing using a 
repository on GitHub and this ticketing project. 

Project general (INFRA)
======

Project wide infrastructural discussions will go this project. 

