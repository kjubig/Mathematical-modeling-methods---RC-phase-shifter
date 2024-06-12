import numpy as np
import matplotlib.pyplot as plt

def main():
    print("PROJEKT MMM - ZADANIE 16 - ŁUKASZ KUBIK 193178 & NIKODEM KOZAK 193388")
    
    # Pobieranie wartości od użytkownika
    C1 = float(input("Podaj wartość C1 (Farady): "))
    C2 = float(input("Podaj wartość C2 (Farady): "))
    R1 = float(input("Podaj wartość R1 (Ohmy): "))
    R2 = float(input("Podaj wartość R2 (Ohmy): "))

    # Stałe w programie
    h = 0.001  # krok obliczeń
    T = 100.0  # całkowity czas symulacji – przedział [0, T]
    L = 2.5  # liczba okresów sygnału sinus w przedziale T
    M = 1.0  # amplituda sygnału sinus i skoku jednostkowego
    PI = np.pi  # liczba PI

    # zmienne globalne w programie
    total = int(T / h) + 1
    u_sinus = np.zeros(total)  # sygnał wejściowy (sinus)
    y_sinus = np.zeros(total)  # sygnał wyjściowy (sinus)
    u1p = np.zeros(total)  # pierwsza pochodna sygnału sinusoidalnego
    u2p = np.zeros(total)  # druga pochodna sygnału sinusoidalnego
    y1p_sinus = np.zeros(total)  # pierwsza pochodna sygnału wyjściowego (sinus)
    y2p_sinus = np.zeros(total)  # druga pochodna sygnału wyjściowego (sinus)
    

    u_step = np.zeros(total)  # sygnał wejściowy (skok jednostkowy)
    y_step = np.zeros(total)  # sygnał wyjściowy (skok jednostkowy)
    y1p_step = np.zeros(total)  # pierwsza pochodna sygnału wyjściowego (skok)
    y2p_step = np.zeros(total)  # druga pochodna sygnału wyjściowego (skok)

    # wczytanie parametrów modelu
    a2 = 1
    a1 = (R1*C1+R1*C2+R2*C2)/(R1*C1*R2*C2)
    a0 = 1/(R1*C1*R2*C2)
    b2 = 0
    b1 = 0
    b0 = 1/(R1*C1*R2*C2)

    # Obliczanie częstotliwości sinusoidy
    w = 2.0 * PI * L / T

    # sygnał wejściowy i jego pochodne (sinusoidalny)
    for i in range(total):
        t = i * h
        u_sinus[i] = M * np.sin(w * t)  # sygnał wejściowy: u=M*sin(w*t)
        u1p[i] = M * w * np.cos(w * t)  # pochodna 1: u'(t)
        u2p[i] = -M * w * w * np.sin(w * t)  # pochodna 2: u''(t)

        u_step[i] = M  # sygnał wejściowy: skok jednostkowy

    # zerowe warunki początkowe
    y_sinus[0] = 0
    y1p_sinus[0] = 0
    y2p_sinus[0] = 0
    y_step[0] = 0
    y1p_step[0] = 0
    y2p_step[0] = 0

    # główna pętla obliczeń (sinusoidalny)
    for i in range(total - 1):
        y2p_sinus[i] = -a1 * y1p_sinus[i] - a0 * y_sinus[i] + b2 * u2p[i] + b1 * u1p[i] + b0 * u_sinus[i]
        y1p_sinus[i + 1] = y1p_sinus[i] + h * y2p_sinus[i]
        y_sinus[i + 1] = y_sinus[i] + h * y1p_sinus[i] + (h * h / 2.0) * y2p_sinus[i]

    # główna pętla obliczeń (skok jednostkowy)
    for i in range(total - 1):
        y2p_step[i] = -a1 * y1p_step[i] - a0 * y_step[i] + b2 * 0 + b1 * 0 + b0 * u_step[i]
        y1p_step[i + 1] = y1p_step[i] + h * y2p_step[i]
        y_step[i + 1] = y_step[i] + h * y1p_step[i] + (h * h / 2.0) * y2p_step[i]

    # Tworzenie wykresu sygnałów
    time = np.arange(0, T + h, h)

    plt.figure(figsize=(12, 10))

    # Wykres sygnału wejściowego (sinusoidalny)
    plt.subplot(4, 1, 1)
    plt.plot(time, u_sinus, label='Sygnał wejściowy (sinusoidalny)')
    plt.title('Sygnał wejściowy i wyjściowy (sinusoidalny)')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid()

    # Wykres sygnału wyjściowego (sinusoidalny)
    plt.subplot(4, 1, 2)
    plt.plot(time, y_sinus, label='Sygnał wyjściowy (sinusoidalny)', color='orange')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid()

    # Wykres sygnału wejściowego (skok jednostkowy)
    plt.subplot(4, 1, 3)
    plt.plot(time, u_step, label='Sygnał wejściowy (skok jednostkowy)')
    plt.title('Sygnał wejściowy i wyjściowy (skok jednostkowy)')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid()

    # Wykres sygnału wyjściowego (skok jednostkowy)
    plt.subplot(4, 1, 4)
    plt.plot(time, y_step, label='Sygnał wyjściowy (skok jednostkowy)', color='orange')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig('MMM.png')


if __name__ == "__main__":
    main()
