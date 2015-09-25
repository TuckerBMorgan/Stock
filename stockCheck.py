import ystockquote;

class StockInfo():
	capital = 0;
	stocks = {}

	def createStock(self, file):
		value = open(file, 'r');
		lines = tuple(value);
		self.capital = float(lines[0]);
		count = 0;
		for v in lines:
			if count > 0:
				words = v.split(':');
				self.stocks[words[0]] = float(words[1]);
			count+=1;

	def printStockAmount(self):
		for k,v in self.stocks.items():
			print(str(v) + " of " +  k + " for a value of "  + str(float(ystockquote.get_price(k)) * v))

	def buyStockIfPossible(self):
		for k,v in self.stocks.items():
			cost = float(ystockquote.get_price(k));
			if(cost < self.capital):
				self.stocks[k] = v + 1;
				self.capital -= cost;

	def writeInfo(self):
		

sto = StockInfo();


txt = "values.txt"
sto.createStock(txt);
sto.printStockAmount();
sto.buyStockIfPossible();
sto.printStockAmount();


#capital = float(lines[0])

#stockCount = float(lines[1])

#stockCost = ystockquote.get_price('TSLA');

#if float(stockCost) < capital:
#	stockCount+=1;
#	capital-=float(stockCost);


#values = open("values.txt", 'w')
#values.write(str(capital) + "\n");
#values.write(str(stockCount));

#print("Current Capital " + str(capital) + "\n");
#print("Current Number of stocks " + str(stockCost) + "\n");
#print("Current Value of portfolio " + str(float(stockCost) * stockCount) + "\n")