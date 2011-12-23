## -*- coding: utf-8 -*-
<HTML>
    <HEAD>
    </HEAD>
    <BODY>
      <TABLE border="1">
          %for line in matrix:
          <TR>
              %for word in line:
              <TD>${word}</TD>
              %endfor
          </TR>
          %endfor
      </TABLE>
    </BODY>
</HTML>