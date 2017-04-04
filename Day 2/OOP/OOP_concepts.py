# OOP concepts used include inheritance , Polymorphism and encapsulation
class Cups (object):
  def __init__ (self, color, size, make):
    self.color = color
    self.size = size
    self.make = make

  def purchase_cup(self, make):
    if self.make == 'Tea cup':
      return "Price is 50 Kenya Shillings"
    elif self.make == 'Porcelain':
      return "Price is 70 Kenya Shillings"
    else:
      return "Out of stock!"

      # protected function that cannot be accessed outside of the class
  def __source_info(self, source):
    if self.source == "China":
        return "GangZhou Industries"
    else:
        return "That is a royalty free item"

# class Mugs inherits from Cups
class Mugs (Cups):

  def __init__ (self, color, size, make):
    super (Mugs, self).__init__(color, size, make)

    # polymorphic function with varying implementation from the above Cup class
  def purchase_cup(self, make):
    if self.make == 'China Mugs':
      return "Price is 250 Kenya Shillings"
    elif self.make == 'Porcelain':
      return "Price is 200 Kenya Shillings"
    else:
      return "Out of stock!"

  def sizes_available(self, size):
    if self.size == "small":
      return "Out of stock"
    elif self.size == "Big":
      return "Mugs are available"
    else:
      return "Medium sizes coming soon"

  def mug_colors (self, color):
    colors_available = ["red", "black", "white"]
    if self.color not in colors_available:
      return "Invalid color"
    else:
      return " That Color is available"



inventory = Cups ('Black', "Big", 'new')
purchase_Mug = Mugs ('black', "Big", 'China Mugs')


print (purchase_Mug.purchase_cup("China Mug"))

__author__ = 'Justin M'
