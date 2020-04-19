% Set span 
t0 = 0; 
tf = 15;
% Set initial states
y0 = [20, 20];

% Obtain numerical solutions
[t, y] = ode45('Lotka1', [t0,tf], y0);

% Plot the figure
len = length(y(:,1));
t = 1:1:len;

close all
hold on
plot(t, y(:,1), '-r');
plot(t, y(:,2), '-g');
legend('Predator', 'Prey', 'Location', 'NE');
xlabel('Time');
ylabel('Population size');
