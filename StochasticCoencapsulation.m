%% Stochastic Coencapsulation
% Calculation of the probability for a droplet encapsulates different
% number of strains. 
% The outcome of the code are stored in M_all and p
% M_all contains of rows of different combo (n1, n2, ..., n10), which means
% n1 cells of strain#1, n2 cells of strain #2, etc
% the probability of combo described by row j in M_all is stored in the jth
% element of p.

clear;

%% Input
% Number of strains
N = 10;

% Lambdas for each strain
lambda_i = 1;
% Assume same lambda for all strains
lambda = lambda_i*ones(1, N);
lambda_all = sum(lambda);

% Maximum number of a single strain considered
m = 2 * lambda_i;

% Total number of droplets generated
n_total_drop = 1e6;

%% Event Space
% Each row in matrix M_all consists of N numbers [n1, n2, ...], 
% representing the event of n1 strain#1, n2 strain#2, .... etc.

% v = repmat(0:m,1,N);
% M_all = nchoosek(v,N);
% rows of possible combinations
% M_all = unique(M_all,'rows'); 

% Initialize the matrix with all 0s
M_all = zeros((m+1)^N, N);

% Populate the matrix with all possible combinations
for i = 1:N
    v_i = repmat(0:m, 1, (m+1)^(i-1));
    v_ij = repmat(v_i, (m+1)^(N-i), 1);
    M_all(:,i) = v_ij(:);
end

%% Probability of Different Combinations in One Droplet
lambda_M = repmat(lambda, size(M_all, 1), 1);
p_i = poisspdf(M_all(:), lambda_M(:));
p_M = reshape(p_i, size(M_all));
% Calculate the overall probability along each row
p = prod(p_M, 2);

%% Truncate and Sort Event Space
prob_thres = 1 / n_total_drop;
% Sort all event probabilities in descending order
[p_descend, ind] = sort(p, 'descend');
% Find the cutoff index for probability threshold and truncate the rest
ind_thres = sum(p_descend >= prob_thres);
p = p_descend(1:ind_thres);
M_filter = M_all(ind(1:ind_thres),:);
