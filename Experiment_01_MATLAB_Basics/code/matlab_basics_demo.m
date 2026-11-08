%% SIGNALS AND SYSTEMS LAB - EXPERIMENT 1: MATLAB BASICS
% This script demonstrates the Experiment 1 topics and exercises.
% Run it by opening this file in the MATLAB Editor and pressing Run/F5,
% or type matlab_basics_demo at the Command Window prompt (>>).
% It creates lab_outputs in MATLAB's current folder and saves the session
% log and workspace variables there.

clc; clear; format short g;
outputFolder = fullfile(pwd, 'lab_outputs');
if ~exist(outputFolder, 'dir')
    mkdir(outputFolder);             % Create the folder if it does not exist.
end
diary(fullfile(outputFolder, 'session.txt')); % Record Command Window output.
disp('SIGNALS AND SYSTEMS LAB - EXPERIMENT 1: MATLAB BASICS');

%% 1. Introduction to MATLAB and running commands
% MATLAB accepts commands at the Command Window prompt (>>) and in .m files.
% This command could be typed after >> or placed in this script and run.
introExample = 2 + 3;
disp('Section 1: 2 + 3 evaluates to:'); disp(introExample);
% To execute a script from the Editor, press Run or F5. From the Command
% Window, type its filename without the .m extension and press Enter.

%% 2. MATLAB as a calculator: arithmetic and precedence
% Operators: + addition, - subtraction, * multiplication, / division, ^ power.
additionResult = 8 + 3;             % 11
subtractionResult = 8 - 3;          % 5
multiplicationResult = 8 * 3;       % 24
divisionResult = 8 / 3;             % Approximately 2.6667
powerResult = 2 ^ 4;                % 16
% Parentheses are evaluated first, then powers, then * and / left-to-right,
% then + and - left-to-right.
precedenceResult = 2 + 3/4*5;       % 5.75 = 2 + (3/4)*5
bracketsResult = 2 + 3/(4*5);       % 2.15: parentheses group denominator.
leftToRightResult = 20/5*2;         % 8: / followed by *.
disp('Section 2: [addition subtraction multiplication division power]');
disp([additionResult subtractionResult multiplicationResult divisionResult powerResult]);
disp('Precedence, grouped denominator, left-to-right examples:');
disp([precedenceResult bracketsResult leftToRightResult]);

%% 3. Numbers and display formats
% MATLAB numeric literals are normally double precision. Inf is infinity;
% NaN means Not-a-Number. format changes display, not stored precision.
integerValue = 1362;                % Integer-valued number.
realValue = 1.234;                  % Real number with a fractional part.
complexValue = 3.21 + 4.3i;          % Real plus imaginary component.
infinityValue = 1/0;                % Inf: nonzero divided by zero.
nanValue = 0/0;                     % NaN: undefined result.
disp('Section 3: integer, real, complex, Inf, and NaN:');
disp([integerValue realValue complexValue infinityValue nanValue]);
disp('Display examples: format short, format long, format bank.');

%% 4. Variables, ans, and legal/illegal names
% An expression without assignment is stored in the default variable ans.
7 + 5                              % Displays 12 and stores 12 in ans.
defaultAnswerExample = ans;         % Preserve ans in a named variable.
namedValue = 10;                    % Assignment stores a value by name.
namedValuePlusFive = namedValue + 5;
% Names are case-sensitive; legal names start with a letter, then use
% letters, digits, or underscores.
NetCost = 120;                      % Legal.
Left2Pay = 35;                      % Legal: digit follows a letter.
sample_value = 4;                   % Legal: underscore is allowed.
CaseName = 1; casename = 2;         % Both legal and distinct names.
% ILLEGAL examples below stay comments so this script remains executable:
% 2pay = 10;                        % Illegal: starts with a digit.
% net-cost = 10;                    % Illegal: hyphen is an operator.
% total value = 10;                 % Illegal: spaces are not allowed.
% percent% = 10;                    % Illegal: % begins a comment.
% @sign = 1;                        % Illegal: @ is not a name character.
disp('Section 4: [ans example namedValue namedValuePlusFive]');
disp([defaultAnswerExample namedValue namedValuePlusFive]);
disp('Legal examples: NetCost, Left2Pay, sample_value. See comments for illegal examples.');

%% 5. Suppressing output and multiple statements on one line
% Semicolons suppress automatic display while still executing assignments.
hiddenValue = 6 * 7;                % Stored as 42; not printed automatically.
firstOnLine = 2; secondOnLine = 3; thirdOnLine = firstOnLine + secondOnLine;
% The semicolons above separate multiple statements on one line.
disp('Section 5: values assigned with semicolons, shown explicitly afterward:');
disp([hiddenValue firstOnLine secondOnLine thirdOnLine]);

%% 6. Built-in functions: real and complex examples
% Trigonometric functions use radians; inverse trigonometric functions
% return radians as well.
theta = pi/6;
sinReal = sin(theta);                % 0.5
cosReal = cos(theta);                % About 0.866
tanReal = tan(theta);                % About 0.577
asinReal = asin(0.5);                % pi/6
acosReal = acos(0.5);                % pi/3
atanReal = atan(1);                  % pi/4
sqrtReal = sqrt(9);                  % 3
expReal = exp(1);                    % e
logReal = log(exp(2));               % 2; log is natural logarithm.
log10Real = log10(1000);             % 3; log10 is base-10 logarithm.
absReal = abs(-7);                   % 7
% For z=3+4i, abs is magnitude, angle is phase in radians, real/imag
% extract components, and conj reverses the imaginary sign.
z = 3 + 4i;
absComplex = abs(z);                 % 5
angleComplex = angle(z);             % About 0.9273 radians.
realComplex = real(z);               % 3
imagComplex = imag(z);               % 4
conjComplex = conj(z);               % 3-4i
% Complex examples for the same built-in functions:
sqrtComplex = sqrt(-1);              % 1i, principal square root.
expComplex = exp(1 + 1i);
logComplex = log(-1);                % pi*1i, principal complex logarithm.
sinComplex = sin(1 + 1i);
cosComplex = cos(1 + 1i);
tanComplex = tan(1 + 1i);
asinComplex = asin(2);               % Complex outside real asin domain [-1,1].
acosComplex = acos(2);               % Complex outside real acos domain [-1,1].
atanComplex = atan(1 + 1i);
disp('Section 6: real [sin cos tan asin acos atan]:');
disp([sinReal cosReal tanReal asinReal acosReal atanReal]);
disp('Real [sqrt exp log log10 abs]:'); disp([sqrtReal expReal logReal log10Real absReal]);
disp('Complex [z abs angle real imag conj]:');
disp([z absComplex angleComplex realComplex imagComplex conjComplex]);
disp('Additional complex function results [sqrt exp log sin cos tan]:');
disp([sqrtComplex expComplex logComplex sinComplex cosComplex tanComplex]);
disp('Complex inverse trig results [asin(2) acos(2) atan(1+i)]:');
disp([asinComplex acosComplex atanComplex]);

%% 7. Vectors, colon notation, indexing, and transpose
% Spaces/commas separate row entries. Addition is entry-by-entry for
% vectors of matching size. MATLAB vector indices start at 1.
rowVector = [1 2 3 4];
anotherRow = [10 20 30 40];
rowVectorSum = rowVector + anotherRow; % [11 22 33 44]
rowVectorScaled = 3 * rowVector;       % [3 6 9 12]
thirdElement = rowVector(3);           % 3
% Semicolons inside brackets separate rows and create a column vector.
columnVector = [1; 2; 3; 4];
anotherColumn = [10; 20; 30; 40];
columnVectorSum = columnVector + anotherColumn;
columnVectorScaled = 2 * columnVector;
secondColumnElement = columnVector(2); % 2
% Colon forms: start:stop (step defaults to 1), start:step:stop.
colonDefaultStep = 1:5;               % [1 2 3 4 5]
colonEvenNumbers = 2:2:10;            % [2 4 6 8 10]
colonCountdown = 5:-1:1;              % [5 4 3 2 1]
subVector = rowVector(2:4);            % Entries 2 through 4.
alternateEntries = rowVector(1:2:4);   % Positions 1 and 3: [1 3].
% Apostrophe ' means conjugate transpose; dot-apostrophe .' is plain transpose.
rowAsColumn = rowVector';
columnAsRow = columnVector';
complexRow = [1+3i, 2-2i];
complexConjugateTranspose = complexRow'; % [1-3i; 2+2i]
complexPlainTranspose = complexRow.';    % [1+3i; 2-2i]
disp('Section 7: row vector, sum, scaled vector, third element:');
disp(rowVector); disp(rowVectorSum); disp(rowVectorScaled); disp(thirdElement);
disp('Column vector, sum, scaled vector, second element:');
disp(columnVector); disp(columnVectorSum); disp(columnVectorScaled); disp(secondColumnElement);
disp('Colon vectors and subvectors:');
disp(colonDefaultStep); disp(colonEvenNumbers); disp(colonCountdown);
disp(subVector); disp(alternateEntries);
disp('Complex row, conjugate transpose, plain transpose:');
disp(complexRow); disp(complexConjugateTranspose); disp(complexPlainTranspose);

%% 8. Keeping a record: diary, save, load, who, and whos
% DIARY has recorded Command Window text since the start of this script.
% SAVE stores variables in a MAT-file. LOAD into a structure to avoid
% overwriting existing workspace variables. who/whos list workspace contents.
radius = 5;                         % Example variable included in the MAT-file.
circleArea = pi * radius^2;
variablesFile = fullfile(outputFolder, 'variables.mat');
save(variablesFile);                % Save the current script workspace.
loadedVariables = load(variablesFile); % Load saved data into a structure.
loadedRadius = loadedVariables.radius;
disp('Section 8: who lists variable names:'); who;
disp('whos lists names, sizes, bytes, and classes:'); whos;
disp('Radius read back from the MAT-file:'); disp(loadedRadius);

%% 9. Exercises
% Exercise 1.1: y = 2*cos(exp(1-4j)); report magnitude and phase in radians.
% Use 1i explicitly so the imaginary unit is not affected if i was reassigned.
exercise1Y = 2*cos(exp(1 - 4*1i));
exercise1Magnitude = abs(exercise1Y);
exercise1PhaseRadians = angle(exercise1Y);

% Exercise 1.2 in the photo is y=5*x^3+2*x^2+9*x+16 at x=2.
exercise2X = 2;
exercise2YFromPhoto = 5*exercise2X^3 + 2*exercise2X^2 + 9*exercise2X + 16; % 82
% The typed request omits the powers: y=5*x+2*x+9*x+16 at x=2 gives 48.
exercise2YTyped = 5*exercise2X + 2*exercise2X + 9*exercise2X + 16;

% Exercise 1.3 as typed gives v=[5 4], v1=[5 4], and v+v1=[10 8].
% In the photo, spacing appears to show v=[2+3 4] and v1=[2 +3 4]. MATLAB
% reads those as [5 4] and [2 3 4], different lengths, so addition errors.
exercise3V = [2+3 4];
exercise3V1 = [2+3 4];
exercise3SumAsTyped = exercise3V + exercise3V1;

disp('Exercise 1.1: [y magnitude phase in radians]:');
disp([exercise1Y exercise1Magnitude exercise1PhaseRadians]);
disp('Exercise 1.2 from photo, x=2 (5*x^3+2*x^2+9*x+16):'); disp(exercise2YFromPhoto);
disp('Exercise 1.2 as typed, x=2 (5*x+2*x+9*x+16):'); disp(exercise2YTyped);
disp('Exercise 1.3 as typed: v, v1, and v+v1:');
disp(exercise3V); disp(exercise3V1); disp(exercise3SumAsTyped);

% Save again so the MAT-file also contains the exercise results.
save(variablesFile);
diary off;                          % Close lab_outputs/session.txt.
disp('Finished. See lab_outputs/session.txt and lab_outputs/variables.mat.');
