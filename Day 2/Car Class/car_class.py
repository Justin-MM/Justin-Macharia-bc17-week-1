class Car(object):

  
  def __init__(self, name="General", model="GM", vehicle_type="saloon"):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type

    num_of_doors = 4
    if self.name == "Porshe" or self.name == "Koenigsegg":
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    speed = 0
    self.speed = 0
    if self.vehicle_type == 'trailer':
      if self.speed <= 0:
        self.speed = 0
      else:
        self.speed = 77
    elif self.name == 'Mercedes':
      if self.speed <= 0:
        self.speed = 0
      else:
        self.speed = 1000

    num_of_wheels = 4
    if self.vehicle_type == "trailer":
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4

  def is_saloon(self):
    if self.vehicle_type == "trailer":
      return False
    else:
      return True

  def drive(self, the_speed):
    self.the_speed = the_speed
    if self.vehicle_type == 'trailer':
      if the_speed == 0:
        self.speed = 0
        return self
      elif the_speed > 0:
        self.speed = 77
        return self

    elif self.name == 'Mercedes':
      if the_speed == 0:
        self.speed = 0
        return self
      elif the_speed > 0:
        self.speed = 1000
        return self

__author__ = 'Justin M'
