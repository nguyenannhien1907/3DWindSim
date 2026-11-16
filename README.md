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
```

---

## Getting Started

### Prerequisites
* **Python 3.8+**
* **NumPy** (and any other packages imported in `main.py`)
* A modern web browser (Chrome, Firefox, Edge, or Safari)

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nguyenannhien1907/3DWindSim.git
   cd 3DWindSim
   ```

2. **Install dependencies:**
   ```bash
   pip install numpy
   ```

3. **Run the simulation backend:**
   ```bash
   python main.py
   ```

4. **Launch the 3D visualization:**
   * Start a local server in the project directory:
     ```bash
     python -m http.server 8000
     ```
   * Open your browser and navigate to `http://localhost:8000` (or open `index.html` directly if your setup does not require a local server).
