import re


def clean_text(text):

    if not text:
        return ""

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # Keep only alphabets, numbers and spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)

    # Final trim
    return text.strip()
