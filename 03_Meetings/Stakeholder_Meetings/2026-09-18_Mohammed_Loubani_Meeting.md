# Meeting with Taha 
**Meeting Notes:**
- can't integrate with their app bc of privacy and things
- can maybe provide data and help?
- to work with us we need to meet a provincial standard and other PHIPA & other ethical standards
- can help us with a startup, we wouldn't really be able to get data from them or even kavita (she'd have a challenge asking each patient for data)

- main limitation is resources on avaros's side - can't really afford resources at this early stage when it's not looking like we will have a product for them to use
- they have 6 engineers, they'd probably need to assign 1-2 engineers to us and that's a third of their team that they can't afford to assign
- even if we wanted to do use their APIs 

- he doesn't think we need avaros, we could mock smth up in railway with mock data & have a working prototype without them
- demo with AI and without AI to show how it works

- also Mohammed can give us mock data } deidentify and anonymize mock data to meet PHIPPA standards to preserve important clinical context while keeping private
    - this is used to train the data
    - example with lung issues and mammogram data (radiologist who read it saw that this is cancer & needed biopsy immediately) -> MOA manually filed with the wrong provider (a ghost user) and wasn't addressed for 3-5 months. meanwhile avaros's ai would've recognized it as important immediately and connected with right provider
        - "need to be OCR'd by us"
    - they'd be happy to change that vignette with us too

- Greg's Wings } based on this happening to someone in Alberta
    - melanoma noted in a fax and faxed to a doctor, but the printout messed up or smth, and the doctor didn't know, he didn't know
    - it ended up getting worse and metastasizing and he passed away because of it

- how many cases would you like to see - mohammed
    - kyle: how many do you currently see / able to provide
    - mohammed: 10-15 very detailed core vignettes
    - break down the vignettes into testing scenarioes (ex testing scenario: nonurgent that deceptively looks like an urgent request)

- their main idea that they have is the inbox management system - no other backlog projects that they can give us

- they can def see the proof of concept becoming smth that they can see and work off of in the future in some way, but it will be diff bc it's diff from production (scaling, load, etc)

- from a business perspective, we might be competitors in the future -> might want to sign an NDA with them to protect our ideas

- mohammed's opinion on medication reconciliation project: 5 days to produce a POC - the challenge is to get the requirements, not to build the prototype

- kyle: if we were interested in building a project to integrate with avaros in the future, would they be willing to share requirements (user requirements) that they have
    - mohammed: yes, they do user interviews & create a requirements page (ex med reconciliation was a thing they considered by deprioritized)
    - med reconciliation may not be entirely a inbox management thing

- usability & UX & human factors ppl don't really understand healthcare (think it's all wrong) but they do work with them to some degree ?? avaros tries to build from first principles

- happy to send us data and be our stakeholders

- from kavita:
    - different specialists could have their lists stored in different pdfs. not sure if we want ai to go through all their documents and then compare it to the new pdf email coming in. automatic updates to some of the patient information
    - emr does not have consolidated list, kavita has to type the drugs into a input. inside the avaros. kavita is the ai that is consolidating it. brand name vs generic name of the drug. this one has been discontinued. its all text in the pdf. 
    - written in a little paragraph and is looking through the entire paragraph
    - she thinks avaros is the best emr company in terms of responsiveness


**Action Items:**
- decide if we want to fully decide the specs & spoke of the project
    - issues: we'd have to build so much scaffolding/infrastructure to just start working on the key tasks (triaging, LLM/RAG-based search engine, medicine reconciliation)
- send them a thank you email + our final decision

