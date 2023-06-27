import numpy as np

value_list={"a":"001","b":"002","c":"003","d":"004","e":"005","f":"006",
            "g":"007","h":"008","i":"009","j":"010","k":"011","l":"012",
            "m":"013","n":"014","o":"015","p":"016","q":"017","r":"018",
            "s":"019","t":"020","u":"021","v":"022","w":"023","x":"024",
            "y":"025","z":"026"}

key_list={0:" ",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",
          7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",
          13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",
          19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

s=input("text:")
l=[]
if len(s)>=9:
  for i in s:
    l.append(ord(i))
else:
  print(">9")

code=[]
for v in s.lower():
  code.append(value_list[v])

#sum of keys
keynum=str(int(code[2]))
keynum=str(int(keynum)+len(s))
#does not handle odd len values

mid=int(len(keynum)/2)

key_text=''
for ky in range(10):
  if ky==3:
    key_text+=keynum[:mid]
    continue
  elif ky==9:
    key_text+=keynum[mid:]
    continue
  elif ky==2:
    key_text+=key_list[int(code[-3])]
    continue
  else:
    rnm=np.random.randint(26)
    key_text+=key_list[rnm]
    continue
    
#temporary validaion without the knowledge of database
user_key=input("key: ")
user_key=user_key.upper()
try:
  numvald=int(user_key[3]+user_key[9])
  if numvald-len(s)==int(code[2]) and value_list[user_key[2].lower()]==code[-3]:
    print("valid")
  else:
    print("invalid")
except:
  print("Enter valid key credentials")
