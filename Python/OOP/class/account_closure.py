# 계좌를 closure로 만듬
def make_account(client_name, balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return (client_name, balance)
    return deposit
    

if __name__=="__main__":
    my_acnt = make_account('greg', 5000)
    result = my_acnt(3000)
    print(result)