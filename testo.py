import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("fairbas nik.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://nik10-73dfe-default-rtdb.firebaseio.com/'})

ref = db.reference("/5mo/")


def sayHi(a):
    if a.data == 'Е':
        print(ref.get())
        ref.update({'dk': 'MLS'})


ref.listen(sayHi)
