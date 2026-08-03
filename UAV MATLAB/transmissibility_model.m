% Project: Cyber-Physical UAV Flight Controller
% Script: Transmissibility Curve Derivation for IMU Mount

clear; clc; close all;

% System Properties
m = 0.025;      % IMU + Mounting Plate mass (25 grams)
k = 1800;       % Total stiffness of 4 Shore 30A mounts (N/m)
c = 1.2;        % Viscous damping coefficient (N*s/m)

% Derived Parameters
wn = sqrt(k/m);               % Natural angular frequency (rad/s)
fn = wn / (2*pi);             % Natural frequency (Hz)
zeta = c / (2*sqrt(k*m));     % Damping ratio

% Frequency Range (0 to 200 Hz covers standard BLDC motor excitation)
f = linspace(0, 200, 2000);   % Excitation frequency in Hz
w = 2 * pi * f;               % Excitation angular frequency (rad/s)
r = w ./ wn;                  % Frequency ratio

% Calculate Transmissibility Tr
num = 1 + (2 * zeta * r).^2;
den = (1 - r.^2).^2 + (2 * zeta * r).^2;
Tr = sqrt(num ./ den);

% Isolation Boundary Identification
r_iso = sqrt(2);
f_iso = r_iso * fn;

% Plotting
figure('Name', 'IMU Transmissibility Spectrum', 'Color', [1 1 1]);
plot(f, Tr, 'k-', 'LineWidth', 2); hold on;

% Threshold lines
yline(1.0, 'r--', 'LineWidth', 1.2, 'DisplayName', 'Unity (No Isolation)');
xline(fn, 'b:', 'LineWidth', 1.2, 'DisplayName', sprintf('Resonance (f_n = %.1f Hz)', fn));
xline(f_iso, 'g--', 'LineWidth', 1.2, 'DisplayName', sprintf('Isolation Start (%.1f Hz)', f_iso));

% Highlight Isolation Zone
patch([f_iso 200 200 f_iso], [0 0 1 1], [0.8 0.95 0.8], ...
      'FaceAlpha', 0.3, 'EdgeColor', 'none', 'DisplayName', 'Isolation Region (Tr < 1)');

xlabel('Excitation Frequency f (Hz)');
ylabel('Transmissibility T_r');
title('IMU Mount Transmissibility vs Excitation Frequency');
legend('Location', 'northeast');
grid on;
ylim([0 4]);
xlim([0 200]);