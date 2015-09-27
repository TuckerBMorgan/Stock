import ystockquote;

class Stock
	cost = 0;
	count = 0;
	ticker = " ";

class StockInfo():
	capital = 0;
	stocks = [];
	fileName = "";

	def createStock(self, file_):
		self.fileName = file_;
		value = open(file_, 'r');
		lines = tuple(value);
		self.capital = float(lines[0]);
		count = 0;
		for v in lines:
			if count > 0:
				words = v.split(':');
				cls = Stock();
				cls.cost = float(words[2]);
				cls.count = float(words[1]);
				cls.ticker = words[0];
				self.stocks.append(cls);
			count+=1;
		value.close();

	def printStockAmount(self):
		for k,v in self.stocks.items():
			print(str(v) + " of " +  k + " for a value of "  + str(float(ystockquote.get_price(k)) * v));

	def buyStockIfPossible(self):
		for k,v in self.stocks.items():
			cost = float(ystockquote.get_price(k));
			if(cost < self.capital):
				count = int(self.capital / cost);
				self.stocks[k] = v + count;
				self.capital -= cost * count;

	def writeInfo(self):
		writing = open(self.fileName, 'w');
		writing.write(str(self.capital) + "\n");
		for k,v in self.stocks.items():
			writing.write(k + ":" + str(v) + "\n");


sto = StockInfo();
txt = "values.txt"
sto.createStock(txt);
sto.printStockAmount();
sto.buyStockIfPossible();
sto.printStockAmount();
sto.writeInfo();