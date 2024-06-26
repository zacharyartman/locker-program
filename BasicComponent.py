class BasicComponent:
  def __init__(self, id: str):
    self.id = id
  
  def get_id(self):
    return self.id
  
  def get_location(self):
    # returns col, row
    return self.id.split('_')[1], int(self.id.split('_')[2])
  
  def get_row(self):
    return int(self.id.split('_')[2])
  
  def get_col(self):
    return self.id.split('_')[1]