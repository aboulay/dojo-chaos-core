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

COPY --chown=aperture:aperture core_types core_types
COPY --chown=aperture:aperture external_core.py external_core.py

CMD ["gunicorn", "external_core:app"]