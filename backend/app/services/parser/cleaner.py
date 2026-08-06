import re


class DocumentCleaner:
    """
    Responsible for cleaning text extracted
    from SEC filings.
    """

    def clean(self, text: str):

        # Keep only the human-readable report
        marker = "Form 10-K"

        index = text.find(marker)

        if index != -1:
            text = text[index:]

        # Normalize whitespace
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()