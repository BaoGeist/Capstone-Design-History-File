# Milestone 0: Timeline & Project Planning
**Created:** 2026-10-02

## Timeline
### Stakeholder Milestones
| Week # | Dates | Milestone Tasks | Project Manager | 
| --- | --- | --- | --- |
| 1 | 2026-09-26 - 2026-10-02 | M0: Timeline & Project Planning | Seaya |
| 2-4 | 2026-10-03 - 2026-10-23 | M1: Preliminary Research & Design Inputs | Ursula (co-lead with Kyle) |
| 5-6 | 2026-10-24 - 2026-11-06 | M2: Research & Design Planning | Kyle (co-lead with Ursula) |
| 7-9 | 2026-11-07 - 2026-11-20 | M3: Component Prototyping & Design Outputs | Baoze |
| 9-10 | 2026-11-21 - 2026-12-04 | M4: Final Implementation Plan | Seaya |

### Course Deadlines
| Week # | Deadline | Deliverable | Complete With |
| --- | --- | --- | --- | 
| 1 | 2026-10-02 | Progress Report 1 | M0 |
| 2-4 | 2026-10-23 | Progress Report 2 | M1 |
| 5-6 | 2026-10-29 | Graded Advisor Meeting 1 | M2 |
| 9-10 | 2026-11-26 |  Graded Advisor Meeting 2 | M3 |
| 9-10 | 2026-12-03 | Proof of Concept (POC) Demo Deadline | M3 + M4 | 
| >10 | 2026-12-11 | Progress Report 3 | M4 |



## Milestone Descriptions
### Milestone 0: Timeline & Project Planning

**Due:** 2026-10-02

**Lead:** Seaya

Create a fall semester timeline for stakeholder milestones, defining research topics, user needs, rough deadlines, and project manager assignments. 

Progress Report 1 requirements: [Appendix A — Progress Report 1](#progress-report-1)

#### Course Deliverable(s)
1. **Progress Report 1** is due on **October 2nd**, focusing on the topics: 
    - [Background and motivation](#background-and-motivation) (Ursula)
    - [User needs and project statement](#user-needs-and-project-statement) (Seaya)

<br>
<hr style="border: none; border-top: 1px dashed;">

### Milestone 1: Preliminary Research & Design Inputs

**Due:** 2026-10-23

**Lead:** Ursula

Complete preliminary research on the following topics to guide design input decisions and development planning:
 
1. Doppler ultrasound (B-mode, Doppler, FMD)
    - **Assignee:** Baoze
    - Determine what we need to test (which kinds of ultrasounds - ex. interventions vs standard, how many and type of test subjects)
    - Bonus: ECG (Pan-Tompkins Algorithm)
2. Danny Green's software
    - **Assignee:** Ursula
    - Written in 4tran, can do perpendicular diameter measurement, cannot do cross sectional area
    - Does not meet all user need requirements
3. PhysioMerge integration
    - **Assignee:** Kyle
    - What functions/commands can we use? How will we use them?
    - What additional features does it enable us to add to our software?
4. Image processing tools & libraries
    - **Assignee:** Seaya
    - Research commonly used tools for edge detection
    - Are there specific tools better suited for ultrasound imaging?

#### Planned Tasks
**Requirements & data**

- List the image processing requirements: every region on screen, every measurement, and the robustness cases (ruler baseline and scale changes, depth changes, movement, bad frames)
- Determine hardware constraints: the target machine, GPU or CPU only, and whether processing must run in real time
- Build a small test dataset from our recordings, with Danny Green's values where possible and hand-extracted ground truth (scale, expected graph values)
- Write a validation test plan against Danny Green's software and any other references
- Brainstorm methods to segment the video into regions (ultrasound image, graph, scales)

**GUI & PhysioMerge**

- List UI requirements: view selection, vessel selection, edge editing, reviewing values
- PhysioMerge recon: how it handles data, and what functions and commands it gives us
- Write a PhysioMerge integration spec: how it handles noise, and what error handling we need on our end

**Stakeholder**

- Send our question list to Taha: hardware, the PhysioMerge interface, green box behaviour, depth changes mid-recording, how messy data should appear in the output, frame rate, how vessels are selected, and whether he is marking the fall reports

Progress Report 2 requirements: [Appendix A — Progress Report 2](#progress-report-2). Our scope-specific notes for those sections:

#### Design Input Notes
- Based on Doppler ultrasound research + stakeholder defined user needs, create a list of ultrasound data types needed to produce robust, full-coverage software.
    - i.e. interventional vs standard - and what kinds of interventions? How will that define our coverage?
- Use preliminary FMD recording to detail specific Doppler ultrasound metrics and data.

#### Development Process Notes
- How will we be exploring/testing different image processing tools/libraries? 
- What are high-level design outputs that we will be working towards?

#### Course Deliverable(s)
1. **Progress Report 2** is due on **October 23rd**, focusing on the topics: 
    - Updated user and problem framing (Seaya)
    - [Design inputs](#design-inputs) (Baoze)
    - [Concept-development process and preliminary analysis](#development-process--preliminary-plan)  (All)
    - [Preliminary risk analysis](#preliminary-risk-analysis) (Ursula)
2. A **graded advisor meeting** is scheduled for **October 29th**, with Dr. McDonald, Dr. Smith, and Mohamad. **The meeting agenda must be submitted to the advisors *one week* before the scheduled meeting, on October 22nd.** See Milestone 2 course deliverables for more details on meeting requirements.

<br>
<hr style="border: none; border-top: 1px dashed;">

### Milestone 2: Research & Design Planning

**Due:** 2026-11-06

**Lead:** Kyle

Complete and compile research from Milestone 1 towards defining and detailing specific project tickets. Refine and iterate on the design plan based on continual stakehodler feedback, determine design outputs, create a rough stage-based timeline, and discuss responsibility divisions. 

Determine if any materials or resources need to be requested for the prototyping stage (and future development stages).

**// insert excalidraw plan here? discuss iterations + future questions + write we will specific task divisions are TBD depending on research results + other planning details**

#### Planned Tasks
**Region segmentation & test harness**

- Compare video segmentation methods in an evaluation matrix
- Throwaway test: reliably segment the regions on the test dataset, starting with fixed regions
- Design a test harness that runs each image processing task against the test dataset

**Throwaway tests for the highest-risk algorithms**

- Doppler: read the scale with OCR (values, baseline, inversion, changes mid-recording)
- Doppler: convert the bottom graph into time-series data and find the upper, middle and lower envelope
- Doppler: separate the green ECG trace from the white Doppler trace and detect R-peaks
- Doppler: follow the timeline using timestamps rather than an assumed fixed frame rate
- B-mode: read the depth scale with OCR
- Longitudinal view: edge-detect the artery wall contours
- Longitudinal view: calculate the true (angle-corrected) diameter rather than the vertical distance
- Transverse view: detect circular vessel candidates

**UI**

- Define UI states and expected uses: process a full video, edge-detect an artery on one frame, let the user fix the detection and show them clear feedback, pause, cancel and undo
- Wireframe the UI and start the Figma overlay design

#### Course Deliverable(s)
1. A **graded advisor meeting** is scheduled for **October 29th**, with Dr. McDonald, Dr. Smith, and Mohammed.

    The graded instructor meetings evaluate the quality of the team’s engineering design process across the full year. They provide recurring checkpoints for students to demonstrate preparation, technical progress, engineering judgement, responsiveness to evidence and feedback, and a credible plan for subsequent work.

    At this stage of the project, the team is expected to have preliminary ideas and research completed to present. The meeting will also be used for eliciting feedback and expertise from the instructors.

<br>
<hr style="border: none; border-top: 1px dashed;">

### Milestone 3: Component Prototyping & Design Outputs

**Due:** 2026-11-20

**Lead:** Baoze

#### Planned Tasks
**Foundation**

- Prototype automatic region detection, replacing the fixed regions
- Implement the test harness and verify it on the FMD video
- Define the output interface to the UI and PhysioMerge, including how messy data is represented (deleted frames, nulls, error values)

**Doppler**

- Turn the scale, waveform and envelope, ECG R-peak and timeline tests into prototypes
- Define the real-time metrics: velocity, systole/diastole, pulsatility index (using PhysioMerge where possible)

**Longitudinal view**

- Turn the depth scale, artery wall and true diameter tests into prototypes
- Isolate the green placement box, including when it changes shade or opacity or disappears
- Track diameter across frames (pulse, FMD dilation, movement)

**Transverse view**

- Prototype vessel detection and CSA for arteries and veins
- Track CSA across frames, including vein collapse

**GUI**

- Finish the Figma overlay design
- Prototype the overlay on the FMD video: show the best vessel candidate and accept user edits

All prototypes should be working by the end of this milestone, so Milestone 4 is for validation and documentation rather than new algorithm work.

#### Course Deliverable(s)
1. A **graded advisor meeting** is scheduled for **November 26th**, with Dr. McDonald, Dr. Smith, and Mohamad. **The meeting agenda must be submitted to the advisors one week before the scheduled meeting, on November 19th.**

2. The **POC demo** will take place **between December 3rd and December 10th**. For our timeline purposes we are aiming to complete corresponding tasks and deliverables for December 3rd. At this time (2026-10-02), the demo rubric has not been released, so the following tasks are high-level ideas aligned with what we would want to test/prototype in these planning stages for our end product:
    - Demo image processing library/tool tests with initial FMD imaging (and other data if possible) → discuss the results of each tool and which ones will be used in future development of the product.
    - Present UI prototyping (ex. Figma) and vision for PhysioMerge integration. 

<br>
<hr style="border: none; border-top: 1px dashed;">

### Milestone 4: Final Implementation Plan

**Due:** 2026-12-04

**Lead:** Seaya

Compile research, prototypes, decisions, and design plan drafts into one comprehensive final implementation plan. This plan should meet all the requirements outlined in [Final concept and preliminary design configuration](#final-concept-and-preliminary-design-configuration) in Appendix A.

Progress Report 3 requirements: [Appendix A — Progress Report 3](#progress-report-3)

#### Planned Tasks
- Validate the Doppler metrics on the test dataset
- Validate perpendicular diameter against Danny Green's software on the test dataset
- Validate CSA against manual tracings
- Finalize the PhysioMerge integration design: which steps we hand off (systole/diastole, data deletion, metrics)
- Compile the final design document

#### Course Deliverable(s)
1. A **graded advisor meeting** is scheduled for **November 26th**, with Dr. McDonald, Dr. Smith, and Mohamad. 

    At this stage of the project, the team is expected to present a preliminary prototype and explain the design outputs that are chosen. Instructors use this meeting to provide constructive criticism and challenge the team to consider scenarios that have yet to be implemented. The team will consolidate and refine the prototype before the POC demonstration.

2. **Progress Report 3** is due on **December 11th**, focusing on topics: (responsibility divisions are TBD)
    - [Summary](#summary) (background, user inputs and solution)
    - [Design outputs](#design-outputs)
    - [Final concept and preliminary design configuration](#final-concept-and-preliminary-design-configuration)
    - [Risk and compliance management plan](#risk-and-compliance-management-plan)
3. **Proof of Concept Demo** occurs on **December 3rd**, focusing on the following (All):
    - Explanation of design choices and assumption
    - Showcasing prototype of project
    - Feedback from professors and teaching assistants

<br>
<hr style="border: none; border-top: 1px dashed;">

## Appendix A: Progress Report Instructions

Section requirements copied from the IBEHS 5P06 progress report instructions. Each milestone above links to the sections it covers.

### Progress Report 1
**Due:** 2026-10-02 — see [Milestone 0](#milestone-0-timeline--project-planning)

#### Background and Motivation
- Describe the problem context and the circumstances that motivate the project.
- Use stakeholder discussions and relevant literature to explain why the problem is important and why an
engineering response is warranted.
- Define the intended user(s), stakeholder(s), and setting of use with enough specificity to guide later design
decisions.

#### User needs and project statement
- Summarize the user needs that your team has identified and distinguish needs from proposed solutions.
- Explain the expected impact of a successful design on the stakeholder, broader society, or environment.
Consider health, safety, economic, social, environmental, legal, and cultural dimensions where relevant.
- End with a short, explicit need statement that is visually distinct from the surrounding text (e.g. bolded,
italicized, on a separate line etc.)

### Progress Report 2
**Due:** 2026-10-23 — see [Milestone 1](#milestone-1-preliminary-research--design-inputs)

#### Design Inputs
- Define the requirements, specifications, objectives, and constraints that the design is expected to satisfy.
- Develop objective and, wherever feasible, quantitative criteria through stakeholder consultation, literature
review, and discussions with disciplinary instructors.
- Consider technical, economic, environmental, ergonomic, societal, safety, legal, and regulatory inputs as
applicable.
- Trace each important design input to a user need, stakeholder expectation, risk, standard, or other credible
source

#### Development Process & Preliminary Plan
- Describe the structured process your team will use to generate, analyze, and compare multiple design
concepts.
- Use relevant theory, calculations, models, or simulations to investigate feasibility to an appropriate
preliminary depth.
- Consider uncertainty and trade-offs, including societal, environmental, and legal factors that could affect
concept selection.

#### Preliminary Risk Analysis
- Identify early health and safety risks associated with implementation, prototyping, verification,
manufacturing, deployment, or use.
- Identify potentially applicable standards, codes, laws, and regulatory requirements, including the
consequences of non-compliance.
- Identify relevant ethical concerns and their possible effects on users or society.
- Comment on how the identified risks or constraints influence design concept generation and evaluation

### Progress Report 3
**Due:** 2026-12-11 — see [Milestone 4](#milestone-4-final-implementation-plan)

#### Summary
- Provide a concise overview of the problem, user need, selected solution direction, planned implementation, and
expected impact.
- Include only the background from earlier reports that is necessary to understand this stage of the project.

#### Design Outputs
- Present detailed, objective, and appropriately quantitative design outputs derived from the design inputs.
- Justify outputs using stakeholder evidence, literature, engineering analysis, standards, and disciplinary
guidance.
- Address technical, economic, environmental, ergonomic, societal, safety, and regulatory considerations where
relevant.

#### Final concept and preliminary design configuration
- Justify selection of the final design concept by tracing the decision to user needs, design inputs, evaluation criteria, analytical work, and documented trade-offs.
- Show a credible starting configuration using calculations, models, simulations, low-fidelity prototypes, schematics, pseudocode, or working demonstrations as appropriate.
- Incorporate the findings of your proof-of-concept to demonstrate the feasibility of your final design concept.
- Explain assumptions, limitations, constraints, feasibility, required resources, unanswered questions, and next steps.
- If an output will not be implemented, identify it explicitly and justify the omission using documented evidence.
- If the user need or project framing changed, explain the evidence and obtain instructor approval for the change.

#### Risk and compliance management plan
- Meet with your disciplinary instructor to identify and approve an appropriate risk management tool for your project. Use the approved tool to develop a risk management plan. If no specific tool is recommended, a Failure Mode and Effects Analysis (FMEA) is used.
- Identify health and safety risks associated with implementation, prototyping, verification, manufacturing, deployment, and use.
- Define feasible risk-mitigation and compliance strategies tied to applicable standards, codes, laws, and regulatory requirements.
- State which strategies must be implemented and verified in the final prototype.
