CREATE TABLE [dbo].[test]
(
[doctorKey] [nchar] (50) COLLATE Chinese_PRC_CI_AS NOT NULL,
[doctorName] [varchar] (50) COLLATE Chinese_PRC_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[test] ADD CONSTRAINT [PK_test] PRIMARY KEY CLUSTERED  ([doctorKey]) ON [PRIMARY]
GO
