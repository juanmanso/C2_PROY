# Script para comparar mediciones


close all
clear all;

o1="./Mediciones/t1_______ic(vbe).txt"; %Blanco
o2="./Mediciones/t2_______ic(vbe).txt"; %Negro
o3="./Mediciones/t3_______ic(vbe).txt";	%Naraja

m1=dlmread(o1,'|',1,0);
m2=dlmread(o2,'|',1,0);
m3=dlmread(o3,'|',1,0);

figure
plot(m1(1,:),m1(2,:),"ro");

figure
plot(m2(1,:),m2(2,:),"go");

figure
plot(m3(1,:),m3(2,:),"bo");

figure
hold on;
plot(m1(1,:),m1(2,:),"ro");
plot(m2(1,:),m2(2,:),"go");
plot(m3(1,:),m3(2,:),"bo");
