import os
from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin
from models.user import User
from playhouse.hybrid import hybrid_property

class IdolFanRelationships(BaseModel,UserMixin):
    idol = pw.ForeignKeyField(User, backref='fans')
    fan = pw.ForeignKeyField(User, backref='idols')


# example
# user = User.get_by_id(X)
# user.fans will return all the people that follows me (i.e. their idol_id)

# equivalent to:
# user = User.get_by_id(1)
# user.fans # same as
# IdolFanRelationships.select().where(IdolFanRelationships.idol_id == user.id)
