from tabulate import tabulate

d = {1:{"Naam":"Bjorn","Woonplaats":"Bilzen"},2:{"Naam":"Frans","Woonplaats":"Hasselt"}
      ,3:{"Naam":"Evelien","Woonplaats":"Bilzen"},4:{"Naam":"Peter","Woonplaats":"Hasselt"},
         5:{"Naam":"Sofie","Woonplaats":"Bilzen"}}

filter_dic ={}
filter_rec ={}
teller = 0
for x in d.values():

    if(x["Woonplaats"]=="Hasselt"):
        teller = teller + 1
        filter_rec.update({teller:{"Naam":x["Naam"],"Woonplaats":x["Woonplaats"]}})
        filter_dic.update(filter_rec)
        
print(tabulate(filter_dic.values()))
