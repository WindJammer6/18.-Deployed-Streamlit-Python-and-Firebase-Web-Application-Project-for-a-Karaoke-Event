# 18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event
This project is a deployed, budget full stack website in Python with Streamlit (Python Framework) and Firebase (API)'s Realtime Database. The purpose of this project is to be used as a supporting technology project to support a Karaoke Event (titled SingUTD), organised by me and other members of the student committee of our school. It contains 2 Streamlit (Python Framework) Web Applications, which are connected to a Firebase (API)'s Realtime Database.

I described this project as a 'budget' full stack website as this website is built on top of existing frameworks, rather than from scratch (basic programming languages such as via HTML, CSS, JavaScript, SQL, etc.)

The purpose of this seperate repository is due to that the deployed 2 Streamlit (Python Framework) Web Applications is connected to this Github account, and hence this is the repository that the 2 Streamlit (Python Framework) Web Applications is connected to in this Github account. Deployment of Streamlit (Python Framework) Web Applications connected to Github apparently dosen't work if the files for deployment are within folders so I couldn't use the [17.-Projects-from-School](https://github.com/WindJammer6/17.-Projects-from-School) repository, which documented the creation of this project, to host the deployed Streamlit (Python Framework) Web Applications on Github. This repository acts as the 'code base' of the 2 deployed Streamlit (Python Framework) Web Applications in the Streamlit (Python Framework) cloud deployment platform (link: https://streamlit.io/cloud), where any changes in the code in this repository will directly affect the output, the 2 deployed Streamlit (Python Framework) Web Applications in the Streamlit (Python Framework) cloud deployment platform.

More information can be found in the [17.-Projects-from-School](https://github.com/WindJammer6/17.-Projects-from-School) repository in this Github account. 

*This project's deployed Streamlit (Python Framework)'s Web Applications and Firebase (API) links:*
+ https://8kbtr2cyktbh4qn2doay5g.streamlit.app/ (Karaoke Singer Registration Streamlit (Python Framework) Web Application)
+ https://2bgope7myic8tuh3dy6vi4.streamlit.app/ (Song queue display Streamlit (Python Framework) Web Application)
+ https://console.firebase.google.com/u/0/project/karaokeeventproject/database/karaokeeventproject-default-rtdb/data (Direct link to this project's Firebase (API) Realtime database, but only accessible by me through email)  

## Table of Contents
Here is a directory to explain the purpose of each file in this repository in the creation of the deployed, budget full stack website in Python with Streamlit (Python Framework) and Firebase (API)'s Realtime Database:
1. '.streamlit' folder  
   i. 'config.toml' file
2. 'README.md' file
3. 'firebase_key.json' file
4. 'karaoke_poster.jpg' file
5. 'karaoke_singer_class.py' file
6. 'queue_data_structure_class.py' file
7. 'register.py' file
8. 'requirements.txt' file
9. 'song_queue.py' file

<br>

**1. '.streamlit' folder**  
*i. config.toml' file*
```python
# This 'config.toml' file sets the custom theming of the Streamlit (Python) web applications. This file is created using ChatGPT.
[theme]
primaryColor = '#1a237e'  # Set your desired primary color
backgroundColor = '#121212'  # Set your desired background color
secondaryBackgroundColor = '#0d47a1'  # Set your desired secondary background color
textColor = '#ffffff'  # Set your desired text color
font = 'sans-serif'  # Set your desired font
```
This is an optional folder/file, in accordance to the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit), which allows you to set customised configurations or themings to the deployed Streamlit (Python Framework) Web Application.

I do not know how to use this 'config.toml' file very proficiently, so this file is created by ChatGPT to set the dark theming to my 2 deployed Streamlit (Python Framework) Web Applications.

<br>

<br>

**2. 'README.md' file**  
The 'README.md' file.

<br>

<br>

**3. 'firebase_key.json' file**
```python
{
  "type": "service_account",
  "project_id": "karaokeeventproject",
  "private_key_id": "502b60b589f5df059a8acda78671bd70693d099d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC8br45N0sc40eB\nzxRQz1huRCetv8TC31JnUapuFOD/dZo/3mzWDpZeg8bu4jS41x7d8j0zEa6Pwdcs\nYrHJBuMh8qpatQvilH3PvjLMSnVCW9Nk7R0ew/t3fRwfijQlsG4jaZT1EQIdmHrP\nChaKa+PyhxJAEvzsJYMuQLdiUOxzaHgjhROM5bpaLk41tQadtaY5HUXg4C5AaxS/\nJ6JpdKNLGEQ7DC/p7pvdBgpGz2ry7uU0dq69Gb5DloQOM2Ynds73WnidqTTWk2aM\nsjKiV0+tyzpf0Ok4sApXsPemKTnmdsGcYGkVasNB6S1q9U11i3TnP/989B9kL2mb\n6OfioWsxAgMBAAECggEAGXortBa6zCwatf1mtMpkHXyPlNlx5BtHy/ppvbqK9V9U\nPMB5HLQaNqtAkXn6QOetH7sp9Sa14HAIBNNPUGvi9+sUh3ElKzyCij0gJykGE7PQ\nsDuzDT7YWD6NN+J6zIG/UoBrCHuFOrUsHaQyigKublM+73Thx5gG1ZEgemWQosXI\nlLWa1VHqPvKFcPFpFhoCOsAfLFhBnqBYXem5x0fGC4EwXa6UjqLj/799ZdlLwHDJ\nbK6GZvHT7WJ+drvyXwFTlEVpSG8Kq1amoY0KGmYzZxM5mtxKalWzCwQt5995hz6f\nPwEDFTdGcyIADJJ5Hacy5YMVOV/6E3hTWkeJoLFSJQKBgQDx+7Tpr3D/qs73R+vs\nMn5vv7wowmaCLf3yXDLc0CAjRI15gbNFV8Ri1F2iU4xZQNi7JpEcaOC1uIRF1mNi\n1s6ZWi9J9KXvzsLM/CLnETTiFrKIWhQRGLUUtgc4FnMrSgCaQhbBwp9BQcCvGDkL\n9ZKkEd1jH5rnKku+1sq+NcmLAwKBgQDHWPNk+j0DAJc7UyrIGDXJnwOCoJYaARfK\no2EtsRdURu7B27qPTJVUuLQLdiU8k7T65Ca3sy4AN3MWvy6n2ULB6yUSAVJ0t86x\np1XIrfzKD6r6XLOXXOhJBKLRGLMZQERjzX8DGjd7WA81eSx55Ao/9I8NXyJJFdng\n1fbYZi2guwKBgG+SF6r7akVncv/O2HdSHLvXkqDUaUEyhXkei5EGIRtBu10/sPGS\n8wiCVB3JGdf5LzSzJosLzDfdOJeerrpewmkwjMczluLH2Ud8JXeWlmR8BJsbtU7g\nrnU7LH7u0vEtsLNvL2DtJFKJR5czuvHJq3AckI/ofZqCBOSb0mT7Fc8TAoGAAty/\nGesR5zIh+cMW8SqP0yZKWZzOqu7rFYjFA2/wgtBF61ipVBdoaYABbcyzeiwwxA10\nlNyow24IZAI4vEY9VCV5Mcn9Ehn1iM17SNdestQIw3GDTqAR4cKER/ZP1AP9N2Wi\n9jtxIn9AMKddwR5KG2L6jtmX127N4xGPasoEy7MCgYBRe1Q6lZC9mNktODoutH5Z\ncTPQC+FANB1nv/gzV65gKTnfIZacEoW/7lnpVqNJ2QllSKZCQpzHseNjqiUbbcWI\nWwHS8rxYDu9ui6sQRFwqFyGI/1Sxor5QFrLGPt2yvQGMQBt8pbjnUV5pitZlvaiN\ncjwn2PttAYre+rFUaDICVw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bto3h@karaokeeventproject.iam.gserviceaccount.com",
  "client_id": "106409655899062355465",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bto3h%40karaokeeventproject.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```
This file represents the authetication key. Apparently, when accessing to APIs (such as the Firebase API), you will need to have a sort of, authentication key, which is what this file is to ensure that only authorized users can access the API. Refer to this video to understand how the Firebase API authetication key is used with your Python code: https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 

<br>

<br>

**4. 'karaoke_poster.jpg' file**
<p align="center"> 
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/karaoke_poster.jpg"  width="450" height="200">
</p>
An image used for aesthetic purposes in the song registration Streamlit (Python Framework) Web Application.

<br>

<br>

**5. 'karaoke_singer_class.py' file**
```python
class KaraokeSinger:
    def __init__(self, name, song_choice, song_artist):
        self.name = name
        self.song_choice = song_choice
        self.song_artist = song_artist

    #Just want to be able to see the 'KaraokeSinger' object's attribute in the terminal when it is printed rather than
    #a 'KaraokeSinger' object
    def __repr__(self):
        return "KaraokeSinger('{}', '{}', '{}')".format(self.name, self.song_choice, self.song_artist)
    
    #Allows the 'KaraokeSinger' object to be recreated as a dictionary so it can be used to be reuploaded into the csv 
    #database in 'karaoke_singer_registration_streamlit.py' file
    def as_dict(self):
        return {'name': self.name, 'song_choice': self.song_choice, 'song_artist': self.song_artist}
```
A supporting OOP Python 'Karaoke Singer' class file used in building the project. 

<br>

<br>

**6. 'queue_data_structure_class.py' file**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def front_element(self):
        return self.buffer[-1]
    
    def last_element(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def __repr__(self):
        return '{}'.format(self.buffer)
```
A supporting OOP Python Queue Data Structure class file used in building the project, for the song queue Streamlit (Python Framework) Web Application.

<br>

<br>

**7. 'register.py' file**  
The main Python file for the song registration Streamlit (Python Framework) Web Application itself.

<br>

<br>

**8. 'requirements.txt' file**
```python
firebase_admin
streamlit_autorefresh
```
This is a compulsory file, in accordance to the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit), which allows you to tell Streamlit (Python Framework) to download the necessary external libraries/framework/packages specified in this 'requirements.txt' file in the deployment environment that is required for the deployment of the Streamlit (Python Framework) Web Application. 

Had quite the trouble during deployment of the Streamlit (Python Framework) Web Applications as the Streamlit deployment platform keep giving an error that it could not find the relevant external libraries/Framework/packages required to deploy my Streamlit (Python Framework) Web Applications until I found out in the  deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit) that apparently I needed this seperate 'requirements.txt' file in order to tell the Streamlit deployment platform to download the necessary external libraries/framework/packages during the deployment of the Streamlit (Python Framework) Web Applications.

Apparently,the 'requirements.txt' file is a common practice across various deployment platforms in Python, not just for Streamlit (Python Framework). Whether you are deploying your Streamlit app on platforms like Heroku, AWS, or others, specifying dependencies in a 'requirements.txt' file allows the platform to understand and install the necessary packages.

<br>

<br>

**9. 'song_queue.py' file**  
The main Python file for the song queue Streamlit (Python Framework) Web Application itself.



