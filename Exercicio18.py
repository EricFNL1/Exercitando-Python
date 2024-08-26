franciso = 1.10
sara = 1.50

crescfranc = 0.03
crescsara = 0.02

anos =0

while franciso < sara:
    franciso+=crescfranc
    sara+=crescsara
    anos+=1
    if franciso > sara:
        print("Francisco levou",anos,"anos para ser maior que Sara")
        
    