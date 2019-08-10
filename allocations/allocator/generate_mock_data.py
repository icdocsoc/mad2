from random import randint

from models import Fresher, Interests, Student

import pandas as pd

from rstr import xeger


shortcode_pattern = "[a-z]{2}\d{1,2}19"


def rand_interest():
    return randint(0, 4)


df = pd.read_csv('MOCK_DATA.csv')

for _, row in df.iterrows():
    fresher = Fresher(
        student=Student(
            firstName=row['fname'],
            lastName=row['lname'],
            shortcode=xeger(shortcode_pattern)
        ),
        interests=Interests(
            alcohol=rand_interest(),
            clubbing=rand_interest(),
            anime=rand_interest(),
            sports=rand_interest(),
            cooking=rand_interest(),
            performingMusic=rand_interest(),
            kpop=rand_interest(),
            dance=rand_interest()
        )
    )
    fresher.save()