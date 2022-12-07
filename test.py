from copy import deepcopy


class TreeStore:
    def __init__(self, objects: list[dict]) -> None:
        self.array = deepcopy(objects)
        self.map = dict()
        self.children = dict()
        for obj in objects:
            self.map[obj["id"]] = obj
            if obj["parent"] not in self.children:
                self.children[obj["parent"]] = []
            self.children[obj["parent"]].append(obj)
            if obj["id"] not in self.children:
                self.children[obj["id"]] = []

    def getAll(self):
        return self.array

    def getItem(self, idx):
        return self.map[idx]

    def getChildren(self, idx):
        return self.children[idx]

    def getAllParents(self, idx):
        res = []
        obj = self.map[idx]
        while obj["parent"] in self.map:
            res.append(self.map[obj["parent"]])
            obj = self.map[obj["parent"]]
        return res


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]

ts = TreeStore(items)

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]

print(ts.getChildren(4))
