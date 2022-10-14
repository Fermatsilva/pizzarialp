def list_ingredientes(tipo, ingredientes):
    print(ingredientes.loc[tipo, :])
        
def rem_ingredientes(ingrediente, escolhas):
    del escolhas[ingrediente]
    
def add_ingredientes(ingrediente, escolhas, ingredientes):
    escolhas[ingrediente] = ingredientes.xs(ingrediente, level=1, drop_level=False)[0][0]
    
def list_escolhas(escolhas):
    print(pd.Series(escolhas))

def calc_valor(escolhas):
    return sum(escolhas.values())
