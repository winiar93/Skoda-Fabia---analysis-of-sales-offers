# Skoda-Fabia---analysis-of-sales-offers
Analysis of skoda fabia sales offers, based on scraped data from the auction site 

Tools used in this project:

sklearn          : 0.23.2
pandas           : 1.1.3
matplotlib       : 3.3.2
selenium         : 3.141.0
seaborn          : 0.11.0




Using very simply web scraper, I downloaded about 900 Skoda Fabia offers.
Made analyse to find voivodeship with lowest mean price, using pandas in jupyter notebook.
Also applayed a regression model to predict price of Skoda Fabia on parameters like: mileage,
year of production, location/voivodeship, fuel type

Close future plans:

- implement adaline perceptron 

Update v2:
- prepared data to use with linear regression model ( standarization and label encoding)
- added scikit-learn lib to predict car price but model score is very bad

Update v3:
- after apply IQR method to delete outliers, model accuracy is 78%
- added a plot with milage and price coefficient and with regression line
- example of prediction price of two cars with different parameters
