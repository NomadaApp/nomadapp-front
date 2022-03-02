# Nomad App
The app for digital nomads.

## Usage
Run the app by clicking [here](https://nomadapp-akukb5qdcq-ew.a.run.app/).

Run front locally by:
```
streamlit run ./nomadapp_front/streamlit_main.py
```

Build front locally with Docker:
```
docker build --tag nomadapp-front:latest .
```
Run front locally with Docker:
```
docker run nomadapp-front:latest
```


## Architecture
![architecture](./docs/img/nomadaap_architecture.svg)


