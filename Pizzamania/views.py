import pandas as pd
from django.shortcuts import render
from .model_utils import load_model, make_prediction
from recipes.models import recipe

def index(request):
    dough_data = recipe.objects.filter(cat = 'Dough').values()
    sauce_data = recipe.objects.filter(cat = 'Sauce').values()
    pizza_data = recipe.objects.filter(cat = 'Pizza').values()
    data = {
        'dough_data' : dough_data,
        'sauce_data' : sauce_data,
        'pizza_data' : pizza_data
    }
    print(data)
    return render(request,'index.html',data)


def show(request, slug):
    showdata = recipe.objects.filter(name = slug).values()
    ing_data = showdata[0]['ing'].replace('\\n ', '<br><br>🍕 ')
    des_data = showdata[0]['des'].replace('\\n ', '<br><br>👩🏻‍🍳 ')
    des_data = des_data.replace('\\n', '<br>')
    print(ing_data)
    data = {
        'slug' : showdata,
        'ing_data' : ing_data,
        'des_data' : des_data
    }
    return render(request,'recipe.html',data)

def price(request):
    model = load_model()
    print(model)
    choice1 = {'Yes' : 1, 'No' : 0}
    choice2 = {'XL' : 0, 'Jumbo' : 1, 'Large' : 2,'Medium' : 3, 'Reguler' : 4, 'Small' : 5}
    choice3 = {'Beef' : 0, 'Black Papper' : 1, 'Chicken' : 2, 'Meat' : 3, 'Mozzarella' : 4, 'Mushrooms' : 5, 'Onion' : 6, 'Papperoni' : 7, 'Sausage' : 8, 'Smoked Beef' : 9, 'Tuna' : 10, 'Vegetables' : 11}
    list1 = []
    size = [0,0,0,0,0,0]
    topping = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    if request.method == "POST":
        list1.append(int(request.POST['diameter']))
        list1.append(choice1[request.POST['sauce']])
        list1.append(choice1[request.POST['cheese']])
        s = choice2[request.POST['size']]
        size[s] = 1
        list1 = list1 + size
        t = choice3[request.POST['topping']]
        topping[t] = 1
        list1 = list1 + topping
        input_data = pd.DataFrame([list1])
       
        #result = 'The Price of your Pizza is : ' + model.predict(input_data)
        result = make_prediction(model, input_data)
        data = {
            'price' : result
        }
        return render(request, 'price.html', data)

    return render(request,'price.html')