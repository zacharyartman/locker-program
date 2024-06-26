from Apartment import Apartment
from Locker import Locker
from Package import Package
from Tenant import Tenant

def main():
  column = 'A'
  locker_A = Locker(3, 12, 80, column)
  print(locker_A)
  
  apt_1516 = Apartment("1516")
  zach = Tenant('Zach', apt_1516, 6096130439)
  apt_1516.add_tenant(zach)
  package = Package(2, apt_1516, '1Z092039423')
  package_B = Package(10, apt_1516, '1HF9023')

  locker_A.store_package(package)
  locker_A.store_package(package_B)
  print(locker_A)

  locker_A.pickup_packages(apt_1516)
  
main()
