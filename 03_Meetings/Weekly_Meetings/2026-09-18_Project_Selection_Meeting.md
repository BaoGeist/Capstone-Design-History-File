# Capstone Project Selection Meeting
**Date & Time:** 2:30 PM, Friday, September 18th, 2026
**Attendees:** Baoze Lin, Kyle Hagerman, Seaya Liu

## General Meeting Notes
### Proposal 1: Family Doctor Assistance Tool
| | |
| --- | --- | 
| **Stakeholder** | Dr. Kavita Patel, Mohammed Loubani (avaros) |
| **High Level Description** | Build a tool to assist family doctors in streamlining patient medical data management processes, in particular in regards to EMR systems & inbox management. |
| **Main Technical Elements** | LLM/RAG search, OCR, AI safety/data privacy

--- 
#### Specific Goals
- Build an LLM/RAG pattern integrated search engine to allow users to find items via "loose" search terms (ex. "show me all labs with a TSH above 3').
- Build a triage tool to identify "urgent" items in the inbox. 
- Build a medication reconcialiation tool to automatically insert/upsert medications from labs/consult notes to a consolidated list for each patient.
    - Human in the loop deletion tool

### Proposal 2: Duplex Doppler Ultrasound Wrapper
| | |
| --- | --- | 
| **Stakeholder** | Taha Abbasi Hashemi (PhD Student, McMaster Vascular AI Lab)  |
| **High Level Description** | Build a software that takes in duplex Doppler ultrasound videos and process them to display enriched content and data towards analyzing volumetric flow. |
| **Main Technical Elements** | Image processing/edge detection, signal processing

---
### Specific Goals
- In a longitudinal view recording, utilize the ruler tool & edge detection to take a blood vessel diameter measurement perpendicular to the direction of the blood flow. Integrate with Doppler data to assess volumetric blood flow. 
- In a transverse view recording, utilize the ruler tool & edge detection to take the take cross-sectional area of a blood vessel. Also integrate with other data to assess volumetric blood flow. 
- Build a GUI to allow users to see data and change the detected edges manually if desired. 
- BONUS goal: integrate with Physio Merge (lab's propietary software)

### Potential Scope Extension Notes
- Ultrasound supports simultaneous ECG recordings: we could add ECG processing with pantompkins to find the R peaks
- Calculate intima-media thickness (vascular wall thickness)(https://pmc.ncbi.nlm.nih.gov/articles/PMC3968727/#:~:text=Intimo%2Dmedial,B%2Dmode%20ultrasound)
- Work with M mode technology
- Calculate morphological data from Doppler waveforms (https://link.springer.com/article/10.1186/s13089-023-00327-4) in integration wiht PhysioMerge