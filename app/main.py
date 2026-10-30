from fastapi import FastAPI 
from prometheus_fastapi_instrumentator import Instrumentator 
from app.api import route_auth, route_predict 
from app.middleware.logging_middleware import LoggingMiddleware 
from app.core.exceptions import register_exception_handlers 

app = FastAPI(title = " Car Price Prediction API")

#link middleware 
app.add_middleware(LoggingMiddleware)

#link endpoints 
app.include_router(route_auth.router, tags=['Auth'])
app.include_router(route_predict.router, tags=['Prediction'])

#monitoring using Prometheus 
Instrumentator().instrument(app).expose(app)

#add exception handler 
register_exception_handlers(app)