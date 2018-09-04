import binascii,struct,zlib
from struct import *

class MyPNG:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pix = []

    for h in range(height):
      self.pix.append([1] * width)

  def save(self, filepath):
    self.open(filepath)

    self.write_png_header()
    self.write_ihdr_chunk()
    self.write_idat_chunk()
    self.write_iend_chunk()
    self.close()


  def open(self, filepath):
    self.f = open(filepath, 'wb')

  def close(self):
    self.f.close()

  def write_png_header(self):
    self.write((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))

  def write_ihdr_chunk(self):
    self.write((0x00, 0x00, 0x00, 0x0D))

    datas = []

    datas.extend((0x49, 0x48, 0x44, 0x52))
    datas.extend(unpack('BBBB', pack('>L', self.width)))
    datas.extend(unpack('BBBB', pack('>L', self.height)))

    datas.extend((0x01, 0x00, 0x00, 0x00, 0x00))

    self.write(datas)
    self.write(self.crc32(datas))

  def write_idat_chunk(self):
    datas = []
    for y in range(self.height):
      line = ""
      datas.append(0)
      for x in range(self.width):
        line += str(self.pix[y][x])
        if len(line) == 8:
          datas.append(int(line, 2))
          line = ""

      if line != "":
        line += "0" * (8 - len(line))
        datas.append(int(line, 2))

    target = ""
    for d in datas:
      target += chr(d)

    lines = zlib.compress(target.encode())
    datas = []
    for l in lines:
      datas.append(l)

    self.write(unpack('BBBB', pack('>L', len(datas))))
    datas.insert(0, 0x49)
    datas.insert(1, 0x44)
    datas.insert(2, 0x41)
    datas.insert(3, 0x54)

    datas.extend(self.crc32(datas))
    self.write(datas)

  def write_iend_chunk(self):
    self.write((0x00, 0x00, 0x00, 0x00))
    self.write((0x49, 0x45, 0x4E, 0x44))  
    data = [0x49, 0x45, 0x4E, 0x44]
    self.write(self.crc32(data))

  def write(self, values):
    for v in values:
      self.f.write(pack('B', v))

  def crc32(self, datas):
    target = ""
    for d in datas:
      target += chr(d)

    crc = binascii.crc32(target.encode())
    return unpack('BBBB', pack(">L", crc))

if __name__ == '__main__':
  png = MyPNG(width=200, height = 50)
  png.save('test.png')
  print(type(MyPNG.crc32(MyPNG, (0x49, 0x45, 0x4E, 0x44))))
