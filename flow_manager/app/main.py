from fastapi import FastAPI
from .models import FlowRequest
from .flow_engine import FlowEngine

app = FastAPI(title="Flow Manager Microservice")

@app.get("/")
def read_root():
    return {"message": "Flow Manager Microservice is running", "endpoints": ["/execute-flow"]}

@app.post("/execute-flow")
def execute_flow(flow_request: FlowRequest):
    engine = FlowEngine(flow_request.flow)
    return engine.execute()
