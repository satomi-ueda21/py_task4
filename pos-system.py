import pandas as pd

CSV_PATH = "./item_master.csv"

def item_master_csv():
    item_master = []
    df = pd.read_csv(CSV_PATH, dtype={"item_code":object}, header=0)
    for item_code, item_name, price in zip(df["item_code"], df["item_name"], df["price"]):
        item_master.append(Item(item_code, item_name, price))
    print(df)
    print(item_master)

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

    def register_order(self):
        while True:
            item_code = input("オーダーする商品コードを入力してください。"
                              "オーダーを終了するときは0と入力してください>>>")
            if int(item_code) != 0:
                self.add_item_order(item_code)
            else:
                break

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def view_item_oreder(self):
        for order_code in self.item_order_list:
            res = self.get_item_order(order_code)
            if res != None:
                print(f"商品コード:{order_code} 商品名:{res[0]} 商品価格:{res[1]}")
            else:
                print(f"商品コード{order_code}は存在しません。")



### メイン処理
def main():
    # マスタ登録
    item_master_csv()
    item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))

    # オーダー登録
    order=Order(item_master)
    order.register_order()
    # order.add_item_order()
    # order.add_item_order("002")
    # order.add_item_order("003")

    # オーダー表示
    order.view_item_list()
    order.view_item_oreder()
1

if __name__ == "__main__":
    # order_code = input("オーダーする商品コードを入力してください>>>")
    main()