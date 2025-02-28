-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 28/02/2025 às 19:21
-- Versão do servidor: 10.11.10-MariaDB
-- Versão do PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `u228502032_TesteLdl2`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `avise_quando_chegar`
--

CREATE TABLE `avise_quando_chegar` (
  `id` int(11) NOT NULL,
  `id_produto` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `dt_solicitacao` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Despejando dados para a tabela `avise_quando_chegar`
--

INSERT INTO `avise_quando_chegar` (`id`, `id_produto`, `id_usuario`, `dt_solicitacao`) VALUES
(15, 188, 29, '2025-02-24 16:22:23');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `descricao` text DEFAULT NULL,
  `valor` decimal(10,2) NOT NULL,
  `tipo_produto` varchar(50) NOT NULL,
  `dt_cadastro` datetime DEFAULT NULL,
  `qtd_comprada` int(11) NOT NULL,
  `variacao` varchar(255) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `imagem` varchar(512) NOT NULL,
  `peso` float NOT NULL,
  `altura` float NOT NULL,
  `largura` float NOT NULL,
  `comprimento` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

--
-- Despejando dados para a tabela `produtos`
--

INSERT INTO `produtos` (`id`, `nome`, `descricao`, `valor`, `tipo_produto`, `dt_cadastro`, `qtd_comprada`, `variacao`, `tipo`, `imagem`, `peso`, `altura`, `largura`, `comprimento`) VALUES
(132, 'Sabonete Facial Skin Comfort', 'O Sabonete Facial Skin Comfort possui fórmula que limpa sem agredir e garante o conforto que seu rosto merece. A presença da Vitamina E, bisabolol e Gengibre em sua formulação garante uma pele mais hidratada com um toque delicado. O cuidado que você precisa sem agredir a sua pele. Ideal para pele mista a oleosa.', 18.99, 'Skincare', '2025-02-24 17:26:55', 3, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(133, 'Sabonete Facial Óleo Rosa Mosqueta', 'O Sabonete Facial Óleo de Rosa Mosqueta é ideal para uso diário por deixar a pele limpa e macia. Formulado com Óleo de rosa Mosqueta, que é extraído das sementes do fruto da Rosa Mosqueta, ele atua na limpeza facial sem comprometer a hidratação da pele. Sua textura adapta o uso para proporcionar maciez, suavidade e hidratação, reparando a pele e intensificando a sensação de cuidado por mais tempo. O cuidado que a sua pele precisava. Ideal para pele seca.', 18.99, 'Skincare', '2025-01-19 22:41:14', 3, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(134, 'Sabonete Antiacne', 'O Sabonete Antiacne Phállebeauty possui eficácia comprovada e intensa, auxilia na remoção da oleosidade, sem ressecar ou agredir a pele, age combatendo cravos e acnes.', 20.90, 'Skincare', '2025-01-19 22:41:14', 15, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(135, 'Sabonete Micelar Pré e Pós Make 3 em 1', 'Este demaquilante oferece uma limpeza profunda e suave, auxilia de maneira eficiente a maquiagem, impurezas e resíduos de poluição, preparando a pele para a aplicação da maquiagem ou para o momento de desintoxicação após um longo dia. Sua fórmula conta com ácido hialurônico e extrato de pepino.', 8.99, 'Skincare', '2025-01-19 22:41:14', 15, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(136, 'Sabonete Líquido Facial Rosa Mosqueta', 'Além de oferecer uma limpeza eficiente, enriquecido com extrato de rosa mosqueta, ajuda a manter a pele hidratada e reduz oleosidade e tudo isso com uma fragrância maravilhosa.', 8.99, 'Skincare', '2025-01-19 22:41:14', 15, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(137, 'Sabonete Líquido Facial Vitamina C', 'Oferece uma limpeza delicada, indicado para todos os tipos de pele e enriquecido com vitamina C. Auxilia na remoção de impurezas, resíduos de maquiagem e deixa sua pele iluminada.', 8.99, 'Skincare', '2025-01-19 22:41:14', 14, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(138, 'Hidratante Vegano Calmante', 'O hidratante Multifuncional Calmante possui na sua estrutura o leite de amêndoas, um composto onde entrega uma nutrição e hidratação deliciosa a pele. Além do Blend Botânico Aloe e Vera, calêndula e Hamamelis: que juntos auxiliam no processo de cicatrização, regeneração e hidratação da pele.', 15.49, 'Skincare', '2025-01-19 22:41:14', 14, NULL, 4, 'inglês', 100, 12, 8, 8),
(139, 'Gel Creme Facial Regenerador Noturno', 'Levissíma fórmula, 100%livre de óleos e gorduras, contém Niacinamida e Bisabolol.\r\n\r\nMúltiplos Benefícios:\r\n\r\nHidratação Delicada e Efetiva\r\nAção Tonificante e Revigorante\r\nAção Antioxidante\r\nEfeito primer, Pré-Maquiagem e pré-filtros', 18.90, 'Skincare', '2025-01-19 22:41:14', 3, NULL, 4, 'inglês', 84, 3.5, 6.9, 7.3),
(140, 'Hidratante Vegano Peles Sensíveis', 'O Hidratante Multifuncional de peles Sensíveis auxilia na diminuição na irritação da pele causada por raios UV, acalma a pele, mantém a elasticidade e aumenta a hidratação da pele. Com água de coco, traz a pele a recrescência e sedosidade.', 14.99, 'Skincare', '2025-01-19 22:41:14', 4, NULL, 4, 'inglês', 100, 12, 8, 8),
(141, 'Gel Hidratante Facial Equilibrante Antioleosidade', 'Levissíma fórmula, 100%livre de óleos e gorduras, contém Niacinamida e Bisabolol.\r\n\r\nMúltiplos Benefícios:\r\n\r\nHidratação Delicada e Efetiva\r\nAção Tonificante e Revigorante\r\nAção Antioxidante\r\nEfeito primer, Pré-Maquiagem e pré-filtros', 18.90, 'Skincare', '2025-01-19 22:41:14', 16, NULL, 4, 'inglês', 84, 3.5, 6.9, 7.3),
(142, 'Máscara Facial Hidroplástica Pérola Verde Peel Off', 'Máscaras faciais são produtos de cuidados com a pele aplicados para oferecer benefícios específicos, como hidratação, limpeza profunda, ou tratamento anti-idade.', 4.98, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 5, 'inglês', 9, 1, 6, 6),
(143, 'Máscara Facial Hidroplástica Pérola Rosa Peel Off', 'Máscaras faciais são produtos de cuidados com a pele aplicados para oferecer benefícios específicos, como hidratação, limpeza profunda, ou tratamento anti-idade.', 4.98, 'Skincare', '2025-01-19 22:41:14', 7, NULL, 5, 'inglês', 9, 1, 6, 6),
(144, 'Máscara Facial Colágeno', 'Máscaras faciais são produtos de cuidados com a pele aplicados para oferecer benefícios específicos, como hidratação, limpeza profunda, ou tratamento anti-idade.', 4.98, 'Skincare', '2025-01-19 22:41:14', 7, NULL, 5, 'inglês', 9, 1, 6, 6),
(145, 'Máscara Facial Carvão Ativado e Argila Branca', 'Máscaras faciais são produtos de cuidados com a pele aplicados para oferecer benefícios específicos, como hidratação, limpeza profunda, ou tratamento anti-idade.', 11.98, 'Skincare', '2025-01-19 22:41:14', 5, NULL, 5, 'inglês', 45, 10, 3, 2),
(146, 'Máscara Facial Argila Branca Kaolin e Chá Verde', 'Máscaras faciais são produtos de cuidados com a pele aplicados para oferecer benefícios específicos, como hidratação, limpeza profunda, ou tratamento anti-idade.', 11.98, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 5, 'inglês', 45, 10, 3, 2),
(147, 'Sérum para Olhos Vegano Pele Blindada com Ácido Hialurônico', 'O Sérum para Área dos Olhos Pele Blindada da Mia Make é um aliado essencial para quem busca uma pele mais saudável e bonita ao redor dos olhos. Com sua fórmula de alta qualidade e eficácia comprovada, este sérum é uma opção indispensável para quem valoriza o cuidado com a pele.', 24.99, 'Skincare', '2025-01-19 22:41:14', 10, NULL, 6, 'inglês', 31, 11.7, 1.8, 1.8),
(148, 'Sérum para Olhos Vegano Pele Blindada com Rosa Mosqueta', 'O Sérum para Área dos Olhos Pele Blindada da Mia Make com rosa mosqueta também é um aliado essencial para quem busca uma pele mais saudável e bonita ao redor dos olhos. Com sua fórmula de alta qualidade e eficácia comprovada, este sérum é uma opção indispensável para quem valoriza o cuidado com a pele.', 24.99, 'Skincare', '2025-01-19 22:41:14', 9, NULL, 6, 'inglês', 31, 11.7, 1.8, 1.8),
(149, 'Sérum Facial Beads Carvão Ativado', 'O Sérum Facial Beads Carvão Ativado Max Love proporciona efeito detox para a pele, auxiliando na remoção de oleosidade e promovendo leve esfoliação graças ao carvão ativado entregue por cápsulas biotecnológicas. O resultado é uma pele iluminada. Além disso sua fórmula é vegana pois não contém ingredientes de origem animal.', 15.49, 'Skincare', '2025-01-19 22:41:14', 7, NULL, 6, 'inglês', 90, 9.5, 4, 4),
(150, 'Sérum Vitamina C Booster Antiaging', 'Projetado para ser absorvido rapidamente, o sérum visa fornecer benefícios específicos, como hidratação intensa, anti-envelhecimento, clareamento da pele ou tratamento de problemas dermatológicos.', 17.50, 'Skincare', '2025-01-19 22:41:14', 4, NULL, 6, 'inglês', 86, 10, 3, 3),
(151, 'Sérum Facial com Ácido Hialurônico', 'Projetado para ser absorvido rapidamente, o sérum visa fornecer benefícios específicos, como hidratação intensa, anti-envelhecimento, clareamento da pele ou tratamento de problemas dermatológicos.', 17.50, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 6, 'inglês', 86, 10, 3, 3),
(152, 'Máscara para Cílios Big Volume', 'Rímel à prova d’água na cor preta que confere volume na medida exata, em uma embalagem linda e econômica.', 14.99, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 3, 'inglês', 19, 15, 3, 3),
(153, 'Rímel Efeito Boneca', 'Rímel, também conhecido como máscara de cílios, é um produto de maquiagem aplicado nos cílios para realçar o olhar. Geralmente disponível em forma líquida ou cremosa', 10.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 3, 'inglês', 19, 15, 3, 3),
(155, 'Pó Compacto Vegano Dia A Dia Cor 1', 'Esse pó foi desenvolvido com um sistema de alta micronização, que promove um pó fino, com textura delicada, que uniformiza, matifica e sela a maquiagem com uma cobertura natural, além do toque seco e aveludado. É o produto perfeito para socorrer a pele, no tom certo e sem brilho.\r\nCores disponíveis: 1, 2, 3 e 4', 17.90, 'Maquiagem', '2025-01-19 22:41:14', 7, NULL, 1, 'inglês', 30, 1.3, 6.5, 6.5),
(156, 'Pó Compacto Vegano Dia A Dia Cor 2', 'Esse pó foi desenvolvido com um sistema de alta micronização, que promove um pó fino, com textura delicada, que uniformiza, matifica e sela a maquiagem com uma cobertura natural, além do toque seco e aveludado. É o produto perfeito para socorrer a pele, no tom certo e sem brilho.\r\nCores disponíveis: 1, 2, 3 e 4', 17.90, 'Maquiagem', '2025-01-19 22:41:14', 13, NULL, 1, 'inglês', 30, 1.3, 6.5, 6.5),
(157, 'Pó Compacto Vegano Dia A Dia Cor 3', 'Esse pó foi desenvolvido com um sistema de alta micronização, que promove um pó fino, com textura delicada, que uniformiza, matifica e sela a maquiagem com uma cobertura natural, além do toque seco e aveludado. É o produto perfeito para socorrer a pele, no tom certo e sem brilho.\r\nCores disponíveis: 1, 2, 3 e 4', 17.90, 'Maquiagem', '2025-01-19 22:41:14', 9, NULL, 1, 'inglês', 30, 1.3, 6.5, 6.5),
(158, 'Pó Compacto Vegano Dia A Dia Cor 4', 'Esse pó foi desenvolvido com um sistema de alta micronização, que promove um pó fino, com textura delicada, que uniformiza, matifica e sela a maquiagem com uma cobertura natural, além do toque seco e aveludado. É o produto perfeito para socorrer a pele, no tom certo e sem brilho.\r\nCores disponíveis: 1, 2, 3 e 4', 17.90, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 30, 1.3, 6.5, 6.5),
(159, 'Delineador Duo Lua&Neve', 'O delineador lápis de olho Lua&Neve é um produto versátil e prático, ideal para quem gosta de variar o estilo de maquiagem dos olhos. Ele vem com um lápis de olho em uma ponta e um delineador líquido na outra, o que proporciona mais opções de uso em um só produto.', 11.98, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 3, 'inglês', 70, 10, 1.5, 1.5),
(160, 'Lapis de Olho Preto com Apontador', 'Rímel, também conhecido como máscara de cílios, é um produto de maquiagem aplicado nos cílios para realçar o olhar. Geralmente disponível em forma líquida ou cremosa', 7.99, 'Maquiagem', '2025-01-19 22:41:14', 15, NULL, 3, 'inglês', 6, 18.5, 1, 1),
(161, 'Batom All Day Alta Cobertura Longa Duração', 'O Batom All Day Matte Vivai tem textura cremosa e acabamento matte. Seus tons de vermelho são perfeitos para diversas ocasiões.\r\nSão 8 tons de batom para que você possa escolher e arrasar, sem contar que a embalagem é simplesmente linda e apaixonante.', 7.99, 'Maquiagem', '2025-01-19 22:41:14', 8, NULL, 2, 'inglês', 20, 5, 1, 1),
(162, 'Lip Balm Pop Balm com Jojoba e Karité', 'Com uma apresentação alegre e tropical, o POP BALM da LUISANCE vai dar aquela hidratação aos seus lábios, deixando uma cor bem naturalzinha mas com um cheirinho “delicioso” (da vontade de comer hehe). Contém manteiga de karité e óleo de jojoba.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 8, NULL, 2, 'inglês', 20, 7.2, 1, 1),
(163, 'Pó Translúcido Profissional', 'O Pó Solto Lady Beauty Translúcido é um ótimo aliado para que tem pele oleosa, promove a durabilidade da make e forma um véu que evita a oleosidade.\r\n', 9.99, 'Maquiagem', '2025-01-19 22:41:14', 27, NULL, 1, 'inglês', 38, 7, 3, 7),
(164, 'Esponja de Microfibra para Maquiagem 360º', 'A Esponja de Microfibra para Maquiagem 360º Sabrina Sato proporciona acabamento incrível na pele. A esponja de microfibra absorve menos produto, tem essa camada aveludada bem macia, é perfeita!', 10.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 8, 'inglês', 20, 5, 6, 5),
(165, 'Esponja de Maquiagem Gota Chanfrada Microfibra 2 em 1', 'A Esponja de microfibra da Mylife foi desenvolvida para aplicação de produtos líquidos e cremosos, resultando em um acabamento com efeito natural. Suas microfibras permitem a utilização na aplicação do pó facial ou translúcido, aumentando a sua performance sem desperdício de produto. Proporcionando uma cobertura de esponja com polimento de pincel, deixando sua make com o acabamento perfeito.', 14.99, 'Maquiagem', '2025-01-19 22:41:14', 12, NULL, 8, 'inglês', 15, 4, 6, 4),
(166, 'Batom Líquido Matte Cor Bordô', 'Batons são produtos de maquiagem destinados aos lábios, disponíveis em diversas cores e texturas. Geralmente em formato de bastão, creme ou líquido.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 2, 'inglês', 23, 10, 1, 1),
(167, 'Batom Líquido Matte Cor Uva Merlot', 'Batons são produtos de maquiagem destinados aos lábios, disponíveis em diversas cores e texturas. Geralmente em formato de bastão, creme ou líquido.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 2, 'inglês', 23, 10, 1, 1),
(168, 'Base Matte Alta Cobertura Cor 1', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.Cores: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 8, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(169, 'Base Matte Alta Cobertura Cor 2', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 8, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(170, 'Base Matte Alta Cobertura Cor 3', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 7, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(171, 'Delineador em Gel colorido Amarelo', 'O Delineador em Gel Colorido Newface é altamente pigmentado e resistente, ele deixa o olhar com mais vida e alegria com suas cores impactantes por muitas horas, pois não borra nem derrete!\r\nCores disponíveis: Azul, Branco, Amarelo e Vermelho', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 3, 'inglês', 15, 3, 5, 3),
(172, 'Delineador em Gel colorido Azul', 'O Delineador em Gel Colorido Newface é altamente pigmentado e resistente, ele deixa o olhar com mais vida e alegria com suas cores impactantes por muitas horas, pois não borra nem derrete!\r\nCores disponíveis: Azul, Branco, Amarelo e Vermelho', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 3, 'inglês', 15, 3, 5, 3),
(173, 'Delineador em Gel colorido Branco', 'O Delineador em Gel Colorido Newface é altamente pigmentado e resistente, ele deixa o olhar com mais vida e alegria com suas cores impactantes por muitas horas, pois não borra nem derrete!\r\nCores disponíveis: Azul, Branco, Amarelo e Vermelho', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 3, 'inglês', 15, 3, 5, 3),
(174, 'Delineador em Gel colorido Vermelho', 'O Delineador em Gel Colorido Newface é altamente pigmentado e resistente, ele deixa o olhar com mais vida e alegria com suas cores impactantes por muitas horas, pois não borra nem derrete!\r\nCores disponíveis: Azul, Branco, Amarelo e Vermelho', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 3, 'inglês', 15, 3, 5, 3),
(176, 'Lápis Retrátil Para Olhos Preto', 'Ideal para qualquer momento, o Lápis Delineador para Olhos Preto é o queridinho que está sempre na necessaire ajudando em várias situações.', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 6, NULL, 3, 'inglês', 5, 12.5, 1, 1),
(181, 'Primer Facial Efeito Lifting', 'O Primer Facial Efeito Lifting da Phálle Beauty foi desenvolvido para preparar a pele antes de receber a base ou filtro solar. Auxilia no controle da oleosidade. Tem efeito Lifting, que uniformiza a pele e deixa os poros menos visíveis.', 24.50, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 115, 12, 3, 3),
(182, 'Blush Líquido Vegano', 'Textura líquida que espalha super fácil, tem rápida absorção, pigmentação balanceada e resultado de longa duração. Seu efeito natural proporciona um ar de saúde e pele viçosa em instantes!', 17.99, 'Maquiagem', '2025-01-19 22:41:14', 12, NULL, 1, 'inglês', 25, 12, 1, 1),
(183, 'Esponja para Pó Make com 2un', 'Ideal para aplicação de pó, ela tem uma fita de cetim que permite que você segure por ela', 5.49, 'Maquiagem', '2025-01-19 22:41:14', 12, NULL, 8, 'inglês', 7, 7, 5, 1),
(184, 'Toalhas Faciais Umidecidas com Água Micelar', 'As Toalhas Umedecidas para Limpeza Facial com Água Micelar da Fenzza foram desenvolvidas para proporcionar uma alta eficiência na limpeza da pele e remoção de maquiagem, até mesmo as maquiagens à prova da água.', 12.99, 'Skincare', '2025-01-19 22:41:14', 18, NULL, 9, 'inglês', 88, 2, 10, 19),
(185, 'Toalhas Faciais Umidecidas com Vitamina C', 'As Toalhas Umedecidas de Limpeza Facial contém Vitamina C da Fenzza possuem ação firmadora, reduz linhas de expressão, possui efeito clareador, livre de álcool e parabenos.', 12.99, 'Skincare', '2025-01-19 22:41:14', 5, NULL, 9, 'inglês', 88, 2, 10, 19),
(186, 'Delineador Líquido Preto ', 'O delineador líquido Max Love tem alta pigmentação, é resistente à água e tem longa duração. Após a secagem não borra e não transfere.', 15.49, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 3, 'inglês', 10, 12, 1.5, 1.5),
(187, 'Batom Líquido 24 hrs Confot Hidratação cor 736', 'O Batom Líquido 24 Horas Confort combina a fixação e acabamento matte com a hidratação e o conforto de um batom cremoso em um único produto. Sua fórmula com Ácido Hialurônico, hidrata os lábios e sua textura permanece levemente maleável após a secagem.\r\nCor: 736', 17.48, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 2, 'inglês', 19, 14.8, 3, 3),
(188, 'Batom Líquido Matte 12 hrs Cor 108', 'O Batom Líquido Matte Max Love tem textura suave e cremosa. Seu efeito matte garante ótimo acabamento com secagem rápida e duração de 12 horas.\r\nCor: 108', 16.99, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 2, 'inglês', 19, 14.8, 3, 3),
(189, 'Pincel Duplo para Sobrancelha', 'O Pincel para Sobrancelha Duplo é incrível por ter vários jeitos de usar. Com cerdas macias e confortáveis a parte chanfrada pode ser usada pra preencher as sobrancelhas com uma sombra, ou ainda, pra delinear os olhos.', 5.49, 'Maquiagem', '2025-01-19 22:41:14', 15, NULL, 8, 'inglês', 16, 20.5, 5, 1),
(190, 'Delineador em Gel de Sobrancelha Médio', 'O Gel Delineador para Sobrancelhas Max Love tem textura cremosa, o que garante maior precisão na aplicação e é altamente pigmentado. Ideal para preencher falhas e destacar as sobrancelhas.', 8.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 3, 'inglês', 29, 12, 3, 3),
(191, 'Faixa de Cabelo para Maquiagem e Limpeza', 'A faixa da aquela ajudinha na hora de se maquiar e evitar que o cabelo atrapalhe ou até mesmo molhe durante o processo de lavagem do rosto.', 15.99, 'Maquiagem', '2025-01-19 22:41:14', 10, NULL, 8, 'inglês', 25, 1, 4, 5),
(192, 'Delineador em Gel de Sobrancelha Escuro', 'O Gel Delineador para Sobrancelhas Max Love tem textura cremosa, o que garante maior precisão na aplicação e é altamente pigmentado. Ideal para preencher falhas e destacar as sobrancelhas.', 8.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 3, 'inglês', 29, 12, 3, 3),
(193, 'Frasco Pump Espumador', 'Fraco Pup Espumador com massageador de silicone, ideal para limpeza facial profunda, permitindo massagem ativa', 16.99, 'Skincare', '2025-01-19 22:41:14', 14, NULL, 7, 'inglês', 58, 20, 5, 5),
(194, 'Sérum Facial Vitamina C 10 em 1', 'Contém um blend de componentes antioxidantes e hidratantes, que auxiliam na hidratação, maciez e tonificação, proporcionando uma pele com aparência uniforme e fresca.', 17.99, 'Skincare', '2025-01-19 22:41:14', 35, NULL, 6, 'inglês', 84, 9.5, 4, 4),
(195, 'Base Matte Alta Cobertura Cor 4', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 5, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(196, 'Base Matte Alta Cobertura Cor 5', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(197, 'Base Matte Alta Cobertura Cor 6', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(198, 'Base Matte Alta Cobertura Cor 7', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(199, 'Base Matte Alta Cobertura Cor 8', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(200, 'Base Matte Alta Cobertura Cor 9', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(201, 'Base Matte Alta Cobertura Cor 10', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita.\r\nCores disponíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, '', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 47, 12, 5.5, 2.5),
(202, 'Esponja Polvo de Limpeza', 'A esponja polvo de limpeza facial é um acessório suave e poroso, projetado para remover impurezas, células mortas e maquiagem do rosto. Sua forma ergonômica e textura delicada permitem uma limpeza suave e eficaz, preparando a pele para absorver melhor os produtos de skincare subsequentes. É importante usar com cuidado para evitar irritações.', 7.99, 'Skincare', '2025-01-19 22:41:14', 24, NULL, 7, 'inglês', 22, 5, 5, 5),
(203, 'Primer Fixation Jasmyne', 'O Primer para olhos Fixation da Jasmyne é um produto utilizado para preparar a pele das pálpebras antes da aplicação de sombras. Sua fórmula ajuda a uniformizar a textura da pele, prolonga a durabilidade da maquiagem e intensifica a pigmentação das sombras, garantindo um resultado mais vibrante e duradouro. Este primer é especialmente projetado para evitar que as sombras acumulem nas linhas finas e vincos das pálpebras, proporcionando uma aplicação suave e uniforme.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 24, NULL, 1, 'inglês', 5, 9, 3, 3),
(204, 'Sabonete Facial Anti-Oleosidade PhálleBeaty', 'O Sabonete Facial Anti-Oleosidade da PhálleBeauty é um produto desenvolvido para limpar e controlar a oleosidade da pele. Sua fórmula específica ajuda a remover o excesso de óleo e impurezas, deixando a pele fresca e matificada. Além disso, este sabonete facial ajuda a prevenir o aparecimento de acne e proporciona uma sensação de limpeza profunda, ideal para peles oleosas e mistas.', 18.99, 'Skincare', '2025-01-19 22:41:14', 12, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(205, 'Sabonete Micelar Make On Make Off PhálleBeauty', 'O Sabonete Micelar Make On Make Off da PhálleBeauty é um produto multifuncional projetado para limpar a pele, removendo eficazmente a maquiagem, impurezas e oleosidade. Sua fórmula micelar delicada e sem enxágue é suave o suficiente para uso diário, enquanto ainda oferece uma limpeza profunda e refrescante. Ideal para todos os tipos de pele, este sabonete micelar deixa a pele limpa, suave e hidratada, sem a necessidade de esfregar ou enxaguar. É uma opção conveniente e eficaz para remover a maqu', 18.99, 'Skincare', '2025-01-19 22:41:14', 12, NULL, 9, 'inglês', 114, 14.5, 6.3, 3.6),
(206, 'Água Micelar Carvão Ativado Lady Beauty', 'A Água Micelar Carvão Ativado da Lady Beauty é um produto de limpeza facial formulado com micelas, que são pequenas partículas de óleo suspensas na água. O carvão ativado presente na fórmula tem propriedades purificantes, ajudando a remover impurezas, oleosidade e resíduos de maquiagem da pele. Além disso, o carvão ativado auxilia na desobstrução dos poros, deixando a pele limpa e fresca. Esta água micelar é indicada para todos os tipos de pele e pode ser usada diariamente para uma limpeza efica', 11.98, 'Skincare', '2025-01-19 22:41:14', 12, NULL, 9, 'inglês', 331, 20, 4, 4),
(207, 'Frete_5', 'Frete_5', 5.00, '', '2025-01-19 22:41:14', 1000, NULL, 1, 'inglês', 0, 0, 0, 0),
(208, 'Frete_10', 'Frete_10', 10.00, '', '2025-01-19 22:41:14', 1000, NULL, 1, 'inglês', 0, 0, 0, 0),
(209, 'Frete_15', 'Frete_15', 15.00, '', '2025-01-19 22:41:14', 1000, NULL, 1, 'inglês', 0, 0, 0, 0),
(210, 'Frete_20', 'Frete_20', 20.00, '', '2025-01-19 22:41:14', 1000, NULL, 1, 'inglês', 0, 0, 0, 0),
(211, 'Kit de Pincel com 8 mini Pincéis Make', 'O Kit de Pincéis Make Lolita contém 8 mini pincéis de maquiagem, perfeitos para uma aplicação precisa e suave. Com cerdas macias e um design compacto, são ideais para viagens e retoques rápidos.', 11.98, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 8, 'inglês', 28, 15, 10, 1),
(212, 'Hidratante Facial Vitamina C OilFree', 'O Hidratante Facial Vitamina C Oil-Free da Kyrav é uma fórmula leve sem óleo, enriquecida com vitamina C para proporcionar hidratação e proteção antioxidante à pele, deixando-a com uma aparência radiante e uniforme. Ideal para todos os tipos de pele, especialmente as mais propensas à oleosidade.', 9.99, 'Skincare', '2025-01-19 22:41:14', 5, NULL, 4, 'inglês', 44, 10, 2, 2),
(213, 'Esponja para Limpeza de Pincéis com Ventosa', 'A Esponja de Silicone para Limpeza de Pincéis com Ventosa é um acessório prático feito de silicone, com texturas especiais para remover resíduos de maquiagem dos pincéis. Possui uma ventosa na parte de trás para fixação em superfícies lisas, facilitando a limpeza.', 6.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 8, 'inglês', 11, 1, 5, 10),
(214, 'Gel Esfoliante Hidratante Pedras Vulcânicas', 'O Gel Facial Esfoliante Hidratante com Pedras Vulcânicas é um produto que oferece uma combinação de esfoliação suave e hidratação para a pele. Com partículas de pedras vulcânicas, proporciona uma esfoliação delicada, removendo impurezas e células mortas.', 12.99, 'Skincare', '2025-01-19 22:41:14', 3, NULL, 4, 'inglês', 117, 15, 6.2, 3.5),
(215, 'Delineador Líquido Faces', 'O Delineador Líquido Faces da Fenzza é um produto de maquiagem que oferece linhas precisas nos olhos. Sua fórmula líquida e pigmentada permite uma aplicação suave e fácil, garantindo um acabamento duradouro. Ideal para criar diferentes estilos de delineado, sua embalagem prática facilita o uso em qualquer lugar.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 6, NULL, 3, 'inglês', 19, 1, 10, 1),
(216, 'Rímel Wave Lash', 'O Rímel Wave Lash da Luisance realça e curva os cílios, proporcionando volume e alongamento. Sua escova especial alcança todos os cílios, garantindo um efeito duradouro sem borrões. Ideal para destacar o olhar com praticidade.', 29.99, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 3, 'inglês', 31, 2, 12, 2),
(217, 'Batom Líquido Matte cor Chocolate', 'O Batom Líquido Matte da Mahav na cor Chocolate oferece um acabamento opaco e duradouro aos lábios. Sua fórmula de secagem rápida proporciona uma cobertura intensa e confortável, sem ressecar os lábios. Ideal para quem deseja uma aparência sofisticada e elegante.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 2, 'inglês', 23, 10, 2, 2),
(218, 'Batom Líquido Matte cor Grená', 'O Batom Líquido Matte da Mahav na cor Grena oferece uma tonalidade rica e elegante aos lábios. Sua fórmula de secagem rápida proporciona um acabamento opaco de longa duração, perfeito para uma aparência sofisticada e moderna.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 2, 'inglês', 23, 10, 2, 2),
(219, 'Primer Hidratante Facial Anticraquelamento Pre Maquiagem', 'O Primer Hidratante Facial Anticraquelamento Pre Maquiagem da MaxLove é um produto que prepara a pele para a aplicação da maquiagem. Sua fórmula hidratante ajuda a suavizar e hidratar a pele, reduzindo o aparecimento de linhas finas e craquelados.', 14.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 1, 'inglês', 26, 15, 3, 3),
(220, 'Corretivo e Contorno Líquido Dia a Dia cor 3', 'O Corretivo e Contorno Líquido Dia a Dia na cor 3 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(221, 'Po Iluminador e Contorno Matte', 'O Pó Iluminador e Contorno Matte da Belle Angel é um produto multifuncional que oferece iluminação e contorno para realçar os traços do rosto. Sua textura matte proporciona um acabamento natural e sem brilho. Ideal para criar efeitos de luz e sombra para um visual mais definido e esculpido.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 7, NULL, 1, 'inglês', 50, 7, 3, 7),
(222, 'Gel Modelador de Sobrancelhas Melu', 'O Gel Modelador de Sobrancelhas da Melu é um produto projetado para domar e definir as sobrancelhas. Sua fórmula transparente e de longa duração mantém os fios no lugar ao longo do dia, proporcionando um acabamento natural e bem cuidado.', 17.99, 'Maquiagem', '2025-01-19 22:41:14', 6, NULL, 3, 'inglês', 26, 4, 9, 1),
(223, 'Touca de Cetim', 'A touca de cetim é um acessório de cabelo feito de tecido liso e sedoso, conhecido por sua capacidade de proteger os fios durante o sono. Ela reduz o atrito entre o cabelo e o travesseiro, ajudando a prevenir danos como quebra e frizz. Ideal para cabelos cacheados, crespos ou texturizados, a touca de cetim preserva a hidratação natural dos fios e prolonga a duração de tratamentos capilares.', 5.89, 'Maquiagem', '2025-01-19 22:41:14', 17, NULL, 8, 'inglês', 16, 1, 8, 8),
(224, 'Batom Líquido 24 hrs Confort Hidratação cor 719', 'O Batom Líquido 24 Hrs Confort Hidratação Cor 719 da Max Love é uma opção versátil para uma cor vibrante nos lábios. Sua fórmula de longa duração proporciona hidratação e conforto ao longo do dia. Com uma ampla gama de cores disponíveis, este batom líquido é perfeito para qualquer ocasião, garantindo um visual impecável por horas.', 17.48, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 2, 'inglês', 19, 14.8, 3, 3),
(225, 'Batom Líquido 24 hrs Confort Hidratação cor 734', 'O Batom Líquido 24 Hrs Confort Hidratação Cor 734 da Max Love oferece uma cor vibrante e duradoura para os lábios. Sua fórmula hidratante proporciona conforto ao longo do dia, mantendo os lábios macios e suaves. Com uma variedade de tons disponíveis, este batom líquido é perfeito para qualquer ocasião, garantindo um visual impecável por horas.', 17.48, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 2, 'inglês', 19, 14.8, 3, 3),
(226, 'Lip Balm Hidratante Labial Amora - Melancia FPS 15', ' O Blister Lip Balm Hidratante Labial Vegano Amora/Melancia FPS 15 Mais You é um bálsamo labial vegano com fragrância de amora e melancia. Sua fórmula hidratante suaviza os lábios, enquanto o FPS 15 protege contra os raios UV. A embalagem em blister é prática para transportar.', 19.99, 'Maquiagem', '2025-01-19 22:41:14', 14, NULL, 2, 'inglês', 13, 7.3, 2, 2),
(227, 'Hidratante Vegano Vitamina C', 'O Hidratante Vegano Vitamina C combina as propriedades hidratantes com os benefícios antioxidantes da vitamina C. Ele é formulado para proporcionar hidratação profunda, ajudando a manter a pele macia e suave, ao mesmo tempo em que auxilia na proteção contra os danos causados pelos radicais livres.', 15.99, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 4, 'inglês', 100, 12, 8, 8),
(228, 'Frete_25', 'Frete_25', 25.00, '', '2025-01-19 22:41:14', 1000, NULL, 1, 'inglês', 0, 0, 0, 0),
(230, 'Corretivo e Contorno Líquido Dia a Dia cor 2', 'O Corretivo e Contorno Líquido Dia a Dia na cor 2 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(231, 'Corretivo e Contorno Líquido Dia a Dia cor 1', 'O Corretivo e Contorno Líquido Dia a Dia na cor 1 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(232, 'Blush Shine Up Mahav Cor 1', 'O Blush Shine Up da Mahav, na cor 1, oferece um toque sutil de cor e brilho às maçãs do rosto. Sua tonalidade delicada proporciona um acabamento naturalmente radiante, perfeito para um visual fresco e luminoso no dia a dia.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 17, 1, 5, 5),
(233, 'Blush Shine Up Mahav Cor 2', 'O Blush Shine Up da Mahav, na cor 2, oferece um toque sutil de cor e brilho às maçãs do rosto. Sua tonalidade delicada proporciona um acabamento naturalmente radiante, perfeito para um visual fresco e luminoso no dia a dia.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 2, NULL, 1, 'inglês', 17, 1, 5, 5),
(234, 'Blush Shine Up Mahav Cor 3', 'O Blush Shine Up da Mahav, na cor 3, oferece um toque sutil de cor e brilho às maçãs do rosto. Sua tonalidade delicada proporciona um acabamento naturalmente radiante, perfeito para um visual fresco e luminoso no dia a dia.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 1, 'inglês', 17, 1, 5, 5),
(235, 'Blush Shine Up Mahav Cor 4', 'O Blush Shine Up da Mahav, na cor 4, oferece um toque sutil de cor e brilho às maçãs do rosto. Sua tonalidade delicada proporciona um acabamento naturalmente radiante, perfeito para um visual fresco e luminoso no dia a dia.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 3, NULL, 1, 'inglês', 17, 1, 5, 5),
(236, 'Blush Shine Up Cor 1, 2, 3 e 4', 'O Blush Shine Up da Mahav, oferece um toque sutil de cor e brilho às maçãs do rosto. Sua tonalidade delicada proporciona um acabamento naturalmente radiante, perfeito para um visual fresco e luminoso no dia a dia.', 12.99, 'Maquiagem', '2025-01-19 22:41:14', 100, NULL, 1, 'inglês', 17, 1, 5, 5),
(237, 'Corretivo e Contorno Líquido Dia a Dia cor 1, 2 e 3', 'O Corretivo e Contorno Líquido Dia a Dia na cor 1 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-01-19 22:41:14', 100, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(238, 'Sérum Facial 3 em 1', 'O Sérum Facial 3 em 1 da Max Love é um produto multifuncional que combina Vitamina C, Rosa Mosqueta e Ácido Hialurônico para antioxidante e hidratação da pele. Contém DPantenol, Extrato de Gengibre, Figo, Aloe Vera, Algas Marinhas e Algodão, proporcionando emoliência e frescor. Fórmula vegana, sem parabenos e petrolatos, para uma pele firme, macia, hidratada e iluminada.', 16.99, 'Skincare', '2025-01-19 22:41:14', 11, NULL, 6, 'inglês', 88, 9, 3, 3),
(239, 'Base Matte Alta Cobertura', 'Uma base de alta cobertura que proporciona um acabamento matte sem deixar a pele ressecada ou craquelada. Desliza facilmente na pele e proporciona uma cobertura perfeita. Cores: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10', 29.99, 'Maquiagem', '2025-01-19 22:41:14', 100, '168, 169, 170, 195, 196, 197, 198, 199, 200, 201', 1, 'inglês', 47, 12, 5.5, 2.5),
(240, 'Corretivo e Contorno Líquido Dia a Dia cor 5', 'O Corretivo e Contorno Líquido Dia a Dia na cor 1 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(241, 'Sérum Facial Vitamina C OilFree', 'O Sérum Facial Vitamina C OilFree Max Love é um produto de cuidados com a pele que oferece uma formulação leve e sem óleo, ideal para peles oleosas ou propensas a acne. Enriquecido com vitamina C, o sérum ajuda a iluminar a pele, uniformizar o tom e combater os sinais de envelhecimento, como linhas finas e manchas escuras. ', 16.99, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 6, 'inglês', 88, 9, 3, 3),
(242, 'Sabonete Facial Hidratante Vitamina C', 'O Sabonete Facial Hidratante Vitamina C Isis Rezende IS026 é um produto formulado para limpar a pele de forma eficaz enquanto a hidrata. Contendo vitamina C, ele ajuda a iluminar e uniformizar o tom da pele, além de combater os sinais de envelhecimento e oferecer propriedades antioxidantes. ', 14.99, 'Skincare', '2025-01-19 22:41:14', 6, NULL, 9, 'inglês', 117, 14, 6, 3),
(243, 'Argila em Pó Rosa', 'Ideal para todos os tipos de pele, a argila rosa combina benefícios da argila branca e da argila vermelha, oferecendo um efeito delicado de limpeza e rejuvenescimento. Ela ajuda a remover impurezas e células mortas, enquanto proporciona uma leve esfoliação e melhora a luminosidade da pele.', 11.99, 'Skincare', '2025-01-19 22:41:14', 4, NULL, 5, 'inglês', 106, 14, 9, 9),
(244, 'Água Micelar Ácido Hialurônico Toque das Nuvens', ' A Água Micelar é um produto multifuncional que combina a eficácia da água micelar com os benefícios do ácido hialurônico. Esta água micelar é formulada para limpar e remover impurezas, maquiagem e resíduos, enquanto o ácido hialurônico proporciona uma hidratação profunda e melhora a elasticidade da pele.', 11.99, 'Skincare', '2025-01-19 22:41:14', 14, NULL, 9, 'inglês', 290, 17.5, 4.5, 4.5),
(245, 'Esponja Gota para Base Líquida', 'A esponja possui uma textura macia e porosa que ajuda a construir camadas de cobertura de forma leve e natural, permitindo um acabamento impecável e sem marcas de pincel. Geralmente, pode ser usada úmida ou seca, dependendo da preferência e do efeito desejado. Ideal para alcançar um acabamento profissional e suave na pele.', 4.99, 'Maquiagem', '2025-01-19 22:41:14', 12, NULL, 8, 'inglês', 30, 5, 6, 5),
(246, 'Paleta de Sombras para Sobrancelha 2 cores', 'Com duas cores complementares, a paleta permite criar um acabamento natural e personalizado, adaptando-se a diferentes tons de sobrancelhas. A cor \"Lua\" geralmente é uma tonalidade mais clara, enquanto \"Neve\" tende a ser um tom mais escuro. Cor: 1', 16.99, 'Maquiagem', '2025-01-19 22:41:14', 5, NULL, 3, 'inglês', 18, 4, 6.7, 1),
(247, 'Delineador Líquido Preto Vegano', 'Sua fórmula líquida é de secagem rápida e proporciona um acabamento matte e duradouro, ideal para criar linhas definidas e impactantes. Sendo vegano, o delineador não contém ingredientes de origem animal e não é testado em animais, alinhando-se com princípios de cruelty-free e ética. Cor: 5', 9.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 3, 'inglês', 9, 10, 2, 2),
(248, 'Lip Balm Textura Suave 24hrs de Hidratação Cor 1 Melancia', 'O Lip Balm Textura Suave 24hrs de Hidratação Cor 1 é um bálsamo labial desenvolvido para proporcionar hidratação intensa e de longa duração aos lábios. Sua fórmula suave e emoliente é projetada para manter os lábios hidratados por até 24 horas, ajudando a prevenir o ressecamento e a descamação.', 11.99, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 2, 'inglês', 17, 12, 5, 2.5),
(249, 'Lip Balm Textura Suave 24hrs de Hidratação Cor 2 Uva', 'O Lip Balm Textura Suave 24hrs de Hidratação Cor 2 é um bálsamo labial desenvolvido para proporcionar hidratação intensa e de longa duração aos lábios. Sua fórmula suave e emoliente é projetada para manter os lábios hidratados por até 24 horas, ajudando a prevenir o ressecamento e a descamação.', 11.99, 'Maquiagem', '2025-01-19 22:41:14', 4, NULL, 2, 'inglês', 17, 12, 5, 2.5),
(250, 'Lip Balm Textura Suave 24hrs de Hidratação Cor 3 Cereja', 'O Lip Balm Textura Suave 24hrs de Hidratação Cor 3 é um bálsamo labial desenvolvido para proporcionar hidratação intensa e de longa duração aos lábios. Sua fórmula suave e emoliente é projetada para manter os lábios hidratados por até 24 horas, ajudando a prevenir o ressecamento e a descamação.', 11.99, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 2, 'inglês', 17, 12, 5, 2.5),
(251, 'Lip Balm Textura Suave 24hrs de Hidratação Cor 4 Morango', 'O Lip Balm Textura Suave 24hrs de Hidratação Cor 4 é um bálsamo labial desenvolvido para proporcionar hidratação intensa e de longa duração aos lábios. Sua fórmula suave e emoliente é projetada para manter os lábios hidratados por até 24 horas, ajudando a prevenir o ressecamento e a descamação.', 11.99, 'Maquiagem', '2025-01-19 22:41:14', 1, NULL, 2, 'inglês', 17, 12, 5, 2.5),
(252, 'Algodão em Discos com 50 discos', 'O Algodão é um produto essencial para cuidados pessoais e higiene. Com 50 unidades, esses discos de algodão são práticos e versáteis, ideais para a aplicação de tonificantes, demaquilantes e outros produtos de cuidados com a pele. Feitos com algodão de alta qualidade, os discos são suaves ao toque e proporcionam uma limpeza eficaz, sem deixar resíduos.', 11.99, 'Maquiagem', '2025-01-19 22:41:14', 18, NULL, 8, 'inglês', 3, 17, 5, 5),
(253, 'Máscara Facial Argila Negra com Ácido Hialurônico', 'A Máscara Facial +Skin Argila Negra com Ácido Hialurônico combina a ação purificante da argila negra com a hidratação do ácido hialurônico. Ela limpa impurezas e controla a oleosidade enquanto mantém a pele hidratada e macia, oferecendo um efeito revitalizante e equilibrado.', 14.99, 'Skincare', '2025-01-19 22:41:14', 2, NULL, 5, 'inglês', 118, 15, 6, 6),
(254, 'Creme Facial Extrato de Pepino com Ácido Glicólico e Colágeno', 'O Creme Facial +Skin Extrato de Pepino com Ácido Glicólico e Colágeno oferece um cuidado revitalizante para a pele. O extrato de pepino proporciona efeito calmante e refrescante, o ácido glicólico ajuda na renovação celular e na uniformização do tom da pele, e o colágeno contribui para a firmeza e elasticidade.', 14.99, 'Skincare', '2025-01-19 22:41:14', 4, NULL, 4, 'inglês', 118, 15, 6, 6),
(255, 'Creme Facial Colágeno e Niacinamida', 'O Creme Facial +Skin Colágeno e Niacinamida combina dois ingredientes eficazes para o cuidado da pele. O colágeno ajuda a melhorar a firmeza e a elasticidade da pele, enquanto a niacinamida (vitamina B3) atua na uniformização do tom, redução de manchas e aumento da hidratação.', 14.99, 'Skincare', '2025-02-03 22:41:14', 2, NULL, 4, 'inglês', 118, 15, 6, 6),
(256, 'Corretivo e Contorno Líquido Dia a Dia cor 4', 'O Corretivo e Contorno Líquido Dia a Dia na cor 1 é um produto versátil para maquiagem diária. Ele oferece cobertura para corrigir imperfeições e contorno para realçar os traços do rosto. Sua textura líquida proporciona uma aplicação suave e natural, ideal para o uso no dia a dia.', 24.99, 'Maquiagem', '2025-02-03 22:41:14', 1, NULL, 1, 'inglês', 29, 11.6, 1.9, 1.9),
(257, 'Esponja para Pó Compacto Miss France', 'Esponja Pó Compacto', 4.99, 'Maquiagem', '2025-02-03 22:41:14', 12, NULL, 8, 'inglês', 4, 8, 6, 1),
(258, 'Creme Facial Hidratante Pessego Melu by Ruby Rose', 'Creme Facial Hidratante Pessego Melu by Ruby Rose', 19.99, 'Skincare', '2025-02-03 22:41:14', 6, NULL, 4, 'inglês', 57, 12, 4, 4),
(259, 'Lapis Retratil Delineador Bella Femme', 'Lapis Retratil Delineador Bella Femme', 8.99, 'Maquiagem', '2025-02-03 22:41:14', 4, NULL, 3, 'inglês', 5, 12.5, 1, 1),
(260, 'Gloss Volumoso Incolor Ácido Hialurônico Max Love', 'Gloss Volumoso Incolor Ácido Hialurônico Max Love', 19.99, 'Maquiagem', '2025-02-03 22:41:14', 2, NULL, 2, 'inglês', 41, 12, 3, 3),
(261, 'Pó Solto Rosa Mosqueta Lady Beauty', 'Po Solto Rosa Mosqueta Lady Beauty', 12.99, 'Maquiagem', '2025-02-03 22:41:14', 6, NULL, 1, 'inglês', 38, 7, 3, 7),
(262, 'Gel Facil Nutrição Intensiva Phallebeauty', 'Gel Facil Nutrição Intensiva Phallebeauty', 18.90, 'Skincare', '2025-02-03 22:41:14', 3, NULL, 4, 'inglês', 84, 3.5, 6.9, 7.3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_produtos`
--

CREATE TABLE `tipo_produtos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `categoria` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

--
-- Despejando dados para a tabela `tipo_produtos`
--

INSERT INTO `tipo_produtos` (`id`, `nome`, `categoria`) VALUES
(1, 'Face', 'Maquiagem'),
(2, 'Boca', 'Maquiagem'),
(3, 'Olhos', 'Maquiagem'),
(4, 'Hidratante Facial', 'Skincare'),
(5, 'Máscara Facial', 'Skincare'),
(6, 'Sérum', 'Skincare'),
(7, 'Acessórios', 'Skincare'),
(8, 'Acessórios', 'Maquiagem'),
(9, 'Higienização Facial', 'Skincare');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `CPF` char(14) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `telefone` char(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `nascimento` date NOT NULL,
  `rua` varchar(255) DEFAULT NULL,
  `numero` int(10) DEFAULT NULL,
  `complemento` varchar(50) DEFAULT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `senha` text DEFAULT NULL,
  `produtos_favoritos` varchar(512) NOT NULL,
  `first_buy` int(5) NOT NULL DEFAULT 1,
  `nivel` varchar(255) NOT NULL DEFAULT 'User',
  `dt_cadastro` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `CPF`, `nome`, `telefone`, `email`, `nascimento`, `rua`, `numero`, `complemento`, `cep`, `cidade`, `estado`, `senha`, `produtos_favoritos`, `first_buy`, `nivel`, `dt_cadastro`) VALUES
(1, '000.000.000-00', 'Beatriz Regina Rippel', '(51) 98318-2080', 'naotembeatriz@gmail.com', '2000-01-01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(2, '000.999.888-77', 'Claudete Fabro', '(48) 98862-3037', 'claudetefabronaotem@gmail.com', '1962-02-25', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(3, '005.022.839-04', 'Adriana Aparecida Pacheco Germano', '(48) 99615-2319', 'adriananaotem@gmail.com', '1981-02-25', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(4, '011.068.922-40', 'Kelliane Lopes Amaral', '(92) 9510-4159', 'amaralkelly98@gmail.com', '1995-12-21', NULL, NULL, NULL, NULL, NULL, NULL, '211981Fla', '', 1, 'User', '2025-02-24 18:51:10'),
(5, '011.920.994-27', 'Rodrigo Diogenis da Silva Melo', '(11) 99356-5314', 'rodrigodiogenis19@gmail.com', '1984-02-26', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(6, '015.487.889-88', 'Margarete Rosa da Silva', '(48) 99865-6264', 'margaretti.com@gmail.com', '1977-06-17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(7, '025.467.510-77', 'Natiele conceição Gonzaga', '(47) 99244-0461', 'natielegonzaga91@gmail.com', '1991-07-23', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(8, '031.194.742-58', 'Marina Luna de Souza alves', '(48) 99684-8159', 'marinalunasa@gmail.com', '2000-02-19', 'Rua Anita Garibaldi ', 251, 'Ap 404', '88701270', 'Tubarão ', 'SC', 'Mari1902', '[\"252\"]', 0, 'Admin', '2025-02-24 18:51:10'),
(9, '035.303.832-60', 'Samuel Pereira Laurentino ', '(48) 99680-4384', 'enderecospl@gmail.com', '2001-02-26', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(10, '036.219.272-39', 'Luisa Jacqueline Silva Vieira de Lima', '(48) 98831-2992', 'luisa.jcq@icloud.com', '2000-05-16', NULL, NULL, NULL, NULL, NULL, NULL, '160520Lj', '', 1, 'User', '2025-02-24 18:51:10'),
(11, '040.306.920-36', 'Bárbara Lara ', '(51) 98054-8769', 'dbarbaralara@gmail.com', '1998-03-05', 'Rua Thomé da Silva número 106 Fábio Silva tubarão 88702740', NULL, NULL, NULL, NULL, NULL, '20181998', '', 1, 'User', '2025-02-24 18:51:10'),
(12, '044.490.649-50', 'Cristiane Ramos Martinho', '(48) 99653-4794', 'cristiane_martinho@hotmail.com', '1983-07-16', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(13, '045.667.409-86', 'Beatriz Lemos Poletto', '(47) 99676-6017', 'beatriz_poletto@hotmail.com', '1984-12-25', NULL, NULL, NULL, NULL, NULL, NULL, '12345678', '', 1, 'User', '2025-02-24 18:51:10'),
(14, '054.185.559-01', 'Bruna Mendes', '(48) 99989-6189', 'bruna.mdtb3@gmail.com', '1986-11-23', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(15, '055.206.989-29', 'Ana Paula Alegre Elias', '(48) 99933-3844', 'anapaula.ellias@hotmail.com', '1988-04-28', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(16, '057.151.769-21', 'Giulia Soares de Medeiros', '(48) 99910-9351', 'soaresgiulia65@gmail.com', '2003-08-05', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(17, '063.726.489-46', 'Ana Lúcia ', '(48) 99859-9595', 'coananalucia@gmail.com', '1985-10-08', 'Terezinha Desia Goulart n°60 bairro São Martinho Tubarão ', NULL, NULL, NULL, NULL, NULL, '12062013Ni#', '', 1, 'User', '2025-02-24 18:51:10'),
(18, '070.044.159-02', 'Gisele Sá da Silva', '(48) 98816-6331', 'Giselesadasilva1987@gmail.com', '1987-10-22', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(19, '071.562.002-91', 'Edna Tereza Fernandes de Souza', '(91) 98231-0545', 'ednaizo@hotmail.com', '1962-10-18', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(20, '071.788.699-92', 'Kelly Amador', '(48) 99164-3181', 'amadorkelly590@gmail.com', '1989-09-15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(21, '072.255.259-99', 'Caroline Santos de Oliveira', '(48) 98497-0196', 'cs5172725@gmail.com', '2000-01-01', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(22, '074.355.059-51', 'Marília Garcia Pinto', '(48) 98807-6825', 'mari_garciapinto@yahoo.com.br', '1989-01-18', 'Rua Cândido Amaro Damásio 1086/905', NULL, NULL, NULL, NULL, NULL, 'professoraEF10', '', 1, 'User', '2025-02-24 18:51:10'),
(23, '078.055.099-48', 'Camila Moreira Jacinto', '(48) 98846-9890', 'camjacinto25@gmail.com', '1991-09-25', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(24, '078.088.939-86', 'Felipe Torquato Mendes (Hortência)', '(48) 99647-7110', 'naotemhortencia@gmail.com', '1969-02-13', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(25, '084.532.359-88', 'Bruna Boaventura Falacio', '(48) 99935-8635', 'brunabfalacio.357@gmail.com', '1993-06-08', 'Rua Luiz Medeiros, 231. Loteamento Jardim América', NULL, NULL, NULL, NULL, NULL, 'Euzinha08', '', 1, 'User', '2025-02-24 18:51:10'),
(26, '085.758.816-80', 'Alexsandra da Silva', '(48) 99968-9382', 'alexsandraferraz372019@gmail.con', '1981-06-27', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(27, '093.817.699-40', 'Kelvin Eduardo Rosa Gonçalves ', '(48) 98850-4225', 'diflow@icloud.com', '1995-12-07', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(28, '100.000.000-00', 'Kelly', '(92) 99510-4159', 'naotemkelly@gmail.com', '2000-01-01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(29, '102.393.039-03', 'Jenison Schmitt', '(48) 99172-3006', 'schmitt.jeni02@outlook.com', '2001-06-30', 'Rua Anita Garibaldi', 251, 'Apt 404', '88701270', 'Tubarão', 'Santa Catarina', 'Js19738246*', '[]', 0, 'Admin', '2025-02-24 18:51:10'),
(30, '102.505.639-67', 'Thayra Hellen', '(47) 99618-3426', 'thayrahellennn@gmail.com', '1997-03-22', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(31, '118.851.979-42', 'Camila de Almeida Felisberto', '(48) 99808-0030', 'kamilamartinho45@gmail.com', '2000-12-09', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(32, '131.050.889-54', 'Ana Clara Nunes', '(48) 99827-0752', 'pereiranunees0528@gmail.com', '2004-05-28', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(33, '139.911.869-26', 'Emily ', '(48) 9610-9603', 'emilyjanuaria.c@gmail.com', '2005-02-17', 'Luiz Martins collaço, bairro santo Antônio de Pádua ', NULL, NULL, NULL, NULL, NULL, '20050217', '', 1, 'User', '2025-02-24 18:51:10'),
(34, '161.810.316-42', 'Isabela Campos', '(48) 98829-5244', 'isabelacampos@gmail.com', '2004-08-18', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(35, '270.819.720-00', 'Cláudia Andrea Gonçalves', '(48) 99951-7428', 'claudiaandreagoncalves2023@gmail.com', '1972-08-27', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(36, '343.606.039-91', 'Marli Gonçalves ', '(48) 99808-2845', 'marligoncalves64@hotmail.com', '1968-06-17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(37, '436.053.979-72', 'Fátima Pereira de Souza', '(48) 99917-7826', 'fatima.ps21@gmail.com', '1962-01-15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(38, '522.549.172-34', 'Corina Fernandes de Souza', '(93) 9122-5966', 'corina_sou22@yahoo.com.br', '1981-11-28', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(39, '573.320.639-04', 'Kelly Amaral ', '(92) 98590-0997', 'kelly.amaral.58919@gmail.com', '1995-12-21', '88702-103', NULL, NULL, NULL, NULL, NULL, '091991Fla', '', 1, 'User', '2025-02-24 18:51:10'),
(40, '625.742.309-06', 'Maria Ignes Mendes Probst', '(48) 99965-2064', 'mmendesprobst@gmail.com', '1964-04-17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(41, '630.511.509-59', 'Solange de Biasi', '(48) 99934-0511', 'solangedebiasi@8.com', '1964-09-29', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(42, '696.020.002-44', 'Marcela Flávia Fernandes de Souza ', '(48) 98428-3565', 'mffsouza37@gmail.com', '1979-05-12', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(43, '729.596.309-04', 'Cleusa Rosa', '(48) 99842-3565', 'naotemcleusarosa@gmail.com', '1964-11-21', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10'),
(44, '744.006.149-72', 'Silvana Maria Machado da Cunha', '(48) 99990-6309', 'naotem@gmail.com', '2000-01-01', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(45, '750.105.262-04', 'Rafaella Nazaré de Souza Guimarães', '(91) 98846-0800', 'rafaellagui29@hotmail.com', '1985-10-13', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(46, '999.888.777-65', 'Nicole Borges', '(48) 99677-6640', 'nicoleborges@gmail.com', '2000-01-01', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(47, '999.888.777-66', 'Regina Kindermann', '(48) 99928-4040', 'reginakindermann@gmail.com', '1957-06-08', NULL, NULL, NULL, NULL, NULL, NULL, '', '', 1, 'User', '2025-02-24 18:51:10'),
(48, '999.999.888-88', 'Erika', '(48) 99831-6257', 'erikanaotem@gmail.com', '1970-12-31', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 1, 'User', '2025-02-24 18:51:10');

-- --------------------------------------------------------

--
-- Estrutura para tabela `vendas`
--

CREATE TABLE `vendas` (
  `id` int(11) NOT NULL,
  `id_produto` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `qtd_produto` int(11) DEFAULT NULL,
  `dt_registro` datetime DEFAULT current_timestamp(),
  `forma_envio` varchar(100) DEFAULT NULL,
  `transportadora` varchar(255) NOT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `rua` varchar(255) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  `valor_total_produto` decimal(10,2) DEFAULT NULL,
  `valor_frete` decimal(10,2) DEFAULT NULL,
  `valor_total_compra` decimal(10,2) DEFAULT NULL,
  `id_pagamento` varchar(255) DEFAULT NULL,
  `forma_pagamento` varchar(255) DEFAULT NULL,
  `temporario` tinyint(1) DEFAULT 1,
  `obs` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

--
-- Despejando dados para a tabela `vendas`
--

INSERT INTO `vendas` (`id`, `id_produto`, `id_usuario`, `qtd_produto`, `dt_registro`, `forma_envio`, `transportadora`, `cep`, `rua`, `bairro`, `cidade`, `estado`, `numero`, `complemento`, `valor_total_produto`, `valor_frete`, `valor_total_compra`, `id_pagamento`, `forma_pagamento`, `temporario`, `obs`) VALUES
(983, 243, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(984, 255, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 14.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(985, 254, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 59.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(986, 258, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(987, 202, 8, 12, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 95.88, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(988, 193, 8, 10, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 169.90, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(989, 139, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 56.70, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(990, 214, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 25.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(991, 262, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(992, 141, 8, 11, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 207.90, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(993, 212, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 39.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(994, 138, 8, 13, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 201.37, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(995, 140, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 59.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(996, 227, 8, 6, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 95.94, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(997, 146, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 47.92, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(998, 253, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(999, 145, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 23.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1000, 144, 8, 7, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 34.86, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1001, 143, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 47.92, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1002, 142, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 9.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1003, 134, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 83.60, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1004, 204, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 75.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1005, 242, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1006, 132, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 56.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1007, 133, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 56.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1008, 136, 8, 11, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 98.89, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1009, 137, 8, 8, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 71.92, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1010, 205, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 94.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1011, 135, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 80.91, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1012, 238, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 84.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1013, 149, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 46.47, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1014, 194, 8, 27, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 485.73, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1015, 241, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 33.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1016, 151, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 70.00, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1017, 150, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 70.00, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1018, 148, 8, 7, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 174.93, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1019, 147, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 224.91, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1020, 185, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 25.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1021, 184, 8, 11, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 142.89, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1022, 206, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 107.82, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1023, 244, 8, 6, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 71.94, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1024, 252, 8, 12, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 143.88, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1025, 239, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 29.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1026, 161, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 39.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1027, 224, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 17.48, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1028, 225, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 17.48, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1029, 187, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 34.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1030, 188, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 16.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1031, 166, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 19.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1032, 217, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 19.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1033, 218, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 59.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1034, 182, 8, 6, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 107.94, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1035, 167, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 39.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1036, 232, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 12.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1037, 233, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 25.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1038, 234, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 25.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1039, 236, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1040, 231, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 24.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1041, 237, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1042, 230, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 24.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1043, 235, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 12.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1044, 256, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1046, 159, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 35.94, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1047, 220, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 24.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1048, 186, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 43.47, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1049, 247, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 9.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1050, 172, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1051, 215, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 12.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1052, 174, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 6.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1053, 171, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1054, 192, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 8.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1055, 173, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1056, 245, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 19.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1057, 165, 8, 7, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 104.93, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1058, 164, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 32.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1059, 190, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 35.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1060, 257, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1061, 183, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 49.41, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1062, 191, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 79.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1063, 213, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 6.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1064, 260, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1065, 259, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1066, 160, 8, 4, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 35.96, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1067, 222, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 53.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1068, 226, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 179.91, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1069, 249, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 11.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1070, 248, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1071, 162, 8, 7, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 90.93, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1072, 251, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1073, 176, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 34.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1074, 152, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 74.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1075, 250, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1076, 189, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 16.47, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1077, 221, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 99.95, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1078, 181, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 73.50, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1079, 246, 8, 5, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 84.00, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1080, 203, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 25.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1081, 156, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 35.80, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1082, 155, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 17.90, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1083, 219, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 14.99, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1084, 158, 8, 1, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 17.90, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1085, 261, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1086, 163, 8, 17, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 169.83, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1087, 157, 8, 6, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 107.40, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1088, 153, 8, 3, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 32.97, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1089, 211, 8, 0, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', NULL, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1090, 223, 8, 9, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 53.01, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1091, 216, 8, 2, '2025-02-02 12:12:43', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'apt 404', 59.98, 0.00, 1594.52, '1331216451', 'credit_card', 0, 'OK'),
(1092, 168, 8, 7, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', 209.93, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1093, 201, 8, 0, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', NULL, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1094, 195, 8, 2, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', 59.98, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1095, 196, 8, 0, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', NULL, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1096, 169, 8, 5, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', 149.95, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1097, 170, 8, 4, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', 119.96, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1098, 199, 8, 0, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', NULL, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1099, 200, 8, 0, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', NULL, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1100, 197, 8, 0, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', NULL, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1101, 198, 8, 1, '2025-02-02 12:58:33', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88180-431', 'Rua Noêmia Farias', 'Centro', 'Antônio Carlos', 'SC', '251', 'apt 404', 29.99, 0.00, 299.90, '1331216611', 'credit_card', 0, 'OK'),
(1136, 244, 8, 1, '2025-02-06 19:38:45', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'AP 404', 11.99, 0.00, 21.98, '1331216611', 'credit_card', 0, 'OK'),
(1137, 163, 8, 1, '2025-02-06 19:38:45', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'AP 404', 9.99, 0.00, 21.98, '1331216611', 'credit_card', 0, 'OK'),
(1207, 258, 42, 1, '2025-02-23 19:37:58', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', NULL, NULL, 'Bairro', NULL, NULL, NULL, NULL, 19.99, 0.00, 77.96, 'LDL8261252', 'credit_card', 0, 'OK'),
(1208, 185, 42, 1, '2025-02-23 19:37:58', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', NULL, NULL, 'Bairro', NULL, NULL, NULL, NULL, 12.99, 0.00, 77.96, 'LDL8261252', 'credit_card', 0, 'OK'),
(1209, 226, 42, 1, '2025-02-23 19:37:58', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', NULL, NULL, 'Bairro', NULL, NULL, NULL, NULL, 19.99, 0.00, 77.96, 'LDL8261252', 'credit_card', 0, 'OK'),
(1210, 240, 42, 1, '2025-02-23 19:37:58', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', NULL, NULL, 'Bairro', NULL, NULL, NULL, NULL, 24.99, 0.00, 77.96, 'LDL8261252', 'credit_card', 0, 'OK'),
(1212, 262, 8, 1, '2025-02-23 18:26:13', 'Retirada', 'Combinar retirada R$0,00 (Tubarão/SC - Centro)', '88701-270', 'Rua Anita Garibaldi', 'Centro', 'Tubarão', 'SC', '251', 'Apt 404', 18.90, 0.00, 17.95, '1322341626', 'bank_transfer', 0, 'OK');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `avise_quando_chegar`
--
ALTER TABLE `avise_quando_chegar`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_produto` (`id_produto`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Índices de tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_produtos_tipo` (`tipo`);

--
-- Índices de tabela `tipo_produtos`
--
ALTER TABLE `tipo_produtos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_produto` (`id_produto`),
  ADD KEY `id_cliente` (`id_usuario`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avise_quando_chegar`
--
ALTER TABLE `avise_quando_chegar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=269;

--
-- AUTO_INCREMENT de tabela `tipo_produtos`
--
ALTER TABLE `tipo_produtos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de tabela `vendas`
--
ALTER TABLE `vendas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1261;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `avise_quando_chegar`
--
ALTER TABLE `avise_quando_chegar`
  ADD CONSTRAINT `avise_quando_chegar_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id`),
  ADD CONSTRAINT `avise_quando_chegar_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`);

--
-- Restrições para tabelas `produtos`
--
ALTER TABLE `produtos`
  ADD CONSTRAINT `fk_produtos_tipo` FOREIGN KEY (`tipo`) REFERENCES `tipo_produtos` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Restrições para tabelas `vendas`
--
ALTER TABLE `vendas`
  ADD CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id`),
  ADD CONSTRAINT `vendas_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
