class Apartment:
  def __init__(self, apartment_number: str):
    self.apartment_number = apartment_number
    self.packages = []
    self.tenants = []

  def add_package(self, package):
    self.packages.append(package)

  def get_packages(self):
    return self.packages
  
  def add_tenant(self, tenant):
    self.tenants.append(tenant)

  def remove_tennant(self, tenant):
    self.tenants.remove(tenant)

  def get_tenants(self):
    return self.tenants
  
  def __str__(self) -> str:
    return f'Apartment #: {self.apartment_number}'

