from fastapi import APIRouter
from fastapi import HTTPException
from app.services.sec.sec_service import SECService

router = APIRouter()

sec_service = SECService()


@router.get("/sec/{ticker}/submissions", tags=["SEC"])
def get_company_submissions(ticker: str):
    """
    Temporary endpoint to validate company submissions.
    """

    company = sec_service.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    return sec_service.get_company_submissions(company["cik"])

@router.get("/sec/{ticker}/10k", tags=["SEC"])
def get_latest_10k(ticker: str):

    company = sec_service.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    return sec_service.get_latest_10k(company["cik"])

@router.get("/sec/{ticker}/10k-url", tags=["SEC"])
def get_10k_url(ticker: str):
    """
    Temporary endpoint to validate 10-K URL generation.
    """

    company = sec_service.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    return sec_service.get_10k_url(company["cik"])

@router.get("/sec/{ticker}/download", tags=["SEC"])
def download_latest_10k(ticker: str):

    company = sec_service.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    return sec_service.download_latest_10k(company["cik"])