# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame
from typing import Optional, Union

from freqtrade.strategy import (
    BooleanParameter,
    CategoricalParameter,
    DecimalParameter,
    IStrategy,
    IntParameter,
)

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


# This class is a sample. Feel free to customize it.
class EMAStrat(IStrategy):
    INTERFACE_VERSION = 10

    # Can this strategy go short?
    can_short: bool = False

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi".
    minimal_roi = {
        # "120": 0.0,  # exit after 120 minutes at break even
        # "60": 0.01,
        # "30": 0.02,
        "0": 0.06,
    }

    # Optimal stoploss designed for the strategy.
    # This attribute will be overridden if the config file contains "stoploss".
    stoploss = -0.06

    # Trailing stoploss
    trailing_stop = True
    trailing_only_offset_is_reached = True
    trailing_stop_positive = 0.03
    trailing_stop_positive_offset = 0.12  # Disabled / not configured

    # Optimal timeframe for the strategy.
    timeframe = "15m"

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = True

    # These values can be overridden in the config.
    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False

    startup_candle_count: int = 100

    # Optional order type mapping.
    order_types = {
        "entry": "limit",
        "exit": "limit",
        "stoploss": "market",
        "stoploss_on_exchange": False,
    }

    # Optional order time in force.
    order_time_in_force = {"entry": "GTC", "exit": "GTC"}

    plot_config = {
        "main_plot": {
            "tema": {},
            "sar": {"color": "white"},
        },
        "subplots": {
            "MACD": {
                "macd": {"color": "blue"},
                "macdsignal": {"color": "orange"},
            },
            "RSI": {
                "rsi": {"color": "red"},
            },
        },
    }

    def informative_pairs(self):
        return [("BTC/USDT:USDT", "15m"), ("ETH/USDT:USDT", "15m"), ("INJ/USDT:USDT", "15m"), ("LINK/USDT:USDT", "15m"), ("SOL/USDT:USDT", "15m")]

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["rsi"] = ta.RSI(dataframe)

        dataframe["mfi"] = ta.MFI(dataframe)

        # # EMA - Exponential Moving Average
        # dataframe['ema3'] = ta.EMA(dataframe, timeperiod=3)
        dataframe['ema9'] = ta.EMA(dataframe, timeperiod=9)
        dataframe['ema15'] = ta.EMA(dataframe, timeperiod=15)
        dataframe['ema20'] = ta.EMA(dataframe, timeperiod=20)
        # dataframe['ema50'] = ta.EMA(dataframe, timeperiod=50)
        # dataframe['ema100'] = ta.EMA(dataframe, timeperiod=100)

        # TEMA - Triple Exponential Moving Average
        dataframe["tema"] = ta.TEMA(dataframe, timeperiod=9)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        

        ema_condition = (dataframe['ema9'] > dataframe['ema15']) & (dataframe['ema15'] > dataframe['ema20'])#ema9>ema15>ema20
    
        price_above_ema15 = dataframe['close'] > dataframe['ema15']
        price_below_ema15 = dataframe['close'] < dataframe['ema15']
        price_below_ema20 = dataframe['close'] < dataframe['ema20']
    
        condition1 = ema_condition
        condition2 = (
            ((dataframe['ema9'] > dataframe['close']) & price_above_ema15) |#checking if the price falls between any of the bands
            (price_below_ema15 & (dataframe['close'] > dataframe['ema20'])) |
            (ema_condition & price_below_ema20)
        )

        dataframe['enter_long'] = 0#since this bot takes values from columns


        mask = condition1 & condition2
    
    # Perform the check only where the mask is True
        if mask.any():
            for i in np.flatnonzero(mask):#this checks for any true values in mask 
                if i >= 10:  # Ensure we have at least 10 previous candles
                    res = sum(
                        (dataframe['close'].iloc[i-j] - dataframe['ema15'].iloc[i-j]) / dataframe['ema15'].iloc[i-j] > 0.015
                        for j in range(1, 11)
                    )# this basicall sums up the no. of times the % is greater than 1.5% during last 10 candles from the current one.
                    if res > 0:
                        dataframe.loc[i, 'enter_long'] = 1# and if the res is greater than 0 means at least one time our condition became true.



        # condition1 = ((dataframe['ema9'] > dataframe['ema15']) & (dataframe['ema15']> dataframe['ema20']))
        # condition2 = (((dataframe["ema9"]>dataframe['close']) & (dataframe['close']>dataframe['ema15']) & (dataframe["ema15"]> dataframe['ema20']))  | ((dataframe["ema9"]>dataframe['ema15']) & (dataframe['ema15']> dataframe['close']) & (dataframe['close']>dataframe['ema20'])) | ((dataframe["ema9"]> dataframe["ema15"]) & (dataframe["ema15"]>dataframe["ema20"]) & (dataframe["ema20"] > dataframe['close'])))
        # if condition1.any() and condition2.any():
        #     res = 0 
        #     for j in range(0,10,1):
        #         if ((dataframe['close'].iloc[-j-1] - dataframe['ema15'].iloc[-j-1]) / dataframe['ema15'].iloc[-j-1]) > 0.015:
        #             res += 1
        #     if res>0:
        #         dataframe['enter_long'] = 1

        ema_condition_short = (dataframe['ema9'] < dataframe['ema15']) & (dataframe['ema15'] < dataframe['ema20'])
    
        price_below_ema15 = dataframe['close'] < dataframe['ema15']
        price_above_ema15 = dataframe['close'] > dataframe['ema15']
        price_above_ema20 = dataframe['close'] > dataframe['ema20']
    
        condition3 = ema_condition_short
        condition4 = (
            ((dataframe['ema9'] > dataframe['close']) & price_below_ema15) |
            (ema_condition_short & price_above_ema15 & (dataframe['close'] > dataframe['ema20'])) |
            (ema_condition_short & price_above_ema20)
        )

        dataframe['enter_short'] = 0

        maskk = condition3 & condition4
    
    # Perform the check only where the mask is True
        if maskk.any():
            for i in np.flatnonzero(mask):
                if i >= 10:  # Ensure we have at least 10 previous candles
                    res = sum(
                        (dataframe['close'].iloc[i-j] - dataframe['ema15'].iloc[i-j]) / dataframe['ema15'].iloc[i-j] > 0.015
                        for j in range(1, 11)
                    )
                    if res > 0:
                        dataframe.loc[i, 'enter_short'] = 1



        # condition3 = ((dataframe['ema9'] < dataframe['ema15']) & (dataframe['ema15']< dataframe['ema20']))
        # condition4 = (((dataframe["ema9"] < dataframe['close']) & (dataframe['close']< dataframe['ema15']) & (dataframe["ema15"] < dataframe['ema20']))  | ((dataframe["ema9"]< dataframe['ema15']) & (dataframe['ema15'] < dataframe['close']) & (dataframe['close'] < dataframe['ema20'])) | ((dataframe["ema9"] < dataframe["ema15"]) & (dataframe["ema15"] < dataframe["ema20"]) & (dataframe["ema20"] <  dataframe['close'])))
        # if condition3.any() and condition4.any():
        #     res = 0 
        #     for j in range(0,10,1):
        #         if abs((dataframe['close'].iloc[-j-1] - dataframe['ema15'].iloc[-j-1]) / dataframe['ema15'].iloc[-j-1]) > 0.015:
        #             res += 1
        #     if res>0:
        #         dataframe['enter_short'] = 1


        return dataframe
    
    # def custom_stoploss(self, pair: str, trade:"Trade",dataframe:DataFrame,
    #                     current_rate: float, current_profit: float, after_fill: bool, 
    #                     **kwargs) -> Optional[float]:
    #     if trade.is_long:
    #         sl_price = dataframe['ema15']*0.95
        
    #     return sl 

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (#none only taking exit either if it hit tp or sl.
            ),
            "exit_long",
        ] = 1

        dataframe.loc[
            (
            ),
            "exit_short",
        ] = 1

        return dataframe
