%% source: http://home2.fvcc.edu/~dhicketh/DiffEqns/spring03projects/MarkJohn/newpursiut.htm
%% example
%% [t,u]=ode45('line1',[0,8],[0;0],.75);
%% [t,u]=ode45(@line1,[0,8],[0;0],.75);
%% x = t-4;
%% y = t;
%% h = plot(x, y, 'k', u(:,1),u(:,2), 'r');
%% legend(h, 'Pursued Curve', 'Pursuit Curve');
%% axis equal;
function Uprime=line1(t,u,k)
Uprime=zeros(2,1);
p=t-4;
q=t;
dp=1;
dq=1;
Uprime(1)=k*sqrt((dp)^2+(dq)^2)*(p-u(1))/sqrt((p-u(1))^2+(q-u(2))^2);
Uprime(2)=k*sqrt((dp)^2+(dq)^2)*(q-u(2))/sqrt((p-u(1))^2+(q-u(2))^2);
