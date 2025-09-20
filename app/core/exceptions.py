from typing import Any, Dict, Optional
from fastapi import HTTPException, status

class SalesCRMException(Exception):
    """Base exception for SalesCRM application"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

def http_404_not_found(detail: str = "Resource not found"):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )

def http_400_bad_request(detail: str = "Bad request"):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )