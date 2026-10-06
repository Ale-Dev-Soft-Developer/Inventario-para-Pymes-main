from auxiliares.menu import menu_superior, menu_productos, menu_bodega



def menu_principal():
        print("Bienvenido a la Bodega")
    
        while(True):
            
            for clave, valor in menu_superior.items():
                print(f"[{clave}]- {valor}")
            
            try: 
                respuesta_usuario = int(input("Ingresa tu opcion: "))
            
                if respuesta_usuario == 1:
                    print("1")
                elif respuesta_usuario == 2:
                                print("2")
                elif respuesta_usuario == 3:
                    print("Saliendo...")
                    break
                else:
                    print("Opcion invalida")
            except(ValueError):
                print("Ingresa solo numeros. No se permiten palabras.")
                                
            
    
    
    