class Accounts:
    def __init__(self, baseCurrency):
        self.baseCurrency = baseCurrency
        self.marketValues = {self.baseCurrency : 1}
        self.accounts = {}
    
    def getMarketValue(self, assets):
        totalValue = 0
        for i in assets:
            if i in self.marketValues and not i == self.baseCurrency:
                totalValue += assets[i] * self.marketValues[i]['quantity']
        return totalValue

    def getBuyingPower(self, username):
        assets = self.fetchUserAssets(username, 'openOrders')
        fiatHolding = self.fetchUserAssets(username, 'fiat')   
        openOrdersValue = self.getMarketValue(assets)
        buyingPower = fiatHolding - openOrdersValue
        return buyingPower
    
    def fetchUserAssets(self, username, type):
        if username in self.accounts:
            assets = self.accounts[username][type]
            return assets
