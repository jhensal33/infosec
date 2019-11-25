USE [master]
GO
/****** Object:  Database [setUp]    Script Date: 2019/11/25 12:58:50 ******/
CREATE DATABASE [setUp]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'setUp', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\setUp.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'setUp_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\setUp_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [setUp] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [setUp].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [setUp] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [setUp] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [setUp] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [setUp] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [setUp] SET ARITHABORT OFF 
GO
ALTER DATABASE [setUp] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [setUp] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [setUp] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [setUp] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [setUp] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [setUp] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [setUp] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [setUp] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [setUp] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [setUp] SET  DISABLE_BROKER 
GO
ALTER DATABASE [setUp] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [setUp] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [setUp] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [setUp] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [setUp] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [setUp] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [setUp] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [setUp] SET RECOVERY FULL 
GO
ALTER DATABASE [setUp] SET  MULTI_USER 
GO
ALTER DATABASE [setUp] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [setUp] SET DB_CHAINING OFF 
GO
ALTER DATABASE [setUp] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [setUp] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [setUp] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'setUp', N'ON'
GO
ALTER DATABASE [setUp] SET QUERY_STORE = OFF
GO
USE [setUp]
GO
/****** Object:  User [cse4471]    Script Date: 2019/11/25 12:58:50 ******/
CREATE USER [cse4471] FOR LOGIN [cse4471] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [admin]    Script Date: 2019/11/25 12:58:50 ******/
CREATE USER [admin] FOR LOGIN [admin] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [cse4471]
GO
ALTER ROLE [db_datareader] ADD MEMBER [cse4471]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [cse4471]
GO
ALTER ROLE [db_owner] ADD MEMBER [admin]
GO
ALTER ROLE [db_datareader] ADD MEMBER [admin]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [admin]
GO
/****** Object:  Table [dbo].[LoginInfo]    Script Date: 2019/11/25 12:58:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LoginInfo](
	[UserKey] [nchar](50) NOT NULL,
	[UserName] [varchar](25) NULL,
	[Password] [varchar](25) NULL,
 CONSTRAINT [PK_LoginInfo] PRIMARY KEY CLUSTERED 
(
	[UserKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PersonalInformation]    Script Date: 2019/11/25 12:58:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PersonalInformation](
	[UserKey] [nchar](50) NOT NULL,
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[PhoneNumber] [nchar](10) NULL,
 CONSTRAINT [PK_PersonalInformation] PRIMARY KEY CLUSTERED 
(
	[UserKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'1                                                 ', N'a', N'aa')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'10                                                ', N'j', N'jj')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'11                                                ', N'k', N'kk')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'12                                                ', N'l', N'll')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'13                                                ', N'm', N'mm')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'14                                                ', N'n', N'nn')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'15                                                ', N'o', N'oo')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'16                                                ', N'p', N'pp')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'17                                                ', N'q', N'qq')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'18                                                ', N'r', N'rr')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'19                                                ', N's', N'ss')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'2                                                 ', N'b', N'bb')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'20                                                ', N't', N'tt')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'3                                                 ', N'c', N'cc')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'4                                                 ', N'd', N'dd')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'5                                                 ', N'e', N'ee')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'6                                                 ', N'f', N'ff')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'7                                                 ', N'g', N'gg')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'8                                                 ', N'h', N'hh')
INSERT [dbo].[LoginInfo] ([UserKey], [UserName], [Password]) VALUES (N'9                                                 ', N'i', N'ii')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'1                                                 ', N'Wei', N'Yu', N'1233214751')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'10                                                ', N'AJ', N'White', N'2584644263')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'11                                                ', N'Austin', N'Black', N'1651651984')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'12                                                ', N'Kate', N'Baker', N'4561148796')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'13                                                ', N'Cristy', N'Scott', N'1465478471')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'14                                                ', N'Anna', N'Yu', N'2564765136')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'15                                                ', N'David', N'Wing', N'1654478965')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'16                                                ', N'Axay', N'Patel', N'1879653548')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'17                                                ', N'Joe', N'Tracer', N'9784561235')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'18                                                ', N'Zoe', N'Gengi', N'1568465132')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'19                                                ', N'Ashley', N'Jobs', N'6846512356')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'2                                                 ', N'Yu', N'Wei', N'1547895451')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'20                                                ', N'Becky', N'Green', N'1976513248')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'3                                                 ', N'Jeff', N'Johns', N'5874521458')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'4                                                 ', N'Wendy', N'Smith', N'6147584523')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'5                                                 ', N'Will', N'Smith', N'4125789475')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'6                                                 ', N'Sam', N'Green', N'7414785699')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'7                                                 ', N'Bam', N'Min', N'4758884521')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'8                                                 ', N'Alice', N'Wang', N'2598785668')
INSERT [dbo].[PersonalInformation] ([UserKey], [FirstName], [LastName], [PhoneNumber]) VALUES (N'9                                                 ', N'Mike', N'Lyu', N'2145784569')
ALTER TABLE [dbo].[PersonalInformation]  WITH CHECK ADD  CONSTRAINT [FK_PersonalInformation_LoginInfo] FOREIGN KEY([UserKey])
REFERENCES [dbo].[LoginInfo] ([UserKey])
GO
ALTER TABLE [dbo].[PersonalInformation] CHECK CONSTRAINT [FK_PersonalInformation_LoginInfo]
GO
USE [master]
GO
ALTER DATABASE [setUp] SET  READ_WRITE 
GO
