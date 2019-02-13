-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2019 at 10:54 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cleodb`
--

-- --------------------------------------------------------

--
-- Table structure for table `cita`
--

CREATE TABLE `cita` (
  `id` int(11) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `estadoCita_id` int(11) NOT NULL,
  `Sala_id` int(11) NOT NULL,
  `Cliente_id` int(11) NOT NULL,
  `Empleado_id` int(11) NOT NULL,
  `Tratamiento_id` int(11) NOT NULL,
  `HorarioEntrada_id` int(11) NOT NULL,
  `HorarioSalida_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `puntuacion` int(11) DEFAULT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`id`, `dni`, `nombre`, `apellidos`, `email`, `direccion`, `telefono`, `puntuacion`, `password`) VALUES
(15, '12345678B', 'Maria', 'Martin', 'maria@google.com', 'La torre', '123456789', 0, '1234'),
(17, '12345678C', 'Victor', 'Ballesteros', 'victor@ucm.es', 'San Roque', '123456789', 0, '1234');

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `codigo` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `tipoEmpleado_id` int(11) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `empleado`
--

INSERT INTO `empleado` (`id`, `dni`, `codigo`, `nombre`, `apellidos`, `email`, `direccion`, `telefono`, `tipoEmpleado_id`, `password`) VALUES
(4, '12345678A', '1234', 'Silvi', 'Martin', 'silmar@google.es', 'las retamas', '123456789', 1, '1234');

-- --------------------------------------------------------

--
-- Table structure for table `estadocita`
--

CREATE TABLE `estadocita` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `estadocita`
--

INSERT INTO `estadocita` (`id`, `nombre`) VALUES
(1, 'confirmada'),
(2, 'no confirmada');

-- --------------------------------------------------------

--
-- Table structure for table `estadofactura`
--

CREATE TABLE `estadofactura` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `estadofactura`
--

INSERT INTO `estadofactura` (`id`, `nombre`) VALUES
(1, 'pagado'),
(2, 'no pendiente'),
(3, 'fraccionado');

-- --------------------------------------------------------

--
-- Table structure for table `estadomensaje`
--

CREATE TABLE `estadomensaje` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `estadomensaje`
--

INSERT INTO `estadomensaje` (`id`, `nombre`) VALUES
(1, 'leido'),
(2, 'no leido');

-- --------------------------------------------------------

--
-- Table structure for table `estadopedido`
--

CREATE TABLE `estadopedido` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `estadopedido`
--

INSERT INTO `estadopedido` (`id`, `nombre`) VALUES
(1, 'entregado'),
(2, 'en proceso'),
(3, 'cancelado');

-- --------------------------------------------------------

--
-- Table structure for table `factura`
--

CREATE TABLE `factura` (
  `id` int(11) NOT NULL,
  `costePorCobrar` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `estadoFactura_id` int(11) NOT NULL,
  `Cita_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `horario`
--

CREATE TABLE `horario` (
  `id` int(11) NOT NULL,
  `hora` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `horario`
--

INSERT INTO `horario` (`id`, `hora`) VALUES
(1, '09:00:00'),
(2, '10:00:00'),
(3, '11:00:00'),
(4, '12:00:00'),
(5, '13:00:00'),
(6, '14:00:00'),
(7, '15:00:00'),
(8, '16:00:00'),
(9, '17:00:00'),
(10, '18:00:00'),
(11, '19:00:00'),
(12, '20:00:00'),
(13, '21:00:00'),
(14, '22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `horarioempleado`
--

CREATE TABLE `horarioempleado` (
  `fecha` datetime DEFAULT NULL,
  `Empleado_id` int(11) NOT NULL,
  `HorarioEntrada_id` int(11) NOT NULL,
  `HorarioSalida_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `inventario`
--

CREATE TABLE `inventario` (
  `id` int(11) NOT NULL,
  `coste` double DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fechaEntrada` datetime DEFAULT NULL,
  `fechaFin` datetime DEFAULT NULL,
  `Proveedor_id` int(11) NOT NULL,
  `Producto_id` int(11) NOT NULL,
  `Pedido_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `maquina`
--

CREATE TABLE `maquina` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `fechaIngreso` varchar(45) DEFAULT NULL,
  `tipoMaquina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `maquina`
--

INSERT INTO `maquina` (`id`, `nombre`, `fechaIngreso`, `tipoMaquina_id`) VALUES
(4, 'Maquina_1', '2019-02-09', 1);

-- --------------------------------------------------------

--
-- Table structure for table `notificacion`
--

CREATE TABLE `notificacion` (
  `id` int(11) NOT NULL,
  `estadoMensaje_id` int(11) NOT NULL,
  `tipoUsuario_id` int(11) NOT NULL,
  `mensaje` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `pedido`
--

CREATE TABLE `pedido` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `estadoPedido_id` int(11) NOT NULL,
  `Producto_id` int(11) NOT NULL,
  `Proveedor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `tipoProducto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `promocion`
--

CREATE TABLE `promocion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `observaciones` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `proveedor`
--

CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `contacto` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `publicidad`
--

CREATE TABLE `publicidad` (
  `id` int(11) NOT NULL,
  `fechaInicio` datetime DEFAULT NULL,
  `fechaFin` datetime DEFAULT NULL,
  `Promocion_id` int(11) NOT NULL,
  `Cliente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sala`
--

CREATE TABLE `sala` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sala`
--

INSERT INTO `sala` (`id`, `nombre`) VALUES
(2, 'sala1');

-- --------------------------------------------------------

--
-- Table structure for table `tipoempleado`
--

CREATE TABLE `tipoempleado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tipoempleado`
--

INSERT INTO `tipoempleado` (`id`, `nombre`) VALUES
(1, 'encargado'),
(2, 'basico');

-- --------------------------------------------------------

--
-- Table structure for table `tipomaquina`
--

CREATE TABLE `tipomaquina` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tipomaquina`
--

INSERT INTO `tipomaquina` (`id`, `nombre`) VALUES
(1, 'facial'),
(2, 'corporal'),
(3, 'ninguna');

-- --------------------------------------------------------

--
-- Table structure for table `tipoproducto`
--

CREATE TABLE `tipoproducto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `tipousuario`
--

CREATE TABLE `tipousuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tipousuario`
--

INSERT INTO `tipousuario` (`id`, `nombre`) VALUES
(1, 'cliente'),
(2, 'encargado');

-- --------------------------------------------------------

--
-- Table structure for table `tratamiento`
--

CREATE TABLE `tratamiento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `Maquina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`id`,`estadoCita_id`,`Sala_id`,`Cliente_id`,`Empleado_id`,`Tratamiento_id`,`HorarioEntrada_id`,`HorarioSalida_id`),
  ADD KEY `fk_Cita_estadoCita1_idx` (`estadoCita_id`),
  ADD KEY `fk_Cita_Sala1_idx` (`Sala_id`),
  ADD KEY `fk_Cita_Cliente1_idx` (`Cliente_id`),
  ADD KEY `fk_Cita_Empleado1_idx` (`Empleado_id`),
  ADD KEY `fk_Cita_Tratamiento1_idx` (`Tratamiento_id`),
  ADD KEY `fk_Cita_Horario1_idx` (`HorarioEntrada_id`),
  ADD KEY `fk_Cita_Horario2_idx` (`HorarioSalida_id`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD UNIQUE KEY `dni_UNIQUE` (`dni`);

--
-- Indexes for table `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`,`tipoEmpleado_id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD UNIQUE KEY `dni_UNIQUE` (`dni`),
  ADD KEY `fk_Empleado_tipoEmpleado_idx` (`tipoEmpleado_id`);

--
-- Indexes for table `estadocita`
--
ALTER TABLE `estadocita`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `estadofactura`
--
ALTER TABLE `estadofactura`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `estadomensaje`
--
ALTER TABLE `estadomensaje`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `estadopedido`
--
ALTER TABLE `estadopedido`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id`,`estadoFactura_id`,`Cita_id`),
  ADD KEY `fk_Factura_estadoFactura1_idx` (`estadoFactura_id`),
  ADD KEY `fk_Factura_Cita1_idx` (`Cita_id`);

--
-- Indexes for table `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `horarioempleado`
--
ALTER TABLE `horarioempleado`
  ADD PRIMARY KEY (`Empleado_id`,`HorarioEntrada_id`,`HorarioSalida_id`),
  ADD KEY `fk_HorarioEmpleado_Empleado1_idx` (`Empleado_id`),
  ADD KEY `fk_HorarioEmpleado_Horario1_idx` (`HorarioEntrada_id`),
  ADD KEY `fk_HorarioEmpleado_Horario2_idx` (`HorarioSalida_id`);

--
-- Indexes for table `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id`,`Proveedor_id`,`Producto_id`,`Pedido_id`),
  ADD KEY `fk_Inventario_Proveedor1_idx` (`Proveedor_id`),
  ADD KEY `fk_Inventario_Producto1_idx` (`Producto_id`),
  ADD KEY `fk_Inventario_Pedido1_idx` (`Pedido_id`);

--
-- Indexes for table `maquina`
--
ALTER TABLE `maquina`
  ADD PRIMARY KEY (`id`,`tipoMaquina_id`),
  ADD KEY `fk_Maquina_tipoMaquina1_idx` (`tipoMaquina_id`);

--
-- Indexes for table `notificacion`
--
ALTER TABLE `notificacion`
  ADD PRIMARY KEY (`id`,`estadoMensaje_id`,`tipoUsuario_id`),
  ADD KEY `fk_Notificacion_estadoMensaje1_idx` (`estadoMensaje_id`),
  ADD KEY `fk_Notificacion_tipoUsuario1_idx` (`tipoUsuario_id`);

--
-- Indexes for table `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`,`estadoPedido_id`,`Producto_id`,`Proveedor_id`),
  ADD KEY `fk_Pedido_estadoPedido1_idx` (`estadoPedido_id`),
  ADD KEY `fk_Pedido_Proveedor1_idx` (`Proveedor_id`),
  ADD KEY `fk_Pedido_Producto1_idx` (`Producto_id`);

--
-- Indexes for table `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`,`tipoProducto_id`),
  ADD KEY `fk_Producto_tipoProducto1_idx` (`tipoProducto_id`);

--
-- Indexes for table `promocion`
--
ALTER TABLE `promocion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `publicidad`
--
ALTER TABLE `publicidad`
  ADD PRIMARY KEY (`id`,`Promocion_id`,`Cliente_id`),
  ADD KEY `fk_PublicidadCliente_Promocion1_idx` (`Promocion_id`),
  ADD KEY `fk_PublicidadCliente_Cliente1_idx` (`Cliente_id`);

--
-- Indexes for table `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipoempleado`
--
ALTER TABLE `tipoempleado`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipomaquina`
--
ALTER TABLE `tipomaquina`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipoproducto`
--
ALTER TABLE `tipoproducto`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD PRIMARY KEY (`id`,`Maquina_id`),
  ADD KEY `fk_Tratamiento_Maquina1_idx` (`Maquina_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cita`
--
ALTER TABLE `cita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `estadocita`
--
ALTER TABLE `estadocita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `estadofactura`
--
ALTER TABLE `estadofactura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `estadomensaje`
--
ALTER TABLE `estadomensaje`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `estadopedido`
--
ALTER TABLE `estadopedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `factura`
--
ALTER TABLE `factura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `horario`
--
ALTER TABLE `horario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `maquina`
--
ALTER TABLE `maquina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `promocion`
--
ALTER TABLE `promocion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `publicidad`
--
ALTER TABLE `publicidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sala`
--
ALTER TABLE `sala`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipoempleado`
--
ALTER TABLE `tipoempleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipomaquina`
--
ALTER TABLE `tipomaquina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tipoproducto`
--
ALTER TABLE `tipoproducto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tratamiento`
--
ALTER TABLE `tratamiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cita`
--
ALTER TABLE `cita`
  ADD CONSTRAINT `fk_Cita_Cliente1` FOREIGN KEY (`Cliente_id`) REFERENCES `cliente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_Empleado1` FOREIGN KEY (`Empleado_id`) REFERENCES `empleado` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_Horario1` FOREIGN KEY (`HorarioEntrada_id`) REFERENCES `horario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_Horario2` FOREIGN KEY (`HorarioSalida_id`) REFERENCES `horario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_Sala1` FOREIGN KEY (`Sala_id`) REFERENCES `sala` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_Tratamiento1` FOREIGN KEY (`Tratamiento_id`) REFERENCES `tratamiento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Cita_estadoCita1` FOREIGN KEY (`estadoCita_id`) REFERENCES `estadocita` (`id`);

--
-- Constraints for table `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `fk_Empleado_tipoEmpleado` FOREIGN KEY (`tipoEmpleado_id`) REFERENCES `tipoempleado` (`id`);

--
-- Constraints for table `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `fk_Factura_Cita1` FOREIGN KEY (`Cita_id`) REFERENCES `cita` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Factura_estadoFactura1` FOREIGN KEY (`estadoFactura_id`) REFERENCES `estadofactura` (`id`);

--
-- Constraints for table `horarioempleado`
--
ALTER TABLE `horarioempleado`
  ADD CONSTRAINT `fk_HorarioEmpleado_Empleado1` FOREIGN KEY (`Empleado_id`) REFERENCES `empleado` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_HorarioEmpleado_Horario1` FOREIGN KEY (`HorarioEntrada_id`) REFERENCES `horario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_HorarioEmpleado_Horario2` FOREIGN KEY (`HorarioSalida_id`) REFERENCES `horario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `fk_Inventario_Pedido1` FOREIGN KEY (`Pedido_id`) REFERENCES `pedido` (`id`),
  ADD CONSTRAINT `fk_Inventario_Producto1` FOREIGN KEY (`Producto_id`) REFERENCES `producto` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Inventario_Proveedor1` FOREIGN KEY (`Proveedor_id`) REFERENCES `proveedor` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `maquina`
--
ALTER TABLE `maquina`
  ADD CONSTRAINT `fk_Maquina_tipoMaquina1` FOREIGN KEY (`tipoMaquina_id`) REFERENCES `tipomaquina` (`id`);

--
-- Constraints for table `notificacion`
--
ALTER TABLE `notificacion`
  ADD CONSTRAINT `fk_Notificacion_estadoMensaje1` FOREIGN KEY (`estadoMensaje_id`) REFERENCES `estadomensaje` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Notificacion_tipoUsuario1` FOREIGN KEY (`tipoUsuario_id`) REFERENCES `tipousuario` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `fk_Pedido_Producto1` FOREIGN KEY (`Producto_id`) REFERENCES `producto` (`id`),
  ADD CONSTRAINT `fk_Pedido_Proveedor1` FOREIGN KEY (`Proveedor_id`) REFERENCES `proveedor` (`id`),
  ADD CONSTRAINT `fk_Pedido_estadoPedido1` FOREIGN KEY (`estadoPedido_id`) REFERENCES `estadopedido` (`id`);

--
-- Constraints for table `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `fk_Producto_tipoProducto1` FOREIGN KEY (`tipoProducto_id`) REFERENCES `tipoproducto` (`id`);

--
-- Constraints for table `publicidad`
--
ALTER TABLE `publicidad`
  ADD CONSTRAINT `fk_PublicidadCliente_Cliente1` FOREIGN KEY (`Cliente_id`) REFERENCES `cliente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_PublicidadCliente_Promocion1` FOREIGN KEY (`Promocion_id`) REFERENCES `promocion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD CONSTRAINT `fk_Tratamiento_Maquina1` FOREIGN KEY (`Maquina_id`) REFERENCES `maquina` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
