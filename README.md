## cintel-06-custom

Module 6 will explore creating a custom PyShiny app using GitHub, Git, and PyShiny.

# Create and Activate Project Virtual Environment

```shell
py -m venv .venv
.venv\Scripts\Activate
```

# Install and update packages from requirements.txt

```shell
py -m pip install --upgrade -r requirements.txt
```

# Freeze requirements

```shell
py -m pip freeze > requirements.txt
```

# Install websockets
```shell
py -m pip install websocket-client
py -m pip install websockets==10.4 
```

# Build Client-Side App

```shell
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```

Open web browser (I use Chrome) and navigate to http://localhost:8008

# Update GitHub Repository

```shell
git add .
git commit -m "Update GitHub Repository with local build and add to Pages"
git push -u origin main
```

# Dataset

Module 6 will make use of the flights.csv dataset obtained from the seaborn library located at the following url: https://github.com/mwaskom/seaborn-data/blob/master/flights.csv. This csv file has been copied into the Module 6 repository. The dataset contains information of flights between 1949 and 1960 and includes the year, month, and number of passengers.