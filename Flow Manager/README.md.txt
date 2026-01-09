# Flow Manager Microservice

## Overview
This project implements a Flow Manager system that executes tasks sequentially based on predefined conditions.  
The flow logic is defined using a JSON configuration, making the system generic and easy to extend.

The application is implemented as a Python microservice using FastAPI.

---

## 1. Flow Design Explanation

### How do the tasks depend on one another?
The tasks do not directly depend on each other.  
Their execution order is controlled by conditions defined in the flow configuration.  
Each condition decides which task should run next.

---

### How is the success or failure of a task evaluated?
Each task is implemented as a Python function that returns:
- `True` if the task succeeds
- `False` if the task fails  

The flow manager checks this return value to determine the next step.

---

### What happens if a task fails or succeeds?
- If a task succeeds, the flow manager proceeds to the next task.
- If a task fails, the flow manager immediately stops the execution and ends the flow.
- Task results are stored in an execution log for tracking.

---

## 2. Project Structure
flow-manager/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── flow_engine.py
│ └── tasks.py
│
├── tests/
│ └── test_flow_engine.py
│
├── sample_flow.json
├── requirements.txt
└── README.md

## 3. How to Run the Application

### Install Dependencies
pip install -r requirements.txt

Start the service
uvicorn app.main:app --reload

The service will be available at:
http://127.0.0.1:8000


4. API Endpoint
Execute Flow

POST /execute-flow

Request Body:
JSON flow definition (see sample_flow.json)

Response:
Execution status and task execution log

5. Run Unit Tests
   pytest

6. Summary

The Flow Manager executes tasks sequentially and uses conditions to control the execution flow.
Tasks proceed only when the previous task succeeds, and the flow ends immediately if a task fails.
