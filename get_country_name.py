from tronapi import Tron
from tronapi import HttpProvider
import time as tt
import requests

full_node = HttpProvider('https://api.trongrid.io')
solidity_node = HttpProvider('https://api.trongrid.io')
event_server = HttpProvider('https://api.trongrid.io')
tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

default_address = input('The wallet address that want to airdrop from (your address, start with " T "): ')
private_key = input('Your address private key: ')

tron.default_address = str(default_address)
tron.private_key = str(private_key)




token_id = int(input('input the TRC10 token ID that you want to airdrop its holders (e.g: BTT = 100200 ): '))
add_to_show = input('input how many addresses you want to airdrop (min 1 / max 2000): ')
token_amount = int(input("token to be dropped for each address (note: check your token precision: if 6, then input 1000000 to airdrop 1 x token to each address): "))
url = f"https://tron-radar.de/api/hold/{token_id}.json"
response = requests.request("GET", url)
accounts = (response.json()['Holder'])


addrs = []
for x in accounts:

    address = (x['add'])
    addrs.append(address)


holders_list = addrs[:int(add_to_show)]


for adr in holders_list:
    print(f' \n airdropping {adr} \n')
    pay = tron.trx.send_token(str(tron.address.from_hex(adr).decode('ASCII')),
                              token_amount, token_id, default_address)

    print(pay)
    tt.sleep(0.45)


print(f'Successfully airdropped {len(holders_list)} TRX address')
