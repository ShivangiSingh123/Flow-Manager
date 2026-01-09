# Flow Manager Microservice

## Overview

This is a Python microservice that implements a Flow Manager system for executing tasks sequentially based on predefined conditions. The system uses JSON configuration to define flow logic, making it generic and extensible. Tasks are executed in order, with conditions determining the next step based on success or failure outcomes.

The core functionality allows users to submit a flow definition via API, and the engine processes tasks one by one, stopping on failure or completing when all tasks succeed.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Framework & API Design
- **FastAPI** serves as the web framework, providing a single POST endpoint `/execute-flow`
- Pydantic models handle request validation and data structure definitions
- The API accepts a complete flow definition in the request body rather than referencing stored configurations

### Flow Engine Pattern
- **FlowEngine class** (`app/flow_engine.py`) orchestrates task execution using a state machine approach
- Tasks are executed sequentially starting from `start_task`
- Conditions determine branching: each condition maps a source task to success/failure targets
- Execution continues until reaching "end" or encountering an error
- Returns an execution log tracking each task's result

### Task Registry Pattern
- Tasks are Python functions registered in a `TASK_REGISTRY` dictionary (`app/tasks.py`)
- Each task returns `True` (success) or `False` (failure)
- New tasks are added by defining a function and registering it in the dictionary
- This decouples task implementation from flow configuration

### Data Models
- **Flow**: Contains id, name, start_task, list of tasks, and list of conditions
- **Task**: Simple name/description pair
- **Condition**: Defines source task, expected outcome, and target tasks for success/failure paths

### Execution Flow
1. API receives flow definition
2. FlowEngine initializes with the flow
3. Engine looks up current task in registry and executes it
4. Based on result, engine finds matching condition and determines next task
5. Process repeats until "end" is reached or task lookup fails

## External Dependencies

### Python Packages
- **FastAPI**: Web framework for the REST API
- **Uvicorn**: ASGI server for running the FastAPI application
- **Pytest**: Testing framework for unit tests
- **Pydantic**: Data validation (bundled with FastAPI)

### Runtime Requirements
- Python 3.x environment
- No database or external services required
- No authentication mechanism implemented
- Stateless design - no persistent storage of flow executions