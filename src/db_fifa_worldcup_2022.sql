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
  `match_time_in_min` BIGINT NULL DEFAULT NULL)
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
  `match_id` BIGINT NULL DEFAULT NULL,
  `competition_id` BIGINT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`metricas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`metricas` (
  `match_id` BIGINT NULL DEFAULT NULL,
  `team` TEXT NULL DEFAULT NULL,
  `corners` BIGINT NULL DEFAULT NULL,
  `faltas_lanzadas` BIGINT NULL DEFAULT NULL,
  `faltas_directas_lanzadas` BIGINT NULL DEFAULT NULL,
  `faltas_realizadas` BIGINT NULL DEFAULT NULL,
  `penaltis` BIGINT NULL DEFAULT NULL,
  `penaltis_marcados` BIGINT NULL DEFAULT NULL,
  `%_acierto_penaltis` TEXT NULL DEFAULT NULL,
  `saques_banda` BIGINT NULL DEFAULT NULL,
  `saques_banda_recepcionados` BIGINT NULL DEFAULT NULL,
  `%_acierto_sb` DOUBLE NULL DEFAULT NULL,
  `ofrecimientos` BIGINT NULL DEFAULT NULL,
  `ofrecimientos_con_movimiento` BIGINT NULL DEFAULT NULL,
  `ofrecimientos_con_movimiento_camp_contr` BIGINT NULL DEFAULT NULL,
  `ofrecimientos_con_movimiento_ult_terc` BIGINT NULL DEFAULT NULL,
  `remates_totales` BIGINT NULL DEFAULT NULL,
  `remates_totales_fa` BIGINT NULL DEFAULT NULL,
  `remates_on_target` BIGINT NULL DEFAULT NULL,
  `remates_on_target_fa` BIGINT NULL DEFAULT NULL,
  `remates_off_target` BIGINT NULL DEFAULT NULL,
  `%_remates_on_target` DOUBLE NULL DEFAULT NULL,
  `goles` BIGINT NULL DEFAULT NULL,
  `goles_fa` BIGINT NULL DEFAULT NULL,
  `%_gol/on_target` DOUBLE NULL DEFAULT NULL,
  `goles_concedidos` BIGINT NULL DEFAULT NULL,
  `centros_totales` BIGINT NULL DEFAULT NULL,
  `centros_completados` BIGINT NULL DEFAULT NULL,
  `asistencias_centro` BIGINT NULL DEFAULT NULL,
  `pases` BIGINT NULL DEFAULT NULL,
  `pases_completados` BIGINT NULL DEFAULT NULL,
  `%_acierto_pases` DOUBLE NULL DEFAULT NULL,
  `pases_completados_linebreak` BIGINT NULL DEFAULT NULL,
  `asistencias_pase` BIGINT NULL DEFAULT NULL,
  `cambios_de_juego` BIGINT NULL DEFAULT NULL,
  `pases_ultimo_tercio` BIGINT NULL DEFAULT NULL,
  `pases_completados_ultimo_tercio` BIGINT NULL DEFAULT NULL,
  `progresiones` BIGINT NULL DEFAULT NULL,
  `intentos_regate` BIGINT NULL DEFAULT NULL,
  `intentos_regate_ult_terc` BIGINT NULL DEFAULT NULL,
  `regates_completados` BIGINT NULL DEFAULT NULL,
  `regates_completados_ult_terc` BIGINT NULL DEFAULT NULL,
  `recepciones` BIGINT NULL DEFAULT NULL,
  `recep_behind` BIGINT NULL DEFAULT NULL,
  `recep_3_4` BIGINT NULL DEFAULT NULL,
  `recep_2_3` BIGINT NULL DEFAULT NULL,
  `recep_1_2` BIGINT NULL DEFAULT NULL,
  `recep_inside` BIGINT NULL DEFAULT NULL,
  `%_recep_inside` DOUBLE NULL DEFAULT NULL,
  `recep_outside` BIGINT NULL DEFAULT NULL,
  `%_recep_outside` DOUBLE NULL DEFAULT NULL,
  `recep_ultimo_tercio` BIGINT NULL DEFAULT NULL,
  `bloqueos` BIGINT NULL DEFAULT NULL,
  `despejes` BIGINT NULL DEFAULT NULL,
  `intercepciones` BIGINT NULL DEFAULT NULL,
  `entradas_totales` BIGINT NULL DEFAULT NULL,
  `entradas_exitosas` BIGINT NULL DEFAULT NULL,
  `%_entradas_exitosas` DOUBLE NULL DEFAULT NULL,
  `take_on_against` BIGINT NULL DEFAULT NULL,
  `pushing-on` BIGINT NULL DEFAULT NULL,
  `presiones` BIGINT NULL DEFAULT NULL,
  `presiones_directas` BIGINT NULL DEFAULT NULL,
  `%_presion_directa` DOUBLE NULL DEFAULT NULL,
  `gk_active_eng` BIGINT NULL DEFAULT NULL,
  `gk_aerial_control` BIGINT NULL DEFAULT NULL,
  `gk_def_support` BIGINT NULL DEFAULT NULL,
  `gk_goalprevention_tot` BIGINT NULL DEFAULT NULL,
  `gk_goalprevention_tot_saved` BIGINT NULL DEFAULT NULL,
  `duelos_totales` BIGINT NULL DEFAULT NULL,
  `duelos_totales_ganados` BIGINT NULL DEFAULT NULL,
  `%_duelos_totales_ganados` BIGINT NULL DEFAULT NULL,
  `duelos_campo_ganados` BIGINT NULL DEFAULT NULL,
  `duelos_físicos_ganados` BIGINT NULL DEFAULT NULL,
  `duelos_aereos_ganados` BIGINT NULL DEFAULT NULL,
  `sustituciones` BIGINT NULL DEFAULT NULL,
  `posesion` DOUBLE NULL DEFAULT NULL,
  `posesión_disputa` DOUBLE NULL DEFAULT NULL,
  `pases_verticales` BIGINT NULL DEFAULT NULL,
  `pases_adelante` BIGINT NULL DEFAULT NULL,
  `pases_atras` BIGINT NULL DEFAULT NULL,
  `pases_horizontales` BIGINT NULL DEFAULT NULL,
  `%_pases_verticales` BIGINT NULL DEFAULT NULL,
  `%_pases_adelante` BIGINT NULL DEFAULT NULL,
  `%_pases_atras` BIGINT NULL DEFAULT NULL,
  `%_pases_horizontales` BIGINT NULL DEFAULT NULL,
  `recuperaciones` BIGINT NULL DEFAULT NULL,
  `recuperaciones_campo_contr` BIGINT NULL DEFAULT NULL,
  `%_recuperaciones_campo_contr` BIGINT NULL DEFAULT NULL,
  `recuperaciones_campo_prop` BIGINT NULL DEFAULT NULL,
  `%_recuperaciones_campo_prop` BIGINT NULL DEFAULT NULL,
  `recuperaciones1` BIGINT NULL DEFAULT NULL,
  `recuperaciones_campo_contr1` BIGINT NULL DEFAULT NULL,
  `%_recuperaciones_campo_contr1` BIGINT NULL DEFAULT NULL,
  `recuperaciones_campo_prop1` BIGINT NULL DEFAULT NULL,
  `%_recuperaciones_campo_prop1` BIGINT NULL DEFAULT NULL,
  `perdidas` BIGINT NULL DEFAULT NULL,
  `perdidas_campo_prop` BIGINT NULL DEFAULT NULL,
  `%_perdidas_campo_prop` BIGINT NULL DEFAULT NULL,
  `tarj_amarillas` BIGINT NULL DEFAULT NULL,
  `tarjetas_rojas` BIGINT NULL DEFAULT NULL,
  `asistencias_totales` BIGINT NULL DEFAULT NULL,
  `xG` DOUBLE NULL DEFAULT NULL,
  `distancia_recorrida_km` DOUBLE NULL DEFAULT NULL,
  `n_speed_runs_(15-20km/h)` BIGINT NULL DEFAULT NULL,
  `n_of_sprints_(>20km/h)` BIGINT NULL DEFAULT NULL,
  `total_average_speed_(km/h)` DOUBLE NULL DEFAULT NULL)
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
  PRIMARY KEY (`player_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fifa_worldcup_2022`.`teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fifa_worldcup_2022`.`teams` (
  `team_id` BIGINT NULL DEFAULT NULL,
  `team_name` TEXT NULL DEFAULT NULL,
  `team_code` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
