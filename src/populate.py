import datetime

import argon2

from auth import Argon2
from models.user import User
from models.photo import Photo
from models.followers import FollowerRelation
from manage_db import (connect, create_tables)

connect()
create_tables()

passw = Argon2().generate_password_hash("test")

#yab = User.create(username="yab")
yab, created = User.get_or_create(username="test",
                                  defaults={
                                      'password':passw,
                                      'email':"test@gt.com",
                                      'confirmation_sent_at':datetime.datetime.now(),
                                      'last_sign_in_at':1
                                  })

lol = User.create(username="lol", password=passw, email="yab@g.com", confirmation_sent_at=datetime.datetime.now(),last_sign_in_at=1)
FollowerRelation.create(
    user = lol,
    follows = yab
)
"""
photos = (Photo.select().where(Photo.upload_date >= datetime.date.today()))

for photo in photos:
    print(photo)
    print(photo.json())

"""
