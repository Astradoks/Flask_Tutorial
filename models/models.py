from app import db

#For table clientes
class Cliente(db.Model):
    __tablename__ = 'cliente'
    cliente_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_nombre = db.Column(db.String(100), nullable=False)
    cliente_contrato = db.relationship('Contrato', backref='clienteContrato', lazy=True)

#For table contratos
class Contrato(db.Model):
    __tablename__ = 'contrato'
    contrato_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contrato_cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'), nullable=False)
    contrato = db.Column(db.String(100), nullable=False)
    contrato_monto = db.Column(db.Numeric(10,2))
    contrato_fecha = db.Column(db.Date, nullable=False)

db.create_all()