class Plane:
    BASE_SPEED = 750    
    def __init__(self, model_type: str, model_speed_coeficient: float, name_suffix: str,)-> None:
        self.model_type = model_type        
        self.model_speed_coeficient = model_speed_coeficient        
        self.name_suffix = name_suffix    
        
    def get_plane_name(self)-> str:
        return self.name_suffix + self.model_type    
    
    def get_plane_type(self)-> str:
        return self.model_type    
    
    def get_max_speed(self)-> float:
        return self.model_speed_coeficient * self.BASE_SPEED

class Boeing(Plane):
    NAME_SUFFIX = "B"    
    
    BOEING_TYPE_SPEED_COEF = {
        "737" : 1,
        "747" : 1.2,
        "757" : 1.35,
        "767" : 1.5,
        "777" : 1.8,
        }
    
    def __init__(self, model_type: str)-> None:
        self.model_type = model_type        
        speed_coef = self._get_type_speed_coef()
        super().__init__(model_type = model_type, name_suffix = self.NAME_SUFFIX, model_speed_coeficient= speed_coef)
    
    def _get_type_speed_coef(self)-> float:
        return self.BOEING_TYPE_SPEED_COEF.get(self.model_type)

my_plane = Boeing("747")
print(my_plane.get_plane_name())
print(f"Your plane speed is {my_plane.get_max_speed()} km/h")