import re
with open('data.txt', 'r', encoding = 'utf-8') as file:
    text = file.read()
def stringtonum(st):
    st = st.replace(',', '.')
    st = st.replace(' ', '')
    return float(st)
for i, item in enumerate(items):
    print(f'{i + 1}) {item[0]}')
    print(f'\t{item[1]} x {item[2]} = {item[3]}')
    fullsum = fullsum + stringtonum(item[3])

fullsum = None
fullsum = 0
Company_Name = re.search(r'ДУБЛИКАТ\n(.*)\n', text).group(1)
bin_space = re.search(r'БИН (\d+)', text).group(1)
Items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', text)
Date = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', text).group()
Address = re.search(r'г\.[^\n]+', text).group()
fullprice = re.search(r'ИТОГО:\n([0-9, ]+)', text).group(1)
print(f'Conpany name: {Company_Name}\nspace BIN: {bin_space}\nData: {Date}\nAddress: {Address}\n')

print(f'total price sum: {fullprice}')
print(f'total sum: {fullsum}')