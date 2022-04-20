import machine,time,dht

d = dht.DHT11(machine.Pin(1)) # Set data pin

while True:
    d.measure() # Measure and read data once.
    print("Temp={0}℃,RH={1}%".format(d.temperature(),d.humidity()))
    time.sleep(1)
    