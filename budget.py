


class Category:
#First Commit
    def __init__(self, name):
        self.name = name;
        self.total = 0.0;
        self.ledger = [];
    
    def deposit(self, amount, description=""):
        self.total += amount;
        obj_to_append = {"amount": amount, "description": description};
        self.ledger.append(obj_to_append);
    
    def withdraw(self, amount, description=""):
        if not (self.check_funds(amount)):
            return False;
        else:
            self.total -= amount;
            obj_to_append = {"amount": (amount*-1), "description": description};
            self.ledger.append(obj_to_append);
            return True;

    def transfer(self, amount, cat2):
        
        if (self.check_funds(amount)):
            description = f"Transfer to {cat2.name}"
            self.withdraw(amount,description)
            description = f"Transfer from {self.name}"
            cat2.deposit(amount,description);
            return True;
        else:
            return False;


    def get_balance(self):
        return self.total;

    def check_funds(self,amount):
        return (self.total>=amount);
    
    def __repr__(self) -> str:
        s = f"{self.name:*^30}\n"    
        for moves in self.ledger:
            s += f"{moves['description'][0:23]}{format(moves['amount'],'.2f'):>{30-len(moves['description'][0:23])}}\n"
        s += f"Total: {format(self.get_balance(),'.2f')}"
        return s;   





def create_spend_chart(categories):
    total = 0;
    longest_name = 0;
    for cat in categories:
        if longest_name < len(cat.name):
            longest_name = len(cat.name);
        for moves in cat.ledger:
            if (moves['amount']<0):
                total+=moves['amount'];
    arr_of_perc = [];
    arr_of_wdn = [];
    for cat in categories:
        sub_total = 0;
        for moves in cat.ledger:
            if (moves['amount']<0):
                sub_total+=moves['amount'];
        arr_of_wdn.append(sub_total);
    for wdn in arr_of_wdn:
        pct = (wdn*100)//total;
        arr_of_perc.append(pct);
    s = f"Percentage spent by category\n"
    
    for n in range(100, -1, -10):
        line = f"{str(n)+'|':>4}"
        for perc in arr_of_perc:
            if(arr_of_perc.index(perc)==0):
                if (perc >= n):
                    line +=f" o"
                else:
                    line+=f"  "
            else:
                if (perc >= n):
                    line +=f"  o"
                else:
                    line+=f"   "
        line += f"  \n";
        s += line;
    s+=f"    {(str('-')*(3*len(categories)+1))}\n"
    n = 0;
    s+=f"     "
    while n <= longest_name-1:
        for cat in categories:
            if n < len(cat.name):
                s+=f"{cat.name[n]}  "
            else:
                s+=f"   "
        if n !=longest_name-1:
            s+=f"\n"
            s+=f"     "
        
        n+=1;
    return s;

