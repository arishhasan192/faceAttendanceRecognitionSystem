import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://faceattendacerealtime-29122-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654" :
        {
            "name" : "Ahmar Hasan Arish",
            "major" : "computer science",
            "starting year" : 2020,
            "total_attendance" : 6,
            "standing":"G",
            "year":4,
            "last_attendance_time" : "2024-12-12 00:54:34"

        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Polity",
            "starting year": 2014,
            "total_attendance": 16,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2024-12-12 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "computer science",
            "starting year": 2014,
            "total_attendance": 3,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-12 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)











