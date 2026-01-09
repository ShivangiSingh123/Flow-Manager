from fastapi import FastAPI
from app.models import FlowRequest
from app.flow_engine import FlowEngine

app = FastAPI(title="Flow Manager Microservice")

@app.post("execute-flow")
def execute_flow(flow_request: FlowRequest):
	engine = FlowEngine(flow_request.flow)
	return engine.execute