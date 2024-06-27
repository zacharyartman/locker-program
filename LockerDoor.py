# File: LockerDoor.py
from LockerMagnet import LockerMagnet
from BasicComponent import BasicComponent

class LockerDoor(BasicComponent):
  def __init__ (self, width, height, upper_magnet: LockerMagnet, lower_magnet: LockerMagnet, id: str):
    super().__init__(id)
    self.width = width
    self.height = height
    self.upper_magnet = upper_magnet
    self.lower_magnet = lower_magnet
  
  def get_width(self):
    return self.width

  def get_height(self):
    return self.height
  
  def activate_upper_magnet(self):
    self.upper_magnet.activate_magnet()
  
  def deactivate_upper_magnet(self):
    self.upper_magnet.deactivate_magnet()
  
  def activate_lower_magnet(self):
    self.lower_magnet.activate_magnet()
  
  def deactivate_lower_magnet(self):
    self.lower_magnet.deactivate_magnet()
    
  def get_upper_magnet(self):
    return self.upper_magnet

  def get_lower_magnet(self):
    return self.lower_magnet
  
  def __str__(self) -> str:
    return f"Door Width: {self.width}.\t Door Height: {self.height}.\t Door ID: {self.get_id()}"
  
  def to_dict(self):
    return {
      'id': self.id,
      'width': self.width,
      'height': self.height,
      'upper_magnet': self.upper_magnet,
      'lower_magnet': self.lower_magnet
    }