from tabulate import tabulate
import load

load.init()
load.importFile("datavolley-master/Python/data/","testing_truncated.dvw")


head = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
 
#print(tabulate(load.set1[4:10], headers=head, tablefmt="grid"))
print(tabulate(load.set1[4:-1]))