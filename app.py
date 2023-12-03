# api lugar para desponibilizar recursos ou funcionalidades

# 1 obejtivo criar uma api disponibiliza consulta , criação , edição e exclusão de produtos.
# 2 url base localhost
# 3 endpoints

#    - localhost/produtos (get)
#    - localhost/produtos (post) 
#    - localhost/produtos/id (get)
#    - localhost/produto/id (put)
#    - localhost/produtos/id (delete)

# 4 quais recursos produtos

from flask import Flask, jsonify, request
import uuid

app=Flask(__name__)

contador_id=1

produtos = [
    {
        'id': contador_id,
        'produto':'Oleo 0w20',
        'fabricante':'Shell HX8'
    },
    {
        'id': contador_id+1,
        'produto':'Filtro de oleo',
        'fabricante':'Tecfill'

    },
    {
        'id': contador_id+2,
        'produto':'Militec',
        'fabricante':'Militec1'
    },
]

# cadastrar
@app.route('/produtos',methods=['POST'])
def cadastrar_novo_produto():
    global contador_id
    novo_produto=request.get_json()
    novo_produto['id'] = contador_id
    produtos.append(novo_produto)
    contador_id+=1
    return jsonify(produtos)
# consultar todos
@app.route('/produtos',methods=['GET'])
def obter_produtos():
    return jsonify(produtos)
# consultar(id)
@app.route('/produtos/<int:id>',methods=['GET'])
def obter_produto_por_id(id):
    for produto in produtos:
        if produto.get('id')==id:
            return jsonify(produto)
# editar 
@app.route('/produtos/<int:id>',methods=['PUT'])
def editar_produto_por_id(id):
    produto_alterado=request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get('id')==id:
            produtos[indice].update(produto_alterado)  
            return jsonify(produtos[indice]) 
# excluir 
@app.route('/produtos/<int:id>',methods=['DELETE'])
def excluir_produto(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id')==id:
            del produtos[indice]
    return jsonify(produtos)    
    
app.run(port=5000,host='localhost',debug=True)