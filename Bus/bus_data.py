#import pandas as pd
import pyrebase
#dataset=pd.read_excel('bus_list.xlsx')
class Data_set:
    data={'Tiruchirapalli': {'Chennai': {'name': ['NorthLay', 'Tiger ', 'Circum', 'Cube', 'Hippie'], 'fare': [200, 450, 300, 450, 450], 's_point': ['Central Bus Stand', 'Mannarpuram', 'Central Bus Stand', 'Central Bus Stand', 'Mannarpuram'], 'e_point': ['Koyambedu', 'Arumpakkam', 'Guindy', 'Guindy', 'Tambaram'], 'bus_type': ['Ac', 'Ac', 'Nc', 'Ac', 'Nc']}}, 'Velankanni': {'Chennai': {'name': ['Amity', 'Fastmove', 'Mega', 'UniRide', 'Master', 'Lion'], 'fare': [300, 500, 350, 200, 550, 400], 's_point': ['Annai Maria', 'Bus stand velankanni', 'RMT office', 'Velankanni', 'Annai Maria', 'RMT office'], 'e_point': ['Tambaram', 'Guindy', 'Koyambedu', 'Tambaram', 'Koyambedu', 'Guindy'], 'bus_type': ['Nc', 'Nc', 'Nc', 'Ac', 'Ac', 'Ac']}}, 'Chennai ': {'Salem': {'name': ['Calm', 'Lava', 'Yellow', 'Fun', 'Bus4U'], 'fare': [500, 700, 350, 600, 750], 's_point': ['Salem new bus stand', 'Kondaalampatti', 'Koyambedu', 'Tambaram', 'Tambaram'], 'e_point': ['Koyambedu', 'Tambaram', 'New bus stand', 'New bus stand', 'Salem new bus stand'], 'bus_type': ['Nc', 'Nc', 'Ac', 'Nc', 'Ac']}}, 'Chennai': {'Kumbakonam': {'name': ['Solid', 'Instant', 'Angel', 'Big', 'Pop'], 'fare': [600, 550, 800, 450, 400], 's_point': ['Koyambedu', 'Guindy', 'Koyambedu', 'Tambaram', 'Tambaram'], 'e_point': ['Kumbakonam Bus stand', 'Kumbakonam Bus stand', 'Rathimeena office', 'Kumbakonam Bus stand', 'Kumbakonam Bus stand'], 'bus_type': ['Ac', 'Nc', 'Ac', 'Nc', 'Nc']}, 'Hosur': {'name': ['Fast', 'Rainbow', 'Bold', 'Blue', 'Break Away'], 'fare': [500, 800, 689, 650, 520], 's_point': ['Koyambedu', 'Tambaram', 'Tambaram', 'Koyambedu', 'Koyambedu'], 'e_point': ['Hosur bus stand', 'Hosur bus stand', 'Hosur bus stand', 'Hosur bus stand', 'Hosur bus stand'], 'bus_type': ['Nc', 'Nc', 'Nc', 'Nc', 'Ac']}}, 'Madurai': {'Chennai': {'name': ['Go'], 'fare': [650], 's_point': ['Maatuthaavani'], 'e_point': ['Koyambedu'], 'bus_type': ['Nc']}}, 'Mattuthavani': {'Koyambedu': {'name': ['Magic ', 'Ace', 'Shaker', 'Mini', 'A2Z'], 'fare': [400, 200, 700, 650, 351], 's_point': ['Maatuthaavani', 'Maatuthaavani', 'Maatuthaavani', 'Maatuthaavani', 'Maatuthaavani'], 'e_point': ['Koyambedu', 'Koyambedu', 'Koyambedu', 'Koyambedu', 'Koyambedu'], 'bus_type': ['Ac', 'Nc', 'Ac', 'Nc', 'Ac']}}, 'Coimbatore': {'Tenkasi': {'name': ['Rapid', 'Sundhara'], 'fare': [300, 420], 's_point': ['Gandhipuram', 'singanallur'], 'e_point': ['Tenkasi', 'Tenkasi Bus stand'], 'bus_type': ['Ac', 'Nc']}, 'Chennai': {'name': ['Safe', 'Abacus', 'Amazing', 'Dance Fever'], 'fare': [600, 350, 325, 140], 's_point': ['singanallur', 'Gandhipuram', 'singanallur', 'Gandhipuram'], 'e_point': ['Koyambedu', 'Guindy', 'Koyambedu', 'Koyambedu'], 'bus_type': ['Ac', 'Ac', 'Ac', 'Nc']}}}
"""
for froms in dataset["Froms"]:
    data[froms]={}
for froms,to in zip(dataset["Froms"],dataset["To"]):
    if(froms in data):
        data[froms][to]={}
for froms,to in zip(dataset["Froms"],dataset["To"]):
    if(froms in data):
        try:
            data[froms][to]['name']=list()
            data[froms][to]['fare']=list()
            data[froms][to]['s_point']=list()
            data[froms][to]['e_point']=list()
            data[froms][to]['bus_type']=list()
        except:
            pass
for froms,to,name,fare,s_point,e_point,bus_type in zip(dataset["Froms"],dataset["To"],dataset["Name"],dataset["Fare"],dataset["Starting point"],dataset["End point"],dataset["Bus type"]):
    #print(froms,to,name,fare,s_point,e_point)
    
    data[froms][to]['name'].append(name)
    data[froms][to]['fare'].append(fare)
    data[froms][to]['s_point'].append(s_point)
    data[froms][to]['e_point'].append(e_point)
    data[froms][to]['bus_type'].append(bus_type)
    
print(data)

firebaseConfig = {
        "apiKey": "AIzaSyAEzl4aWGVQnTb4Sk9pMNRhzNCxe3MFAmw",

        "authDomain": "sece-hackathon-390a0.firebaseapp.com",

        "projectId": "sece-hackathon-390a0",

        "storageBucket": "sece-hackathon-390a0.appspot.com",

        "databaseURL":"https://sece-hackathon-390a0-default-rtdb.firebaseio.com/",

        "messagingSenderId": "772188818031",

        "appId": "1:772188818031:web:1d02b48b391ce1602b9b9a",

        "measurementId": "G-Y5YXYRMD9M"

    }
firebase=pyrebase.initialize_app(firebaseConfig)

storage=firebase.storage()
try:
        storage.child('diwali.jpg').put('diwali.jpg')
except:
        print("hii")
"""