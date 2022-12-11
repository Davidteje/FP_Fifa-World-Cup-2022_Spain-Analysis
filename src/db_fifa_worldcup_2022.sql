-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema fifa_worldcup_2022
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema fifa_worldcup_2022
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `fifa_worldcup_2022` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `fifa_worldcup_2022` ;

-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`teams` (
  `team_id` BIGINT NOT NULL,
  `team_name` TEXT NULL DEFAULT NULL,
  `team_code` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`team_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`matches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`matches` (
  `match_date` DATETIME NULL DEFAULT NULL,
  `match_time` BIGINT NULL DEFAULT NULL,
  `match_number` BIGINT NULL DEFAULT NULL,
  `competition_name` TEXT NULL DEFAULT NULL,
  `city` TEXT NULL DEFAULT NULL,
  `stadium` TEXT NULL DEFAULT NULL,
  `team_1` TEXT NULL DEFAULT NULL,
  `team_2` TEXT NULL DEFAULT NULL,
  `group` TEXT NULL DEFAULT NULL,
  `attendance` DOUBLE NULL DEFAULT NULL,
  `match_id` BIGINT NOT NULL,
  `competition_id` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`match_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`events` (
  `match_id` BIGINT NULL DEFAULT NULL,
  `match_run_time_in_ms` BIGINT NULL DEFAULT NULL,
  `match_run_time` TEXT NULL DEFAULT NULL,
  `match_time_in_ms` BIGINT NULL DEFAULT NULL,
  `event_id` BIGINT NULL DEFAULT NULL,
  `player_seq_id` BIGINT NULL DEFAULT NULL,
  `event_order` BIGINT NULL DEFAULT NULL,
  `half_time` BIGINT NULL DEFAULT NULL,
  `side` TEXT NULL DEFAULT NULL,
  `category` TEXT NULL DEFAULT NULL,
  `event` TEXT NULL DEFAULT NULL,
  `event_type` TEXT NULL DEFAULT NULL,
  `action_type` TEXT NULL DEFAULT NULL,
  `from_player_id` BIGINT NULL DEFAULT NULL,
  `from_player_name` TEXT NULL DEFAULT NULL,
  `from_player_shirt_number` BIGINT NULL DEFAULT NULL,
  `to_player_id` DOUBLE NULL DEFAULT NULL,
  `to_player_name` TEXT NULL DEFAULT NULL,
  `to_player_shirt_number` DOUBLE NULL DEFAULT NULL,
  `team_id` BIGINT NULL DEFAULT NULL,
  `team_name` TEXT NULL DEFAULT NULL,
  `sequence_type` TEXT NULL DEFAULT NULL,
  `outcome` TEXT NULL DEFAULT NULL,
  `outcome_additional` TEXT NULL DEFAULT NULL,
  `opposition_touch` TEXT NULL DEFAULT NULL,
  `body_type` TEXT NULL DEFAULT NULL,
  `direction` TEXT NULL DEFAULT NULL,
  `pressure` TEXT NULL DEFAULT NULL,
  `style` TEXT NULL DEFAULT NULL,
  `style_additional` TEXT NULL DEFAULT NULL,
  `frame_location` TEXT NULL DEFAULT NULL,
  `game_state` TEXT NULL DEFAULT NULL,
  `origin` TEXT NULL DEFAULT NULL,
  `origin_additional` TEXT NULL DEFAULT NULL,
  `save_type` TEXT NULL DEFAULT NULL,
  `save_detail` TEXT NULL DEFAULT NULL,
  `stance` TEXT NULL DEFAULT NULL,
  `x_frame` DOUBLE NULL DEFAULT NULL,
  `y_frame` DOUBLE NULL DEFAULT NULL,
  `movement` TEXT NULL DEFAULT NULL,
  `offering_to_receive_total_units` DOUBLE NULL DEFAULT NULL,
  `line_break_direction` TEXT NULL DEFAULT NULL,
  `line_break_outcome` TEXT NULL DEFAULT NULL,
  `team_shape` TEXT NULL DEFAULT NULL,
  `team_unit` TEXT NULL DEFAULT NULL,
  `team_units_broken` TEXT NULL DEFAULT NULL,
  `total_team_units` DOUBLE NULL DEFAULT NULL,
  `event_end_time_in_ms` DOUBLE NULL DEFAULT NULL,
  `x` DOUBLE NULL DEFAULT NULL,
  `x_mirrored` DOUBLE NULL DEFAULT NULL,
  `y` DOUBLE NULL DEFAULT NULL,
  `y_mirrored` DOUBLE NULL DEFAULT NULL,
  `x_location_start` DOUBLE NULL DEFAULT NULL,
  `x_location_start_mirrored` DOUBLE NULL DEFAULT NULL,
  `x_location_end` DOUBLE NULL DEFAULT NULL,
  `x_location_end_mirrored` DOUBLE NULL DEFAULT NULL,
  `y_location_start` DOUBLE NULL DEFAULT NULL,
  `y_location_start_mirrored` DOUBLE NULL DEFAULT NULL,
  `y_location_end` DOUBLE NULL DEFAULT NULL,
  `y_location_end_mirrored` DOUBLE NULL DEFAULT NULL,
  `x_abs` DOUBLE NULL DEFAULT NULL,
  `y_abs` DOUBLE NULL DEFAULT NULL,
  `x_location_start_abs` DOUBLE NULL DEFAULT NULL,
  `y_location_start_abs` DOUBLE NULL DEFAULT NULL,
  `x_location_end_abs` DOUBLE NULL DEFAULT NULL,
  `y_location_end_abs` DOUBLE NULL DEFAULT NULL,
  `match_time_in_min` BIGINT NULL DEFAULT NULL,
  INDEX `fk_events_teams1_idx` (`team_id` ASC) VISIBLE,
  INDEX `fk_events_matches1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_events_teams1`
    FOREIGN KEY (`team_id`)
    REFERENCES `fifa_worldcup_2022`.`teams` (`team_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_events_matches1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fifa_worldcup_2022`.`matches` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`players` (
  `competition_id` BIGINT NULL DEFAULT NULL,
  `team_id` BIGINT NULL DEFAULT NULL,
  `team` TEXT NULL DEFAULT NULL,
  `player_id` BIGINT NOT NULL,
  `player_shirt_number` BIGINT NULL DEFAULT NULL,
  `player_position` TEXT NULL DEFAULT NULL,
  `player_name` TEXT NULL DEFAULT NULL,
  `player_first_name` TEXT NULL DEFAULT NULL,
  `player_last_name` TEXT NULL DEFAULT NULL,
  `player_date_birth` DATETIME NULL DEFAULT NULL,
  `team_code` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`player_id`),
  INDEX `fk_players_teams_idx` (`team_id` ASC) VISIBLE,
  CONSTRAINT `fk_players_teams`
    FOREIGN KEY (`team_id`)
    REFERENCES `fifa_worldcup_2022`.`teams` (`team_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
