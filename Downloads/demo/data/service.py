from django.http import JsonResponse
from demo import commanResponse

class sumres():
    def summ(self,roll_no,marks,strength,request):
        display =  {}
        select = request.data['select']
        print(select)
        
        if select == 'simulator1': 
            x = roll_no+marks
            y = marks+strength
            z = roll_no+strength
            display['x']=x
            display['y']=y
            display['z']=z
            return display
        
        if select == 'simulator2':
            x = round(roll_no+marks)
            y = round(marks+strength)
            z = round(roll_no+strength)
            display['x']=x
            display['y']=y
            display['z']=z
            return display
        