import httpx

def calculate_tax_for_user(income):
    response = httpx.get(f'http://localhost:8000/tax/{income}')
    print(f'response text: {response.text} - type: {type(response.text)}')
    print(f'response json: {response.json()} - type: {type(response.json())}')
    tax = response.json()['tax']
    return tax



calculate_tax_for_user(1000)
calculate_tax_for_user(5000)