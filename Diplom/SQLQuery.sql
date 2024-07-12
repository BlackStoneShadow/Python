SELECT [DateTime],
       [Person_Id],
       [Contract_Id],
       [Account_Id],
       [AccountPart_Id],
       [Instrument_Id],
       [Quantity],
       [Number],
       [ExternalAccount],
       [Comments]
FROM   [BackOffice].[Consolidated Transactions]
WHERE  [DateTime] > CAST ( CONVERT ( VarChar ( 4 ), GETDATE(), 112 ) AS Date )
  AND [Number] IS NOT NULL