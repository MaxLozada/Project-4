FROM python:3.8-buster
COPY requirements.txt .
ENV FLASK_APP=app
ENV PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:////home/myuser/database/db.sqlite
ENV GOOGLE_API_KEY=AIzaSyAdaKDjt-rFgTpGooHvXbKX-RvtKRvI5eU
ENV CRYPTO_API_KEY=e04bb542-3462-4856-b8e1-85f6db5ba4d4
ENV PATH="/home/myuser/.local/bin:${PATH}"
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    adduser myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
CMD gunicorn -w 4 --bind 0.0.0.0:$PORT "app:create_app()"