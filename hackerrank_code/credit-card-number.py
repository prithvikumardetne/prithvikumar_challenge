import re

def is_valid_credit_card(card_number):
    # Regex pattern to match the card number format
    pattern = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
    
    # Check if the card number matches the pattern
    if not pattern.match(card_number):
        return "Invalid"
    
    # Remove hyphens for further validation
    card_number = card_number.replace('-', '')
    
    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_number):
        return "Invalid"
    
    return "Valid"

# Sample Input
cards = [
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "4123356789123456",
    "5133-3367-8912-3456",
    "5123 - 3567 - 8912 - 3456"
]

# Validate each card
for card in cards:
    print(is_valid_credit_card(card))