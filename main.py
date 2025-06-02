from core.parse_header import parse_header


with open('./test/data2.csv', 'r') as file:
    print(parse_header(file.read().split('\n')[0]))
   
    
