import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("fivethirtyeight")

qndl_api_key = '264CUZedQbfZRKwENQWV'


def state_list():
    fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return fiddy_states[0][0][1:]


def grab_init_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=qndl_api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    pickle_out = open("fiddy_states.pickle", "wb")
    pickle._dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=qndl_api_key)
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    return df


# grab_init_state_data()

ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data['TX1yr'] = HPI_data["TX"].resample('A').mean()
print(HPI_data[['TX', 'TX1yr']].head())
#HPI_data.dropna(how="all",inplace=True)
HPI_data.fillna(method='bfill',inplace=True)
print(HPI_data[['TX', 'TX1yr']].head())

print(HPI_data.isnull().values.sum())

HPI_data[['TX', 'TX1yr']].plot(ax=ax1)

plt.legend(loc=4)
plt.show()
