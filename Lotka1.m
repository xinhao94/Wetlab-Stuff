function dy = Lotka1(t, y)

dy = zeros(2,1);

% Set parameters
alpha = 0.01;
beta = 0.02;

% Set function
dy(1) = y(1) - alpha*y(1)*y(2);
dy(2) = -y(2) + beta*y(1)*y(2);
end
