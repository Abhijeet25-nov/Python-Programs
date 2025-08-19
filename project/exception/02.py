def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai....")
        print("--------------------")
        if flavour =="unknown":
            raise ValueError ("We don't know that flavour")
    except ValueError as e:
        print("Error: ",e)
        print("--------------------")
    else:
        print(f"{flavour} chai is served")
        # print("--------------------")
    finally:
        print("Next customer please")
        # print("--------------------")
        
serve_chai("masala")        
serve_chai("unknown")   
            
            
        