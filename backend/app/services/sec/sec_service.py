import requests


class SECService:
    """
    Service responsible for interacting
    with the SEC EDGAR system.
    """

    BASE_URL = "https://www.sec.gov"

    HEADERS = {
        "User-Agent": "EquiMindAI/1.0 (crookshanks2807@gmail.com)",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov",
    }

    def get_company_tickers(self):
        """
        Download the SEC company ticker dataset.
        """

        url = f"{self.BASE_URL}/files/company_tickers.json"

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()