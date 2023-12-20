##Coloque a porcentagem da margem e o valor do frete empresa

def calculaFrete(mar, val):
    por = (100 - mar) / 100

    return  val * por

calculaFrete(15, 290)