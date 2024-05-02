import requests

def check_number(number):
  url = f"https://api.p.2chat.io/open/whatsapp/check-number/+62895379798855/+{number}"
  headers = {'X-User-API-Key': 'UAK932a94a7-54fc-45c6-8d01-410bd36a6c62'}
  response = requests.get(url, headers=headers).json()
  
  is_true = response.get('on_whatsapp')
  return is_true

#check_number('6282278559895')