from BasicComponent import BasicComponent

class LockerMagnet(BasicComponent):
  def __init__(self, active: bool, id: str):
    super().__init__(id)
    self.active = active
  
  def deactivate_magnet(self):
    self.active = False
  
  def activate_magnet(self):
    self.active = True
    
  def get_magnet_status(self):
    return self.active
  
  def __str__(self) -> str:
    return f"Magnet Active: {self.get_magnet_status()}\tMagnet ID: {self.get_id()}"
  
  def to_dict(self):
    return {
      'id': self.id,
      'active': self.active,
    }