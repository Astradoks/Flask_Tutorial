from flask import Flask, render_template, request
from app import app
from models.models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    contracts = Contrato.query.all()
    filteredContracts = []
    if request.method == 'POST':
        initialDate = request.form['initialDate']
        endDate = request.form['endDate']
        filteredContracts = Contrato.query.filter(Contrato.contrato_fecha >= initialDate, Contrato.contrato_fecha <= endDate).all()
        dic = {filcon.clienteContrato.cliente_nombre : 0 for filcon in filteredContracts}
        for con in filteredContracts:
            nombre_cliente = con.clienteContrato.cliente_nombre
            monto = con.contrato_monto + dic.get(nombre_cliente)
            dic.update({nombre_cliente : monto})
        filteredContracts = dic.items()
    return render_template('index.html', contracts = contracts, filteredContracts = filteredContracts)