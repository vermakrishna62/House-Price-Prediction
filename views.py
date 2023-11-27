
def house_price(request):
    
    if request.method == 'POST':
        data = request.POST
    
        features = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
        'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
        'parking', 'prefarea', 'furnishingstatus']
        
        feature_values = []
        
        for i in features:
            feature_values.append(int(data.get(i)))
        print(feature_values)
        price = house_price_model.predict([feature_values])
        # formatted_price = "{:.2f}".format(price[0])
        formatted_price = f"{price[0]:,.2f}"


        print(formatted_price)
        return render(request,'house_price.html',{'price':formatted_price})
    
    return render(request,'house_price.html')
