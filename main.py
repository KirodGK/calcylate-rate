from core.parse_header import parse_header
from utils import counter
from outputs import pretty_output

with open('./test/data1.csv', 'r') as file:
    splitFile = file.read().split('\n')
    header = parse_header(splitFile[0])
    newData = counter(data=splitFile[1:], header=header)
    pretty_output(results=newData)
    # for i in newData:
    #     print(i)

