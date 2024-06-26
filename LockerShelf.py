from BasicComponent import BasicComponent

class LockerShelf(BasicComponent):
  def __init__(self, retracted: bool, id: str):
    super().__init__(id)
    self.retracted = retracted
  
  def retract_shelf(self):
    self.retracted = True
  
  def extend_shelf(self):
    self.retracted = False
  
  def get_shelf_retracted_status(self):
    return self.retracted
  
  def __str__(self) -> str:
    return f"Shelf Retracted: {self.get_shelf_retracted_status()}\tShelf ID: {self.get_id()}"