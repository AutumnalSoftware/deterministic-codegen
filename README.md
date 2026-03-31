# Deterministic Code Generation Example

This is the companion code for the upcoming book "Raising the Level of Abstraction: Deterministic Code Generator for C++"

This repository contains a minimal example of deterministic code generation using a YAML-based DSL and Jinja2 templates.

The generator reads a model, validates it, and produces C++ code that reflects the structure of the system.

---

## Overview

The system is described using a YAML model:

```
measurements:
  - Temperature
  - Humidity

queues:
  - TemperatureQueue

stages:
- TemperatureSensor
- Logger

connections:
  - from: TemperatureSensor
    to: TemperatureQueue
  - from: TemperatureQueue
    to: Logger
```

This model defines:

- data types (`measurements`)
- communication channels (`queues`)
- processing components (`stages`)
- data flow (`connections`)

The generator transforms this model into C++ source files.

---

## Repository Structure
generator.py # code generator
model.yaml # system model
templates/ # Jinja2 templates
output/ # generated files (not committed)


---

## How It Works

The generator performs three steps:

```
1. Load the YAML model
2. Validate the structure
3. Apply templates to produce code

Each template generates a specific part of the system:

- `measurements.h.j2` -> data types  
- `queues.h.j2` -> queue definitions  
- `stages.h.j2` -> processing stages  
- `pipeline.h.j2` -> system structure  
```
---

## Running the Generator
``` ./generator.py ```


Generated files will appear in the `output/` directory.

---

## Notes

- Generated files are not committed to the repository.
- The generator is intentionally simple and explicit.
- Templates are responsible for how the system is implemented.
- The model defines what exists and how it is connected.

---

## Purpose

This example demonstrates a deterministic approach to code generation:

- The model describes the system at a high level
- The generator produces consistent, repeatable output
- The structure of the system is defined by the model, not handwritten code

This repository accompanies a book on deterministic code generation and system design.
