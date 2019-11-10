from quantconnect.api import Api
from sys import getsizeof
import json

class QuantConnector:
    def getReport(algoID, backtestID):
        quant = Api(88707, "84f84df437a2bfe887962a4d09d9a28967c4f69d1297b53ee7e40f49259f1015")

        with open('strategies.json') as json_file:
            data = json.load(json_file)

        backtest = {}

        report = quant.read_backtest(algoID, backtestID)
        p = quant.list_projects()

        backtest['stats'] = report

        return backtest
'''
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
        # RuntimeStatistics'''