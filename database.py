import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAlUWRF3ISCOGlB2KLftbKO7-1e1x2atuU",
    "authDomain": "py-auth-2eff3.firebaseapp.com",
    "databaseURL": "https://py-auth-2eff3-default-rtdb.firebaseio.com",
    "projectId": "py-auth-2eff3",
    "storageBucket": "py-auth-2eff3.appspot.com",
    "messagingSenderId": "8507796776",
    "appId": "1:8507796776:web:173400486f1e9e4ac8b41d",
    "measurementId": "G-V9KH2XTHVQ",
}

firebase = pyrebase.initialize_app(firebaseConfig)
