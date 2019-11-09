from quantconnect.api import Api
from IPython.core.display import display, HTML

algorithmid = 3382674
backtestid = "2dc0332ae782dd1d0be91b39cef813bf"

quant = Api(88707, "84f84df437a2bfe887962a4d09d9a28967c4f69d1297b53ee7e40f49259f1015")
report = quant.read_backtest(algorithmid, backtestid)

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