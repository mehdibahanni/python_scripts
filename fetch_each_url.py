import requests

# URL to send the POST request to
url = 'https://aa.3isk.icu/3isk978924.php'

# Headers as specified
headers = {
    'Host': 'aa.3isk.icu',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://3isk.biz',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://3isk.biz/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=0, i'
}

# Payload with the provided `news` parameter and `submit`
payload = {
    'news': 'UHRINktUTWR4ZkhoMDVCYVM5bFdtWDF1dHZacXJhNTU1ODVTNm5HOGd1cko3VzM5WWVXQkZzeVdZTEtBb3VvU3FFWGpoZklabnlaa1pzSXErMkIvT2NQazkrN3p5YUZDU1QvNEhNZ1Z0cERBcTJuQ2tBKytlUXh5NWhlL3hQc2pvK0lHNmQ0WktTK2FhZDdMRnBuS1ZkaWpZRU9wMUlpejk2NGd6elZoODhpc0Y5ZXFWeWo4N29oZEF1WU05aUZkdFBwN2V5NXpoSE5uR1Vpd1dRZlNPRnJVelBjMzlMR3ZwWjFCMlE1QUtXVFJzeG5RUkFiR01GMGtTYWdQRU1OcUU5UXRBMGdHbmFzMEF1cEQwRUdkMzNkRmpLREhXUkZsN3ZhTWtKQnFSNnN2dVhmWkora2I4cTlLeUxrNS96eXNmNkRYK2JTTlJ1TkwzdUR2MTlrWm9Yd0s5RDF1TEhzUWp1aEZ5bndQTlFyWGg5ZmNTbXBaZ04zdS8yaFVnVFBCSnJzL1A0R3llbDlscnJmcmN0TW04dTdZMUlDTG1BemdmMzhxbFlpaDkvNzZ5WURBOC9Bdk5lU05xU0dtNDFadGswWjZmYXFvMlMrM05VazJzWXJzR2tod2ZkRVRkUVRZZDkxdStHSG1QSTF4MXB2aTFyTUJPM2ZBM3lTdWt1WFo%3D',
    'submit': 'submit'
}
requests.post(url, headers=headers, data=payload)
# Send the POST request
response = requests.post(url, headers=headers, data=payload)

# Check if the redirection occurred by inspecting the final URL
if response.history:
    for resp in response.history:
        print(f"Redirected from {resp.url} with status code {resp.status_code}")
    print(f"Final destination: {response.url}")
else:
    print("No redirection occurred.")

# Print the response text
print(response.text)
