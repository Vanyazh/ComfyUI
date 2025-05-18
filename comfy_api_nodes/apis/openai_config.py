from typing import Optional, Dict, Any
from pydantic import BaseModel

class OpenAIImageGenerationRequest(BaseModel):
    model: str
    prompt: str
    n: int = 1
    size: str = "1024x1024"
    quality: str = "standard"
    style: str = "vivid"
    response_format: str = "url"
    seed: Optional[int] = None

class OpenAIImageEditRequest(BaseModel):
    model: str
    prompt: str
    n: int = 1
    size: str = "1024x1024"
    image: Any = None  # Will be handled as file upload
    mask: Optional[Any] = None  # Will be handled as file upload
    response_format: str = "url"

class OpenAIImageGenerationResponse(BaseModel):
    created: int
    data: list[Dict[str, str]]