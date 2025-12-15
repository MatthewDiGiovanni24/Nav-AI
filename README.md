NavAI: LLM-Guided Navigation for Virtual Reality

NavAI is a generalizable Large Language Model (LLM)–based framework for automating navigation in immersive Virtual Reality (VR) environments. Unlike prior approaches designed for 360° images or 3D simulators, NavAI operates directly on unseen VR scenes and supports both basic movement commands and complex, goal-driven navigation through natural language.

Overview

NavAI bridges human intent, visual scene understanding, and low-level VR controls using LLM-based reasoning. The framework interprets screenshots from the user’s field of view, classifies navigation intent, and executes actions through a structured control interface. It is designed to generalize across diverse VR environments without environment-specific training.

Architecture

NavAI consists of four core components:

Comprehensive Interpreter
Generates textual and spatial interpretations of VR scenes from screenshots.

Navigation Category Classifier
Classifies user queries into semantic queries, explicit actions, or goal-oriented navigation.

Decision Voter
Uses multiple LLM agents to determine goal progress and guide next actions.

Decision-to-Control Mapping
Translates high-level decisions into executable VR control functions.

Supported Actions

Movement

move_forward

move_left

move_right

Stability / View

in_place_rotate_to_left

in_place_rotate_to_right

look_up

look_down

scan_360

Evaluation

NavAI was evaluated in three Unity VR environments: Highway, Country House, and Ship.

100% success on basic action commands (21/21)

89% success rate on direct goal-oriented navigation (16/18)

Average action overhead: ~0.74 seconds

Exploratory scans completed in ~41 seconds on average

Results show strong generalization and accuracy, with latency primarily driven by LLM-based scene interpretation.

Limitations and Future Work

Current limitations include high interpretation latency and inconsistent stopping conditions during exploratory tasks. Future work will focus on reducing latency through lightweight local models, parallel decision voting, and improved context management.

Tech Stack

Unity Simulator

Python

Large Language Models (GPT-4o, Grok-2, Gemini 2.5 Flash)

LLM function calling for control execution
