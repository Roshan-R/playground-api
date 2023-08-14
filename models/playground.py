from mongoengine import (
    Document,
    StringField,
    BooleanField,
    PointField,
    ReferenceField,
    IntField,
)


class Location(Document):
    name = StringField(required=True, unique=True)
    co_ordinates = PointField()


class Playground(Document):
    playground_id = IntField(required=True, unique=True)
    name = StringField()
    location_id = ReferenceField(Location)
    availability = BooleanField()
