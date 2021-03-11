import random


rare =      ["", "dobry", "doskonały"]
prefix =    ["zwinny", "szybki", "demoniczny", "Runiczny"]
type_item = ["maczuga", "nóż", "sztylet", "Długi Łuk"] 
sufix =     ["klanu", "doskonałości", "trafienia"]

def lotto():
    return (random.sample(rare,k=1)+random.sample(prefix,k=1)+random.sample(type_item,k=1)+random.sample(sufix,k=1))

  

print(*lotto())