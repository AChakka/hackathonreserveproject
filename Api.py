from serpapi import GoogleSearch
class Api:
    def __init__(self, stock):
        self.stockSearch = stock + ":NASDAQ"
        params = {
            "engine": "google_finance",
            "q": self.stockSearch,
            "api_key": "4a9e8eab4776299e0239ea0c6ad79522b47b27130a3e78f73259c0af7b07b40d"
        }
        search = GoogleSearch(params)
        self.results = search.get_dict()
    def getStockInfoPrice(self, stock):
        if stock in self.results:
            return(self.results[stock]["price"])

    def getStockInfoPercent(self, stock):
        if stock in self.results:
            return(self.results[stock]["price_movement"]["percentage"])

    def getStockInfoDirection(self, stock):
        if stock in self.results:
            if(self.results[stock]["price_movement"]["movement"] == "Up"):
                return "+"
            else:
                return "-"

    def getStockInfoIncome(self, stock):
        if stock in self.results:
            return(self.results[stock][0]["results"][0]["table"][2]["value"])

    def getStockInfoBalance(self, stock):
        if stock in self.results:
            return(self.results[stock][1]["results"][0]["table"][2]["value"])

    def getStockInfoCash(self, stock):
        if stock in self.results:
            return(self.results[stock][2]["results"][0]["table"][2]["value"])
        
    def getStockSearch(self):
        return self.stockSearch
    
    def setStockSearch(self, stock):
        self.stockSearch = stock + ":NASDAQ"

    def getStockInfoRange(self, stock):
        if stock in self.results:
            return(self.results[stock]["key_stats"]["stats"][2]["value"])
        
    def getStockInfoNews(self, stock):
        if stock in self.results:
            return(self.results[stock]["items"]["stats"][2]["value"])


        
api = Api("GOOG")
api.setStockSearch("AAPL")
print(api.getStockInfoCash("financials"))
