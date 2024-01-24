from models.product import Product as ProductModel

class ProductService():
    def __init__(self, db) -> None:
        self.db=db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result
    
    def create_product(self, product: ProductModel):
        new_product =  ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return
    
    def delete_product(self, name):
        self.db.query(ProductModel).filter(ProductModel.name == name).delete()
        self.db.commit()
        return

