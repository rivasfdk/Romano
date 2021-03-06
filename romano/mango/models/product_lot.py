from .jsonable import JSONableModel

class ProductLot(JSONableModel):
  def __init__(self, code, stock, comment):
    self.code = code
    self.stock = stock
    self.comment = comment
  
  @classmethod
  def fromDict(cls, dict_):
    product_lot = cls(dict_['code'], dict_['stock'], dict_['comment'])
    product_lot.id = dict_['id']
    product_lot.content_name = dict_['get_content']['product']['name']
    product_lot.content_code = dict_['get_content']['product']['code']
    return product_lot
