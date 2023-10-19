% Define a predicate to check if a triangle is a right triangle
is_right_triangle(Angle1, Angle2, Angle3) :-
    % Ensure that the angles add up to 180 degrees
    TotalAngle is Angle1 + Angle2 + Angle3,
    TotalAngle =:= 180,
    % Check if one of the angles is 90 degrees
    (Angle1 = 90; Angle2 = 90; Angle3 = 90).

% Example usage:
% You can call the is_right_triangle predicate with the angles of your triangle.
% For example, is_right_triangle(90, 45, 45) will return true because it's a right triangle.
% is_right_triangle(45, 45, 90)
