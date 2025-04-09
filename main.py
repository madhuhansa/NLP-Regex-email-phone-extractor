from contact_extractor import ContactExtractor

text_input = "Contact: name@example.com, call: 071 1234567"
extractor = ContactExtractor(text_input)

emails = extractor.get_email()
phones = extractor.get_phone()

print("Emails:", emails)
print("Phones:", phones)
