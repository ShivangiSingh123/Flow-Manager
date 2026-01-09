# Flow Manager Microservice

## Overview

This is a Python microservice that executes tasks sequentially based on predefined conditions. The system uses a JSON-driven flow configuration to determine task execution order, making it generic and extensible. Built with FastAPI, it provides a REST API endpoint for triggering flow executions.

The core concept is a workflow engine where:
- Tasks are discrete units of work that return success/failure
- Conditions define the routing logic between tasks
- The flow stops immediately on any task failure

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Flow Engine Design

**Problem:** Need a flexible way to define and execute sequential tasks with conditional routing.

**Solution:** JSON-based flow configuration with a registry-based task system.

- **Flow Configuration**: Defines tasks and conditions as JSON, allowing non-code changes to workflow logic
- **Task Registry Pattern**: Tasks are Python functions registered in a dictionary (`TASK_REGISTRY`), enabling easy addition of new tasks
- **Condition-based Routing**: Each condition maps a source task's result to the next task (success path or failure path)

**Key Design Decisions:**
1. Tasks return boolean values (True/False) for simple success/failure evaluation
2. Flow execution stops on first failure - no retry or error recovery built-in
3. Execution log captures each task's result for debugging/auditing

### API Structure

Single endpoint architecture:
- `POST /execute-flow` - Accepts a flow configuration and executes it

**Request Model:**
```
FlowRequest
  └── Flow
        ├── id, name, start_task
        ├── tasks[] (Task: name, description)
        └── conditions[] (Condition: source_task, target_task_success, target_task_failure)
```

### Project Structure

```
flow_manager/
├── app/
│   ├── main.py          # FastAPI application and endpoint
│   ├── models.py        # Pydantic models for request validation
│   ├── flow_engine.py   # Core execution logic
│   └── tasks.py         # Task implementations and registry
├── tests/
│   └── test_flow_engine.py
├── sample_flow.json     # Example flow configuration
└── requirements.txt
```

### Running the Application

```bash
cd flow_manager
uvicorn app.main:app --reload
```

### Testing

```bash
cd flow_manager
pytest tests/
```

**Note:** The test file currently has syntax errors (missing `=` signs, using `:` instead of `=` in kwargs) that need to be fixed before tests will run.

## External Dependencies

### Python Packages

| Package | Purpose |
|---------|---------|
| FastAPI | Web framework for REST API |
| Uvicorn | ASGI server for running FastAPI |
| Pytest | Testing framework |
| Pydantic | Data validation (included with FastAPI) |

### No External Services

This microservice is self-contained with no external database, message queue, or third-party API integrations. All task implementations are in-memory Python functions.