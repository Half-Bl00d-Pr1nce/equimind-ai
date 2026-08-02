from pydantic import BaseModel, Field


class Company(BaseModel):
    """
    Represents a publicly traded company.
    """

    ticker: str = Field(..., description="Stock ticker symbol")