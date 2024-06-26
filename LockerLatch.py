from BasicComponent import BasicComponent

class LockerLatch(BasicComponent):
  def __init__(self, latched: bool, id: str):
    super().__init__(id)
    self.latched = latched
  
  def latch_door(self):
    self.latched = True
  
  def unlatch_door(self):
    self.latched = False
  
  def is_latched(self):
    return self.latched
  
  def __str__(self):
    return f"Latched: {self.is_latched()}.\t Latch ID: {self.get_id()}"
  
  def to_dict(self):
    return {
      'id': self.id,
      'latched': self.latched,
    }