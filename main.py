import pandas as pd
import matplotlib.pyplot as plt
import uuid
from pathlib import Path

input_path = "BTC.csv"

print("Reading file path")

df = pd.read_csv(input_path)


def make_dataset(df,path="TrainDataset"):

    def make_paths(path):
        path = Path(path)
        path.mkdir(exist_ok=True)

        charts_path  = path / 'chart'
        charts_path.mkdir(exist_ok=True)

        rsi_path = path / 'rsi'
        rsi_path.mkdir(exist_ok=True)

        (charts_path / 'up').mkdir(exist_ok=True)
        (charts_path/'down').mkdir(exist_ok=True)

        (rsi_path/'up').mkdir(exist_ok=True)
        (rsi_path/'down').mkdir(exist_ok=True)

        return charts_path,rsi_path


    charts_path,rsi_path = make_paths(path)

    for i in range(len(df) - 21):
        records = df[i:i+20]
        next_record = df.iloc[i+20]

        next_day_price = next_record['Close']


        x = records['Date']
        y = records['Close']
        y_1 = records['High']
        y_2 = records['Low']

        x_1 = range(len(x))

        fig1 = plt.figure(figsize=(10,7))
        

        plt.fill_between(x_1,y,color="blue")
        plt.scatter(x_1,y,color="red")
        plt.plot(x_1,y,color="green")
        plt.axis("off")

        name = str(uuid.uuid4())
        if next_day_price > y.iloc[-1]:
            plt.savefig("{}/up/fig{}.jpg".format(str(charts_path),name))

        else:
            plt.savefig("{}/down/fig{}.jpg".format(str(charts_path),name))



        plt.close()

        fig2 = plt.figure(figsize=(10,7))
        plt.plot()
        plt.fill_between(x_1,y_1,y_2,color="blue")
        # plt.plot(x_1,y_1,y_2,color="black")
        plt.scatter(x_1,y_1,color="orange")
        plt.scatter(x_1,y_2,color="green")
        plt.plot(x_1,y,color="purple")
        plt.axis("off")

        if next_day_price > y.iloc[-1]:
            plt.savefig("{}/up/fig{}.jpg".format(str(rsi_path),name))
        else:
            plt.savefig("{}/down/fig{}.jpg".format(str(rsi_path),name))

        print("Saving {} chart info ".format(name))

        plt.close()


        


make_dataset(df[:1000])
make_dataset(df[1000:1500])
