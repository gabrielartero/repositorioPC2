# VERSIÓN PYTHON
FROM python:3.7.7-slim

WORKDIR .

# COPY editarTituloHTML.py practica_creativa2/bookinfo/src/productpage


RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

EXPOSE 9080

ENV GROUP_NAME numeroGrupo

ENTRYPOINT ["pyhton3", "editarTituloHTML.py"]

ENTRYPOINT ["python3", "productpage_monolith.py", "9080"]