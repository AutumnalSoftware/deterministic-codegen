# Deterministic Code Generation Example

This is the companion code for the book "Raising the Level of Abstraction: Deterministic Code Generator for C++"

This repository contains a minimal example of deterministic code generation using a YAML-based DSL and Jinja2 templates.

The generator reads a model, validates it, and produces C++ code that reflects the structure of the system.

---

## Overview

The system is described using a YAML model:

```
measurements:

Temperature
Humidity

queues:

TemperatureQueue

stages:

TemperatureSensor
Logger

connections:

from: TemperatureSensor
to: TemperatureQueue
from: TemperatureQueue
to: Logger
```
