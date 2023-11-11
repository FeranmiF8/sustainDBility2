import pandas as pd

data = {
    "Temperature":[12, 43, 35],
    "Moisture":[65, 43, 32]
}

df = pd.DataFrame(data)

df.to_csv("test.csv")

print(df)

# {
#     "method":"get/set/delete",
#     "username":"kenzie",
#     "accountkey":"poop",
#     "tableName":"table1",
#     "data":"whatever"
# }


# get func call
def getCall():
    return

# set func call
def setCall():
    return

# delete func call
def deleteCall():
    return