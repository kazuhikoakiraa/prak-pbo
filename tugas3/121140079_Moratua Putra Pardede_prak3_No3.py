class Oyo:
  __list = [] #merupakan atribut private, cmn bisa diakses oyo

  def __init__(self,nama,hp,umur,room):
    self.__nama = nama #atribut private
    self._hp = hp #atribut protected
    self.umur = umur #atribut public
    self._room = room #sama seperti hp, atribut protected
    Oyo.__list.append(self.__nama) #bisa diakses method walaupun private


  def _upgrade_room(self,up):
    self._room = up

  def cust(self):
    print("Nama  : ", self.__nama)
    print("Nomor HP : ", self._hp)
    print("Umur  : ", self.umur)
    print("Room  : ", self._room)

cust1 = Oyo("Balthazar","085812356789",14,"Gryfindor")
cust2 = Oyo("Barbie","1223344556789",54,"Disney")
cust3 = Oyo("Kaori","089867563214",10,"Graveyard")

cust1.cust()
print()
cust2._upgrade_room("Hollywood")
cust2.cust()
print()
cust3.cust()
print()
#print(cust1.__nama) nama termasuk atribut private pada program oyo ini
  