# UAV-SWARM-DRONE
A FAULT-TOLERANT CYBER-PHYSICAL FLIGHT CONTROLLER DETECTING MAVLINK TELEMENTRY ATTACKS AND MITIGATING HARMONIC REASONANCE IN UAVs
<div align="center">

# 🛸 UAV Cyber-Physical Resilience & Resonance Injection Framework
### *Advanced Aeronautical Engineering & Cyber-Physical Security Portfolio*

[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()
[![Institution](https://img.shields.io/badge/Institution-USTO--MB-blue.svg)]()
[![Focus](https://img.shields.io/badge/Domain-Aeronautics%20%7C%20Cybersecurity-orange.svg)]()
[![Python](https://img.shields.io/badge/Python-3.x-blueviolet.svg)]()
[![MATLAB](https://img.shields.io/badge/MATLAB-R2023b-red.svg)]()
[![SolidWorks](https://img.shields.io/badge/CAD-SolidWorks-blue.svg)]()

</div>

---

## 📑 Table of Contents
* [Overview](#-overview)
* [Repository Architecture](#-repository-architecture)
* [Technical Modules](#-technical-modules)
  * [1. Offensive Vector (resonance_injection.py)](#1-offensive-vector-resonance_injectionpy)
  * [2. Defensive Filter (sensor_defense.py)](#2-defensive-filter-sensor_defensepy)
  * [3. Structural Analysis & CAD (matlab/ & cad/)](#3-structural-analysis--cad-matlab--cad)
* [Installation & Execution](#-installation--execution)
* [Academic Context](#-academic-context)

---

## 🔭 Overview

Modern Unmanned Aerial Vehicles (UAVs) rely heavily on complex sensor suites and digital telemetry pipelines. This repository documents a complete research and development pipeline investigating cyber-physical vulnerabilities in flight control systems. It demonstrates how high-frequency harmonic actuator injections can compromise structural stability via MAVLink, followed by an engineered software-defined defense proxy utilizing real-time anomaly detection and adaptive PWM clamping.

---

<div>

## 🗂️ Repository Architecture

`text
uav/
│
├── 📂 src/
│   ├── 📜 resonance_injection.py      # MAVLink high-frequency pulse injection script
│   └── 📜 sensor_defense.py           # Real-time anomaly detection and PWM clamp proxy
│
├── 📂 matlab/
│   └── 📜 resonance_analysis.m        # Frequency response and mechanical transmissibility models
│
├── 📂 cad/
│   ├── 📐 quadcopter_assembly.sldasm  # Carbon fiber airframe and avionics bay assembly
│   └── 📐 imu_mount.sldprt            # Silicone-damped inertial measurement unit bracket
│
└── 🛡️ .gitignore                      # Workspace exclusion rules
