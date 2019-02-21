
config_graph;

f = [4.16, 10, 24, 53, 104, 470, 1e3, 6.3e3, 18e3, 21e3, 32e3, 51e3, 61e3, 98e3,150e3,240e3];

V0 = [51.2, 51.6, 51.6, 52, 52.4, 52.4, 52.4, 52.4, 52, 52, 51.2, 48.8, 47.6, 42.8, 34, 23];

T = V0./0.174;
T = 20*log10(T);


figure
semilogx(f,T,'b.-');
xlabel('Frecuencia [\si{\Hz}]');
ylabel('Amplitud [\si{\dB}]');
grid minor

