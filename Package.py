from Apartment import Apartment
from LockerModule import LockerModule


class Package:
  def __init__(self, package_height: float, apartment_unit: Apartment, tracking_number = 'Missing', package_location=[]):
    self.package_height = package_height
    self.package_location = package_location
    self.apartment_unit = apartment_unit
    self.tracking_number = tracking_number
  
  def get_package_height(self):
    return float(self.package_height)

  def set_package_location(self, package_location: list[LockerModule]):
    self.package_location = package_location
  
  def get_package_location(self) -> list[LockerModule]:
    return self.package_location
  
  def get_apartment_unit(self):
    return self.apartment_unit
  
  def get_tracking_number(self):
    return self.tracking_number

  def set_tracking_number(self, tracking_number):
    self.tracking_number = tracking_number
  
  def __str__(self) -> str:
    return f"Tracking Number: {self.get_tracking_number()}. {self.get_apartment_unit()}. Package Height {self.get_package_height()}"