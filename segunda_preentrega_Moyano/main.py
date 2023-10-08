from segunda_preentrega.clientes import ClienteMayorista, ClienteMinorista


cliente1 = ClienteMayorista('Roberto SA','roberto@roberto', 'Rawson 2222', '2235866557', '30756258996', 'Resp. Inscripto', True)
cliente2 = ClienteMinorista('Richard Fort', 'richardo@elcomandante.com', '232 5th Avenue', '11556622330', '23656444', 'Por supuesto', 'No')

print(cliente1)
print(cliente1.compra(5000))
print(cliente2)