%% source: http://home2.fvcc.edu/~dhicketh/DiffEqns/spring03projects/MarkJohn/newpursiut.htm
%% example
%% [t,u]=ode45('circle',[0,6],[0;0],1); %% matlab
%% [t,u]=ode45(@circle,[0,6],[0;0],1); %% octave
%% x = cos(t);
%% y = sin(t);
%% h = plot(x, y, 'k', u(:,1),u(:,2), 'r');
%% legend(h, 'Pursued Curve', 'Pursuit Curve');
%% axis equal;
function Uprime=circle(t,u,k)
Uprime=zeros(2,1);
p=cos(t);
q=sin(t);
dp=-sin(t);
dq=cos(t);
Uprime(1)=k*sqrt((dp)^2+(dq)^2)*(p-u(1))/sqrt((p-u(1))^2+(q-u(2))^2);
Uprime(2)=k*sqrt((dp)^2+(dq)^2)*(q-u(2))/sqrt((p-u(1))^2+(q-u(2))^2);

