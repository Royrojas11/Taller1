-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-05-2022 a las 22:24:14
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle`
--

CREATE TABLE `detalle` (
  `iddetalle` int(10) NOT NULL,
  `idreserva` int(10) NOT NULL,
  `respusta` varchar(250) NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documentos`
--

CREATE TABLE `documentos` (
  `iddocumento` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `documentos`
--

INSERT INTO `documentos` (`iddocumento`, `nombre`, `estado`) VALUES
(1, 'Permiso de Permanencia', 'Inactivo'),
(2, 'Carnet Diplomarico', 'Activo'),
(3, 'Pasaporte', 'Activo'),
(4, 'Tarjeta de Extranjeria', 'Activo'),
(5, 'NIT', 'Activo'),
(6, 'Adulto sin Identificacion', 'inactivo'),
(11, 'Cedula de Cuidadania', 'Activo'),
(12, 'Registro Civil', 'Activo'),
(13, 'Permiso Especial', 'Inactivo'),
(14, 'Cedula de Extranjeria', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `idempleado` int(10) NOT NULL,
  `idusuario` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `idperfil` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `perfil`
--

INSERT INTO `perfil` (`idperfil`, `nombre`, `estado`) VALUES
(1, 'Administrador', 'Activo'),
(2, 'Operador', 'Activo'),
(3, 'Auxiliar de odontologia', 'Inactivo'),
(4, 'Medico Odontologo', 'Activo'),
(5, 'Enfermera', 'Activo'),
(6, 'Medico Especialista', 'Activo'),
(7, 'Anasteciologo', 'Inactivo'),
(8, 'Cirujano General', 'Activo'),
(9, 'Ortodoncista', 'Activo'),
(10, 'Aprendiz Sena', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `idreserva` int(10) NOT NULL,
  `idusuario` int(10) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `estado` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` int(10) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `iddocumento` int(10) NOT NULL,
  `numdocu` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `idperfil` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idusuario`, `nombre`, `iddocumento`, `numdocu`, `user`, `pass`, `estado`, `idperfil`) VALUES
(1, 'Administrador General', 11, '123456789', 'admin', 'admin', 'Activo', 1),
(2, 'Royman Rojas Noriega', 11, '1042452108', 'rrojas', '1707', 'Activo', 2),
(3, 'Angie Paola Arrieta', 11, '1042446819', 'aarieta', '1234', 'Activo', 4),
(4, 'Maria Luisa Gonzalez', 1, 'PA123355222', 'mgonzalez', '1234', 'Activo', 2),
(5, 'Gabriel Arrieta', 6, 'NA', 'Garrieta', '0125', 'Activo', 2),
(20, 'Eisner Polo Mendoza', 11, '7284766', 'Epolo', '0000', 'Inactivo', 2),
(21, 'Fernando Uribe', 4, '02878855', 'furibe', 'furibe', 'Activo', 2),
(22, 'Tania Perez', 11, '1045478897', 'Tperez', 'perez1520', 'Inactivo', 6),
(24, 'Bryan Fernandez', 11, '1145587896', 'Bfernandez', '1234', 'Activo', 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `detalle`
--
ALTER TABLE `detalle`
  ADD PRIMARY KEY (`iddetalle`),
  ADD KEY `Tabla Reservas` (`idreserva`);

--
-- Indices de la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`iddocumento`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`idempleado`),
  ADD KEY `Tabla usuarios` (`idusuario`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`idperfil`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`idreserva`),
  ADD KEY `Tabla Usuario` (`idusuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuario`),
  ADD KEY `Tabla Documentos` (`iddocumento`),
  ADD KEY `Tabla Perfiles` (`idperfil`) USING BTREE;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `detalle`
--
ALTER TABLE `detalle`
  MODIFY `iddetalle` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `documentos`
--
ALTER TABLE `documentos`
  MODIFY `iddocumento` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `idempleado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `idperfil` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `idreserva` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalle`
--
ALTER TABLE `detalle`
  ADD CONSTRAINT `detalle_ibfk_1` FOREIGN KEY (`idreserva`) REFERENCES `reservas` (`idreserva`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`idperfil`) REFERENCES `perfil` (`idperfil`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`iddocumento`) REFERENCES `documentos` (`iddocumento`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
