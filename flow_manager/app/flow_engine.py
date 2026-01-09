from app.tasks import TASK_REGISTRY

class FlowEngine:
	def __init__(self, flow):
		self.flow = flow
		self.conditions = flow.conditions


	def _get_condition(self, task_name):
		for condition in self.conditions:
			if condition.source_task == task_name:
				return condition
		return None

	def execute(self):
		current_task = self.flow.start_task
		execution_log = []

		while current_task != "end":
			task_function = TASK_REGISTRY.get(current_task)

			if not task_function:
				return {
					"status": "failed",
					"reason": f"Task '{current_task}' not found",
					"log": execution_log
					}

			result = task_function()
			execution_log.append({"task": current_task,						      "result": "success" if result else "failure"})
			
			condition = self._get_condition(current_task)
			if not condition:
				break

			current_task = (condition.target_task_success if result else condition.target_task_failure)

		return {"status": "completed", "log": execution_log}