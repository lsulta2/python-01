tea_price_bdt = {
    'Iced mint tea' : 30,
    'Ginger tea': 20 ,
    'karak tea' : 10 ,
    'Iced lemon tea' : 34,
}


tea_price_usd = {tea:price / 80 for tea, price in tea_price_bdt.items()}

print(tea_price_usd)