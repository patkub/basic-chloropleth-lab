# Making a basic choropleth

Run read_data.py to generate `my-data-vals.csv` based on the csv files in `US_COVID_CASES_AS_OF_2021_10_31`.
On Linux/Mac this is:
```
chmod +x read_data.py
./read_data.py
```

```
python -m http.server 8888 &
```
Go to http://localhost:8888/choropleth_our_example.html
