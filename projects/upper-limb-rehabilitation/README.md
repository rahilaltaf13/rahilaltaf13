# Development of Rehabilitation System for Upper Limb Movement

## Project Overview
This project develops a cost-effective upper-limb rehabilitation prototype using a CAD-designed exoskeleton structure, EMG-based muscle activity detection, and pneumatic actuation for assisted movement.

## Project Team
- Eshwar Ram T M (21R213)
- Rahil Altaf Wani (21R229)
- Shivakumarasamy J (22R441)
- Yograj S M (22R443)

**Project Guide:** Dr. M. Suresh  
**Department:** Robotics and Automation Engineering, PSG College of Technology

## Motivation
The project presentation identifies limitations in conventional rehabilitation approaches, including expense, limited adaptability, and reliance on human intervention. The proposed system aims to explore a cost-effective and adaptable approach to upper-limb movement rehabilitation.

## System Concept
The project uses EMG sensing to detect muscle activity and pneumatic actuation to assist movement.

### Control flow
```text
EMG Sensor
    ↓
Arduino
    ↓
Relay
    ↓
5/2 Solenoid Directional Control Valve
    ↓
Double-Acting Pneumatic Cylinder
    ↓
Assisted Upper-Limb Movement
```

The project presentation also records an earlier sensor acquisition demonstration using an EMG sensor and Arduino, with a servo motor used to check sensor response.

## Design and Fabrication
- Exoskeleton CAD modeling completed in SolidWorks
- Exoskeleton components fabricated using 3D printing
- Pneumatic actuation implemented using a cylinder and solenoid valve

## Project Status
The April 2025 review presentation reported approximately 80% completion at that stage. It states that the system did not yet include feedback integration.

## Future Work
The presentation identifies real-time feedback mechanisms as a possible future enhancement to improve system adaptability.

## Documentation
- [Project synopsis](../../docs/upper-limb-rehabilitation-synopsis.md)
- Source presentation: project review PPT (to be added as a downloadable repository file)
- Project photographs, CAD renders, and demonstration video: to be added when available

## Important Scope Note
This repository documents the academic prototype and the information available in the submitted synopsis and review presentation. It does not claim clinical validation or proven therapeutic effectiveness.
