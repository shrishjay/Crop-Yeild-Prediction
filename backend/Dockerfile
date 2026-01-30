FROM python:3.12
WORKDIR /backend
COPY . /backend
RUN pip install uv
RUN uv sync
ENV VIRTUAL_ENV=/backend/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
EXPOSE 8000
CMD [ "uvicorn","app:app","--host","0.0.0.0","--port","8000" ]
