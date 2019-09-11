import random
KREWES=dict()
KREWES['orpheus']=['Emily', 'Kevin','Vishwaa','Erick','ray','Jesse','Tiffany','Amanda',
                   'Junhee','Jackie','Tyler','Emory','Ivan','Elizabeth','Pratham','Shaw',
                    'Yaru','Kelvin','Tanzim']
KREWES['rex']=['William','Joseph','Calvin','Ethan','Moody','Mo','Alex','David','Hannah','Alex','Jiangho','Devin']
KREWES['endymilon']=['Grace','Nahi','Derek','Manfred','Leila','Ahmed','Wilson','Connor','Brandon','Jackson']
# to see the size of the list:print 'first list:'+str (len(KREWES['orpheus']))
#print 'second list:'+str (len(KREWES['rex']))
#print 'third list:'+str (len(KREWES['endymilon']))

def chooseStudent():
    x=random.randint(1,3)
    if x==1:
        print KREWES['orpheus'][random.randint(0,18)]
    elif x==2:
        print KREWES['rex'][random.randint(0,11)]
    else:
        print KREWES['endymilon'][random.randint(0,9)]
chooseStudent()
