FROM python:3.12

RUN python -m pip install flask flask-cors chardet numpy pandas seaborn scipy scikit-learn matplotlib gunicorn pillow

WORKDIR /app

ADD pipeline.py pipeline.py
ADD targetpay.py targetpay.py
ADD pipelines.pkl pipelines.pkl

EXPOSE 8080

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "targetpay:app" ]