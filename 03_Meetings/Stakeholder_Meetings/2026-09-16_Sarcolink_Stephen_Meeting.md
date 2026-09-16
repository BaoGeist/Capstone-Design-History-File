# Meeting with Stephen from Sarcolink
**Questions:**
- From the description, it sounds like the scope is confined to designing the UI for the therapy tool, is that correct? Would we be also responsible for the hardware part?
  - depends on the talents that each group has
  - they're open to having duplicated groups
- they wanted to scale from python on pc to running on anything. is that the main goal? or do they care about robustness for various types of users?
  - yes, both are main focus.
  - they're open to modifying scope if anything is out of scope of our discipline, so sticking to software. explicitly said "it's fine to cut the hardware stuff out". we just need to simulate outputs of EMG device with some simulate function that replaces the bluetooth connection.
- can we test prototype? we'd have limited access to it because they only have one and it is very expensive so it's in use already in their r&d

**Project clarifications:**
- they have software that was developed by a self-taught developer (stephen) that makes use of his expertise in understanding biosignals from muscles in movement
- they think it has huge potential for rehab in muscle issues
- want to plug tech right into muscles so that even if they can't produce real and stable form, proper amplitude movements, they can still have _some_ form of exercise, and give them feedback based on their attempted muscle generation patterns
- (all hardware related so context for us but not what we'd do) currently have a refined pipeline for recording the sensor data
  - use surface electromyography to record from 2 points on the surface of the skin on top of the muscle
  - have a system that integrates activity from 4 diff muscles at a time, so 8 electrodes
  - use 8 channel exg system (actually an eeg system) and their pair those channels to end up with 4 bipolar amplifiers
  - they get a stream of emg data from 4 locations now, which feeds a signal processing pipeline
  - software works with that to translate it into controls fora video game, currently tetris
  - hardware is off-the-shelf rn, uses bluetooth so not wired
  - device is attached to the skin directly without wires
  - approx 15000 for that device, designed to amplify brain signal
  - lots of extra hardware and sensing power in that device that they don't need, so want to get better signal with a much less expensive device
- on software side, looking to move from a pc only prototype in python to something that can be deployed using cloud backend and installed across different platforms
- want it working on android phone, iphone, laptop, etc.
- need two different user experiences, one for "non-technical user", person who might take device home with them to do some exercise (must be easy to use, user is likely old and less tech savvy). the other is a physio/clinician who is familiar with device and needs to use data that is logged in the cloud backend and they can access the info easily
- device is meant for clinical use so must be HIPA compliant and secure and have all of the documentation around how the software works to meet regulatory requirements
- need thorough design history file for that device
- we'll need to do research to understand regulatory landscape around device so that we can produce all the needed documentation for the work
- sampling rate must be at least 1000Hz
- the video game experience isn't the main thing:
  - when working on ui across platforms, just want to see that it opens and runs
  - what they're most likely to take from us is the UI that has python program cloud-hosted and can call functions from it from whatever device they're using
  - then making the interfaces workable for the desired use case of the game
- the hardware side is a smaller part of the scope in terms of ensuring the bluetooth
- the idea is that we take ownership of the project, then they go forward at the end and take quality pieces of our project to build into the foundation of their product

- **IP:** everything worked on isn't really revolutionary (whoops) in terms of being something that you could patent, they already have an IEEE publication that describes how the system works
  - that being said, anything that we produce, they will take ownership of to whatever degree is needed to integrate into their final product
  - he believes it's B2 situation for IP docs from capstone
- **Most useful stuff from them is the software and documentation side**
 
**Other notes:**
- initial feedback of prototype with patients:
  - feedback generally positive but also changing.
  - made a few tweaks
  - biggest challenge has been that some folks are just not game people, just a preference thing, not something we need to address
  - **are considering adding a game that's more stripped down and unique to them, open to letting us add it to our project**
    - **Kyle's idea:** why don't we make it a music based thing for people who don't like games as much? moving muscles to the beat of music is a great way to get people moving  
- looking to add more muscle groups?
  - movements are completely flexible based on how they attach the emg, software doesn't change to accommodate different movement patterns into game
- at the start, he threw out an idea of they're looking for a POC that they can make a low-cost emg sensor
  - it's a future thing and not the current phase of development that they're in
  
