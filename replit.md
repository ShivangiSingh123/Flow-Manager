# Flow Manager Microservice

## Overview

This project implements a Flow Manager system that executes tasks sequentially based on predefined conditions. The system uses JSON configuration to define flow logic, making it generic and extensible. Built as a Python microservice using FastAPI, it provides an API endpoint to execute configurable task workflows.

The core functionality centers around:
- Sequential task execution controlled by conditional logic
- Task success/failure evaluation to determine flow progression
- Execution logging for tracking task results

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Flow Engine Pattern

The system uses a state-machine-like pattern where:
- **Problem**: Need to execute multiple tasks in sequence with conditional branching
- **Solution**: A FlowEngine class that reads flow configuration and executes tasks based on conditions
- **Approach**: Tasks are registered in a registry (dictionary mapping task names to functions). The engine starts at a designated task and uses conditions to determine the next task based on success/failure results.

### Task Registry Pattern

- **Problem**: Need a flexible way to map task names from configuration to actual executable code
- **Solution**: A simple dictionary-based registry (`TASK_REGISTRY`) that maps string task names to Python functions
- **Pros**: Easy to extend by adding new functions and registry entries
- **Cons**: Tasks must be pre-registered; no dynamic task loading

### Configuration-Driven Flow Definition

- **Problem**: Hardcoding flow logic makes changes difficult
- **Solution**: JSON-based flow configuration that defines tasks, conditions, and execution paths
- **Components**:
  - `tasks`: List of task definitions with names and descriptions
  - `conditions`: Rules that connect tasks and define branching based on success/failure
  - `start_task`: Entry point for flow execution

### API Layer

- **Framework**: FastAPI
- **Endpoint**: `POST /execute-flow` accepts a flow configuration and returns execution results
- **Data Validation**: Pydantic models (`Flow`, `Task`, `Condition`, `FlowRequest`) handle request validation

### Project Structure

```
flow_manager/
├── app/
│   ├── main.py          # FastAPI application and endpoints
│   ├── models.py        # Pydantic data models
│   ├── flow_engine.py   # Core flow execution logic
│   └── tasks.py         # Task implementations and registry
├── tests/
│   └── test_flow_engine.py
├── sample_flow.json     # Example flow configuration
└── requirements.txt
```

## External Dependencies

### Python Packages

| Package | Purpose |
|---------|---------|
| FastAPI | Web framework for API endpoints |
| Uvicorn | ASGI server to run FastAPI |
| Pytest | Testing framework |

### No External Services

The current implementation has no external database, message queue, or third-party API integrations. All task execution is in-memory and stateless per request.