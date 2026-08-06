import requests
from pathlib import Path


class SECService:
    """
    Service responsible for interacting
    with the SEC EDGAR system.
    """

    BASE_URL = "https://www.sec.gov"

    HEADERS = {
        "User-Agent": "EquiMindAI/1.0 (crookshanks2807@gmail.com)",
        "Accept-Encoding": "gzip, deflate",
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

    def get_cik(self, ticker: str):
        """
        Find the SEC CIK for a given ticker symbol.

        Args:
            ticker (str): Stock ticker symbol (e.g., AAPL)

        Returns:
            dict | None: Company information containing ticker,
            company name, and zero-padded CIK if found.
            Returns None if the ticker does not exist.
        """

        companies = self.get_company_tickers()

        ticker = ticker.upper()

        for company in companies.values():

            if company["ticker"] == ticker:

                return {
                    "ticker": company["ticker"],
                    "company": company["title"],
                    "cik": str(company["cik_str"]).zfill(10),
                }

        return None
    
    def get_company_submissions(self, cik: str):
        """
        Retrieve the SEC submissions JSON for a company.
        """

        url = f"https://data.sec.gov/submissions/CIK{cik}.json"

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
    
    def get_latest_10k(self, cik: str):
        """
        Retrieve metadata for the latest 10-K filing.
        """

        submissions = self.get_company_submissions(cik)

        recent = submissions["filings"]["recent"]

        forms = recent["form"]

        for index, form in enumerate(forms):

            if form == "10-K":

                return {
                    "filing_date": recent["filingDate"][index],
                    "accession_number": recent["accessionNumber"][index],
                    "primary_document": recent["primaryDocument"][index],
                }

        return None
    
    def get_10k_url(self, cik: str):
        """
        Construct the download URL for the latest 10-K filing.
        """

        filing = self.get_latest_10k(cik)

        if filing is None:
            return None

        accession_number = filing["accession_number"].replace("-", "")

        cik_number = str(int(cik))

        return {
            "filing_date": filing["filing_date"],
            "document_url": (
                f"https://www.sec.gov/Archives/edgar/data/"
                f"{cik_number}/"
                f"{accession_number}/"
                f"{filing['primary_document']}"
            ),
        }
    
    def download_latest_10k(self, cik: str):
        """
        Download and save the latest 10-K HTML filing.
        """

        filing = self.get_10k_url(cik)

        if filing is None:
            return None

        response = requests.get(
            filing["document_url"],
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        save_dir = Path("data/filings")
        save_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{cik}_10K.html"

        file_path = save_dir / filename

        file_path.write_text(
            response.text,
            encoding="utf-8",
        )

        return {
            "file": str(file_path),
            "length": len(response.text),
        }