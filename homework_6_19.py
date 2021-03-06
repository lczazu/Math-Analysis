import numpy as np
from math import exp
from math import floor

def adjust_bina_search( fun, a, b, m ):
    """用二分法求fun函数的零根
    a，b为区间，并且fun(a) * fun(b) <= 0
    m为精确到几位小数
    前置条件：fun在[a,b]上连续"""
    
    if fun( a ) == 0:
        return a
    if fun( b ) == 0:
        return b
    
    cou = 0
    while True:
        ai = floor( a )
        bi = floor( b )
        ax = str( a ).split( '.' )
        bx = str( b ).split( '.' )
        
        if( ai == bi and len( ax ) > 1 and len( bx ) > 1 and len( ax[ 1 ] ) >= m and len( bx[ 1 ] ) >= m and ax[ 1 ][ 0:m] == bx[ 1 ][ 0:m] ):
            break
        
        cou = cou + 1
        mid = (a + b ) / 2
        
        if fun( mid ) == 0:
            return mid
        
        if fun( mid ) * fun( a ) < 0:
            b = mid
        else:
            a = mid
            
    return ( a + b ) / 2, cou



def bina_search( fun, a, b, eps ):
    """用二分法求fun函数的零根
    a，b为区间，并且fun(a) * fun(b) <= 0
    eps为精度
    前置条件：fun在[a,b]上连续"""
    eps = eps * 2
    
    if fun( a ) == 0:
        return a
    if fun( b ) == 0:
        return b
    
    cou = 0
    while b - a >= eps:
        cou = cou + 1
        mid = (a + b ) / 2
        
        if fun( mid ) == 0:
            return mid
        
        if fun( mid ) * fun( a ) < 0:
            b = mid
        else:
            a = mid
            
    return ( a + b ) / 2, cou


def fixed_point_ite( fun, x0, eps ):
    """不动点迭代法"""
    x1 = fun( x0 )
    
    cou = 0
    while abs( x1 - x0 ) > eps:
        cou = cou + 1
        x0 = x1
        x1 = fun( x1 )
    
    return x1, cou
def fun_1( x ):
    return x * x - x - 1 
def fun_2_1( x ):
    return 1 / ( x * x )
def fun_2_2( x ):
    return ( 1 + x * x ) ** ( 1 / 3 )
def fun_2_3( x ):
    return 1 / ( (x -1) ** ( 0.5 ) )
def fun_3_1( x ):
    return exp( x ) + 10 * x - 2
def fun_3_2( x ):
    return ( 2 - exp( x ) ) / 10

if __name__ == '__main__':
    print( '第一题')
    a = 0
    b = 2
    print( '计算结果:', bina_search( fun_1, a, b, 0.05 )[ 0 ], '\n' )
    
    print( '**********\n第二题' )
    eps = 0.001
    x0 = 1.5
    print( '第二个公式计算的结果:')
    print( '   ', fixed_point_ite( fun_2_2, x0, eps )[ 0 ])

    a = 0
    b = 1
    x0 = 0
    eps = 0.5 * 0.0001
    eps = ( 1 -0.825 ) / 0.825 * eps
    print( '\n*********\n第三题' )
    print( '二分法求解' )
    res = adjust_bina_search( fun_3_1, a, b, 3 )
    print( '近似根:', res[ 0 ], '计算次数:', res[ 1 ] )
    print( '不动点迭代' )
    res = fixed_point_ite( fun_3_2, x0, eps )
    print( '近似根:', res[ 0 ], '计算次数:', res[ 1 ] )
