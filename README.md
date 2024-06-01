<img src='https://res.cloudinary.com/dwle3oqep/image/upload/v1717200491/banner_pp1n9k.png'>


# <center><b>STOCK MARKET PRICE PREDICTION</b></center>
## A model that utilizes indicators and other data from the stock market to predict the closing price of a stock for the following day.
<center>
<div>
<img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/murratefe/smpp"> <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/murratefe/smpp/total"> <img alt="Python Version" src="https://img.shields.io/badge/python-v3.10.11-rgb(0%2C210%2C0)"> <img alt="Project Type" src="https://img.shields.io/badge/type-machine_learning-purple"> <img alt="GitHub Issues" src="https://img.shields.io/github/issues/murratefe/smpp"> <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-blue"> <a href="https://buymeacoffee.com/murratefe"><img alt="Static Badge" src="https://img.shields.io/badge/%24-donate-rgb(255%2C20%2C147)"></a>
</div>
</center>



This model predicts the <b><u>next day's closing price</u></b> of a stock with using <b>scikit-learn ridge</b> model for machine learning with the using of these <b>indicators and datas:</b>
* <b>Open:</b> Intraday opening price of the stock.
* <b>High:</b> Intraday higher price of the stock.
* <b>Low:</b> Intraday lower price of the stock.
* <b>Close:</b> End-of-day closing price of the stock.
* <b>Volume:</b> Total number of shares traded during the day.
* <b>Support:</b> Refers to the price level at which a stock tends to find buying interest as it falls.
* <b>Resistance:</b> Refers to a price level where a stock tends to find selling interest as it rises.
* <b>SMA:</b> Simple Moving Average for n days.
* <b>Daily Change:</b> It indicates how much the closing price + / - change as a percentage compared to the previous day's closing price.
* <b>WMA:</b> Weighted Moving Average for n days.
* <b>EMA:</b> Exponential Moving Average for n days.
* <b>MACD:</b> Moving Average Convergence Divergence.
* <b>MACD Signal:</b> Bullish / Bearish Signal.
* <b>RSI:</b> Relative Strength Index.
* <b>Bolling Bands Upper:</b> this is calculated by adding a specified number of standard deviations (usually 2) to the middle band.
* <b>Bolling Bands Middle:</b> Simple Moving Average(SMA) This is typically a 20-period SMA.
* <b>Bollinger Bands Lower:</b> This is calculated by subtracting a specified number of standard deviations (usually 2) from the middle band. 

## How to install:
1. Clone this project.<br>``` git clone https://github.com/murratefe/smpp.git ```
2. Install Anaconda. (<a href='https://www.youtube.com/watch?v=WUeBzT43JyY'>How to install Anaconda</a>)
3. Install requirements with pip on Anaconda env:<br/>``` pip install -r requierements.txt ```

## Usage:
### For Train a Model:
1. Open <b>train_model.ipynb with</b> jupyter or colab.
2. Change this section according to your needs: <br/> <img src='https://res.cloudinary.com/dwle3oqep/image/upload/v1717200491/carbon2_tiqhdm.png'>
3. And press ▶ Run All.

### For Prediction:
A quick tip, retraining the model with the data of the stock you want to predict when you are going to use the model will provide you with better predictions.
1. Open a terminal on SMPP folder.
2. Type in: <br/>``` python launch_model.py ```
3. Enter model name which do you want to use.
4. Enter ticker.
5. Enter the date. (Please note that this model predicts the closing price of the next day, so please enter the date one day before the date you want to predict.)
6. And Voila
<br/><img src='https://res.cloudinary.com/dwle3oqep/image/upload/v1717205866/terminal_1_do0o9o.gif' alt='Terminal'>

## Tests and Accuracy:
### Ridge Model ALPHA=1.0 Prediction Results for AAPL
<img src='https://res.cloudinary.com/dwle3oqep/image/upload/v1717200491/model_alpha_1_0_pred_chart_lykoxs.jpg'><br/>

* <b>Alpha Number: 1.0</b>
* <b>Model Score</b>(X_test,y_test): <b>0.8898801408787523</b>
* <b>Mean CV Score</b> (neg_mean_squarred_error)(X_test,y_test): <b>-18.208859252929688</b>
* <b>MAE: 2.1878614<b> 

### Ridge Model ALPHA=0.04 Prediction Results for AAPL
<img src='https://res.cloudinary.com/dwle3oqep/image/upload/v1717200491/alpha_04_pred_chart_hafsti.jpg'>

* <b>Alpha Number: 0.04</b>
* <b>Model Score</b>(X_test,y_test): <b>0.9120292389386958</b>
* <b>Mean CV Score</b> (neg_mean_squarred_error)(X_test,y_test): <b>-8.71382122039795</b>
* <b>MAE: 1.9038935899734497</b>
#### You can find the more details (shap charts etc.) in SMPP_model.ipynb

## Find a bug?
If you found an issue or woul like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to  submit a PR with a fix, reference the issue you created!

## Donations

If you are feeling generous, you can buy me a coffee!<br/>
<a href="https://buymeacoffee.com/murratefe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a><br/>
You can also buy me a coffee with BNB(BEP20): ```0x93525105E9111293d508e6105c86b3191013cf24```
