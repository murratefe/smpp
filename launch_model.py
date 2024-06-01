import yfinance as yf
import pickle
import datetime
def pred_share_price(symbol:str, end:str, model_name:str, period:str='max', interval:str='1d', start:str=''):
    if start == "":
        data = yf.download(symbol.upper(), period=period.lower(), end=end, interval=interval, auto_adjust=True)  
    else:
        data = yf.download(symbol.upper(), period=period.lower(), start=start, end=end, interval=interval, auto_adjust=True)
    data.reset_index(inplace=True)
    #Load Model
    with open(f'models/{model_name}/model.pkl', 'rb') as f:
        model = pickle.load(f)
    #Load pipeline for predict
    with open(f'models/{model_name}/pipeline_for_predict.pkl', 'rb') as f:
        pipe = pickle.load(f)
    data = pipe.fit_transform(data)
    return model.predict(data.iloc[-1:])

if __name__ == '__main__':
    model_select = str(input("Please specify the model you would like to use: "))
    symbol = str(input("Symbol: ")).upper()
    date = str(input("Please enter the date you want to forecast the stock price in YYYY-MM-DD format: "))

    pred = pred_share_price(symbol, date, model_name=model_select)
    predicted_date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=1)
    print(f'The predicted closing price for {symbol} stock on {predicted_date} is: {pred[0]:.2f}$')