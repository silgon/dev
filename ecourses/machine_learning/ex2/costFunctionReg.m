function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

# for i =1:m
#   sgmd=sigmoid(theta'*X(i,:)');
#   J=J-y(i)*log(sgmd)-(1-y(i))*log(1-sgmd);
# end
# J=J/m;


# %penalizig J
# J_pen=lambda*sum(theta(2:end).^2)/(2*m);
# J=J+J_pen;

# for j=1:length(theta)
# dJ=0;
# for i =1:m
#     sgmd=sigmoid(theta'*X(i,:)');
#       dJ=dJ+(sgmd-y(i))*X(i,j);
#       end
# dJ=dJ/m;
# if theta(j)>1
# dJ_pen=lambda/m*theta(j);
# dJ=dJ+dJ_pen;
# end
# grad(j)=dJ;
# end

sgmd=sigmoid(X*theta);
J=sum(-y.*log(sgmd)-(1-y).*log(1-sgmd))/m;
J_pen=lambda*sum(theta(2:end).^2)/(2*m);
J=J+J_pen;

dJ=0;
dJ=X'*(sgmd-y)/m+[0; lambda/m*theta(2:end)];
grad=dJ;




% =============================================================

end
