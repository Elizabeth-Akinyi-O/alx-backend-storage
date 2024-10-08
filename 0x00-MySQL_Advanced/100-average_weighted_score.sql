-- Creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
-- Requirements:- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE w_avg_score FLOAT;
    
    SET w_avg_score = (SELECT SUM(score * weight)/ SUM(weight)
                        FROM users AS U
                        JOIN corrections AS C ON C.user_id=U.id
                        JOIN projects AS P ON C.project_id=P.id
                        WHERE U.id=user_id);
    UPDATE users SET average_score = w_avg_score WHERE users.id=user_id;
END $$
DELIMITER ;
