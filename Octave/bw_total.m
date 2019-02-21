
config_graph;

f = [12, 107, 1e3, 2e3, 3e3, 4e3, 15e3, 20e3, 40e3, 48e3, 58e3, 69e3, 74e3, 84e3, 91e3, 103e3, 125e3, 145e3,162e3, 240e3, 300e3, 320e3, 440e3, 510e3];

V0 = [8.64, 8.64, 8.64, 8.64,8.64, 8.64, 8.4, 8.4, 8.08, 8, 7.8, 7.62, 7.44, 7.2, 7.12, 6.8, 6.5, 6, 5.6, 4.4,3.9, 3.2, 2.8, 2.4];

T = V0./0.348;
T = 20*log10(T);


figure
semilogx(f,T,'b*-');
xlabel('Frecuencia [Hz]');
ylabel('Amplitud [dB]');
grid minor

print("bw_total.pdf", "-dpdf")
