FROM python:3.8

#ENV PYTHONPATH "${PYTHONPATH}:./venv/bin/python"
WORKDIR /backend

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./backend /backend


CMD ["uvicorn", "main:app", "--reload"]
EXPOSE 8000