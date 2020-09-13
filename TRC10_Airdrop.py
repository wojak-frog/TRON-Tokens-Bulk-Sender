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

print("\n\n\t\t\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n"
      "\t\t\t\t we suggest to use a seperated wallet to do the airdrop from, not your main/personal one\n
      keep some TRX in your wallet which will be consumed by the network for bandwidth"
      "\n\n\t\t\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n")



base58 = input("Your TRX address (which starts with ' T '): ")
pk = input("Your wallet's private key: ")
tron.private_key = pk 
tron.default_address = base58 


token_id = (input('input the TRC10 token ID that you want to airdrop its holders (e.g: BTT = 1002000 ): '))
decimals = int(input("Decimals of the token to be dropped: "))
trc10_drop = int(input("The ID of token to be dropped: "))
add_to_show = input('input how many addresses you want to airdrop (min 1 / max 2000): ')
token_amount = float(input("token to be dropped for each address: "))
token_amount = int(token_amount * (10**decimals))

print("\n-------------------------------------------------------\n")
confirmation = input(f"Your bulk package:\n"
                     f"Your want to airdrop {add_to_show} holder(s)  of {token_id} TRC10 token\n"
                     f"Each one will receive {token_amount / (10**decimals)} of {trc10_drop}"
                     f"\n\nTap CONFIRM to confirm this: ")
print("\n-------------------------------------------------------\n")

if confirmation != 'CONFIRM':
    exit()
else:
    print("\n\n[*] Collecting TRX addresses for the airdrop, please wait...\n")
    pass

url = f"https://tron-radar.de/api/hold/{token_id}.json"
response = requests.request("GET", url)
accounts = (response.json()['Holder'])


addrs = []
for x in accounts:

    address = (x['add'])
    addrs.append(address)


holders_list = addrs[:int(add_to_show)]
print(f"[*] Addresses collected:\n"
      f"{holders_list}\n"
      f"total: {len(holders_list)} address(es)\n\n")

tt.sleep(3)
for adr in holders_list:
    print(f' \n\n airdropping {adr} \n')
    pay = tron.trx.send_token(str(tron.address.from_hex(adr).decode('ASCII')),
                              token_amount, int(trc10_drop), base58)

    print(pay)
    tt.sleep(0.45)


print(f'\n **Successfully airdropped {len(holders_list)} TRX address **')
