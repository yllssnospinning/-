
class Book:
  def __init__(self, tickerName, tickSize):
    self.tickSize = tickSize
    self.instrumentName = tickerName
    # Market book format 
    # {'bids':[orders], 'asks':[orders]}
    # Limit book format
    # {price1:[bids, offers], price2:[bids, offers], ...}
    # Order Format
    # [traderID, orderID, qty] where orderID is in chronological order, smaller orderID is placed earlier and vice versa
    self.limitBook = {}
    self.marketBook = {'buys':[], 'sells':[]}

def getBestOrder(self, side):
  # Following code assuming self.limitBook is fuly ordered
  i
