# Thoughts-to-text-using-eye-signal
# INTRODUCTION:
Communication is a fundamental human need, but millions of people with motor disabilities, paralysis, or speech impairments struggle to express themselves. Traditional communication methods, such as human assistance or physical boards, are slow and often impractical for real-time communication.

The Blink-to-Text using Eye Signal system leverages Artificial Intelligence (AI), Computer Vision, and Deep Learning to detect eye blinks and gaze patterns, translating them into text or speech. Users can select letters, form words, and communicate efficiently using only their eyes. This provides independence and faster communication for users with severe motor limitations.


# SCOPE OF THE PROJECT:
The Blink-to-Text project is designed as a real-time assistive communication system:

Detects single, double, or long blinks as input signals.

Allows selection of letters from a virtual keyboard using eye blinks.

Integrates AI-based autocomplete to predict words and reduce typing effort.

Converts generated text into speech using Text-to-Speech (TTS).

Supports emergency messaging, e.g., sending “Nurse” via SMS.

This system uses OpenCV for video capture, dlib for facial and eye landmark detection, and AI/ML models for blink pattern interpretation and word prediction.

# EXISTING SYSTEM:
Current communication aids for motor-impaired users rely on:

Physical devices like switches, sip-and-puff systems, or eye trackers.

Manual typing on on-screen keyboards with limited automation.

Limitations:

Expensive and require specialized hardware.

Slow communication with manual selection.

Limited real-time predictive features and no automated emergency alerts.


# PROPOSED SYSTEM:
The Blink-to-Text using Eye Signal system provides a software-based, real-time solution that converts eye blinks into text and speech:

Eye Detection & Landmarking: Uses dlib to detect eyes and track blinks.

Blink Classification: Differentiates short, long, or multiple blinks to select letters or commands.

AI Autocomplete: Predicts next words to accelerate sentence formation.

Text-to-Speech Output: Reads text aloud for effective communication.

Emergency Messaging: Sends predefined messages like “Nurse” via SMS.

The system is lightweight, user-friendly, and works under variable lighting without specialized hardware.

# MODEL ARCHITECTURE:
<img width="1280" height="800" alt="Architecture diagram" src="https://github.com/user-attachments/assets/a7163a71-3506-4156-aa10-8aa052251337" />

Pipeline Overview:

Camera Input – Captures real-time video of the user’s face.

Facial Landmark Detection – Identifies eye region using dlib.

Eye Blink Detection – Computes Eye Aspect Ratio (EAR) to detect blinks.

Signal Mapping – Maps blinks to letters/commands on a virtual keyboard.

AI Autocomplete – Suggests next words for faster communication.

Text-to-Speech & SMS – Converts generated text into voice and optionally sends emergency alerts.


# OUTPUT:

##  Eye-Controlled Virtual Keyboard Interface Output
<img width="637" height="526" alt="o1" src="https://github.com/user-attachments/assets/e4d5b5a7-c382-4fb6-a4f5-22a0e884d051" />



## BlinkToText Video Feed – Face and Eye Detection Output
<img width="802" height="707" alt="o2" src="https://github.com/user-attachments/assets/62c0d15b-65f2-400e-8245-2a4dd0b9b74a" />

  

# REFERENCES:
[1] M. Ezzat, M. Maged, Y. Gamal et al., “Blink‑To‑Live eye‑based communication system for
users with speech impairments,” Scientific Reports, vol. 13, art. no. 7961, 2023.
[2] K. Vignaashri and S. Jesima, Eyegaze Communication System, Int. J. Eng. Res. Technol.
(IJERT), vol. 7, no. 11, 2019.
[3] Xi Liu, Bingliang Hu, Yang Si, and Quan Wang, “The role of eye movement signals in
non‑invasive brain‑computer interface typing system,” Med. & Biol. Eng. & Comput., 2024,
DOI:10.1007/s11517‑024‑03070‑7.
[4] S. Anzarus Sabab, M. R. Kabir, S. R. Hussain et al., “VIS‑iTrack: Visual Intention through
Gaze Tracking using Low‑Cost Webcam,” ArXiv Preprint, 2022.
[5] A. Raj and A. Kumar, EOG Communication Interface for Quadriplegics: Prototype & Signal
Processing, ArXiv Preprint, 2025.
[6] U. R. Rani, V. B., Vandana A. S., Wamiq Yousuf & J. K., “Communication System for
Incapacitated using Eye Blink,” Perspectives in Communication, Embedded‑Systems and
Signal‑Processing (PiCES)
[7] S. T. Dehzangi, M. Farooq, and H. Taheri, Development of an electrooculogram‑based
eye‑computer interface for communication of individuals with ALS, J. NeuroEngineering
Rehabil., 2017
[8] Xi Liu, B. Hu, Y. Si & Q. Wang, “Eye‑Tracking and BCI Integration for Assistive
Communication in Disorders of Consciousness,” J. Med. Syst., 2025.
[9] T. O. Zander et al., Passive brain‑computer interfaces: a perspective on increased interactivity,
in Brain‑Computer Interfaces: Technological and Theoretical Advances, Frontiers Publishing,
2018.
[10] PubMed Authors, “Deep learning‑based eye sign communication system for people with
speech impairments,” PubMed, 2025
  assets/6e4e3f68-9821-48a5-901f-9db1a8bdfaa6" />
