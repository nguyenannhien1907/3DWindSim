# 3DWindSim
<img width="1470" height="802" alt="Screenshot 2026-11-16 at 20 50 56" src="https://github.com/user-attachments/assets/77013ace-0a56-4051-868d-6db6b678b8b3" />

A 3D wind flow and aerodynamic load simulation tool. Built to model airflow behavior and structural wind effects in a 3D environment.

## Overview

`3DWindSim` simulates wind velocity fields and visualizes how airflow interacts with 3D geometry. It combines a Python computational backend (`main.py`) with an interactive web-based visualization frontend (`index.html`).

### Key Features
* **3D Airflow  Modeling:** Simulates directional wind vectors, speed profiles, and flow behavior across a 3D domain.
* **Web Visualization:** Renders the simulation environment, particle streamlines, or pressure/load distributions directly in the browser via `index.html`.
* **Configurable Parameters:** Adjust wind speed, angle of attack, boundary conditions, or obstacle/building geometry to observe real-time aerodynamic responses.

  ---

## Project Structure

```text
3DWindSim/
├── main.py       # Core simulation logic, numerical solver, and data processing
├── index.html    # 3D rendering frontend and interactive controls
└── README.md     # Project documentation
