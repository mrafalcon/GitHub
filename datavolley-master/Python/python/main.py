from tabulate import tabulate
import load

global dvwGame 

load.init()
load.importFile("datavolley-master/Games/&crm23.po.sem5-8.1 BEL-ASK3-2.dvw")
dvwGame = load.dvwGame



#head = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
 
#print(tabulate(load.set1[4:10], headers=head, tablefmt="grid"))
print(tabulate(dvwGame[5][4:-1]))