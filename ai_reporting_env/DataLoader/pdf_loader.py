# import pdfplumber
# path = "F:\personal\vasant_documents\Resume\2026\AI_ENGINEER\Vasant_Deware_AI_Engineer.pdf"
# with pdfplumber.open(path) as pdf:
#     text = ""
#     for page in pdf.pages:
#         text += page.extract_text()

# print(text)

import pdfplumber

path = r"F:\personal\vasant_documents\Resume\2026\AI_ENGINEER\Vasant_Deware_AI_Engineer.pdf"

with pdfplumber.open(path) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

text_length = len(text)
print("Text length:", text_length)
# print("\nFirst 1000 characters:")
# print(text[:1000])
