import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model, neighbors
import logging

oecd = pd.read_csv ("C:\Users\Soo\Downloads\BLI_04092017201038720.csv", thousands=",")

gdpc = pd.read_csv ("C:\Users\Soo\Downloads\weoreptc.aspx", thousands=",", delimiter='\t', 
                   encoding="latin1", na_values="n/a")
#print oecd.head()
#print "gdp per captia"
#print gdpc.head()
#print oecd["Country"][:5]
#print oecd["INDICATOR"][:5]
def prepData (oecd, gdpc):
    
    pcMap = dict (zip (gdpc["Country"], gdpc["2015"]))
    oCountry = oecd["Country"]
    oValue = oecd["Value"]
    oEq = oecd["INEQUALITY"]
    countries = []
    happs = []
    perCaps = []
    for i,ind in enumerate (oecd["INDICATOR"]):
        if ind != "SW_LIFS":
            continue
        if oEq[i] != "TOT":
            continue
        country = oCountry[i]
        if country == "OECD - Total":
            continue
        perCap = pcMap.get (country, None)
        if perCap is None:
            logging.error ("Could not find perCapita for %s", country)
            continue
        ind = oValue[i]
        if perCap > 80000 and ind < 7:
            logging.error ("%s > 80,000 for %s with %s happ", perCap, country, ind)
            continue

        logging.debug ("[%d]Added:%s,%s,%s", len(countries), country, perCap, ind)
        countries.append (country)
        happs.append (ind)
        perCaps.append (perCap)
    
    return pd.DataFrame({"Country":countries, "HapInd":happs, "PerCapita":perCaps})#, columns=["Country", "HapInd", "PerCapita"])

logger = logging.getLogger()
logger.setLevel (logging.INFO)
stats = prepData (oecd, gdpc)
stats.plot (kind="scatter", x="PerCapita", y="HapInd")
plt.show()

x = np.c_[stats["PerCapita"]]
y = np.c_[stats["HapInd"]]

def predict (val, x, y, model):
    model.fit(x, y)
    logging.info ("%s -> %s", val, model.predict ([[val]]))

predict (22587, x, y, linear_model.LinearRegression ())
predict (22587, x, y, neighbors.KNeighborsRegressor (n_neighbors=3))
