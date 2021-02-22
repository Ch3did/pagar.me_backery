from flask import jsonify

def handler_ping():
  return jsonify({
    'result': 'pong'
  })


def handler_get_all_store():
    return jasonify (  {
      'id': store_id, 
      'nome': store_name,
      'cep': cep
    }  )



def handler_get_all_prod():
    return jasonify (  {
      'id' : product_id,
      'name': product_name,
      'price': price,
      'store_id': store_id
    }  )



def handler_get_all_order():
    return jasonify (  {
      'order_id' : order_id,
      'total' : total,
      'adress' : adress,
      'id_prod' : id_prod,
      'name_user' : name_user

    }  )



