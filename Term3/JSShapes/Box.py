class Box():
	def __init__(self,length,breadth,height):
		self.length = length
		self.breadth = breadth
		self.height = height
	def getVolume(self):
		self.volume = (length * breadth * height)
		return volume
	def getSurfaceArea(self):
		self.sArea = (2 * length * height) + (2 * length * breadth)
		return sArea
