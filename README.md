# Neuro-Adaptive Roadway Optimization Algorithm (NAROA)

NAROA is a modular A* pathfinding system enhanced with real-time cognitive load awareness. It dynamically adjusts route selection based on simulated driver stress metrics, such as eye tracking and head movement, with the goal of improving urban navigation safety and reducing mental fatigue.

## Features

- Neuroadaptive edge weighting for smarter routing
- Stress-tagged interchange identification (`low`, `medium`, `high`)
- Reconstructs and logs cognitively optimized paths
- Runtime and memory profiling built-in

---

## Requirements

- Python 3.7+
- `psutil`
- `heapq` (standard)
- `pytest` (for test suite)

Install dependencies using:

```bash
pip install -r requirements.txt
