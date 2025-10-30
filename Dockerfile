FROM python:3.11-slim

RUN useradd --create-home appuser

USER appuser

WORKDIR /home/appuser
