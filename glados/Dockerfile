FROM python:3.8.5-alpine

RUN adduser -D aperture
RUN apk add --no-cache libc-dev gcc

USER aperture
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install  --user -r requirements.txt

ENV PATH="/home/aperture/.local/bin:${PATH}"
ENV PORT=5000
ENV PYTHONUNBUFFERED=TRUE

COPY --chown=aperture:aperture templates templates
COPY --chown=aperture:aperture glados.py glados.py

CMD ["gunicorn", "glados:app"]