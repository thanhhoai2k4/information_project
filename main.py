from tools.loadData import LoadDdata
from tools.Radix_Trees import RadixNode
import 

def init_Form():

    path =  r"E:\github\information_project\datasets\data.txt"
    dataset = LoadDdata(path).data
    root = RadixNode()
    root.insert_many(dataset)
    return root



