# EMA-SRSI_BB

This repo is combined for both 3EMA strategy, SRSI and BB strategy.

Here are the results of backtesting - 

EMA strat 365 days Bt - 
                   SUMMARY METRICS                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2023-08-20 01:00:00   │
│ Backtesting to              │ 2024-08-18 12:45:00   │
│ Max open trades             │ 5                     │
│                             │                       │
│ Total/Daily Avg Trades      │ 590 / 1.62            │
│ Starting balance            │ 10000 USDT            │
│ Final balance               │ 13555.49 USDT         │
│ Absolute profit             │ 3555.49 USDT          │
│ Total profit %              │ 35.55%                │
│ CAGR %                      │ 35.67%                │
│ Sortino                     │ 29.41                 │
│ Sharpe                      │ 2.39                  │
│ Calmar                      │ 16.97                 │
│ Profit factor               │ 1.17                  │
│ Expectancy (Ratio)          │ 6.03 (0.07)           │
│ Avg. daily profit %         │ 0.10%                 │
│ Avg. stake amount           │ 1290.895 USDT         │
│ Total trade volume          │ 761628.142 USDT       │
│                             │                       │
│ Best Pair                   │ SOL/USDT:USDT 18.87%  │
│ Worst Pair                  │ LINK/USDT:USDT -1.57% │
│ Best trade                  │ INJ/USDT:USDT 6.22%   │
│ Worst trade                 │ BTC/USDT:USDT -6.97%  │
│ Best day                    │ 593.197 USDT          │
│ Worst day                   │ -340.213 USDT         │
│ Days win/draw/lose          │ 135 / 101 / 126       │
│ Avg. Duration Winners       │ 1 day, 16:47:00       │
│ Avg. Duration Loser         │ 1 day, 18:00:00       │
│ Max Consecutive Wins / Loss │ 16 / 10               │
│ Rejected Entry signals      │ 0                     │
│ Entry/Exit Timeouts         │ 0 / 0                 │
│                             │                       │
│ Min balance                 │ 9877.393 USDT         │
│ Max balance                 │ 14760.071 USDT        │
│ Max % of account underwater │ 11.00%                │
│ Absolute Drawdown (Account) │ 11.00%                │
│ Absolute Drawdown           │ 1623.337 USDT         │
│ Drawdown high               │ 4760.071 USDT         │
│ Drawdown low                │ 3136.734 USDT         │
│ Drawdown Start              │ 2024-03-14 14:15:00   │
│ Drawdown End                │ 2024-07-05 00:00:00   │
│ Market change               │ 193.96%               │
└─────────────────────────────┴───────────────────────┘
                              BACKTESTING REPORT                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃           ┃        ┃           ┃      Tot ┃           ┃          ┃ Win  Draw ┃
┃           ┃        ┃       Avg ┃   Profit ┃       Tot ┃      Avg ┃      Loss ┃
┃      Pair ┃ Trades ┃  Profit % ┃     USDT ┃  Profit % ┃ Duration ┃      Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ SOL/USDT… │    176 │      0.93 │ 1886.652 │     18.87 │   1 day, │       103 │
│           │        │           │          │           │  9:56:00 │   0    73 │
│           │        │           │          │           │          │      58.5 │
│ INJ/USDT… │    228 │      0.44 │ 1023.629 │     10.24 │ 21:43:00 │       124 │
│           │        │           │          │           │          │   0   104 │
│           │        │           │          │           │          │      54.4 │
│ BTC/USDT… │     36 │       1.1 │  467.620 │      4.68 │  5 days, │        22 │
│           │        │           │          │           │ 10:20:00 │   0    14 │
│           │        │           │          │           │          │      61.1 │
│ ETH/USDT… │     36 │       0.8 │  334.815 │      3.35 │  4 days, │        21 │
│           │        │           │          │           │  8:21:00 │   0    15 │
│           │        │           │          │           │          │      58.3 │
│ LINK/USD… │    114 │      0.04 │ -157.226 │     -1.57 │   1 day, │        59 │
│           │        │           │          │           │ 19:55:00 │   0    55 │
│           │        │           │          │           │          │      51.8 │
│     TOTAL │    590 │      0.57 │ 3555.490 │     35.55 │   1 day, │       329 │
│           │        │           │          │           │ 17:19:00 │   0   261 │
│           │        │           │          │           │          │      55.8 │
└───────────┴────────┴───────────┴──────────┴───────────┴──────────┴───────────┘

EMA strategy 666 days - 

                             BACKTESTING REPORT                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃           ┃        ┃           ┃      Tot ┃           ┃          ┃ Win  Draw ┃
┃           ┃        ┃       Avg ┃   Profit ┃       Tot ┃      Avg ┃      Loss ┃
┃      Pair ┃ Trades ┃  Profit % ┃     USDT ┃  Profit % ┃ Duration ┃      Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ INJ/USDT… │    432 │      0.45 │ 2111.637 │     21.12 │ 21:52:00 │       234 │
│           │        │           │          │           │          │   0   198 │
│           │        │           │          │           │          │      54.2 │
│ SOL/USDT… │    299 │      0.48 │ 1842.032 │     18.42 │   1 day, │       163 │
│           │        │           │          │           │  9:57:00 │   0   136 │
│           │        │           │          │           │          │      54.5 │
│ ETH/USDT… │     73 │      0.91 │  750.268 │       7.5 │  4 days, │        43 │
│           │        │           │          │           │  6:34:00 │   0    30 │
│           │        │           │          │           │          │      58.9 │
│ BTC/USDT… │     63 │      0.85 │  643.218 │      6.43 │  6 days, │        37 │
│           │        │           │          │           │  3:18:00 │   0    26 │
│           │        │           │          │           │          │      58.7 │
│ LINK/USD… │    185 │      0.01 │ -262.593 │     -2.63 │   1 day, │        94 │
│           │        │           │          │           │ 23:15:00 │   0    91 │
│           │        │           │          │           │          │      50.8 │
│     TOTAL │   1052 │      0.44 │ 5084.562 │     50.85 │   1 day, │       571 │
│           │        │           │          │           │ 18:52:00 │   0   481 │
│           │        │           │          │           │          │      54.3 │
└───────────┴────────┴───────────┴──────────┴───────────┴──────────┴───────────┘

                    SUMMARY METRICS                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2022-10-22 01:00:00   │
│ Backtesting to              │ 2024-08-17 13:30:00   │
│ Max open trades             │ 5                     │
│                             │                       │
│ Total/Daily Avg Trades      │ 1052 / 1.58           │
│ Starting balance            │ 10000 USDT            │
│ Final balance               │ 15084.562 USDT        │
│ Absolute profit             │ 5084.562 USDT         │
│ Total profit %              │ 50.85%                │
│ CAGR %                      │ 25.31%                │
│ Sortino                     │ 11.25                 │
│ Sharpe                      │ 1.85                  │
│ Calmar                      │ 10.38                 │
│ Profit factor               │ 1.13                  │
│ Expectancy (Ratio)          │ 4.83 (0.06)           │
│ Avg. daily profit %         │ 0.08%                 │
│ Avg. stake amount           │ 1293.351 USDT         │
│ Total trade volume          │ 1360605.635 USDT      │
│                             │                       │
│ Best Pair                   │ INJ/USDT:USDT 21.12%  │
│ Worst Pair                  │ LINK/USDT:USDT -2.63% │
│ Best trade                  │ SOL/USDT:USDT 6.90%   │
│ Worst trade                 │ BTC/USDT:USDT -7.37%  │
│ Best day                    │ 661.678 USDT          │
│ Worst day                   │ -458.37 USDT          │
│ Days win/draw/lose          │ 226 / 202 / 235       │
│ Avg. Duration Winners       │ 1 day, 15:45:00       │
│ Avg. Duration Loser         │ 1 day, 22:35:00       │
│ Max Consecutive Wins / Loss │ 17 / 10               │
│ Rejected Entry signals      │ 0                     │
│ Entry/Exit Timeouts         │ 0 / 0                 │
│                             │                       │
│ Min balance                 │ 9800.602 USDT         │
│ Max balance                 │ 16424.733 USDT        │
│ Max % of account underwater │ 14.07%                │
│ Absolute Drawdown (Account) │ 14.07%                │
│ Absolute Drawdown           │ 1798.501 USDT         │
│ Drawdown high               │ 2785.74 USDT          │
│ Drawdown low                │ 987.238 USDT          │
│ Drawdown Start              │ 2023-04-17 15:00:00   │
│ Drawdown End                │ 2023-09-10 04:00:00   │
│ Market change               │ 329.87%               │
└─────────────────────────────┴───────────────────────┘

SrsiBB strat 365 days Bt results - 

                              BACKTESTING REPORT                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃           ┃        ┃           ┃      Tot ┃           ┃          ┃ Win  Draw ┃
┃           ┃        ┃       Avg ┃   Profit ┃       Tot ┃      Avg ┃      Loss ┃
┃      Pair ┃ Trades ┃  Profit % ┃     USDT ┃  Profit % ┃ Duration ┃      Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ INJ/USDT… │    411 │      0.26 │ 1089.378 │     10.89 │  9:48:00 │       270 │
│           │        │           │          │           │          │   0   141 │
│           │        │           │          │           │          │      65.7 │
│ SOL/USDT… │    391 │      0.13 │  542.148 │      5.42 │ 10:43:00 │       245 │
│           │        │           │          │           │          │   0   146 │
│           │        │           │          │           │          │      62.7 │
│ LINK/USD… │    417 │      0.07 │  217.164 │      2.17 │ 10:10:00 │       262 │
│           │        │           │          │           │          │   0   155 │
│           │        │           │          │           │          │      62.8 │
│     TOTAL │   1219 │      0.15 │ 1848.690 │     18.49 │ 10:13:00 │       777 │
│           │        │           │          │           │          │   0   442 │
│           │        │           │          │           │          │      63.7 │
└───────────┴────────┴───────────┴──────────┴───────────┴──────────┴───────────┘

                   SUMMARY METRICS                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2023-08-20 01:00:00   │
│ Backtesting to              │ 2024-08-18 15:45:00   │
│ Max open trades             │ 3                     │
│                             │                       │
│ Total/Daily Avg Trades      │ 1219 / 3.35           │
│ Starting balance            │ 10000 USDT            │
│ Final balance               │ 11848.69 USDT         │
│ Absolute profit             │ 1848.69 USDT          │
│ Total profit %              │ 18.49%                │
│ CAGR %                      │ 18.54%                │
│ Sortino                     │ 2.48                  │
│ Sharpe                      │ 2.39                  │
│ Calmar                      │ 5.01                  │
│ Profit factor               │ 1.12                  │
│ Expectancy (Ratio)          │ 1.52 (0.04)           │
│ Avg. daily profit %         │ 0.05%                 │
│ Avg. stake amount           │ 1180.855 USDT         │
│ Total trade volume          │ 1439462.498 USDT      │
│                             │                       │
│ Best Pair                   │ INJ/USDT:USDT 10.89%  │
│ Worst Pair                  │ LINK/USDT:USDT 2.17%  │
│ Best trade                  │ INJ/USDT:USDT 10.00%  │
│ Worst trade                 │ INJ/USDT:USDT -10.24% │
│ Best day                    │ 328.571 USDT          │
│ Worst day                   │ -496.978 USDT         │
│ Days win/draw/lose          │ 220 / 10 / 135        │
│ Avg. Duration Winners       │ 6:54:00               │
│ Avg. Duration Loser         │ 16:04:00              │
│ Max Consecutive Wins / Loss │ 19 / 9                │
│ Rejected Entry signals      │ 0                     │
│ Entry/Exit Timeouts         │ 0 / 0                 │
│                             │                       │
│ Min balance                 │ 9900.312 USDT         │
│ Max balance                 │ 13570.475 USDT        │
│ Max % of account underwater │ 19.37%                │
│ Absolute Drawdown (Account) │ 19.37%                │
│ Absolute Drawdown           │ 2628.286 USDT         │
│ Drawdown high               │ 3570.475 USDT         │
│ Drawdown low                │ 942.189 USDT          │
│ Drawdown Start              │ 2024-03-17 14:30:00   │
│ Drawdown End                │ 2024-08-05 06:15:00   │
│ Market change               │ 260.99%               │
└─────────────────────────────┴───────────────────────┘


SrsiBB strategy BT results 666 days - 

                             BACKTESTING REPORT                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃           ┃        ┃           ┃      Tot ┃           ┃          ┃ Win  Draw ┃
┃           ┃        ┃       Avg ┃   Profit ┃       Tot ┃      Avg ┃      Loss ┃
┃      Pair ┃ Trades ┃  Profit % ┃     USDT ┃  Profit % ┃ Duration ┃      Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ INJ/USDT… │    744 │      0.36 │ 3087.251 │     30.87 │  9:58:00 │       495 │
│           │        │           │          │           │          │   0   249 │
│           │        │           │          │           │          │      66.5 │
│ LINK/USD… │    748 │      0.09 │  703.460 │      7.03 │ 10:27:00 │       477 │
│           │        │           │          │           │          │   0   271 │
│           │        │           │          │           │          │      63.8 │
│ SOL/USDT… │    715 │      0.08 │  614.930 │      6.15 │ 10:47:00 │       449 │
│           │        │           │          │           │          │   0   266 │
│           │        │           │          │           │          │      62.8 │
│     TOTAL │   2207 │      0.18 │ 4405.642 │     44.06 │ 10:24:00 │      1421 │
│           │        │           │          │           │          │   0   786 │
│           │        │           │          │           │          │      64.4 │
└───────────┴────────┴───────────┴──────────┴───────────┴──────────┴───────────┘


                    SUMMARY METRICS                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2022-10-23 01:00:00   │
│ Backtesting to              │ 2024-08-18 15:30:00   │
│ Max open trades             │ 3                     │
│                             │                       │
│ Total/Daily Avg Trades      │ 2207 / 3.32           │
│ Starting balance            │ 10000 USDT            │
│ Final balance               │ 14405.642 USDT        │
│ Absolute profit             │ 4405.642 USDT         │
│ Total profit %              │ 44.06%                │
│ CAGR %                      │ 22.18%                │
│ Sortino                     │ 2.93                  │
│ Sharpe                      │ 2.82                  │
│ Calmar                      │ 6.51                  │
│ Profit factor               │ 1.14                  │
│ Expectancy (Ratio)          │ 2.00 (0.05)           │
│ Avg. daily profit %         │ 0.07%                 │
│ Avg. stake amount           │ 1305.214 USDT         │
│ Total trade volume          │ 2880606.327 USDT      │
│                             │                       │
│ Best Pair                   │ INJ/USDT:USDT 30.87%  │
│ Worst Pair                  │ SOL/USDT:USDT 6.15%   │
│ Best trade                  │ SOL/USDT:USDT 10.19%  │
│ Worst trade                 │ INJ/USDT:USDT -10.24% │
│ Best day                    │ 456.205 USDT          │
│ Worst day                   │ -610.939 USDT         │
│ Days win/draw/lose          │ 405 / 17 / 244        │
│ Avg. Duration Winners       │ 7:08:00               │
│ Avg. Duration Loser         │ 16:17:00              │
│ Max Consecutive Wins / Loss │ 27 / 9                │
│ Rejected Entry signals      │ 0                     │
│ Entry/Exit Timeouts         │ 0 / 0                 │
│                             │                       │
│ Min balance                 │ 9996.372 USDT         │
│ Max balance                 │ 16518.663 USDT        │
│ Max % of account underwater │ 19.45%                │
│ Absolute Drawdown (Account) │ 19.45%                │
│ Absolute Drawdown           │ 3212.079 USDT         │
│ Drawdown high               │ 6518.663 USDT         │
│ Drawdown low                │ 3306.584 USDT         │
│ Drawdown Start              │ 2024-03-17 14:30:00   │
│ Drawdown End                │ 2024-08-05 06:15:00   │
│ Market change               │ 457.75%               │
└─────────────────────────────┴───────────────────────┘
