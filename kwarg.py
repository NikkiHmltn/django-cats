# def test_kwarg(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} === {value}')
# test_kwarg(name="Nikki", age=28, having_fun=True)

# request coming in. use :id route because id="28383"
def home_view(request, **kwargs):
    print(request)

# this will produce an error because of the key called 'id'
# home_view("request", id='user_id')
home_view("request", id="user_id")

# this is an *arg
# ('hello')

#this is a **kwarg
# (greeting='hello)