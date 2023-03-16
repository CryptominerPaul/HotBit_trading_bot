# HotBit_trading_bot
Python Trading bot

1. Market Making
2. Wash Trading
3. Info (Balances, Markets, Market Depth{bids & asks})

You will need two files to run the bot

1. Make a directory for the files for the bot 
```
mkdir Hotbit_Trading_Bot
```
than 
```
cd Hotbit_Trading_Bot
```
2. Download files to the new directory you just created
```
.env

HotBit_Bot.py
```
Email: cryptominer8245@yahoo.com to get the files of this bot

Click here to contact me on Discord: <a href="https://discord.com/users/412476381725720576">Cryptominer8245</a>

For Install you will need Python3
check your version by opening a terminial and type
```python3 --version```

Update the package list and upgrade any existing packages:
```
sudo apt-get update
sudo apt-get upgrade
```
Install Python by running the following command:
```
sudo apt-get install python3
```
Verify the installation by checking the Python version:
```
python3 --version
```

The Bot needs a few libraries

to Install the libraries:
```
pip install requests
pip install termcolor
pip install prettytable
pip install python-dotenv
```

Using nano you will need to update your ``Private Keys`` and ``Coin Pairs`` in the .env file
Example:
```
nano .env
```

```
# Hotbit  Keys
# Api-Key
api_key=ENTER_YOUR_KEY_HERE
# Api-Secret-Key
secret_key=ENTER_YOUR_KEY_HERE
```
In The Bot.py using nano command you can change lines of code 
```
nano Hotbit_Bot.py
```

You can update the following lines of code to your stratigies
```
Sells:
min_sell_price = 0.006250
price = round(ask_price - 0.00001, 5)
min_amount = 200.00  # set this for the least amount of coins to buy
max_amount = 2000.00 # set this for the max amount of coins to buy
amount = round(random.uniform(min_amount, max_amount), 2)

Buys:
max_buy_price = 0.00600
min_amount = 0.01  # set this for the least amount of coins to buy
max_amount = 500.00 # set this for the max amount of coins to buy
amount = round(random.uniform(min_amount, max_amount), 2)

Spread:
spread = (ask_price - bid_price) / bid_price
if spread < 0.06: # Change to the % you want
```
add # to the `sell(market="{pair}", isfee=0)` or `buy(market="{pair}", isfee=0)` line of code to stop the bot order from being placed

To start Bot in Terminal:
1. `screen -S Hotbit_Trading_Bot` this is the folder where the bot is located
2. start bot
```
python3 Hotbit_Bot.py
```
3. to exit screen and keep bot running hold the key `Control` and than press keys `a d` at the same time
4. to resume screen type `screen -r`
5. to stop bot press `Control c`

Trading Bot Example:

<img src="https://user-images.githubusercontent.com/40405385/225494942-4e4c5096-7ed6-42c5-9e04-1391720e3588.png" width="25%" alt="Hotbit_Bot">
![image](https://user-images.githubusercontent.com/40405385/225494942-4e4c5096-7ed6-42c5-9e04-1391720e3588.png)



<div style="color: yellow;">

**Disclaimer:**

The trading bot provided herein is designed for informational and educational purposes only. It is not intended to be, and should not be construed as, financial, investment, or trading advice. Users of this trading bot assume full responsibility for any decisions made based on its outputs, and the creators and maintainers of the bot shall not be held liable for any losses, damages, or claims arising from the use of this tool. Trading in financial markets involves substantial risks, including the potential for loss of principal, and may not be suitable for all investors. Before using this trading bot, users should carefully consider their financial objectives, risk tolerance, and level of experience. We strongly recommend consulting with a qualified financial advisor before making any investment or trading decisions.

</div>


