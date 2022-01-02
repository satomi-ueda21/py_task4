### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master

    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)

    def get_item_order(self,order_code):
        for code in self.item_master:
            if order_code == code.item_code:
                return code.item_name, code.price

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def view_item_oreder(self,order_code):
        res = self.get_item_order(order_code)
        print(f"商品名:{res[0]}")
        print(f"商品価格:{res[1]}")





### メイン処理
def main(order_code):
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))

    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    # order.get_item_order(order_code)

    # オーダー表示
    order.view_item_list()
    order.view_item_oreder(order_code)
1

if __name__ == "__main__":
    order_code = input("オーダーする商品コードを入力してください>>>")
    main(order_code)