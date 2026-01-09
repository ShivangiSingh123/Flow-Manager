# Flow Manager Microservice

## Overview

This project implements a Flow Manager system that executes tasks sequentially based on predefined conditions. The flow logic is defined using JSON configuration, making the system generic and extensible. Tasks are executed in order, with conditions determining the next step based on success or failure outcomes.

The application is built as a Python microservice using FastAPI.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Design Pattern: Condition-Based Flow Engine

**Problem**: Need a flexible system to execute tasks in sequence where the execution path depends on task outcomes.

**Solution**: A flow engine that reads JSON configuration defining tasks and conditions. Each condition maps a source task's result to the next task.

**How it works**:
- Tasks are simple Python functions that return `True` (success) or `False` (failure)
- Conditions define what happens after each task completes
- The engine loops through tasks until reaching "end" or encountering an error

### Project Structure

```
flow_manager/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── models.py         # Pydantic models for request validation
│   ├── flow_engine.py    # Core flow execution logic
│   └── tasks.py          # Task implementations and registry
├── tests/
│   └── test_flow_engine.py
├── sample_flow.json      # Example flow configuration
└── requirements.txt
```

### Key Components

1. **FlowEngine** (`flow_engine.py`): Executes flows by looking up tasks in a registry, running them, and using conditions to determine the next task.

2. **Task Registry** (`tasks.py`): A dictionary mapping task names to Python functions. New tasks are added here.

3. **Pydantic Models** (`models.py`): Define the structure for Flow, Task, Condition, and FlowRequest objects.

4. **API Endpoints** (`main.py`):
   - `GET /` - Health check
   - `POST /execute-flow` - Execute a flow from JSON configuration

### Flow Configuration Format

Flows are defined with:
- `start_task`: Which task to run first
- `tasks`: List of task definitions (name + description)
- `conditions`: Rules mapping task results to next steps

## External Dependencies

### Python Packages
- **FastAPI**: Web framework for the REST API
- **Uvicorn**: ASGI server to run the FastAPI application
- **Pytest**: Testing framework

### Running the Application
```bash
cd flow_manager
uvicorn app.main:app --reload
```

### No Database
Currently no database is used. Flow configurations are passed directly via API requests. Task results are returned in the response but not persisted.