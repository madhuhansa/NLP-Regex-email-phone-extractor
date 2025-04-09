import re

class ContactExtractor:
    def __init__(self, text):
        self.text = text

    def get_email(self):
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, self.text)
        return emails

    def get_phone(self):
        phone_pattern = r"\(\d{3}\) \d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\+\d{2}[-\s]?\d{9}|0\d{9}|\d{3} \d{7}|\d{3} \d{3} \d{4}|\d{3}[-\s]?\d{3}[-\s]?\d{4}"
        phones = re.findall(phone_pattern, self.text)
        return ["".join(p) if isinstance(p, tuple) else p for p in phones]

# Example test (optional)
if __name__ == "__main__":
    sample = "You can reach me at name.example@mail.com or call me at (123) 456-7890. 077 3761477"
    extractor = ContactExtractor(sample)
    print("Emails:", extractor.get_email())
    print("Phones:", extractor.get_phone())
