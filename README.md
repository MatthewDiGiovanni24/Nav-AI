# NavAI

---

## Introduction

NavAI is a Large Language Model (LLM)–guided framework designed to automate navigation in immersive Virtual Reality (VR) environments. Existing navigation approaches largely focus on 360° image datasets or traditional 3D simulators, which do not translate well to fully immersive VR. This project explores how LLMs can bridge natural language intent, visual scene understanding, and low-level control to support generalizable navigation across unseen VR environments.

NavAI was developed as a research project to evaluate the feasibility, performance, and limitations of LLM-driven navigation in VR.

---

## Specifications

- **Generalizable VR Navigation Framework**: Operates across diverse Unity VR environments without environment-specific training.
- **Natural Language Interface**: Supports both basic motion commands and complex goal-driven navigation.
- **LLM-Based Scene Interpretation**: Uses visual and textual reasoning to understand the user’s field of view.
- **Multi-Agent Decision Voting**: Improves robustness by aggregating decisions from multiple LLMs.
- **Structured Control Mapping**: Translates high-level intent into executable VR control actions.

---

## Navigation Framework

NavAI follows a four-stage pipeline:

1. **Comprehensive Interpreter**  
   Captures screenshots from the VR environment and generates textual descriptions and spatial interpretations using an LLM.

2. **Navigation Category Classification**  
   Classifies user input into semantic queries, explicit action commands, or goal-oriented navigation tasks.

3. **Decision Voter**  
   Uses multiple LLM agents to determine whether a navigation goal has been reached or requires further action.

4. **Decision-to-Control Mapping**  
   Maps navigation decisions to predefined VR control functions and executes them in the simulator.

---

## Supported Actions

**Movement Actions**
- move_forward  
- move_left  
- move_right  

**Stability / View Actions**
- in_place_rotate_to_left  
- in_place_rotate_to_right  
- look_up  
- look_down  
- scan_360  

---

## Evaluation

NavAI was evaluated across three Unity VR environments:

- Highway (outdoor, dynamic obstacles)
- Country House (indoor, multi-room)
- Ship (confined space)

Results:
- 100% success on basic action commands (21/21)
- 89% success rate on direct goal-oriented navigation
- Average action overhead of approximately 0.74 seconds
- Exploratory scans completed in approximately 41 seconds on average

The primary performance bottleneck was LLM-based scene interpretation latency.

---

## Impact

This project demonstrates:
- The feasibility of LLM-guided navigation in immersive VR
- Strong generalization across unseen environments
- Practical limitations of current LLMs in real-time embodied tasks
- Design tradeoffs between reasoning accuracy and system latency

NavAI provides a foundation for future work in VR automation, accessibility, and intelligent virtual assistants.

---

## Conclusion

NavAI highlights both the potential and current constraints of using large language models for embodied navigation. While the system achieves high accuracy and generalization, further optimization is required for real-time use. The project contributes insights into LLM orchestration, multimodal reasoning, and human-centered AI system design.
