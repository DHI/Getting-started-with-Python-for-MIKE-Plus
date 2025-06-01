# %%
import mikeio1d

res = mikeio1d.open(r"network.res1d")
res

# %%
res.reaches["116l1"].Discharge.add()
res.reaches["12l1"].Discharge.add()
res.to_dfs0("model_results.dfs0")
# %%
import mikeio

ds = mikeio.open("model_results.dfs0")
ds
# %%
import pandas as pd
df = pd.read_csv("flow_meter_data.csv", index_col=0, parse_dates=True)
ds = mikeio.from_pandas(
    df,
    items=[
        #116l1_observed
        mikeio.ItemInfo(
            itemtype=mikeio.EUMType.Discharge,
            unit=mikeio.EUMUnit.meter_pow_3_per_sec,  
        ),
        #12l1_observed
        mikeio.ItemInfo(
            itemtype=mikeio.EUMType.Discharge,
            unit=mikeio.EUMUnit.meter_pow_3_per_sec,  
        ),
    ]
)
ds.to_dfs("flow_meter_data.dfs0")
