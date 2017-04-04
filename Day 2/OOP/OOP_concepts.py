
class Cups (object):
  def __init__ (self, color, size, make):
    self.color = color
    self.size = size
    self.make = make

# class Mugs inherits from Cups
class Mugs (Cups):

  def __init__ (self, color, size, make):
    super (Mugs, self).__init__(color, size, make)

  def purchase_mug(self, make):
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
      return "Color is available"



inventory = Cups ('Black', "Big", 'new')
purchase_Mug = Mugs ('black', "Big", 'China Mugs')


print (purchase_Mug.purchase_mug("China Mug"))

__author__ = 'Justin M'
