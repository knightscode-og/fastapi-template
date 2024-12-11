from odmantic import ObjectId, Model

class Item(Model):
    name: str
    description: str
    effect: str
    owner_id: ObjectId
