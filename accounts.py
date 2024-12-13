class accounts:
    def __init__(self):
        self.accounts = {}
    
    def createAccount(self, accountName, startingCapital):
        if not accountName in self.accounts:
            # Create account with initial balance
            account = {'fiat':float(startingCapital), 'pos':{}, 'openOrder':{}}
            self.accounts[accountName] = account
    
    def getHolding(self, accountName, assetName):
        if accountName in self.accounts:
            account = self.accounts[accountName]
            if assetName == 'fiat':
                return account['fiat']
            else:
                holdings = account['pos']
                if assetName in holdings:
                    return holdings[assetName]
                else:
                    return 0
    
    def editAssets(self, accountName, assetName, qty):
        if accountName in self.accounts:
            account = self.accounts[accountName]
            if assetName == 'fiat':
                asset = account['fiat']
                asset += qty
            else:
                if assetName in account['pos']:
                    asset = account['pos'][assetName]
                    asset += qty
                else:
                    if qty >= 0:
                        account['pos'][assetName] = qty
    
    def transact(self, buyer, seller, assetName, qty, price):
        if buyer in self.accounts and seller in self.accounts:
            # Buyer pays fiat while seller pays in asset
            sellerHolding = self.getHolding(seller, assetName)
            # Check if seller has enough assets to transact
            if sellerHolding >= qty:
                amountPayable = qty * price
                buyerCash = self.getHolding(buyer, 'fiat')
                if buyerCash >= amountPayable:
                    self.accounts[buyer]['fiat'] += -1 * amountPayable
                    self.accounts[buyer]['pos']
                    self.accounts[seller]['']
            
