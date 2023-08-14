from models import Playground
from models.playground import Location


def create_db():
    ust_campus = Location.objects(name="UST Campus").modify(
        co_ordinates=[12, 3], upsert=True, new=True
    )
    ust_bhavani = Location.objects(name="UST Bhavani").modify(
        co_ordinates=[12, 3], upsert=True, new=True
    )

    Playground.objects(playground_id=1).modify(
        name="Basketball 1", location_id=ust_campus, availability=True, upsert=True
    )
    Playground.objects(playground_id=2).modify(
        name="Basketball 2", location_id=ust_campus, availability=True, upsert=True
    )
    Playground.objects(playground_id=3).modify(
        name="Cricket 1", location_id=ust_campus, availability=True, upsert=True
    )
    Playground.objects(playground_id=4).modify(
        name="Football 1", location_id=ust_bhavani, availability=True, upsert=True
    )
