import json

class revisarJson():
    hol = 1
    def __init__(self):
        
        return None
    def isJson(self,myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True
