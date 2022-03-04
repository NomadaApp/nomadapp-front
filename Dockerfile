FROM python:3.8
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN python setup.py install
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["./nomadapp_front/streamlit_main.py"]
