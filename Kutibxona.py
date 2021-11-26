Kitob={}
def Menu():
    try:
        return int(input("Menu\n1. Qidiruv\n2. Kitob joylash\nTanlov>>"))
    except:
        print("Tanlov xato qaytadan kiriting")
        Menu()
def Qidiruv():
    try:
        return int(input("Qidiruv\n1. Kitob nomi\n2. Kitob id\n3. Kitob muxarriri\nTanlov>>"))
    except:
        print("Tanlov xato qaytadan kiriting")
        Qidiruv()
class Kitob_Javon:
    def __init__(self,k_id,k_muxarrir,k_nomi):
        self.k_id=k_id
        self.k_muxarrir=k_muxarrir
        self.k_nomi=k_nomi
    def kitob_id(self):
        return self.k_id
    def kitob_m(self):
        return self.k_muxarrir
    def kitob_n(self):
        return self.k_nomi
    def qabul():
        return Kitob_Javon(input("Kitob nomi>>"),input("Kitob muxarriri >>"),int(input("Kitob id :")))
 
Kitob.update(input("Kitob nomi"):Kitob_Javon.qabul())
def _Qidiruv_():
    x=input("Kitob nomini>>") 
    if x in Kitob:
        print(x,Kitob_Javon.kitob_id(Kitob[x]),Kitob_Javon.kitob_m(Kitob[x]))
    else :
        print("Xato bunday kitob mavjud emas")

