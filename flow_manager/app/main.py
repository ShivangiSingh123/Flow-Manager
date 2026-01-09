from fastapi import FastAPI
from .models import FlowRequest
from .flow_engine import FlowEngine

app = FastAPI(title="Flow Manager Microservice")

@app.post("/execute-flow")
def execute_flow(flow_request: FlowRequest):
    engine = FlowEngine(flow_request.flow)
    return engine.execute()
