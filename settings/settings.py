DATABASE_PATH = '../crawler.db'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

URL_IBOVESPA = 'https://www.investing.com/equities/StocksFilter?index_id=17920'
URL_NASDAQ = 'https://www.investing.com/equities/StocksFilter?index_id=20'
URL_USD_BRL = 'https://m.investing.com/currencies/usd-brl'

IBOVESPA_NAME_FILE = 'ibovespa.txt' 
NASDAQ_NAME_FILE = 'nasdaq.txt'
USD_BRL_NAME_FILE = 'nasdaq.txt'

COLUMNS_IBOVESPA = {
    'Name': 'name',
    'Last': 'last_rs',
    'High': 'high_rs', 
    'Low': 'low_rs',
    'Chg.': 'chg', 
    'Chg. %': 'chg_perc', 
    'Vol.': 'vol',
    'Time': 'time'
}

COLUMNS_NASDAQ = {
    'Name': 'name',
    'Last': 'last_usd',
    'High': 'high_usd',
    'Low': 'low_usd',
    'Chg.': 'chg',
    'Chg. %': 'chg_perc',
    'Vol.': 'vol',
    'Time': 'time'
}

COLUMNS_USD_BRL = {
    'currency': 'currency',
    'value': 'value',
    'change': 'change',
    'perc': 'perc',
    'timestamp': 'timestamp'
}
