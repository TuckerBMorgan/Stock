import ystockquote;


txt = "values.txt"
value = open(txt, 'r');



lines = tuple(value);
value.close();

capital = float(lines[0])

stockCount = float(lines[1])

stockCost = ystockquote.get_price('TSLA');

if float(stockCost) < capital:
	stockCount+=1;
	capital-=float(stockCost);


values = open("values.txt", 'w')
values.write(str(capital) + "\n");
values.write(str(stockCount));

print("Current Capital " + str(capital) + "\n");
print("Current Number of stocks " + str(stockCost) + "\n");
print("Current Value of portfolio " + str(float(stockCost) * stockCount) + "\n")