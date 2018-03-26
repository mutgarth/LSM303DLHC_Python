import smbus

class acc_LSM303DLHC(object):

	def __init__(self, slave_address):
		self.bus = SMBbus(1)
		self.acc_address = slave_address
		self.bus.write_byte_data(self.slave_address, 0x20, 0x27)
		self.bus.write_byte_data(self.slave_address, 0x23, 0x00)

	def __del__(self):
		del(self.bus)

	def get_x_acc():
		msb = bus.read_byte_data(acc_address,0x29)
		lsb = bus.read_byte_data(acc_address,0x28)
		x_acc = msb*256 + lsb
		if x_acc > 32767:
			x_acc -= 65536
		return x_acc	

	def get_y_acc():
		msb = bus.read_byte_data(acc_address,0x2a)
		lsb = bus.read_byte_data(acc_address,0x2b)
		z_acc = msb*256 + lsb
		if z_acc > 32767:
			y_acc -= 65536
		return y_acc

	def get_z_acc():
		msb = bus.read_byte_data(acc_address,0x2c)
		lsb = bus.read_byte_data(acc_address,0x2d)
		z_acc = msb*256 + lsb
		if z_acc > 32767:
			z_acc -= 65536
		return z_acc

	def get_acc_data():
		acc_data = [x_acc, y_acc, z_acc]
		return acc_data
