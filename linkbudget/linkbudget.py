import math

def linkbudget():

    Fc = int(input("Inserisci la frequenza portante: "))

    wavelength = (3.0e8/(Fc * 1.0e6))

    print("lambda: ", wavelength);

    Ptx = float(input("Inserisci la potenza in trasmissione (dBm): "))
    Atx = float(input("Inserisci attenuazione in trasmissione (dB): "))
    Btx = float(input("Inserisci amplificazione in trasmissione (dB): "))
    Gtx = float(input("Inserisci guadagno antenne in trasmissione (dB): "))
    Arx = float(input("Inserisci attenuazione in ricezione (dB): "))
    Brx = float(input("Inserisci amplificazione in ricezione (dB): "))
    Grx = float(input("Inserisci guadagno antenne in ricezione (dB): "))
    Snr = float(input("Inserisci SNR garantito (dB): "));
    Pn = float(input("Inserisci potenza del rumore (dB): "));

    Prx = Snr + Pn;

    Lp = (Ptx + Btx - Atx) - (Prx - Brx + Arx) + Gtx + Grx 

    d = ((wavelength * (math.pow(10, Lp / 20)) / (4 * math.pi)))

    print("Distanza totale: %f metri" % (d));

linkbudget()