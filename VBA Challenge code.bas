Attribute VB_Name = "Module2"
Sub Stock()


    Dim ws As Worksheet


    For Each ws In Worksheets

   
    Dim ticker As String
    
    Dim VolumeTotal As Double

    Dim OpenPrice As Double
    
    Dim ClosePrice As Double

   
    Dim Summary_Table_Row As Integer
    
    Summary_Table_Row = 2

 
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Volume"

    Dim lastRow As Double
    
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
    
        'skip if opne zero
        If (ws.Cells(i, 3).Value = 0) Then
            
            If (ws.Cells(i + 1).Value <> ws.Cells(i, 1).Value) Then
              
                ticker = ws.Cells(i, 1).Value
                
            End If
            
       
        ElseIf (ws.Cells(i + 1, 1).Value = ws.Cells(i, 1).Value) Then
        
            VolumeTotal = VolumeTotal + ws.Cells(i, 7).Value
            
            
            If (ws.Cells(i - 1, 1).Value <> ws.Cells(i, 1).Value) Then
            
                OpenPrice = ws.Cells(i, 3).Value
                
            End If
            
        Else
            
            ticker = ws.Cells(i, 1).Value
            
            
            VolumeTotal = VolumeTotal + ws.Cells(i, 7).Value
            
            
            ClosePrice = ws.Cells(i, 6).Value
            
            
            ws.Cells(Summary_Table_Row, 9).Value = ticker
            
            ws.Cells(Summary_Table_Row, 12).Value = VolumeTotal
            
            'to avoid dividing by zero
            If (VolumeTotal > 0) Then
            
                'print yearly change
                ws.Cells(Summary_Table_Row, 10).Value = ClosePrice - OpenPrice
                
                    'to determine the conditioning format
                    If (ws.Cells(Summary_Table_Row, 10).Value > 0) Then
                    
                        ws.Cells(Summary_Table_Row, 10).Interior.ColorIndex = 4
                        
                    Else
                    
                        ws.Cells(Summary_Table_Row, 10).Interior.ColorIndex = 3
                        
                    End If
                    
                'print the percent change
                ws.Cells(Summary_Table_Row, 11).Value = ws.Cells(Summary_Table_Row, 10).Value / OpenPrice
                
                
            Else
            
                'to set yearly and percent change if zero
                
                ws.Cells(Summary_Table_Row, 10).Value = 0
                ws.Cells(Summary_Table_Row, 11).Value = 0
                
            End If
            
            ws.Cells(Summary_Table_Row, 11).Style = "percent"
        
            VolumeTotal = 0
    
            Summary_Table_Row = Summary_Table_Row + 1
            
        End If
        
    Next i

    
    Dim greatTotVolume As Double
   
    ws.Cells(2, 14).Value = "Greatest % Increase"
    ws.Cells(3, 14).Value = "Greatest % Decrease"
    ws.Cells(4, 14).Value = "Greatest Total Volume"
    ws.Cells(1, 15).Value = "Ticker"
    ws.Cells(1, 16).Value = "Value"

    greatTotVolume = 0

  
    
    Summary_Table_Row = Summary_Table_Row - 2

    'if cell > greatest total volume, set cell as greatest total volume
    For i = 2 To Summary_Table_Row
    
        If (ws.Cells(i, 12).Value > greatTotVolume) Then
        
            greatTotVolume = ws.Cells(i, 12).Value

           
            ws.Cells(4, 15).Value = ws.Cells(i, 9).Value
            
        End If
        
    Next i

    
    ws.Cells(4, 16).Value = greatTotVolume

    
    Dim incPerc As Double
    Dim decePerc As Double

    
    incPerc = 0
    decPerc = 0

    For i = 2 To Summary_Table_Row
    
        'if cell > greatest % increase, set cell as greatest % increase
        
        If (ws.Cells(i, 11).Value > incPerc) Then
            incPerc = ws.Cells(i, 11).Value

          
            ws.Cells(2, 15) = ws.Cells(i, 9).Value
            
        'if cell < greatest % decrease, set cell as greatest % decrease
        ElseIf (ws.Cells(i, 11).Value < decPerc) Then
            decPerc = ws.Cells(i, 11).Value

         
            ws.Cells(3, 15).Value = ws.Cells(i, 9).Value
            
        End If
        
    Next i

    ws.Cells(2, 16).Value = incPerc
    ws.Cells(3, 16).Value = decPerc
 
    ws.Cells(2, 16).Style = "percent"
    ws.Cells(3, 16).Style = "percent"
    ws.Cells(4, 16).Style = "comma"

    ws.Columns("I:P").AutoFit

Next ws

End Sub
