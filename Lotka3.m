function dy = Lotka3(t, y)

dy = zeros(2,1);

% Set parameters
r1 = 2; 
r2 = 1.;
alpha21 = -0.1;
alpha12 = -0.1;
K = 1000;

% Set function
dy(1) = r1*y(1)*(1-(y(1)+alpha21*y(2))/(K-y(2)));
dy(2) = r2*y(2)*(1-(y(2)+alpha12*y(1))/(K-y(1)));
end
