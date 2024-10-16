DELIMITER //

CREATE PROCEDURE print_pattern(IN R INT) BEGIN DECLARE i INT; SET i = R; WHILE i > 0 DO SELECT REPEAT('* ', i) AS pattern; SET i = i - 1; END WHILE; END //

DELIMITER ;

CALL print_pattern(20);