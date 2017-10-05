from sympy import*
Upr, Ux, Rv, Rm = symbols ( ['Upr', 'Ux', 'R_v', 'R_m'])
DUx, DUpr, DRm, DUdop =  symbols( ['Delta_Ux', 'Delta_Upr', 'Delta_Rm','DeltaUdop'])
eqn = Upr/(Rm + Rv) - Ux/Rv
pprint( eqn )
print ('\n')
Rv = solve (eqn, Rv)[0]

d1 = diff( Rv, Rm) * DRm
d2 = diff( Rv, Ux ) * DUx
d3 = diff( Rv, Upr) * DUpr
D = d1 + d2 + d3
pprint (D)
print('\n')

DD1 = D.subs(DRm, 0).subs(DUx,DUdop).subs(DUpr, DUdop)
pprint (DD1)
print('\n')

DD2 = D.subs (DRm, 0).subs(DUx,DUdop).subs(DUpr, -DUdop)
pprint (DD2)
print('\n')

s = printing.mathml( DD2 )
print(s)

with open( "out.html", 'w') as f:
	f.write( s );
