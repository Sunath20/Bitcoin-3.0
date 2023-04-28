import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from pathlib import Path
import uuid
df = pd.read_csv("BTC.csv",index_col=0,parse_dates=True)
df.index.name = "Date"


def candlestick_dataset(dataframe,root_path):

	path = Path(root_path)

	path.mkdir(exist_ok=True)

	up = path / 'up'
	up.mkdir(exist_ok=True)

	down = path / 'down'
	down.mkdir(exist_ok=True)


	for i in range(len(dataframe)-21):
		chart_data = df[i:i+20]
		next_col = df.iloc[i+20+1]
		save_path = path / ( 'up' if next_col['Close'] > chart_data.iloc[-1]['Close'] else 'down')
		# print(next_col['Close'])
		# print(chart_data.iloc[-1]['Close'])
		file_path = str(save_path  /  str(uuid.uuid4()) )
		mpf.plot(chart_data,type="candle",savefig=file_path)
		print("Saved {} ".format(file_path))





candlestick_dataset(df[:1000],"./TrainDataset/candlestick")
