from fastapi import APIRouter

from app.services.sec.sec_service import SECService

router = APIRouter()

sec_service = SECService()


@router.get("/sec/tickers", tags=["SEC"])
def get_company_tickers():
    """
    Temporary endpoint to validate
    communication with the SEC.
    """

    return sec_service.get_company_tickers()