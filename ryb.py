import time
def sarki():
    lines = [
        ("I wanna da-", 1.0),
        ("I wanna dance in the lights", 2.5),
        ("I wanna ro-", 0.9),
        ("I wanna rock your body", 2.7),
        ("I wanna go", 1.3),
        ("I wanna go for a ride", 2.5),
        ("Hop in the music and", 1.9),
        ("Rock your body", 1.85 ),
        ("Rock that body", 1.1),
        ("Come on, come on", 1.0),
        ("Rock that body", 1.1),
        ("Rock your body", 1.1),
        ("Rock that body", 1.0),
        ("Come on, come on", 0.9),
        ("Rock that body", 1.8),
        ("Rock that body", 1.1),
        ("Come on, come on", 1.0),
        ("Rock that body", 1.1),
        ("Rock your body", 1.1),
        ("Rock that body", 1.0),
        ("Come on, come on", 0.9),
        ("Rock that body", 1.7)
    ]
    for text, delay in lines:
        sozler = text.split()  
        duraklama = delay / max(len(sozler), 1)  
        for sozler in sozler:
            print(sozler, end=' ', flush=True)
            time.sleep(duraklama)
        print() 
sarki()