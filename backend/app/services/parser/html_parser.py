from bs4 import BeautifulSoup


class HTMLParser:
    """
    Responsible for extracting clean text
    from SEC HTML filings.
    """

    def parse(self, html: str):
        """
        Parse raw SEC HTML and
        return cleaned text.
        """

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        # Remove unnecessary HTML elements
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        return text
    
    def find_text(self, text: str, keyword: str, window: int = 300):
        """
        Find a keyword and return surrounding text.
        """

        index = text.find(keyword)

        if index == -1:
            return None

        start = max(0, index - window)
        end = min(len(text), index + window)

        return text[start:end]