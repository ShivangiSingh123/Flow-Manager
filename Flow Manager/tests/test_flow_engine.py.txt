from app.flow_engine import FlowEngine
from app.models import Flow, Task, Condition

def build_flow():
	return Flow(
            id="flow123",
	    name="Test Flow",
	    start_task"="task1",
	    tasks=[
                  Task(name= "task1", description: "Fetch data"),
		  Task(name= "task2", description: "Process data"),
		  Task(name= "task3", description: "Store data")
		  ],

	   conditions=[
		  Condition(
			name: "condition1",
			description: "task1 condition",
			source_task": "task1",
			outcome": "success",
			target_task_success": "task2",
			target_task_failure": "end"
                  ),
                 Condition(
			name: "condition2",
			description: "task2 condition",
			source_task": "task2",
			outcome": "success",
			target_task_success": "task3",
			target_task_failure": "end"
                  ),
                ]
         )

def test_successful_flow():
	flow = build_flow()
	engine = FlowEngine(flow)
	result = engine.execute()

	assert result["status"] == "completed"
        assert len(result["log"]) == 3
        assert result["log"][-1]["task"] == "task3"

def test_missing_flow():
	flow = build_flow()
	flow.start_task = "invalid_task"

	engine = FlowEngine(flow)
	result = engine.execute()

	assert result["status"] == "failed"
        	
