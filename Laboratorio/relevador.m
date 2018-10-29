close all;
clear all;

c = -1;

% Establesco la configuración particular: Cantidad de mediciones y archivo de salida
MAX_MED=60;
mkdir "Mediciones";
output_file_name="./Mediciones/i_vs_v.txt";



I_med=zeros(1,MAX_MED);
V_med=zeros(1,MAX_MED);
%s_x=input("Variable independiente")
%s_y=input("Variable dependiente")
s_V="Tension\n";
s_I="Corriente\n";


#### Relevamiento ####
% Para cortar manualmente, introducir 0's %
subindex=1;
puts("Para cortar manualmente, introducir 0\n");
while (c!=0 && subindex<=MAX_MED)
	c=input([s_V]);
	V_med(subindex)=c;	
	c=input([s_I]);
	I_med(subindex)=c;
	subindex++;
endwhile
% Si cortó manualmente o si cortó por cantidad máxima (el subínidice es mayor al máximo), el subindice está "adelantado" en ambos.
subindex--; 

% Si cortó manualmente, se guardaron los 0's de corte y hay que sacarlos.
if(subindex<MAX_MED)
	subindex-=1;
endif;


# Exporto los datos relevados #
header=sprintf("Medicion de Corriente [mA] vs. Tensión [V] | Cantidad de mediciones = %i | Primera Fila: V_CE - Segunda Fila: I_C | Icmax = 7,5mA",subindex);
dlmwrite(output_file_name,header,"")
dlmwrite(output_file_name,[V_med(1:subindex);I_med(1:subindex)],'|',"-append");


# Gráficos para verificar las mediciones
figure
title("Plot en lineal")
plot(V_med(1:subindex),I_med(1:subindex),"-ro","Markersize",5)

%return;

figure
title("Plot con y logarítmico")
semilogy(V_med(1:subindex),I_med(1:subindex),"-g","LineWidth",3)

return;

