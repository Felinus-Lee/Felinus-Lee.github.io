Sub FindText()
    Dim findRange As Range
    Set findRange = ActiveDocument.Range ' 可以根据需要设置搜索的范围

    With findRange.Find
        .Text = "要查找的文本"  ' 设置要查找的文本
        .Forward = True  ' 设置搜索方向为向前
        .Wrap = wdFindContinue ' 设置搜索到文档末尾时是否回到文档开头
    End With

    Do While findRange.Find.Found
        ' 执行找到文本后的操作，比如打印位置等
        Debug.Print "找到文本在位置：" & findRange.Start
        findRange.Collapse Direction:=wdCollapseEnd ' 移动到下一个搜索位置
    Loop
End Sub
