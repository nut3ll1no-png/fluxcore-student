# FluxCore Energy Waste Simulator - Versione 18 anni, zero euro

def calcola_consumo():
    print("=== FluxCore Energy Simulator ===\n")
    
    num_gpus = int(input("Quante GPU hai nel cluster? "))
    watt_per_gpu = float(input("Potenza di una GPU (Watts)? "))
    utilizzo_percent = float(input("Utilizzo medio % (0-100)? ")) / 100
    
    potenza_totale_watt = num_gpus * watt_per_gpu * utilizzo_percent
    consumo_kwh_ora = potenza_totale_watt / 1000
    energia_sprecata_kwh = num_gpus * watt_per_gpu * (1 - utilizzo_percent) / 1000
    gpus_necessarie = int(num_gpus * utilizzo_percent) + 1
    
    print("\n--- RISULTATI ---")
    print(f"Consumo totale attuale: {consumo_kwh_ora:.2f} kWh/ora")
    print(f"Energia sprecata (idle): {energia_sprecata_kwh:.2f} kWh/ora")
    print(f"GPU da tenere accese: {gpus_necessarie} su {num_gpus}")
    print(f"Risparmio possibile: {energia_sprecata_kwh*24*30/1000:.1f} MWh al mese!")

calcola_consumo()
