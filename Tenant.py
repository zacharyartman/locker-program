from Apartment import Apartment

class Tenant:
  def __init__(self, name: str, apartment: Apartment, phone_number: int):
    self.name = name
    self.apartment = apartment
    self.phone_number = phone_number
  
  def notify_tenant(self):
    print(f"TENANT {self.name} HAS NEW PACKAGE")