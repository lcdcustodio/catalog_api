from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List


from app import db

api = Namespace("Tech Assessment", description="Recomendações de Arquitetura e Engenharia")



@api.route("/<id>")
@api.param("id", "Informe o id da recomendação")
@api.param("customer", "Informe o novo cliente para a recomendação")
class UpdateRecommendation(Resource):

    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def put(self, id):        
        """Editar recomendação"""         


        doc_ref_1 = db.collection("MT").document(id)
        doc = doc_ref_1.get()
        result = {}
        cust = []

        customer = request.args.get('customer')

        if customer:

            if doc.exists:


                tot = doc.to_dict().get('total_usage') + 1
                cust = doc.to_dict().get('customers')
                cust.append(customer)

                #data = {'total_usage': tot, 'customers': cust}
                data = {'mt': doc.to_dict().get('mt'), 'total_usage': tot, 'dimension': doc.to_dict().get('dimension'), 'customers': cust, 'recommendation': doc.to_dict().get('recommendation')}

                doc_ref_1.set(data)


                #result.update({'recommendations': doc.to_dict()})
                result.update({'result': f'doc {id} updated!'})
                result.update({'success': True})

                return result,200
            

            

            


            else:
                
                result.update({'result': 'No such document'})
                result.update({'success': False})
                return result,404
            
        else:    
        
            result.update({'result': 'customer parameter is missing'})
            result.update({'success': False})
            return result,404


@api.route("/new")
@api.param("dimension", "Digite a dimensão/categoria desejada.")
@api.param("mt", "Informe o grau de maturidade da organização com relação à dimensão")
@api.param("recommendation", "Digite a nova recomendação")
@api.param("customer", "Informe o cliente da nova recomendação")
class NewRecommendation(Resource):

    @api.response(201, 'Created')
    @api.response(400, 'Bad Request')
    def post(self):
        """Inserir nova recomendação"""         

        dimension = request.args.get('dimension')
        mt = request.args.get('mt')
        recommendation = request.args.get('recommendation')
        customer = request.args.get('customer')

        dimension_ref = ['DevSecOps', 'Qualidade', 'Dados', 'Arquitetura Corporativa', 'Arquitetura de Solução', 'Arquitetura de Software', 'Engenharia de Software']
        mt_ref = ['1','2','3','4','5']
        result = {}

        if dimension in dimension_ref and mt in mt_ref:

            data = {'mt': mt, 'total_usage': 1, 'dimension': dimension, 'customers': [customer], 'recommendation': recommendation}
            doc_ref = db.collection("MT")
            doc_ref.document().set(data)        
            result.update({'success': True})
            return result,201
        else:
            result.update({'error': f'either mt is not in list: {mt_ref} or dimension is not in list: {dimension_ref}'})
            result.update({'success': False})
            return result,400




@api.route("")
@api.param("dimension", "Digite a dimensão/categoria desejada.")
@api.param("mt", "Informe o grau de maturidade da organização com relação à dimensão.")
class RecommendationNameResource(Resource):

    
    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def get(self):    
        """Ober lista de recomendações"""

        dimension = request.args.get('dimension')
        mt = request.args.get('mt')


        doc_ref_1 = db.collection("MT")
        query = doc_ref_1.where("dimension", "==", dimension).where("mt", "==", mt)

        query_ref = query.get()        
        result = {}

        if query_ref:        
            out = {}
            i = 1
            for doc in query_ref:
                out.update({f'item_{i}':[{'id':doc.id},{'recommendation': doc.to_dict().get('recommendation')},{'total_usage':doc.to_dict().get('total_usage')},{'customers':doc.to_dict().get('customers')}]})
                i=i+1

            result.update({'recommendations': out})
            return result,200

        else:
            
            result.update({'result': 'No such document'})
            result.update({'success': False})
            return result,404



