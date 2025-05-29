DECLARE @Type_KOR TinyInt = [Pub].[TDictionary]::Value('[Base].[Dic:Persons:Accounts:Types]', 'BANK:KORR')

SELECT 
  [DateTime]              = T.[DateTime],
  [Person_INN]            = P_INN.[Value],
  [Person_BIK]            = B_BIK.[Value],  
  [Person_Bank]           = B.[NameOfficialShort],
  [Person_RAccount]       = A.[Number],
  [Person_KAccount]       = K.[Number],
  [RemotePerson_INN]      = ISNULL(R_INN.[Value], H.[PersonDocument]),
  [RemotePerson_BIK]      = ISNULL(R_BIK.[Value], H.[OrganizationBIK]),  
  [RemotePerson_Bank]     = ISNULL(R.[NameOfficialShort], H.[OrganizationName]),
  [RemotePerson_RAccount] = ISNULL(E.[Number], H.[AccountNumber]), 
  [RemotePerson_KAccount] = K.[Number],  
  [Quantity]              = T.[Quantity],
  [Number]                = T.[Number],  
  [Comments]              = T.[Comments]
FROM [BackOffice].[Consolidated Transactions] T
INNER JOIN [Base].[Persons:Accounts] A ON A.[Id] = T.[Account_Id]
/*INNER JOIN [Base].[Persons:Accounts] K ON K.[Person_Id] = A.[Organization_Id] AND K.[Type_Id] = @Type_KOR*/
INNER JOIN [Base].[Persons:Accounts] K ON K.[Id] = A.[IntermediaryAccount_Id] AND K.[Type_Id] = @Type_KOR
INNER JOIN [Base].[Persons] B ON B.[Id] = A.[Organization_Id]
LEFT  JOIN [Base].[Persons:Accounts] E ON E.[Id] = T.[RemoteStorageClientRoot_Id]
LEFT  JOIN [Base].[Persons] R ON R.[Id] = E.[Organization_Id]
LEFT  JOIN [Base].[Trash Persons] H ON H.[Id] = T.[RemotePersonTrash_Id]
CROSS APPLY (SELECT [Value] FROM [Base].[Persons::Identifiers&Specificators]('RUS:INN', T.[DateTime]) WHERE [Person_Id] = T.[Person_Id]) P_INN 
OUTER APPLY (SELECT [Value] FROM [Base].[Persons::Identifiers&Specificators]('RUS:INN', T.[DateTime]) WHERE [Person_Id] = T.[RemotePerson_Id]) R_INN
OUTER APPLY (SELECT [Value] FROM [Base].[Persons::Identifiers&Specificators]('BANK:BIK', T.[DateTime]) WHERE [Person_Id] = A.[Organization_Id]) B_BIK
OUTER APPLY (SELECT [Value] FROM [Base].[Persons::Identifiers&Specificators]('BANK:BIK', T.[DateTime]) WHERE [Person_Id] = E.[Organization_Id]) R_BIK
WHERE T.[DateTime] > CAST ( CONVERT ( VarChar ( 4 ), GETDATE(), 112 ) AS Date )
  AND T.[Number] IS NOT NULL
  /*AND T.[Id] = 25543000*/
  /*AND T.[Id] = 25506990*/
/*  
SELECT T.[Account_Id] FROM [BackOffice].[Consolidated Transactions] T WHERE T.[Id] =   25506990
SELECT * FROM [Base].[Persons:Accounts] A WHERE A.[Id] = 184
SELECT * FROM [Base].[Persons:Accounts] A WHERE A.[Id] = 465 AND A.[Type_Id] = @Type_KOR
*/