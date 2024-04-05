import threading

import bitcoin as bitcoin


def file_to_list():
    with open('btc.txt', 'r') as f:
        data = f.readlines()
    list = []

    for n in data:
        new = n.replace('\n', '')
        list.append(new)
    return list

def run():
    list = file_to_list()
    i=0
    print("Start searching")
    while True:

        private_key = bitcoin.random_key()
        decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
        wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
        public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
        address = bitcoin.pubkey_to_address(public_key)


        i+=1
        if i%10000==0:
            print(i)

        if address in list:
            print(list.index(address)+1)
            with open('winwin.txt', 'a+') as w:
                w.write(f'{address} ---  {wif_encoded_private_key} \n')
            print(wif_encoded_private_key)
            print(address)




if __name__ == '__main__':
    thread1 = threading.Thread(target=run)
    thread2 = threading.Thread(target=run)
    thread3 = threading.Thread(target=run)
    thread4 = threading.Thread(target=run)
    # list  = file_to_list()
    # run(list)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

