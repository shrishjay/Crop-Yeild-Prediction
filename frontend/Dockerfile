FROM python:3.12
WORKDIR /frontend
COPY . /frontend
RUN pip install uv
RUN uv sync
ENV VIRTUAL_ENV=/frontend/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
EXPOSE 8501
CMD [ "streamlit","run","frontend.py" ]
