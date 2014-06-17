clear all; clc; 
format short
format compact

% Two input: R and gamma
% immediate reward matrix;
% row and column = states; -Inf = no door between room
R=[-inf,-inf,-inf,-inf,   0, -inf;
    -inf,-inf,-inf,   0,-inf, 100;
    -inf,-inf,-inf,   0,-inf, -inf;
    -inf,   0,   0,-inf,   0, -inf;
    0,-inf,-inf,   0,-inf, 100;
    -inf,   0,-inf,-inf,   0, 100];

gamma=0.80;            % learning parameter
goalState=6;

q=zeros(size(R));      % initialize Q as zero
q1=ones(size(R))*inf;  % initialize previous Q as big number
count=0;               % counter

for episode=0:5000
    % random initial state
    y=randperm(size(R,1));
    state=y(1);
    while state~=goalState,            % loop until reach goal state
        % select any action from this state
        x=find(R(state,:)>=0);        % find possible action of this state
        if size(x,1)>0
            x1 = x(randperm(size(x,2))); % randomize the possible action
            x1=x1(1);                  % select an action
        end
        qMax=max(q,[],2);
        q(state,x1)= R(state,x1)+gamma*qMax(x1);   % get max of all actions
        state=x1;
    end
    % break if convergence: small deviation on q for 1000 consecutive
    if sum(sum(abs(q1-q)))<0.0001 & sum(sum(q >0))
            episode        % report last episode
            break          % for
    else
        q1=q;
    end
end
%normalize q
g=max(max(q));
if g>0
    q=100*q/g;
end
