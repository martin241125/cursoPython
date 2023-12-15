ingreso_mensual = 83200
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('estas bien pa')
    else:
        print('y hay que ver si te alcanza.')
    
    
elif ingreso_mensual > 1000:
    print('estas bien economicamente en latinoamerica')
    
elif ingreso_mensual > 500:
    print('estas bien economicamente en argentina')
    
else:
    print('sos pobre')
    
    