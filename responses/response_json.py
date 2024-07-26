from fastapi.responses import JSONResponse
from typing import Dict, Any

def response_json(message: str = None, data: Any = None, status: int = 200) -> Dict[str, Any]:
    response_data: Dict[str, Any] = {}
    
    if message:
        response_data["message"] = message
    
    if data is not None:
        if isinstance(data, dict):
            response_data.update(data)
        else:
            response_data["data"] = data

    return response_data
