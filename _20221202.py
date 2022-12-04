import requests
import json


with open('_20221202_horses.txt') as file:
    url_list = [line.strip() for line in file.readlines()]

horses_count = len(url_list)
print(f'HORSES: {horses_count}')

cou_ = 0

headers = {
    'authority': 'data.nrha.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'content-type': 'text/plain',
    'origin': 'https://reinersuite.nrha.com',
    'referer': 'https://reinersuite.nrha.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

data = '{"username":"adgoldtx@gmail.com","password":"W@y!@ndDr1"}'

with requests.Session() as session:

    response = requests.post('https://data.nrha.com/api/app/rs/auth/login', headers=headers, data=data)

    # print(response.json())
    #
    tok__ = json.loads(response.text)
    tok_ = tok__['access']
    # print(tok_)

    for u_ in url_list:
        cou_ += 1

        print(f'HORSE {cou_}/{horses_count}:  {u_}')

        # 'authorization': f'{tok_}',

        headers = {
            'authority': 'data.nrha.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
            'authorization': f'Bearer {tok_}',
            'content-type': 'application/json',
            'origin': 'https://reinersuite.nrha.com',
            'referer': 'https://reinersuite.nrha.com/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        params = {
            'actions': 'false',
        }

        json_data = {
            'name': f'{u_}',
            'birthDate': None,
            'sireId': None,
            'damId': None,
            'damName': '',
            'sireName': '',
            'horseSexId': '',
            'breedRegistrationNumber': '',
            'competitionLicenseNumber': '',
            'partialMatch': False,
            'birthYear': None,
            'nominatorName': '',
            'ownerName': '',
        }

        response = requests.post('https://data.nrha.com/api/app/rs/horses/search', params=params, headers=headers,
                          json=json_data)

        aaa = json.loads(response.text)
        id_ = aaa[0]['id']

        with open(f'{u_}___1.json', 'w', encoding='utf-8') as file:
            json.dump(aaa, file, indent=4, ensure_ascii=False)

        params = {
            'breeds': 'true',
            'earnings': 'true',
            'leases': 'true',
            'nominations': 'true',
            'owners': 'true',
        }

        response = requests.get(f'https://data.nrha.com/api/app/rs/horses/{id_}/info-panel', params=params, headers=headers)
        bbb = json.loads(response.text)

        with open(f'{u_}___2.json', 'w', encoding='utf-8') as file:
            json.dump(bbb, file, indent=4, ensure_ascii=False)
