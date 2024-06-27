from typing import Union
from Apartment import Apartment
from LockerDoor import LockerDoor
from LockerLatch import LockerLatch
from LockerMagnet import LockerMagnet
from LockerModule import LockerModule
from LockerShelf import LockerShelf
import math

from Package import Package

class Locker:
  def __init__(self, num_modules: float, locker_width: float, overall_height: float, col: str):
    self.num_modules = num_modules
    self.locker_width = locker_width
    self.overall_height = overall_height
    self.col = col
    self.modules = self.generate_lockers(num_modules, module_width=locker_width)
    
  def generate_lockers(self, num_modules: float, module_width: float) -> list[LockerModule]:
    module_height = self.get_module_height()
    list_of_locker_modules = []
    
    for i in range(num_modules):
      upper_magnet = LockerMagnet(False, self.generate_id(LockerMagnet, i, self.col, 'upper'))
      lower_magnet = LockerMagnet(False, self.generate_id(LockerMagnet, i, self.col, 'lower'))
      locker_door = LockerDoor(module_width, module_height, upper_magnet, lower_magnet, self.generate_id(LockerDoor, i, self.col))
      locker_latch = LockerLatch(True, self.generate_id(LockerLatch, i, self.col))
      locker_shelf = LockerShelf(True, self.generate_id(LockerShelf, i, self.col))
      locker_module = LockerModule(locker_door, locker_latch, locker_shelf, False, [], self.generate_id(LockerModule, i, self.col))
      list_of_locker_modules.append(locker_module)
    
    return list_of_locker_modules
  
  def get_module_height(self):
    return self.overall_height / self.num_modules
  
  def generate_id(self, type: Union[LockerModule, LockerShelf, LockerMagnet, LockerDoor, LockerLatch], row: int, col: str, magnet_location = 'None'):
    id_dict = {LockerMagnet: 'magnet', LockerModule: 'module', LockerShelf: 'shelf', LockerDoor: 'door', LockerLatch: 'latch'}
    return f"{id_dict[type]}_{col}_{row}_{magnet_location}"

  def modules_needed(self, package: Package) -> int:
    print(package.get_package_height(), type(self.get_module_height()))
    modules_needed = math.ceil(package.get_package_height() / self.get_module_height())
    print(f"{modules_needed} modules needed for package of height {package.get_package_height()}")
    return modules_needed
  
  def get_modules(self) -> list[LockerModule]:
    return self.modules
  
  def get_available_modules(self) -> list[LockerModule]:
    # returns list of locker module ids
    available_modules = []
    for module in self.get_modules():
      if not module.is_occupied():
        available_modules.append(module)
    
    return available_modules
      
    
  def find_consecutive_lockers(self, lst: list, x: int) -> list[LockerModule]:
    if len(lst) < x:
      return []
    
    for i in range(len(lst) - x + 1):
      if all(lst[i + j].get_row() == lst[i].get_row() + j for j in range(x)):
        return lst[i:i + x]
    return []

    
  def store_package(self, package: Package) -> bool:
    modules_needed = self.modules_needed(package)
    modules_to_use = self.find_consecutive_lockers(self.get_available_modules(), modules_needed)
    if modules_to_use == []:
      print("ERROR: NOT ENOUGH LOCKERS")
      return
    print(f"Using lockers: {modules_to_use}")
    self.occupy_locker(modules_to_use, modules_needed)
    package.set_package_location(modules_to_use)
    package.get_apartment_unit().add_package(package)

    modules_occupied: list[LockerModule] = package.get_package_location()
    for module in modules_occupied:
      module.add_package_to_module(package)

  def pickup_packages(self, apartment: Apartment):
    for package in apartment.get_packages():
      # open the lockers
      print(f'Apartment: {apartment}, package: {package}')

    
  def occupy_locker(self, modules_to_use: list[LockerModule], modules_needed: int):
    # When a locker is occupied, the following must happen.
    # The latches must open, the magnets must release
    # The bottom shelf must extend
    
    first_module = modules_to_use[0]
    first_module.occupy_locker()
    first_module.get_latch().unlatch_door()
    
    if modules_needed == 1:
        first_module.get_shelf().extend_shelf()
    else:
        last_module = modules_to_use[-1]
        last_module.occupy_locker()
        first_module.get_door().activate_lower_magnet()
        last_module.get_door().activate_upper_magnet()
        last_module.get_shelf().extend_shelf()
        last_module.get_latch().unlatch_door()
        
        for module in modules_to_use[1:-1]:
            module.occupy_locker()
            module.get_door().activate_lower_magnet()
            module.get_door().activate_upper_magnet()
            module.get_latch().unlatch_door()
    
  def __str__(self):
    string = f"Locker {self.col}"
    for module in self.modules:
      string += module.all_locker_str()
    return string
  
  def unoccupy_locker(self, modules_used: list[LockerModule]):    
    for module in modules_used:
      module.get_shelf().retract_shelf()
      module.get_door().deactivate_lower_magnet()
      module.get_door().deactivate_upper_magnet()
      module.get_latch().latch_door()
    
  def __str__(self):
    string = f"Locker {self.col}"
    for module in self.modules:
      string += module.all_locker_str()
    return string
  
  def to_dict(self):
    return {
      'id': self.id,
      'num_modules': self.num_modules,
      'locker_width': self.locker_width,
      'overall_height': self.overall_height,
      'col': self.col,
    }
