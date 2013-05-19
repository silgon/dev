function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%
poly=X*theta;
J=sum((poly-y).^2)/(2*m);
J_pen=lambda*sum(theta(2:end).^2)/(2*m);
J=J+J_pen;

dJ=0;
dJ=X'*(poly-y)/m+[0; lambda/m*theta(2:end)];
grad=dJ;












% =========================================================================

grad = grad(:);

end
