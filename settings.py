
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

URL_IBOVESPA = 'https://www.investing.com/equities/StocksFilter?index_id=17920'

IBOVESPA_NAME_FILE = 'ibovespa.txt' 

COLUMNS_IBOVESPA = {
    'Name' : 'name',
    'Last': 'last_rs',
    'High': 'high_rs', 
    'Low': 'low_rs',
    'Chg.': 'chg', 
    'Chg. %': 'chg_perc', 
    'Vol.': 'vol',
    'Time': 'time'
}