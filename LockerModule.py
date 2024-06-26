from LockerDoor import LockerDoor
from LockerLatch import LockerLatch
from LockerShelf import LockerShelf
from BasicComponent import BasicComponent

class LockerModule(BasicComponent):
  def __init__(self, door: LockerDoor, latch: LockerLatch, shelf: LockerShelf, occupied: bool, group: list, id: str):
    super().__init__(id)
    self.door = door
    self.latch = latch
    self.shelf = shelf
    self.occupied = occupied
    self.group = group
    self.module_contents = []

  def is_occupied(self):
    return self.occupied

  def occupy_locker(self):
    self.occupied = True
  
  def open_module(self):
    self.latch.unlatch_door()
    
  def get_door(self):
    return self.door
  
  def get_latch(self):
    return self.latch

  def get_shelf(self):
    return self.shelf
  
  def get_upper_magnet(self):
    return self.door.get_upper_magnet()

  def get_lower_magnet(self):
    return self.door.get_lower_magnet()
  
  def all_locker_str(self):
    col, row = self.get_location()
    string = f"\nLocker {col} Module {row}: \n\tComponent: Latch.\t{self.get_latch()}\n\tComponent: Door.\t{self.get_door()}\n\tComponent: Upper Magnet.\t {self.get_door().get_upper_magnet()}\n\tComponent: Lower Magnet.\t {self.get_door().get_lower_magnet()}\n\tComponent: Shelf.\t {self.get_shelf()}\n\tComponent: Module.\t {self.__str__()}"
    return string
  
  def add_package_to_module(self, package):
    self.module_contents.append(package)

  def remove_package_to_module(self, package):
    self.module_contents.remove(package)
  
  def get_module_contents(self):
    return self.module_contents
  
  def __str__(self) -> str:
    return f"Module Occupied: {self.is_occupied()}.\tModule Contents: {[str(package) for package in self.get_module_contents()]}.\tModule ID: {self.get_id()}"
