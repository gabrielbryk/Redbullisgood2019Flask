from quantconnect.api import Api
from IPython.core.display import display, HTML
from sys import getsizeof

algorithm = 1
if algorithm == 1:
    # paired switching algorithm
    algorithmid = 3383088
    backtestid = "fce68177edd4066fb4bf54ec9c1e56b5"

if algorithm == 2:
    # Mean reversion statistical arbitrage algorithm
    algorithmid = 3385763
    backtestid = "b61a205f2037316e957e8e50aa34835e"

if algorithm == 3:
    # Idiosyncratic Skewness long stocks algorithm
    algorithmid = 3385792
    backtestid = "cf2087e486ac230d5a9546f69f5f2917"


quant = Api(88707, "84f84df437a2bfe887962a4d09d9a28967c4f69d1297b53ee7e40f49259f1015")
report = quant.read_backtest(algorithmid, backtestid)
p = quant.list_projects()
print(getsizeof(report))

# for data in p["projects"]:
#     print(data)

if report['success'] == False:
    print("Report Does Not Exist!")
    exit()

equityChart = report['result']['Charts']["Strategy Equity"]["Series"]["Equity"]["Values"]
dailyPerformanceChart = report['result']['Charts']["Strategy Equity"]["Series"]["Daily Performance"]["Values"]

equity = report['result']["RuntimeStatistics"]["Equity"]
totalFees = report['result']["TotalPerformance"]["TradeStatistics"]["TotalFees"]
netProfit = report['result']["TotalPerformance"]["TradeStatistics"]["TotalProfitLoss"]
averageProfit = report['result']["TotalPerformance"]["TradeStatistics"]["AverageProfit"]
averageLoss = report['result']["TotalPerformance"]["TradeStatistics"]["AverageLoss"]

print(equityChart)

def getEquityChart():
    return equityChart

def getDailyPerformance():
    return dailyPerformanceChart

def getEquity():
    return equity

def getTotalFees():
    return totalFees

def getNetProfit():
    return netProfit

def getAverageProfit():
    return averageProfit

def getAverageLoss():
    return averageLoss


#result
    # RollingWindow
    # TotalPerformance
        # TradeStatistics
        # PortfolioStatistics
        # ClosedTrades
    # AlphaRuntimeStatistics
    # Charts
    # Orders
    # ProfitLoss
    # Statistics
    # RuntimeStatistics