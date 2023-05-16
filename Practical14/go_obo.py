from xml.dom.minidom import parse
import xml.dom.minidom
import re

DOMTree = xml.dom.minidom.parse("go_obo.xml")
obo = DOMTree.documentElement
terms = obo.getElementsByTagName("term")

# ls1 stores id, ls2 stores name ,ls3 stores definition, ls4 stores childnodes.
ls1 = []
ls2 = []
ls3 = []
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    name = term.getElementsByTagName('name')[0].childNodes[0].data
    if len(re.findall('autophagosome',defstr))>=1:
            ls1.append(id)
            ls2.append(name)
            ls3.append(defstr)

# use dic1 to caculate the number of childnodes.
dic1 = {}
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    is_a_list = []
    for i in term.getElementsByTagName('is_a'):
        is_a_list.append(i.childNodes[0].data)
    for is_a in is_a_list:
        if is_a in dic1:
            dic1[is_a].append(id)
        else:
            dic1[is_a] = [id]
def calculate(list0):
    for i in list0:
        if i in list0:
            if i not in list1:
                list1.append(i)
                if i in dic1:
                    calculate(dic1[i])
    return len(list1)

ls4 = []
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    if len(re.findall('autophagosome', defstr)) >= 1:
        nodes = 0
        list1 = []
        if id in dic1:
            nodes = calculate(dic1[id])
        ls4.append(nodes)

from pandas import DataFrame
data = {'id': ls1, 'name': ls2, 'definition': ls3, 'childnodes': ls4}
df = DataFrame(data)
df.to_excel('go_obo.xlsx')

