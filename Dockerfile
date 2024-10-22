FROM python:3.11

WORKDIR /planner
COPY requirements.txt /planner
RUN pip install --upgrade pip && pip install -r /planner/requirements.txt

EXPOSE 5000
COPY ./ /planner

CMD ["python", "main.py"]