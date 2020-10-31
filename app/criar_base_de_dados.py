import dbm
import pickle

banco = dbm.open('smartphones', 'c')

smartphones = []

smartphone1 = {'nome': 'S20','marca': 'SAMSUNG','tela': '6.8','preco': '4000'}
smartphone2 = {'nome': 'A10','marca': 'SAMSUNG','tela': '5.5','preco': '1000'}
smartphone3 = {'nome': 'A51','marca': 'SAMSUNG' ,'tela': '6.7','preco': '1600'}
smartphone4 = {'nome': 'S20LITE','marca': 'SAMSUNG','tela': '6.8','preco': '2500'}
smartphone5 = {'nome': 'IPHONE12','marca': 'APPLE','tela':'6.8', 'preco': '11000'}
smartphone6 = {'nome': 'IPHONE11','marca': 'APPLE','tela':'6.7','preco': '7000'}
smartphone7 = {'nome': 'IPHONEX','marca': 'APPLE','tela': '5.5','preco': '4000'}
smartphone8 = {'nome': 'IPHONEXR','marca': 'APPLE','tela':'6.4','preco': '3500'}
smartphone9 = {'nome': 'MOTOG9','marca': 'MOTOROLA','tela':'6.6','preco': '1800'}
smartphone10 = {'nome': 'MOTOG8','marca': 'MOTOROLA','tela':'6.8','preco': '1200'}
smartphone11 = {'nome': 'MOTOG7'  ,'marca': 'MOTOROLA' ,'tela': '6.2' ,'preco': '1000'}

smartphones.append(smartphone1)
smartphones.append(smartphone2)
smartphones.append(smartphone3)
smartphones.append(smartphone4)
smartphones.append(smartphone5)
smartphones.append(smartphone6)
smartphones.append(smartphone7)
smartphones.append(smartphone8)
smartphones.append(smartphone9)
smartphones.append(smartphone10)
smartphones.append(smartphone11)

smart_str = banco['str'] = pickle.dumps(smartphones)

#smart_rec = pickle.loads(banco['str'])

        
banco.close()